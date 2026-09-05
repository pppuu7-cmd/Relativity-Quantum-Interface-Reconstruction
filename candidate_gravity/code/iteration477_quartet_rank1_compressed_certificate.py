#!/usr/bin/env python3
"""Iteration 477: exact quartet-space compression of the frozen central4xcentral4 precision functional.

This audit is algebraic only. It compresses the full 4x4 odd-odd discrepancy sector to the
four positive-node signed quartets without assuming u<->v symmetry, and identifies the
unique quartet direction that can change the mixed derivative.
"""
from fractions import Fraction as F
import json

# Positive-node one-dimensional central4 weights.
g = [F(2, 3), F(-1, 12)]  # nodes +1,+2
M = [[F(64), F(-8)], [F(-8), F(1)]]
Wq = [[x / F(144) for x in row] for row in M]  # g g^T


def frob2(A, B):
    return sum((A[i][j] * B[i][j] for i in range(2) for j in range(2)), F(0))


def scale(a, A):
    return [[a * A[i][j] for j in range(2)] for i in range(2)]


def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(2)] for i in range(2)]


def q(x):
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


# Exact rank-1 coefficient structure.
assert Wq == [[F(4, 9), F(-1, 18)], [F(-1, 18), F(1, 144)]]
assert M[0][0] * M[1][1] - M[0][1] * M[1][0] == 0
assert sum((x * x for x in g), F(0)) == F(65, 144)
Wq2 = frob2(Wq, Wq)
assert Wq2 == F(4225, 20736)

# Signed quartet definition for each positive magnitude pair (a,b):
# Q_ab = F(+a,+b)-F(-a,+b)-F(+a,-b)+F(-a,-b).
# Then DeltaD = <Wq, DeltaQ>_F exactly.
Q = [[F(3), F(-5)], [F(7), F(11)]]  # generic exact probe
DeltaD = frob2(Wq, Q)
Qsens = scale(DeltaD / Wq2, Wq)
Qnull = sub(Q, Qsens)
assert frob2(Wq, Qsens) == DeltaD
assert frob2(Wq, Qnull) == 0

# Integer basis for the three-dimensional exact quartet nullspace, written in
# vector order (Q11,Q12,Q21,Q22). Each is orthogonal to (64,-8,-8,1).
null_basis = [
    (1, 0, 0, -64),
    (0, 1, 0, 8),
    (0, 0, 1, 8),
]
weight_vec = (64, -8, -8, 1)
assert all(sum(F(a) * F(b) for a, b in zip(weight_vec, n)) == 0 for n in null_basis)

# Exact relation between quartet norm and the full 4x4 odd-odd projector norm.
# For X = Qo DeltaF Qo, each positive-node value is DeltaQ_ab/4, repeated over
# four sign-related entries, so ||X||_F = (1/2)||DeltaQ||_F.
quartet_to_full_oddodd_norm_factor = F(1, 2)
full_sensitive_norm_factor = F(72, 65)   # ||DeltaF_sens||_F / |DeltaD|
quartet_sensitive_norm_factor = F(144, 65)  # ||DeltaQ_sens||_F / |DeltaD|
assert quartet_sensitive_norm_factor * quartet_to_full_oddodd_norm_factor == full_sensitive_norm_factor

result = {
    "iteration": 477,
    "classification": "PASS_QUARTET_RANK1_COMPRESSED_PRECISION_CERTIFICATE__DIAGNOSTIC_ONLY_NON_PROMOTING",
    "scientific_gate_pass": True,
    "promotes_physical_coordinate": False,
    "MODEL_READINESS": "24%",
    "readiness_change_pp": 0,
    "quartet_definition": "DeltaQ_ab=DeltaF(+a,+b)-DeltaF(-a,+b)-DeltaF(+a,-b)+DeltaF(-a,-b), a,b in {1,2}",
    "quartet_functional": {
        "positive_weight_vector_g": [q(x) for x in g],
        "weight_matrix_Wq": [[q(x) for x in row] for row in Wq],
        "integer_weight_matrix": M,
        "identity": "DeltaD=<Wq,DeltaQ>_F=(64 DeltaQ11-8 DeltaQ12-8 DeltaQ21+DeltaQ22)/144",
        "weight_rank": 1,
        "weight_frobenius_norm_squared": q(Wq2),
        "weight_frobenius_norm": "65/144",
    },
    "exact_structure": {
        "quartet_space_dimension": 4,
        "derivative_sensitive_dimension": 1,
        "quartet_nullspace_dimension": 3,
        "integer_nullspace_basis_Q11_Q12_Q21_Q22": [list(x) for x in null_basis],
        "sensitive_projection": "DeltaQ_sens=(144/4225) DeltaD [[64,-8],[-8,1]]",
        "sensitive_norm": "||DeltaQ_sens||_F=(144/65)|DeltaD|",
        "full_oddodd_norm_relation": "||Qo DeltaF Qo||_F=(1/2)||DeltaQ||_F",
        "equivalent_bound": "|DeltaD| <= (65/144)||DeltaQ||_F = (65/72)||Qo DeltaF Qo||_F",
    },
    "guardrails": [
        "NO_UV_SYMMETRY_ASSUMPTION",
        "Q12_AND_Q21_REMAIN_DISTINCT",
        "DIAGNOSTIC_PROVENANCE_ONLY",
        "NO_THRESHOLD_CHANGE",
        "NO_ESTIMATOR_CHANGE",
        "NO_SUPPORT_DEDUPLICATION",
        "NO_PHYSICAL_PROMOTION",
        "NO_ANSATZ003",
        "NO_FISHER_RESOURCES",
    ],
    "interpretation": "The future assembled MP precision audit can compute the exact derivative-sensitive discrepancy directly from four signed quartets. Three independent quartet discrepancy combinations are exact derivative null modes. This is an implementation/provenance compression only and does not permit dropping or identifying source coordinates.",
    "next_gate": "raw-consume canonical Iteration455 rank11 run 33989317870 fail-closed; if PASS advance only to next UNTESTED frozen-manifest coordinate",
}
print(json.dumps(result, indent=2, sort_keys=True))
