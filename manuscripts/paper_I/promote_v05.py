from pathlib import Path

path = Path(__file__).with_name("main.tex")
text = path.read_text()
bs = chr(92)

old = "Before submission the temporary Actions artifact will be copied to a long-retention repository or archival record."
new = (
    "A long-retention textual mirror of the clean output is stored at "
    + bs
    + "texttt{manuscripts/paper"
    + bs
    + "_I/certificates/TOY009"
    + bs
    + "_TOY010"
    + bs
    + "_CLEANRUN"
    + bs
    + "_2026-09-08.md}, so the manuscript authority does not depend permanently on the temporary Actions retention window."
)

count = text.count(old)
if count != 1:
    raise SystemExit(f"Expected exactly one obsolete retention sentence, found {count}")

text = text.replace(old, new)
path.write_text(text)
print("Paper I v0.5 permanent-certificate reference synchronized")
