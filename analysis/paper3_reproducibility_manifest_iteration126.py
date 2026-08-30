#!/usr/bin/env python3
"""RQIR Iteration 126 — Paper III minimum reproducibility manifest checker.

Run from repository root. The checker does not claim to replace environment/CI
execution; it verifies that the manuscript-bearing regression authorities exist,
are uniquely named in the manifest, and contain the expected semantic anchors.
External-literature audits are intentionally classified separately from offline
numerical regressions.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MANIFEST = [
    ("final-target", "analysis/robust_campaign_source_target_iteration104.py", "22.5", "deterministic"),
    ("final-crossover", "analysis/final_significance_architecture_crossover_iteration105.py", "u", "deterministic"),
    ("same-state-f2f", "analysis/same_state_f2f_calibration_protocol_iteration101.py", "rho", "deterministic"),
    ("complex-campaign", "analysis/full_complex_campaign_allocation_iteration103.py", "marginal", "deterministic"),
    ("common-gain", "analysis/full_complex_common_gain_rate_iteration115.py", "common", "deterministic"),
    ("joint-reference", "analysis/joint_reference_quota_iteration116.py", "lambda", "deterministic"),
    ("span-rank", "analysis/reference_span_rank_iteration117.py", "rank", "deterministic"),
    ("toy009-014-span", "analysis/toy009_toy014_calibration_span_iteration118.py", "22", "deterministic"),
    ("covariance-partition", "analysis/full_covariance_endpoint_partition_iteration119.py", "partition", "deterministic"),
    ("calibration-bracket", "analysis/calibration_cover_bracket_iteration120.py", "gamma", "deterministic"),
    ("detector-bracket", "analysis/detector_rate_bracket_iteration121.py", "u", "deterministic"),
    ("apparatus-evidence", "analysis/external_apparatus_evidence_matrix_iteration122.py", "evidence", "external-evidence"),
    ("claim-novelty", "analysis/paper3_claim_evidence_matrix_iteration123.py", "claim", "editorial-audit"),
    ("manuscript-skeleton", "analysis/paper3_manuscript_skeleton_iteration124.py", "S6", "editorial-audit"),
    ("notation", "analysis/paper3_notation_dependency_audit_iteration125.py", "final_fisher", "deterministic"),
]

DOC_AUTHORITIES = [
    "docs/PAPER_III_ROBUST_CAMPAIGN_SOURCE_TARGET_ITERATION104.md",
    "docs/PAPER_III_FINAL_SIGNIFICANCE_ARCHITECTURE_CROSSOVER_ITERATION105.md",
    "docs/PAPER_III_SAME_STATE_F2F_CALIBRATION_PROTOCOL_ITERATION101.md",
    "docs/PAPER_III_FULL_COMPLEX_CAMPAIGN_ALLOCATION_ITERATION103.md",
    "docs/PAPER_III_FULL_COMPLEX_COMMON_GAIN_RATE_CERTIFICATE_ITERATION115.md",
    "docs/PAPER_III_JOINT_REFERENCE_QUOTA_ITERATION116.md",
    "docs/PAPER_III_REFERENCE_SPAN_RANK_ITERATION117.md",
    "docs/PAPER_III_TOY009_TOY014_CALIBRATION_SPAN_ITERATION118.md",
    "docs/PAPER_III_FULL_COVARIANCE_ENDPOINT_PARTITION_ITERATION119.md",
    "docs/PAPER_III_CALIBRATION_COVER_BRACKET_ITERATION120.md",
    "docs/PAPER_III_DETECTOR_RATE_BRACKET_ITERATION121.md",
    "docs/PAPER_III_EXTERNAL_APPARATUS_EVIDENCE_ITERATION122.md",
    "docs/PAPER_III_CLAIM_NOVELTY_AUDIT_ITERATION123.md",
    "docs/PAPER_III_MANUSCRIPT_SKELETON_ITERATION124.md",
    "docs/PAPER_III_NOTATION_DEPENDENCY_AUDIT_ITERATION125.md",
]


def main() -> None:
    labels = [x[0] for x in MANIFEST]
    assert len(labels) == len(set(labels)), "duplicate manifest labels"

    counts = {"deterministic": 0, "external-evidence": 0, "editorial-audit": 0}
    for label, rel, anchor, cls in MANIFEST:
        path = ROOT / rel
        assert path.exists(), f"missing manifest script: {rel}"
        text = path.read_text(encoding="utf-8")
        assert anchor.lower() in text.lower(), f"semantic anchor {anchor!r} missing in {rel}"
        counts[cls] += 1

    for rel in DOC_AUTHORITIES:
        assert (ROOT / rel).exists(), f"missing canonical document: {rel}"

    # The manifest must explicitly keep external-evidence work distinct from
    # deterministic regressions so a literature table cannot masquerade as an
    # offline reproduction of an apparatus result.
    assert counts["deterministic"] >= 10
    assert counts["external-evidence"] >= 1
    assert counts["editorial-audit"] >= 2

    print("RQIR Iteration 126 reproducibility manifest: PASS")
    print("manifest entries", len(MANIFEST))
    print("classes", counts)
    print("canonical docs", len(DOC_AUTHORITIES))


if __name__ == "__main__":
    main()
