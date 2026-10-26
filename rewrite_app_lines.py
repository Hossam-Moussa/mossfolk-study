"""Surgically rewrite «لموسفولك:» application blocks into generalized «للاستوديو:» blocks.
Keeps every other byte of the note untouched. Uses Haiku (cheap).
Usage: python rewrite_app_lines.py <file-or-dir> [...]
State: _rewritten.txt next to this script lists processed files.
"""
import os, re, sys
from pathlib import Path
import anthropic

BASE = Path(__file__).parent
DONE = BASE / "_rewritten.txt"
MODEL = "claude-haiku-5-5"

SYS = """أنت محرر نوتس في استوديو ألعاب هايبر/هايبرد-كاجوال بإيقاع لعبة جديدة يوميًا أو 2+ أسبوعيًا. هتاخد عنوان نوتة مذاكرة + بلوك تطبيق قديم مكتوب بعدسة لعبة واحدة (Mossfolk — physics merge puzzle). أعد كتابته كبلوك «**للاستوديو:**» معمم:
- الدرس يتطبق على **أي فكرة لعبة مناسبة له** + على خط إنتاج الاستوديو (اختيار أفكار، بروتوتايب، CPI، تيستر-بوت، أنظمة قابلة لإعادة الاستخدام، إعلانات).
- التطبيقات الموسفولكية المحددة القيمة تتحول لمثال: «(مثال على اللعبة الحالية Mossfolk: ...)» — ماتترميش.
- نفس العامية المصرية والمصطلح الإنجليزي ونفس مستوى التفصيل أو أغنى. حافظ على الـ★ لو موجودة.
- رجّع البلوك الجديد بس، يبدأ بـ «**للاستوديو:**» — من غير أي كلام تاني."""


def client():
    return anthropic.Anthropic()


MARKER = "**لموسفولك"


def find_blocks(text):
    """Yield (start, end) of each application block: from marker line start to the
    next entry separator (--- or ## header) or end of file."""
    blocks = []
    i = 0
    while True:
        m = text.find(MARKER, i)
        if m == -1:
            break
        line_start = text.rfind("\n", 0, m) + 1
        # end: next "\n---" or "\n## " after marker, else EOF
        cands = [text.find("\n---", m), text.find("\n## ", m), text.find("\n# ", m)]
        cands = [c for c in cands if c != -1]
        end = min(cands) if cands else len(text)
        blocks.append((line_start, end))
        i = end
    return blocks


def rewrite_file(cl, p: Path):
    text = p.read_text(encoding="utf-8")
    blocks = find_blocks(text)
    if not blocks:
        return 0
    title_m = re.search(r"^#+ (.+)$", text, re.M)
    title = title_m.group(1) if title_m else p.stem
    out, prev, n = [], 0, 0
    for (s, e) in blocks:
        out.append(text[prev:s])
        old = text[s:e]
        resp = cl.messages.create(
            model=MODEL, max_tokens=4000,
            system=SYS,
            messages=[{"role": "user", "content": f"عنوان النوتة: {title}\n\nالبلوك القديم:\n{old}"}],
        )
        new = "".join(b.text for b in resp.content if b.type == "text").strip()
        if not new.startswith("**للاستوديو") and not new.startswith("- **للاستوديو"):
            new = old  # safety: keep old if model went off-format
        # preserve leading "- " list style if the old block had it
        if old.lstrip().startswith("- ") and not new.startswith("- "):
            new = "- " + new
        out.append(new + "\n")
        prev = e
        n += 1
    out.append(text[prev:])
    p.write_text("".join(out), encoding="utf-8")
    return n


def done_set():
    return set(DONE.read_text(encoding="utf-8").splitlines()) if DONE.exists() else set()


if __name__ == "__main__":
    cl = client()
    targets = []
    for a in sys.argv[1:]:
        pa = Path(a)
        if pa.is_dir():
            targets += sorted(pa.glob("*.md"))
        elif pa.exists():
            targets.append(pa)
    done = done_set()
    for p in targets:
        key = str(p)
        if key in done:
            continue
        try:
            n = rewrite_file(cl, p)
            print(f"{p.name}: {n} blocks rewritten")
        except Exception as ex:
            print(f"{p.name}: ERROR {ex}")
            continue
        with DONE.open("a", encoding="utf-8") as f:
            f.write(key + "\n")
