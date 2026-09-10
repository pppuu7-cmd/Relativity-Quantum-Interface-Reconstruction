# RQIR Paper III — Quantum Science and Technology submission package

This directory contains the journal-adapted version of the scientifically frozen Paper III.

## Files

- `main.tex` and `sections/*.tex` — QST review-manuscript LaTeX source.
- `cover_letter_qst.tex` — one-page QST cover letter source.
- `QST_SUBMISSION_METADATA.md` — title, article type, keywords, author metadata, subject fit, and copy-ready submission text.
- `QST_SUBMISSION_CHECKLIST.md` — final pre-submit checks and the only author declarations still requiring confirmation.

## Formatting choice

IOP states that its LaTeX template is optional and accepts common LaTeX variants; initial submission requires a complete PDF. The review manuscript therefore uses standard 12-pt single-column LaTeX for readability rather than attempting to imitate the typeset journal layout.

## QST adaptation

The title and opening narrative foreground quantum sensing, quantum metrology, Raman atom interferometry, nuisance-aware resource allocation, and traceable calibration. The abstract is 255 words. The manuscript uses an Introduction / Methods / Results / Discussion / Conclusion structure, embedded figures and tables, a numerical reference style with DOI information, a Data availability statement, and disclosure of generative-AI assistance.

## Scientific boundary

The QST adaptation changes presentation and audience framing only. The apparatus numbers, failure controls, provenance boundaries, and resource-closure claims remain downstream of the frozen Paper-III scientific manifest in the repository. It does not claim an observed RQIR departure or select a microscopic gravity model.

## Local preflight

The final review PDF was built twice with `pdflatex` after source-cleanup:

- 17 pages;
- no undefined citations or references;
- no overfull boxes;
- figures and tables embedded in the manuscript;
- rendered PDF visually inspected after the final source correction.

Journal-portal declarations concerning competing interests, funding, originality/exclusivity, and the final peer-review anonymity choice remain author-confirmation items rather than inferred facts.
