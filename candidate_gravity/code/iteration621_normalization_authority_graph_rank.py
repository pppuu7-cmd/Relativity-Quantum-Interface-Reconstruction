#!/usr/bin/env python3
"""Iteration 621: normalization-authority graph/rank audit.

This audit is deliberately independent of Candidate values and of any guessed
N_native. It encodes only frozen authority links summarized by Iter617/620.
Two internally connected convention sectors are present:
  source: Iter589/594/616;
  native: Iter147/149/218/338.
No frozen cross-sector source->Gamma3 absolute normalization equation exists.

For k disconnected nonzero-complex normalization components, quotienting a
single irrelevant common convention leaves k-1 relative C* degrees of freedom.
The expected result here is therefore exactly one relative scale/phase DOF.
"""

from __future__ import annotations

import json

NODES = {
    "source_K_relative": {"authority": [589, 594]},
    "source_S_amp": {"authority": [616]},
    "source_q2_binding": {"authority": [588, 616]},
    "native_Gamma3": {"authority": [147, 149]},
    "native_chi2R": {"authority": [147, 149]},
    "native_connection": {"authority": [218, 338]},
}

EDGES = [
    ("source_K_relative", "source_S_amp"),
    ("source_S_amp", "source_q2_binding"),
    ("native_Gamma3", "native_chi2R"),
    ("native_Gamma3", "native_connection"),
]

# Iter617's authoritative negative audit: no prior equation fixes the absolute
# source-endpoint-amputated MSSC -> native gravitational Gamma3 bridge.
CROSS_SECTOR_BRIDGE_EQUATIONS = []


def connected_components(nodes, edges):
    adj = {n: set() for n in nodes}
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    seen = set()
    components = []
    for n in sorted(nodes):
        if n in seen:
            continue
        stack = [n]
        comp = []
        while stack:
            x = stack.pop()
            if x in seen:
                continue
            seen.add(x)
            comp.append(x)
            stack.extend(sorted(adj[x] - seen))
        components.append(sorted(comp))
    return components


def main():
    components = connected_components(NODES, EDGES + CROSS_SECTOR_BRIDGE_EQUATIONS)
    n_components = len(components)
    remaining_relative_complex_dof = max(0, n_components - 1)

    assert n_components == 2, components
    assert len(CROSS_SECTOR_BRIDGE_EQUATIONS) == 0
    assert remaining_relative_complex_dof == 1

    result = {
        "iteration": 621,
        "authority_components": components,
        "cross_sector_bridge_equation_count": 0,
        "normalization_component_count": n_components,
        "quotient_by_one_common_convention": True,
        "remaining_relative_complex_normalization_dof": remaining_relative_complex_dof,
        "remaining_symbol": "N_native",
        "candidate_values_used": False,
        "threshold_introduced": False,
        "classification": "PASS_ITER621_NORMALIZATION_AUTHORITY_GRAPH_RANK_AUDIT__ONE_CROSS_SECTOR_COMPLEX_SCALE_REMAINS_UNFIXED__OPERATIONAL_BLOCKED_NON_RESIDUAL",
        "MODEL_READINESS": "24%",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
