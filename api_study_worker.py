"""API study worker — burns Anthropic API credit (NOT the Claude Code plan).
Studies transcripts/books losslessly into Arabic notes, matching the main
session's note standard (exemplar enforced in the system prompt).

Usage:
  set ANTHROPIC_API_KEY=sk-ant-...
  python api_study_worker.py transcripts            # study all new transcript .txt
  python api_study_worker.py book <path.txt> <out>  # study a book file chapter-wise

Output: notes/<id>_notes.md per video, or <out> for a book.
State: notes/_done.txt lists finished inputs so reruns skip them.
"""
import os, sys, time, json
from pathlib import Path

import anthropic

BASE = Path(__file__).parent
TRANS = BASE / "transcripts"
NOTES = BASE / "notes"
NOTES.mkdir(exist_ok=True)
DONE = NOTES / "_done.txt"
EXEMPLAR_FILES = [
    BASE / "videos" / "extracredits_notes.md",
    BASE / "videos" / "aiandgames_notes.md",
]

MODEL = "claude-sonnet-5-5"  # Hossam 2026-10-26: lighten API cost — Sonnet is half Opus price

RULES = """أنت باحث مذاكرة في استوديو ألعاب حسام. لعبتنا: Mossfolk — Unity physics merge puzzle (إسقاط مخلوقات في برطمان، اتنين من نفس الحجم بيندمجوا للأكبر، 9 أحجام، 3000 ليفل بأهداف وميزانية إسقاطات، تحديات mossy shells/stones/rot من 2501، تيستر-بوت بيقيس bot_difficulty، وside quests فيها rival contests وminiجيمز). الاستوديو هايبر/هايبرد-كاجوال موبايل.

قاعدة حسام الحرفية الملزمة: «مهم اننا منختصرش، بنفهم التاكتيكس والاحداث والحقايق وبنحاول نفهم الباتيرنز وراهم» — مذاكرة بلا فقد: كل تاكتيك، كل رقم، كل مثال بالاسم، كل حقيقة، والباترن ورا كل تاكتيك. لو المصدر فيه 12 فكرة، النوتس فيها 12.

استثناء وحيد (قاعدة حسام): تجاهل شرح البرمجة والكود والـ implementation التفصيلي — إحنا عارفين البرمجة كفاية. لو المصدر كله برمجة، اكتب 3-4 سطور بس باللي يهم التصميم/العملية منه وقول «الباقي برمجة — متجاهل». الدروس التصميمية جوه فيديو برمجة بتتسجل عادي.

فورمات النوتس (زي الـ exemplar بالظبط):
- عنوان بالمصدر والمدة.
- نقاط بالعامية المصرية، المصطلح التقني إنجليزي، ★/★★/★★★ للأهمية (الأعلى للـ playability والـ challenge/fun والحاجات القابلة للتطبيق عندنا).
- كل تاكتيك: التعريف + الرقم + المثال من المصدر + «الباترن ورا التاكتيك» لو مش بديهي.
- سطر «**لموسفولك:**» في الآخر: تطبيق مباشر على لعبتنا/التيستر/مولد الليفلات/الإعلانات.
- جودتك لازم تساوي أو تتفوق على الـ exemplar المرفق — مش أقل."""


def client() -> anthropic.Anthropic:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY not set")
    return anthropic.Anthropic()


def exemplar() -> str:
    for f in EXEMPLAR_FILES:
        if f.exists():
            t = f.read_text(encoding="utf-8")
            return t[:12000]
    return ""


def call(cl, user_text: str) -> str:
    with cl.beta.messages.stream(
        model=MODEL,
        max_tokens=32000,
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        system=[
            {"type": "text", "text": RULES + "\n\n=== EXEMPLAR (معيار الجودة الملزم) ===\n" + exemplar(),
             "cache_control": {"type": "ephemeral"}},
        ],
        messages=[{"role": "user", "content": user_text}],
    ) as stream:
        resp = stream.get_final_message()
    if resp.stop_reason == "refusal":
        return f"\n> [refusal: {getattr(resp.stop_details, 'category', '?')}]\n"
    return "".join(b.text for b in resp.content if b.type == "text")


def done_set() -> set:
    return set(DONE.read_text(encoding="utf-8").split()) if DONE.exists() else set()


def mark_done(key: str):
    with DONE.open("a", encoding="utf-8") as f:
        f.write(key + "\n")


def study_transcripts(shard: int = 0, nshards: int = 1):
    cl = client()
    txts = sorted(TRANS.glob("*.txt"), key=lambda p: p.stat().st_mtime)
    import re, zlib
    for t in txts:
        vid = t.stem
        if not re.fullmatch(r"[A-Za-z0-9_-]{11}", vid):
            continue
        if zlib.crc32(vid.encode()) % nshards != shard:
            continue
        if vid in done_set():
            continue
        body = t.read_text(encoding="utf-8")
        if len(body) < 500:
            mark_done(vid); continue
        out = NOTES / f"{vid}_notes.md"
        print(f"[{time.strftime('%H:%M:%S')}] studying {vid} ({len(body)//1000}KB)")
        notes = call(cl, f"ذاكر الترانسكريبت ده بلا فقد واكتب النوتس بالفورمات الملزم. معرف الفيديو: {vid}\n\n=== TRANSCRIPT ===\n{body}")
        out.write_text(notes, encoding="utf-8")
        mark_done(vid)
    print("transcripts: all done")


def study_book(path: str, out_path: str, chunk_chars: int = 120_000):
    cl = client()
    src = Path(path)
    out = Path(out_path)
    body = src.read_text(encoding="utf-8", errors="replace")
    done = done_set()
    chunks = [body[i:i + chunk_chars] for i in range(0, len(body), chunk_chars)]
    for i, ch in enumerate(chunks):
        key = f"{src.stem}#{i}"
        if key in done:
            continue
        print(f"[{time.strftime('%H:%M:%S')}] {src.stem} chunk {i+1}/{len(chunks)}")
        notes = call(cl, f"ده جزء {i+1} من {len(chunks)} من كتاب {src.stem}. ذاكره بلا فقد فصلًا فصلًا واكتب النوتس بالفورمات الملزم (كمل ترقيم الفصول من السياق):\n\n{ch}")
        with out.open("a", encoding="utf-8") as f:
            f.write(notes + "\n\n")
        mark_done(key)
    print(f"book {src.stem}: done -> {out}")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "transcripts"
    if mode == "transcripts":
        shard = int(sys.argv[2]) if len(sys.argv) > 2 else 0
        nshards = int(sys.argv[3]) if len(sys.argv) > 3 else 1
        study_transcripts(shard, nshards)
    elif mode == "book":
        study_book(sys.argv[2], sys.argv[3])
