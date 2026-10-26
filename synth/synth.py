"""Synthesis worker — turns lossless study notes into operational skill/playbook drafts.
Runs on the Anthropic API (same key). Hierarchical: digests chunks, then merges.

Usage: python synth.py jobs.json
Each job: {"name", "inputs": [paths or id-list files (*.txt of 11-char ids -> notes/<id>_notes.md)],
           "brief": "...", "out": "path"}
Skips jobs whose `out` already exists.
"""
import json, sys, time
from pathlib import Path

import anthropic

BASE = Path(__file__).parent.parent
NOTES = BASE / "notes"
MODEL = "claude-opus-5-5"
CHUNK = 350_000  # chars per digest pass

SYSTEM = """أنت كبير مصممي المناهج في استوديو ألعاب حسام (هايبر/هايبرد-كاجوال موبايل، إيقاع لعبة جديدة يوميًا أو 2+ أسبوعيًا؛ اللعبة الحالية Mossfolk — Unity physics merge puzzle بتيستر-بوت bot_difficulty و3000 ليفل).
مهمتك: تحويل نوتس مذاكرة بلا فقد إلى **مستند تشغيلي** بيتنفذ منه مباشرة — مش تلخيص.
قواعد:
- عامية مصرية، المصطلح التقني إنجليزي.
- احتفظ بكل رقم وقاعدة وأسماء الأمثلة — الضغط مسموح في الكلام مش في المعلومة.
- نظّم في: قواعد مرقمة قابلة للتنفيذ + جداول قرار + تشيك ليستات فحص + أنتي-باترنز + cheatsheet ختامي.
- علّم ★★★ على اللي بيخدم خط إنتاج «لعبة جديدة كل يوم/أسبوع» (اختيار أفكار، بروتوتايب، CPI، تيستر، إعلانات).
- لو فيه تعارض بين مصدرين، اذكر الاتنين وسمّي المصدرين."""


def client():
    return anthropic.Anthropic()


def call(cl, text, max_tokens=40000):
    with cl.beta.messages.stream(
        model=MODEL, max_tokens=max_tokens,
        betas=["server-side-fallback-2026-07-01"], fallbacks="default",
        system=[{"type": "text", "text": SYSTEM, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": text}],
    ) as s:
        r = s.get_final_message()
    if r.stop_reason == "refusal":
        return "> [refusal]"
    return "".join(b.text for b in r.content if b.type == "text")


def gather(inputs):
    texts = []
    for inp in inputs:
        p = Path(inp)
        if not p.is_absolute():
            p = BASE / inp
        if p.suffix == ".txt" and p.exists():
            # id list -> note files
            ids = [l.strip() for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
            for vid in ids:
                nf = NOTES / f"{vid}_notes.md"
                if nf.exists():
                    texts.append(f"\n\n===== NOTES {vid} =====\n" + nf.read_text(encoding="utf-8"))
        elif p.exists():
            texts.append(f"\n\n===== FILE {p.name} =====\n" + p.read_text(encoding="utf-8"))
    return "".join(texts)


def run_job(cl, job):
    out = Path(job["out"])
    if not out.is_absolute():
        out = BASE / job["out"]
    if out.exists():
        print(f"skip {job['name']} (exists)")
        return
    body = gather(job["inputs"])
    if len(body) < 1000:
        print(f"skip {job['name']} (no input found)")
        return
    print(f"[{time.strftime('%H:%M:%S')}] {job['name']}: {len(body)//1000}KB input")
    if len(body) <= CHUNK:
        result = call(cl, job["brief"] + "\n\n=== المصادر ===\n" + body)
    else:
        parts = [body[i:i+CHUNK] for i in range(0, len(body), CHUNK)]
        digests = []
        for i, part in enumerate(parts):
            print(f"  digest {i+1}/{len(parts)}")
            digests.append(call(cl, job["brief"] + f"\n\n(دي دفعة {i+1} من {len(parts)} — اعمل digest تشغيلي كامل للدفعة دي، وهندمج الدفعات بعدين)\n\n=== المصادر ===\n" + part, max_tokens=32000))
        merged = "\n\n===== DIGEST SPLIT =====\n\n".join(digests)
        result = call(cl, job["brief"] + "\n\n(دول digests جزئية لنفس الكوربس — ادمجهم في مستند واحد نهائي من غير فقد قواعد أو أرقام، شيل التكرار بس)\n\n" + merged)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(result, encoding="utf-8")
    print(f"  -> {out} ({len(result)//1000}KB)")


if __name__ == "__main__":
    jobs = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    cl = client()
    for job in jobs:
        try:
            run_job(cl, job)
        except Exception as e:
            print(f"ERROR {job['name']}: {e}")
    print("SYNTH DONE")
