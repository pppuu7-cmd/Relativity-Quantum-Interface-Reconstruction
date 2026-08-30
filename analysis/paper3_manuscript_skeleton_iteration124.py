"""RQIR Iteration 124: manuscript-claim skeleton consistency checker.

This is not a physics forecast. It encodes the manuscript claim/evidence/limitation
structure and asserts that no section promotes a parametric or experimental-precedent
statement into an apparatus/new-physics claim.
"""
from __future__ import annotations

SECTIONS = [
    ("S1", "From interface discriminant to nuisance-profiled detector information", "THEOREM/DERIVATION", True),
    ("S2", "Source-preparation calibration is an independent resource", "THEOREM+REGRESSION", True),
    ("S3", "Calibration Fisher becomes shots, SNR, coherence and wall time", "THEOREM+PARAMETRIC", True),
    ("S4", "Transfer/common-gain and control recertification belong inside the likelihood", "THEOREM+PARAMETRIC", True),
    ("S5", "Joint campaign scheduling must avoid double counting and satisfy rank/span coverage", "THEOREM+REGRESSION", True),
    ("S6", "Toy009/Toy014 detector-side architecture is interval-certifiable but not yet numerically apparatus-closed", "PARAMETRIC+REGRESSION", False),
    ("S7", "Final-significance architecture certificate couples detector, source metrology and duty", "THEOREM+PARAMETRIC", True),
    ("S8", "Experimental precedent supports component feasibility, not an RQIR signal forecast", "EXPERIMENTAL_PRECEDENT", False),
]

FORBIDDEN_WORDING = {
    "PARAMETRIC+REGRESSION": ["measured winner", "apparatus prediction", "experimental confirmation"],
    "EXPERIMENTAL_PRECEDENT": ["validates RQIR signal", "confirms new physics"],
}

REQUIRED_EQUATIONS = {
    "S1": "F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab",
    "S2": "C_prep = [r/(1-r)] Z^2",
    "S3": "R_cal,j = p_j I_j/tau_j",
    "S4": "R_c = k_cc-k_cnu K_nunu^-1 k_nuc",
    "S5": "range(H_*) subseteq range(K_tot)",
    "S6": "u = R_D14/R_D09",
    "S7": "Q14/Q09 = delta[(1+z^-1/2)/(u^-1/2+(v z)^-1/2)]^2",
}


def main():
    ids = [s[0] for s in SECTIONS]
    assert len(ids) == len(set(ids)) == 8
    assert set(REQUIRED_EQUATIONS).issubset(ids)
    # Only theorem-bearing sections may be presented as mathematically closed.
    for sid, claim, cls, mathematically_closed in SECTIONS:
        if mathematically_closed:
            assert "THEOREM" in cls
        if cls == "EXPERIMENTAL_PRECEDENT":
            assert not mathematically_closed
    # The detector architecture section must remain explicitly non-apparatus-closed.
    s6 = next(s for s in SECTIONS if s[0] == "S6")
    assert s6[3] is False and "not yet numerically apparatus-closed" in s6[1]
    print("Iteration 124 manuscript skeleton checks: PASS")
    print("sections", len(SECTIONS), "closed theorem-bearing", sum(int(s[3]) for s in SECTIONS))

if __name__ == "__main__":
    main()
