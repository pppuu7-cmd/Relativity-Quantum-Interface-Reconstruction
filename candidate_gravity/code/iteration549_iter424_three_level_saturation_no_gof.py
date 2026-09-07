from fractions import Fraction as F

# Three assembled levels under X_s = D + A s^4 + B s^6,
# where s = 1, 1/2, 1/4 for BASE, HALF, QUARTER.
M = [
    [F(1), F(1), F(1)],
    [F(1), F(1,16), F(1,64)],
    [F(1), F(1,256), F(1,4096)],
]

def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

assert det3(M) == F(-2835,65536)

# Exact inverse, previously implicit in the three-level extrapolator/component formulas.
Minv = [
    [F(1,945), F(-16,189), F(1024,945)],
    [F(-16,45), F(208,9), F(-1024,45)],
    [F(256,189), F(-4352,189), F(4096,189)],
]

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

I = matmul(M, Minv)
assert I == [[F(int(i==j)) for j in range(3)] for i in range(3)]

# A pure h^8 contribution C*[1,1/256,1/65536] is exactly aliased into
# fitted (D,A,B) when only three levels are available.
c8 = [[F(1)],[F(1,256)],[F(1,65536)]]
alias = matmul(Minv, c8)
alias = [x[0] for x in alias]
assert alias == [F(1,1344), F(-17,64), F(425,336)]

# A fourth level s=1/8 supplies one residual degree of freedom.
# Integer left-null vector annihilating 1,s^4,s^6 over [1,1/2,1/4,1/8].
w4 = [F(-1), F(81), F(-1104), F(1024)]
s = [F(1),F(1,2),F(1,4),F(1,8)]
for p in (0,4,6):
    assert sum(w4[i]*(s[i]**p) for i in range(4)) == 0
h8_response = sum(w4[i]*(s[i]**8) for i in range(4))
assert h8_response == F(-11475,16384)

print('det(M)=', det3(M))
print('h8 alias into (D,A,B)=', alias)
print('four-level null weight=', w4)
print('four-level h8 response=', h8_response)
print('classification=REGIME_SPECIFIC_NON_IDENTIFIABILITY_ITER424_THREE_LEVEL_H4_H6_GOF__DIAGNOSTIC_ONLY_NON_PROMOTING')
