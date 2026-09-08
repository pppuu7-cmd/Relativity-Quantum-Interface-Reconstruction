from pathlib import Path

path = Path(__file__).with_name("main.tex")
text = path.read_text()
bs = chr(92)


def latex(s: str) -> str:
    return s.replace("§", bs)


def replace_once(old: str, new: str) -> None:
    global text
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"Expected exactly one match, found {count}: {old[:100]!r}")
    text = text.replace(old, new)


def replace_paragraph(prefix: str, new: str) -> None:
    global text
    start = text.find(prefix)
    if start < 0:
        raise SystemExit(f"Paragraph prefix not found: {prefix!r}")
    if text.find(prefix, start + 1) >= 0:
        raise SystemExit(f"Paragraph prefix is not unique: {prefix!r}")
    end = text.find("\n\n", start)
    if end < 0:
        raise SystemExit(f"Paragraph terminator not found: {prefix!r}")
    text = text[:start] + new + text[end:]


replace_once("Working manuscript v0.4 / 8 September 2026", "Working manuscript v0.5 / 8 September 2026")

replace_paragraph(
    "The deterministic scans Toy009 and Toy010 are used to test the hypotheses",
    latex("""The deterministic constructions Toy009 and Toy010 test the hypotheses of Proposition~§ref{prop:rqir-thm-001}; they do not replace its proof. Both use a 25-dimensional Hermitian source parameterization and realize the codimension-one regime $§operatorname{rank}A=24$ under the declared numerical-rank rule. A clean independent GitHub Actions rerun on 8 September 2026, with Python 3.12.14 and NumPy 2.1.3, reproduced the frozen Toy009/Toy010 regression checks at repository commit §texttt{763757788397564d180cfd6b33c28db57412d74c}.""")
)

replace_paragraph(
    "Items 1--5 are mathematical or numerical checks of the construction.",
    latex("""Items 1--5 are mathematical or numerical checks of the construction. Item 6 is a provenance requirement for manuscript-level numerical claims. All six checks are now satisfied by the frozen clean-run certificate. In Toy009 the maximum equality residual is $2.2§times10^{-16}$, the selected mean/noise differences are below $2§times10^{-18}$, both paired density operators are positive, and the ordered responses are opposite with magnitude approximately $1.21§times10^{-2}$. Keeping the Toy009 source fixed while changing only the finite calibration geometry, Toy010 retains $§operatorname{rank}A=24$, gives a maximum equality residual $4.4§times10^{-16}$, retains positive paired states and equal selected mean/noise coordinates, and produces opposite ordered responses of magnitude approximately $1.33§times10^{-2}$. The normalized null directions of the inherited Toy009 and Toy010 calibrations differ by approximately $37.7^{§circ}$. These values are finite-dimensional construction diagnostics rather than experimental forecasts or evidence that gravity transmits the corresponding response coordinate.""")
)

replace_paragraph(
    "Before submission, every numerical statement and every final plot/table must point",
    latex("""The Toy009/Toy010 numerical statements are bound to the frozen generation scripts and the clean-run authority recorded in §texttt{manuscripts/paper§_I/TOY009§_TOY010§_REPRO§_MANIFEST.md}. Workflow run §texttt{34177686395} completed successfully at commit §texttt{763757788397564d180cfd6b33c28db57412d74c}; the uploaded certificate artifact is §texttt{paper-i-toy009-toy010-certificate}, artifact ID §texttt{10037815979}, with archive digest §texttt{sha256:6363cfe9f5fad3ad7d04363921cc6d66e051ce7beaf9e22a3940a1b38c654b95}. A long-retention textual mirror of the clean output is stored at §texttt{manuscripts/paper§_I/certificates/TOY009§_TOY010§_CLEANRUN§_2026-09-08.md}. The authority record includes the exact code revision, seeds/configuration, Python/NumPy environment, numerical-rank policy, positivity/equality diagnostics, ordered-response values and file hashes.""")
)

replace_paragraph(
    "Any quantity calibrated to or compared with an external source additionally requires",
    latex("""Any quantity calibrated to or compared with an external source additionally requires the authority record, convention and extraction rule for that source. A manuscript-level external numerical statement is promotable only when all fields relevant to its evidence class in Table~§ref{tab:evidence-promotion} are frozen. Missing external authority does not invalidate the analytic theorem or the internally reproduced Toy009/Toy010 certificate; it blocks only promotion of the affected external comparison or calibrated number.""")
)

path.write_text(text)
print("Paper I v0.5 guarded replacements applied successfully")
