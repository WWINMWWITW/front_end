"""Compile lab1/scss/main.css — requires: pip install libsass"""
import pathlib
import sys

try:
    import sass
except ImportError:
    print("Run: pip install libsass", file=sys.stderr)
    raise SystemExit(1)

root = pathlib.Path(__file__).resolve().parents[1]
scss = root / "scss" / "main.scss"
out = root / "css" / "main.css"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(sass.compile(filename=str(scss)), encoding="utf-8")
print("wrote", out, out.stat().st_size, "bytes")
