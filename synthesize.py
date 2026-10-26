"""Integration round map-reduce over the study corpus (API-side to spare the plan).
MAP  (Haiku): each note -> JSON: per-theme extracted items (tactic, numbers, example, pattern).
REDUCE (Sonnet): per theme -> organized skill draft section merging all items, deduped.
Output: synth/map/<note>.json ، synth/drafts/<theme>.md
"""
import os, sys, json, time
from pathlib import Path
import anthropic

BASE = Path(__file__).parent
NOTES_DIRS = [BASE / "notes", BASE / "videos", BASE / "books"]
SYNTH = BASE / "synth"
(SYNTH / "map").mkdir(parents=True, exist_ok=True)
(SYNTH / "drafts").mkdir(parents=True, exist_ok=True)

THEMES = {
    "pipeline": "خط إنتاج الاستوديو: اختيار الأفكار، البروتوتايب، CPI، التست المبكر، الببلشرز، إيقاع الإصدار السريع، قتل المشاريع، الإنتاج",
    "challenge": "التحدي والصعوبة: منحنيات، flow، learning curve، catharsis، فشل وretry، scaling، balance، perceived fairness",
    "leveldesign": "تصميم الليفلات: بنية، إيقاع، guidance، metrics، تشريح، توليد، بلوك-آوت، أنماط",
    "feel": "الإحساس واللعب اللحظي: تحكم، juice، فيزياء، توقيتات، إدخال، حركة",
    "progression": "التقدم والريتنشن والاقتصاد: مكافآت، skill trees، أرواح، سكور، ladders، عملات، FOMO وأخلاقياته، monetization design",
    "uxvisual": "الواجهة والفيجوالز والإدراك: UI، onboarding، tutorials، accessibility، قراءة بصرية، صوت، رموز",
    "testerai": "التيستر والـ AI: بوتات شبيهة بالبشر، تيليمتري، تحليلات لاعبين، معايرة، أدوات اختبار آلي",
    "narrative": "السرد والشخصيات والعالم: قصة خفيفة، archetypes، مشاعر، ثيمات",
}

MAP_MODEL = "claude-haiku-5-5"
REDUCE_MODEL = "claude-sonnet-5-5"

MAP_SYS = """هتاخد نوتة مذاكرة من مكتبة استوديو ألعاب. صنّف محتواها على الثيمات دي واستخرج لكل ثيم العناصر اللي تخصه:
""" + "\n".join(f"- {k}: {v}" for k, v in THEMES.items()) + """

رجّع JSON فقط بالشكل:
{"items":[{"theme":"<key>","tactic":"<الاسم>","detail":"<التعريف+الرقم+المثال بالاسم في 1-3 جمل>","pattern":"<الباترن ورا التاكتيك لو موجود>","stars":1-3,"source":"<اسم المصدر/الفيديو>"}]}
- انقل الأرقام والأمثلة بأسمائها حرفيًا — ممنوع التعويم.
- العنصر الواحد ممكن يظهر في ثيم واحد بس (الأنسب).
- النوتة الغنية بتطلع 5-20 عنصر؛ ماتختصرش."""


def client():
    return anthropic.Anthropic()


def map_phase(cl):
    files = []
    for d in NOTES_DIRS:
        files += sorted(d.glob("*_notes*.md")) + sorted(d.glob("*_notes.md"))
    files = sorted(set(files))
    for f in files:
        out = SYNTH / "map" / (f.stem + ".json")
        if out.exists():
            continue
        text = f.read_text(encoding="utf-8")
        if len(text) < 400:
            continue
        # chunk very large note files (books)
        chunks = [text[i:i+90_000] for i in range(0, len(text), 90_000)]
        all_items = []
        try:
            for ch in chunks:
                r = cl.messages.create(
                    model=MAP_MODEL, max_tokens=16000,
                    system=MAP_SYS,
                    messages=[{"role": "user", "content": ch}],
                )
                raw = "".join(b.text for b in r.content if b.type == "text")
                raw = raw[raw.find("{"):raw.rfind("}")+1]
                all_items += json.loads(raw).get("items", [])
        except Exception as ex:
            print(f"{f.name}: MAP ERROR {ex}")
            continue
        out.write_text(json.dumps({"source_file": f.name, "items": all_items}, ensure_ascii=False), encoding="utf-8")
        print(f"{f.name}: {len(all_items)} items")


REDUCE_SYS = """إنت بتبني سكيل معرفي لاستوديو ألعاب هايبر/هايبرد-كاجوال بإيقاع لعبة جديدة يوميًا. هتاخد قايمة عناصر مستخرجة من مئات المصادر عن ثيم واحد. ألّف منها **مسودة سكيل منظمة**:
- بالعامية المصرية، المصطلح الإنجليزي، فورمات ماركداون بعناوين فرعية منطقية.
- ادمج المكرر (نفس التاكتيك من مصادر متعددة = بند واحد بيذكر «أكده N مصادر» وأقوى مثال).
- حافظ على كل رقم ومثال مسمى — اللوسليس مقدس.
- رتب بالأهمية التشغيلية (★★★ الأول)، وكل قسم يقفل بسطر «للاستوديو:» عملي.
- اقفل بـ«تشيت شيت القرارات»: قواعد if-then قابلة للتطبيق فورًا."""


def reduce_phase(cl, themes=None):
    by_theme = {k: [] for k in THEMES}
    for j in (SYNTH / "map").glob("*.json"):
        data = json.loads(j.read_text(encoding="utf-8"))
        for it in data.get("items", []):
            t = it.get("theme")
            if t in by_theme:
                it["_src"] = data.get("source_file", j.stem)
                by_theme[t].append(it)
    for theme, items in by_theme.items():
        if themes and theme not in themes:
            continue
        out = SYNTH / "drafts" / f"{theme}.md"
        if out.exists() or not items:
            continue
        items.sort(key=lambda x: -int(x.get("stars", 1)))
        payload = json.dumps(items, ensure_ascii=False)
        # chunk reduce if huge
        parts = [payload[i:i+150_000] for i in range(0, len(payload), 150_000)]
        drafts = []
        for i, p in enumerate(parts):
            r = cl.messages.create(
                model=REDUCE_MODEL, max_tokens=32000,
                system=REDUCE_SYS,
                messages=[{"role": "user", "content": f"الثيم: {theme} — {THEMES[theme]}\nجزء {i+1}/{len(parts)} من العناصر:\n{p}"}],
            )
            drafts.append("".join(b.text for b in r.content if b.type == "text"))
        if len(drafts) > 1:
            r = cl.messages.create(
                model=REDUCE_MODEL, max_tokens=32000,
                system=REDUCE_SYS,
                messages=[{"role": "user", "content": f"ادمج المسودات الجزئية دي لثيم {theme} في مسودة واحدة نهائية بلا فقد:\n\n" + "\n\n===PART===\n\n".join(drafts)}],
            )
            final = "".join(b.text for b in r.content if b.type == "text")
        else:
            final = drafts[0]
        out.write_text(final, encoding="utf-8")
        print(f"{theme}: {len(items)} items -> {out.name} ({len(final)//1000}KB)")


if __name__ == "__main__":
    cl = client()
    phase = sys.argv[1] if len(sys.argv) > 1 else "map"
    if phase == "map":
        map_phase(cl)
    elif phase == "reduce":
        reduce_phase(cl, set(sys.argv[2:]) or None)
