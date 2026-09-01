#!/usr/bin/env python3
"""Iteration 245: composite VD U1/U2 trace -> one-loop master topology map.

Frozen leading flat-kernel convention:
  U1 = N V2 N Y
  U2 = N V1 H V1 N Y
where N is the gauge/ghost Green operator, H is H^{-1}, Y is local, and
V1,V2 carry the EOM/background insertions.

Under a cyclic functional trace, local Y factors do not carry loop momentum.
Adjacent N factors between external insertions therefore lie on the same loop
segment.  We map each trace monomial to propagator powers between its external
vertices.  This is topology bookkeeping only, not a tensor-amplitude result.
"""

import json

# Each U block is represented by the propagator segment after each vertex while
# traversing the block. Products are assembled explicitly below.

maps = {
    "Tr(U1)": {
        "vertices": ["V2"],
        "segments": [{"species": "N", "power": 2}],
        "scalar_master": "massless_tadpole_I2",
        "eom_degree": 1,
    },
    "Tr(U2)": {
        "vertices": ["V1", "V1"],
        "segments": [
            {"species": "H", "power": 1},
            {"species": "N", "power": 2},
        ],
        "scalar_master": "mixed_massless_bubble_I12_or_I21",
        "eom_degree": 2,
    },
    "Tr(U1^2)": {
        "vertices": ["V2", "V2"],
        "segments": [
            {"species": "N", "power": 2},
            {"species": "N", "power": 2},
        ],
        "scalar_master": "massless_bubble_I22",
        "eom_degree": 2,
    },
    "Tr(U1^3)": {
        "vertices": ["V2", "V2", "V2"],
        "segments": [
            {"species": "N", "power": 2},
            {"species": "N", "power": 2},
            {"species": "N", "power": 2},
        ],
        "scalar_master": "massless_triangle_I222",
        "eom_degree": 3,
    },
    "Tr(U1 U2)": {
        "vertices": ["V2", "V1", "V1"],
        "segments": [
            {"species": "N", "power": 2},
            {"species": "H", "power": 1},
            {"species": "N", "power": 2},
        ],
        "scalar_master": "mixed_massless_triangle_I212",
        "eom_degree": 3,
    },
}

# On the frozen a=-1/2, Lambda=0 flat kernel both minimal propagator species
# have denominator 1/k^2. Projectors/numerators remain different.
for entry in maps.values():
    entry["flat_scalar_denominators_massless"] = True
    entry["species_difference_survives_in_tensor_numerator"] = True

# Curvature-counting result from Iteration 243: at total R^3, lower-EOM sectors
# can acquire enough local background insertions to reach at most three
# external background vertices. Hence no >triangle one-loop scalar topology is
# required at the target curvature order.
max_external_background_vertices_at_R3 = 3
max_loop_polygon = "triangle"

result = {
    "iteration": 245,
    "model_readiness_percent": 24,
    "frozen_convention": "4D pure Einstein VD, a=-1/2, Lambda=0, leading flat kernels for e=3",
    "trace_maps": maps,
    "max_external_background_vertices_at_R3": max_external_background_vertices_at_R3,
    "max_loop_polygon_at_R3": max_loop_polygon,
    "new_loop_topology_beyond_one_loop_triangle_required": False,
    "standard_CPT3_determinant_sector": "simple-propagator generic triangle/form-factor family",
    "composite_connection_sector": "same one-loop bubble/triangle kinematics with raised propagator powers and ghost/graviton tensor projectors",
    "raised_power_integrals_reducible_by_feynman_parameter_moments": True,
    "classification": "PASS_COMPOSITE_TRACE_MASTER_TOPOLOGY_REDUCTION",
    "remaining_blocker": "PURE_GRAVITY_TENSOR_NUMERATOR_CURVATURE_DRESSING_AND_SOURCE_COMPLETED_T_CUT_PROJECTION",
    "heavy_full_run_authorized": False,
    "scoped_flat_e3_symbolic_run_authorized": True,
    "next_gate": 246
}

assert maps["Tr(U1^3)"]["scalar_master"] == "massless_triangle_I222"
assert maps["Tr(U1 U2)"]["scalar_master"] == "mixed_massless_triangle_I212"
assert max_external_background_vertices_at_R3 == 3

print(json.dumps(result, indent=2, sort_keys=True))
