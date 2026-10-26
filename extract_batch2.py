import sys
from pypdf import PdfReader
pairs = [
 ("A_Procedural_Method_for_Automatic_Level.pdf","proclevel"),
 ("the-game-design-toolbox-1nbsped-103236551x-9781032365510-9781032365879-9781003332756_compress.pdf","toolbox"),
 ("2-game-feel.pdf","gamefeel"),
 ("Artificial Intelligence for Games.pdf","aigames"),
 ("Unity AI Game Programming - Second Edition.pdf","unityai"),
 ("Game Programming Patterns.pdf","progpatterns"),
 ("dokumen.pub_the-gamification-of-learning-and-instruction-1nbsped-9781118096345-2011047543.pdf","kapp"),
 ("Introduction_to_Game_Design_Development.pdf","introgd"),
 ("advanced-game-design-a-systems-approach-1nbsped-0134667603-9780134667607_compress.pdf","sellers"),
]
dl = r"C:\Users\Lenovo Thinkpad\Downloads"
out = sys.argv[1]
for fn, name in pairs:
    try:
        r = PdfReader(dl + "\\" + fn)
        txt = []
        for p in r.pages:
            try: txt.append(p.extract_text() or "")
            except Exception as e: txt.append(f"[[page error: {e}]]")
        full = "\n\n".join(txt)
        with open(out + "\\" + name + ".txt", "w", encoding="utf-8") as f:
            f.write(full)
        print(f"{name}: {len(r.pages)} pages, {len(full.split())} words", flush=True)
    except Exception as e:
        print(f"{name}: FAILED {e}", flush=True)
