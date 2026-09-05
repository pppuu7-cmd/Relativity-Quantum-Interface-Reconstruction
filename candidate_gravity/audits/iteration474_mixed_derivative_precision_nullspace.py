from fractions import Fraction

# Iteration 474: exact nullspace/double-centering audit for the frozen
# central4 x central4 mixed derivative precision discrepancy.
#
# Let c=(1/12,-2/3,2/3,-1/12). For a 4x4 discrepancy matrix DeltaF,
# DeltaD = c^T DeltaF c. Since sum(c)=0, DeltaD is invariant under
# DeltaF -> DeltaF + a 1^T + 1 b^T + gamma 11^T.
# Equivalently DeltaD = c^T P DeltaF P c with P=I-(1/4)11^T.

c = [Fraction(1, 12), Fraction(-2, 3), Fraction(2, 3), Fraction(-1, 12)]
one = [Fraction(1) for _ in range(4)]

assert sum(c) == 0
c_norm_sq = sum(x*x for x in c)
assert c_norm_sq == Fraction(65, 72)

P = [[Fraction(int(i == j)) - Fraction(1, 4) for j in range(4)] for i in range(4)]

def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def transpose(A):
    return list(map(list, zip(*A)))

def bilinear(vec_l, A, vec_r):
    return sum(vec_l[i]*A[i][j]*vec_r[j] for i in range(4) for j in range(4))

def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(4)] for i in range(4)]

def outer(a, b):
    return [[a[i]*b[j] for j in range(4)] for i in range(4)]

def frob_sq(A):
    return sum(x*x for row in A for x in row)

# Exact projector identities.
assert matmul(P, P) == P
assert [sum(P[i][j]*one[j] for j in range(4)) for i in range(4)] == [Fraction(0)]*4
assert [sum(one[i]*P[i][j] for i in range(4)) for j in range(4)] == [Fraction(0)]*4

# A generic rational discrepancy matrix.
DeltaF = [[Fraction(7*i - 3*j + i*j + 2, 11) for j in range(4)] for i in range(4)]
DeltaF_int = matmul(matmul(P, DeltaF), P)
DeltaD = bilinear(c, DeltaF, c)
DeltaD_int = bilinear(c, DeltaF_int, c)
assert DeltaD == DeltaD_int

# Exact invariance under arbitrary row/column-separable contamination.
a = [Fraction(3), Fraction(-5), Fraction(7, 2), Fraction(11, 3)]
b = [Fraction(-2), Fraction(13, 5), Fraction(17, 7), Fraction(-19, 4)]
gamma = Fraction(23, 6)
separable = add(add(outer(a, one), outer(one, b)), outer([gamma]*4, one))
DeltaF_shifted = add(DeltaF, separable)
assert bilinear(c, DeltaF_shifted, c) == DeltaD
assert matmul(matmul(P, DeltaF_shifted), P) == DeltaF_int

# Counterexample to the converse of Iteration 472: very large local discrepancies
# can be exactly invisible to the mixed derivative if they are row/column separable.
local_fail = outer([Fraction(1), Fraction(2), Fraction(3), Fraction(4)], one)
assert max(abs(x) for row in local_fail for x in row) == 4
assert bilinear(c, local_fail, c) == 0
assert matmul(matmul(P, local_fail), P) == [[Fraction(0)]*4 for _ in range(4)]

# Correlation-aware Frobenius bound:
# |c^T DeltaF_int c| <= ||c||_2^2 ||DeltaF_int||_F = (65/72)||DeltaF_int||_F.
# Verify squared form exactly on the generic rational test matrix.
lhs_sq = DeltaD_int * DeltaD_int
rhs_sq = c_norm_sq * c_norm_sq * frob_sq(DeltaF_int)
assert lhs_sq <= rhs_sq

print('sum(c) =', sum(c))
print('||c||_2^2 =', c_norm_sq)
print('DeltaD = DeltaD_int =', DeltaD)
print('local-fail separable max discrepancy = 4, assembled DeltaD = 0')
print('PASS: DeltaD invariant under a 1^T + 1 b^T + gamma 11^T')
print('PASS: DeltaD = c^T P DeltaF P c exactly')
print('PASS: |DeltaD| <= (65/72) ||P DeltaF P||_F')
