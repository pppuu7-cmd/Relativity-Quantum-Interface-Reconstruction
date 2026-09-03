#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 340.

Primary-authority audit of the Vilkovisky U2 operator, using Giacchini,
de Paula Netto & Shapiro, PRD 102, 106006 (2020), arXiv:2006.04217v4,
Eqs. (14)-(17).

Eq. (17):
 U2^a_b = N^{a g} A_{i g} (H^{-1})^{ij} A_{j d} N^{d s} Y_{s b},
 A_{i g} := (D_i R^k_g) epsilon_k,
 with H . H^{-1} = -1.

If A is stored field x ghost, the exact matrix orientation is
 N @ A.T @ Hinv @ A @ N @ Y.
For the Iteration-319/339 differential operator K == paper H,
 Hinv_VD = - K^{-1}.  The momentum-routing identity itself remains valid;
only the object inserted into U2 carries this additional frozen minus sign.
"""
from fractions import Fraction as F
import json

# Tiny exact-rational fixture: ghost dimension 2, field dimension 3.
N = [[F(2), F(1)], [F(-1), F(3)]]
A = [[F(1), F(2)], [F(-2), F(1)], [F(3), F(-1)]]  # field x ghost
Kinv = [[F(2), F(0), F(1)], [F(0), F(1), F(-1)], [F(1), F(-1), F(3)]]
Hinv = [[-x for x in row] for row in Kinv]
Y = [[F(1), F(2)], [F(0), F(1)]]

def mm(X, Z):
    return [[sum(X[i][k] * Z[k][j] for k in range(len(Z)))
             for j in range(len(Z[0]))] for i in range(len(X))]

def tr(X):
    return [list(r) for r in zip(*X)]

matrix_form = mm(mm(mm(mm(mm(N, tr(A)), Hinv), A), N), Y)

# Independent explicit-index contraction of Eq. (17).
explicit = [[F(0) for _ in range(2)] for _ in range(2)]
for a in range(2):
    for b in range(2):
        s = F(0)
        for g in range(2):
            for i in range(3):
                for j in range(3):
                    for d in range(2):
                        for sig in range(2):
                            s += N[a][g] * A[i][g] * Hinv[i][j] * A[j][d] * N[d][sig] * Y[sig][b]
        explicit[a][b] = s

wrong_no_transpose_possible = False
# A is 3x2, so N(2x2) @ A(3x2) is not even type-compatible.
if len(N[0]) == len(A):
    wrong_no_transpose_possible = True

# Global sign check against using ordinary +K^{-1} in the same topology.
plus_form = mm(mm(mm(mm(mm(N, tr(A)), Kinv), A), N), Y)
sign_exact = all(matrix_form[i][j] == -plus_form[i][j] for i in range(2) for j in range(2))

assert matrix_form == explicit
assert not wrong_no_transpose_possible
assert sign_exact

result = {
    "iteration": 340,
    "MODEL_READINESS": "24%",
    "primary_authority": "Giacchini-de Paula Netto-Shapiro 2020, arXiv:2006.04217v4, Eqs.14-17",
    "u2_component_definition": "A_{i gamma}=(D_i R^k_gamma) epsilon_k",
    "v1_storage": "A: field x ghost",
    "v1_left_orientation": "A^T: ghost x field",
    "v1_right_orientation": "A: field x ghost",
    "u2_matrix_order": "N_left @ A.T @ Hinv_VD @ A @ N_right @ Y",
    "paper_inverse_convention": "H * Hinv_VD = -1",
    "same_parent_bridge": "Hinv_VD = -K^{-1} when K is the Iteration-319 differential operator",
    "iteration339_status": "shifted inverse routing retained; interpretation as the Eq17 U2 Green object requires one global minus sign",
    "exact_index_vs_matrix_contraction_pass": True,
    "exact_global_sign_check_pass": sign_exact,
    "classification": "PASS_U2_PRIMARY_AUTHORITY_V1_LEFT_RIGHT_ORIENTATION_AND_VD_GREEN_MINUS_SIGN__PHYSICAL_A1_A2_COMPONENTS_REMAIN_BLOCKED",
    "candidate_gravity_consistency_fail": False,
    "candidate_residual": False,
    "next_gate": "derive physical same-parent A1/A2=(D R)*epsilon background expansions in this frozen orientation; then bridge N/Y routing before Tr U2",
}
print(json.dumps(result, indent=2, sort_keys=True))
