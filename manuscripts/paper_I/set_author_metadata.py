from pathlib import Path

path = Path(__file__).with_name("main.tex")
text = path.read_text()

old = r"""\author{Authors to be fixed before submission}
\date{Working manuscript v0.5 / 8 September 2026}"""

new = r"""\author{Aleksey Buyanov\\
\small Independent Researcher\\
\small Moscow, Russia\\
\small \href{mailto:pppuu7@gmail.com}{pppuu7@gmail.com}\\
\small \href{https://orcid.org/0009-0001-2621-9305}{ORCID: 0009-0001-2621-9305}}
\date{Working manuscript v0.6 / 8 September 2026}"""

count = text.count(old)
if count != 1:
    raise SystemExit(f"Expected exactly one author placeholder block, found {count}")

path.write_text(text.replace(old, new))
print("Author metadata inserted; manuscript advanced to v0.6")
