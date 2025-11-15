#!/bin/bash
python3 - <<'PY'
from pathlib import Path
path = Path('build-dissertation.sh')
text = path.read_text()
old = '--filter pandoc-crossref \\\n  --number-sections \\\n  -o dissertation.pdf \\\n  --pdf-engine=xelatex \\\n  --citeproc'
new = '--filter pandoc-crossref \\\n  -o dissertation.pdf \\\n  --pdf-engine=xelatex \\\n  --citeproc'
text = text.replace(old, new)
path.write_text(text)
PY
