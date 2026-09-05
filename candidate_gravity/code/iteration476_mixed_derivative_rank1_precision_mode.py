#!/usr/bin/env python3
from fractions import Fraction as F
import json

c = [F(1,12), F(-2,3), F(2,3), F(-1,12)]
N = 4

def dotv(a,b): return sum((x*y for x,y in zip(a,b)), F(0))
def frob(A,B): return sum((A[i][j]*B[i][j] for i in range(N) for j in range(N)), F(0))
def outer(a,b): return [[a[i]*b[j] for j in range(N)] for i in range(N)]
def matmul(A,B): return [[sum((A[i][k]*B[k][j] for k in range(N)),F(0)) for j in range(N)] for i in range(N)]
def matsub(A,B): return [[A[i][j]-B[i][j] for j in range(N)] for i in range(N)]
def mateq(A,B): return all(A[i][j]==B[i][j] for i in range(N) for j in range(N))
def scale(a,A): return [[a*A[i][j] for j in range(N)] for i in range(N)]
def q(x): return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)

I = [[F(int(i==j)) for j in range(N)] for i in range(N)]
one = [F(1)]*N
P = matsub(I, scale(F(1,4), outer(one,one)))
R = [[F(int(j==N-1-i)) for j in range(N)] for i in range(N)]
Qo = scale(F(1,2), matsub(I,R))
A = outer(c,c)
c2 = dotv(c,c)
A2 = frob(A,A)

assert sum(c,F(0)) == 0
assert c2 == F(65,72)
assert A2 == c2*c2 == F(4225,5184)
Pc = [sum((P[i][j]*c[j] for j in range(N)),F(0)) for i in range(N)]
Qoc = [sum((Qo[i][j]*c[j] for j in range(N)),F(0)) for i in range(N)]
assert Pc == c and Qoc == c
assert mateq(matmul(matmul(P,A),P), A)
assert mateq(matmul(matmul(Qo,A),Qo), A)

functional_rank = 1
kernel_dimension = 16 - functional_rank
odd_vector_dimension = 2
odd_odd_dimension = odd_vector_dimension**2
odd_odd_null_dimension = odd_odd_dimension - 1

X = [[F(10*i+j+1) for j in range(N)] for i in range(N)]
dD = frob(A,X)
Xsens = scale(dD/A2, A)
Xnull = matsub(X,Xsens)
assert frob(A,Xnull) == 0
assert frob(A,Xsens) == dD
XP = matmul(matmul(P,X),P)
Xo = matmul(matmul(Qo,X),Qo)
assert frob(A,XP) == dD == frob(A,Xo)

result = {
  "iteration": 476,
  "classification": "PASS_MIXED_DERIVATIVE_RANK1_PRECISION_SENSITIVE_MODE__DIAGNOSTIC_ONLY_NON_PROMOTING",
  "scientific_gate_pass": True,
  "promotes_physical_coordinate": False,
  "MODEL_READINESS": "24%",
  "readiness_change_pp": 0,
  "central4": {
    "c": [q(x) for x in c],
    "sum_c": q(sum(c,F(0))),
    "norm_c_squared": q(c2),
    "sensitive_matrix_frobenius_norm_squared": q(A2),
    "sensitive_matrix_frobenius_norm": q(c2)
  },
  "exact_structure": {
    "ambient_matrix_dimension": 16,
    "double_centered_subspace_dimension": 9,
    "odd_odd_subspace_dimension": odd_odd_dimension,
    "derivative_sensitive_subspace_dimension": functional_rank,
    "full_functional_nullspace_dimension": kernel_dimension,
    "odd_odd_nullspace_dimension": odd_odd_null_dimension,
    "sensitive_projection": "DeltaF_sens=(DeltaD/(65/72)^2) c c^T=(5184/4225) DeltaD c c^T",
    "sensitive_norm": "||DeltaF_sens||_F=(72/65)|DeltaD|",
    "hierarchy": "|DeltaD| <= (65/72)||Qo DeltaF Qo||_F <= (65/72)||P DeltaF P||_F <= (65/72)||DeltaF||_F",
    "functional_identity": "DeltaD=<cc^T,DeltaF>_F=<cc^T,Qo DeltaF Qo>_F=<cc^T,P DeltaF P>_F"
  },
  "interpretation": "Only the one-dimensional Frobenius component parallel to cc^T can alter the frozen central4xcentral4 mixed derivative. All Frobenius-orthogonal discrepancy modes are exact derivative nullspace, including but not limited to row/column/common modes.",
  "guardrails": [
    "DIAGNOSTIC_PROVENANCE_ONLY",
    "NO_THRESHOLD_CHANGE",
    "NO_ESTIMATOR_CHANGE",
    "NO_SUPPORT_DEDUPLICATION",
    "NO_PHYSICAL_PROMOTION",
    "NO_ANSATZ003",
    "NO_FISHER_RESOURCES"
  ],
  "next_gate": "raw-consume canonical Iteration455 rank11 run 33989317870 fail-closed; if PASS advance only to next UNTESTED frozen-manifest coordinate"
}
print(json.dumps(result, indent=2, sort_keys=True))
