#!/usr/bin/env python3
"""RQIR Iteration 127 — final Paper III priority/claim matrix checker.

This checker encodes the comparator classes audited in the literature review.
It does not prove novelty and contains no web scraping. The source URLs/DOIs are
stored in the accompanying document and must be refreshed before submission.
"""

COMPARATORS = [
    ("nuisance-aware-OED", True, False),
    ("system-identification-transfer-calibration", True, False),
    ("QGEM-entanglement-resource-design", True, False),
    ("classical-gravity-decoherence-diffusion", True, False),
    ("classical-gravity-cross-correlation", True, False),
    ("measurement-disturbance-gravity-test", True, False),
    ("interferometric-quantum-nature-test", True, False),
    ("postquantum-stochastic-gravity-PSD", True, False),
    ("levitated-force-transfer-cross-spectral", True, False),
    ("end-to-end-RQIR-interface-to-wallclock-certificate", False, True),
]

# tuple fields: (class, prior_art_exists_for_ingredients, candidate_RQIR_integration_gap)

def main() -> None:
    names = [x[0] for x in COMPARATORS]
    assert len(names) == len(set(names))
    assert sum(int(x[1]) for x in COMPARATORS) >= 8
    rqir = [x for x in COMPARATORS if x[2]]
    assert len(rqir) == 1
    assert rqir[0][0] == "end-to-end-RQIR-interface-to-wallclock-certificate"
    # Guardrail: the matrix must not label any standard ingredient as unique RQIR novelty.
    for name, prior, gap in COMPARATORS[:-1]:
        assert prior and not gap
    print("RQIR Iteration 127 priority matrix: PASS")
    print("comparator classes", len(COMPARATORS))
    print("candidate integration-level gap", rqir[0][0])
    print("novelty status: finite-search candidate, not proof of priority")


if __name__ == "__main__":
    main()
