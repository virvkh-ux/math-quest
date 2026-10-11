"""Build the public edition (play/) from the family edition (src/).
Run from the project root:  python scripts/build_public.py
The public edition: local-only saves, no family code, no cloud sync, no personal hero/wardrobe."""
import re, json, shutil, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
src, out = root / "src", root / "play"
out.mkdir(exist_ok=True)
html = (src / "index.html").read_text(encoding="utf-8")

def must(old, new, text):
    assert old in text, f"build_public: marker not found: {old[:60]}"
    return text.replace(old, new)

html = must('const EDITION = "family";', 'const EDITION = "public";', html)
# drop the personal hero/wardrobe (drawn from family photos)
html = re.sub(r"/\*@FAMILY_START\*/.*?/\*@FAMILY_END\*/",
              'const OUTFITS={}; function heroOutfitSVG(){return "";} function heroSVG(){return "";} function avatarHTML(a){ return a==="hero:girl" ? "🦄" : a; }',
              html, count=1, flags=re.S)
assert "@FAMILY_START" not in html
# no cloud sync in the public edition
html = re.sub(r'var SYNC_CFG = \{[^}]*\};', 'var SYNC_CFG = { apiKey: "", projectId: "" };', html, count=1)
# let search engines find the public edition
html = html.replace('<meta name="robots" content="noindex, nofollow">\n', '')
(out / "index.html").write_text(html, encoding="utf-8", newline="\n")

man = json.loads((src / "manifest.webmanifest").read_text(encoding="utf-8"))
man.update({"name": "Math Quest", "short_name": "Math Quest", "start_url": "./index.html", "scope": "./", "id": "./"})
(out / "manifest.webmanifest").write_text(json.dumps(man, indent=2), encoding="utf-8")
sw = (src / "sw.js").read_text(encoding="utf-8")
sw = re.sub(r'const VERSION = "([^"]+)";', r'const VERSION = "pub-\1";', sw, count=1)
(out / "sw.js").write_text(sw, encoding="utf-8")
for f in ["icon-192.png", "icon-512.png"]:
    shutil.copyfile(src / f, out / f)
for bad in ["PIPSTAR", "Vismaya", "AIza", "math-quest-9f57b", "Russian School", "RSM"]:
    assert bad not in (out / "index.html").read_text(encoding="utf-8"), f"public build leaked: {bad}"
print("public edition built in", out)
