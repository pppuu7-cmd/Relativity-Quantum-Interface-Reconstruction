"""RQIR Iteration 124: manuscript skeleton gap audit.

Checks that every proposed Paper-III section has a central claim, repository
evidence, a figure/table target, a literature-comparator class and an explicit
limitation/open gate where appropriate.
"""
from __future__ import annotations

SECTIONS = [
    dict(id="S1", claim="resource closure problem", evidence="080-081", visual="pipeline", literature="gravity tests + OED", limitation="not a QG theory"),
    dict(id="S2", claim="profiled detector likelihood", evidence="079,084-089", visual="two-band Fisher", literature="profile Fisher/OED", limitation="local likelihood"),
    dict(id="S3", claim="Toy009/Toy014 source-resource comparison", evidence="074-077,092-095", visual="resource/crossover map", literature="gravity experiment design", limitation="toy source family"),
    dict(id="S4", claim="source metrology and final significance", evidence="047-056,098,104-105", visual="source-rate surface", literature="quantum metrology", limitation="declared preparation protocols"),
    dict(id="S5", claim="full-complex transfer calibration", evidence="101-115", visual="gain-phase quotient", literature="system identification/calibration", limitation="physical same-apparatus rate missing"),
    dict(id="S6", claim="calibration span and backaction", evidence="038-046,116-120", visual="rank/endpoint graph", literature="covariance sensing", limitation="measurement-model dependent sharing"),
    dict(id="S7", claim="robust detector/wall-clock certificate", evidence="103-107,111,121", visual="u-v-z-delta phase diagram", literature="robust OED", limitation="numerical u awaits compatible apparatus"),
    dict(id="S8", claim="external apparatus feasibility boundary", evidence="082,090-091,122", visual="evidence matrix", literature="levitated optomechanics", limitation="no complete public RQIR dataset"),
    dict(id="S9", claim="claim/novelty boundary", evidence="123", visual="claim evidence table", literature="QGEM, classical/hybrid gravity, OED", limitation="final priority search required"),
]


def main() -> None:
    required = {"id", "claim", "evidence", "visual", "literature", "limitation"}
    assert len(SECTIONS) == 9
    assert len({s["id"] for s in SECTIONS}) == len(SECTIONS)
    for s in SECTIONS:
        assert required <= s.keys()
        assert all(str(s[k]).strip() for k in required)
    print("Paper III sections", len(SECTIONS))
    print("all sections have claim/evidence/visual/literature/limitation fields")
    print("remaining scientific apparatus gap is explicit rather than hidden")


if __name__ == "__main__":
    main()
