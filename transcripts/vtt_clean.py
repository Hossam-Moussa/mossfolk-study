"""Convert YouTube VTT captions to clean text with [Nm] minute markers.
Usage: python -I vtt_clean.py <dir>  -> writes <id>.txt next to each <id>.en.vtt
Handles auto-caption rolling duplicates."""
import re, sys
from pathlib import Path

def clean(vtt_path: Path) -> str:
    lines = vtt_path.read_text(encoding="utf-8", errors="replace").splitlines()
    out, last_min, prev = [], -1, ""
    cur_min = 0
    for ln in lines:
        m = re.match(r"(\d+):(\d+):(\d+)[.,]\d+ --> ", ln)
        if m:
            cur_min = int(m.group(1)) * 60 + int(m.group(2))
            continue
        if not ln.strip() or ln.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")):
            continue
        txt = re.sub(r"<[^>]+>", "", ln).strip()
        if not txt or txt == prev:
            continue
        # rolling-caption overlap: skip if txt is contained in prev or vice versa tail
        if prev and (txt in prev):
            continue
        if cur_min != last_min:
            out.append(f"\n[{cur_min}m] ")
            last_min = cur_min
        out.append(txt + " ")
        prev = txt
    return "".join(out)

if __name__ == "__main__":
    d = Path(sys.argv[1])
    n = 0
    for vtt in sorted(d.glob("*.vtt")):
        vid = vtt.name.split(".")[0]
        txt_path = d / f"{vid}.txt"
        if txt_path.exists():
            continue
        txt_path.write_text(clean(vtt), encoding="utf-8")
        n += 1
    print(f"converted {n}")
