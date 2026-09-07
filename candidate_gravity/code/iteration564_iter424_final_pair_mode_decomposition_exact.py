from fractions import Fraction
from sympy import Matrix, Rational, sqrt, symbols, simplify

# Final frozen QUARTER coordinates after a raw-valid rank10 PASS:
# rank11 = (+2h,-h), rank12 = (+2h,+h).
# Frozen central4 first-derivative integer weights are w(+2)=-1, w(-1)=-8, w(+1)=+8.
# Hence tensor coefficients are (+8,-8) for (rank11, rank12).
coeff = Matrix([8, -8])

# Orthogonal common/differential basis:
# q_common=(x+y)/sqrt(2), q_diff=(x-y)/sqrt(2).
U = Matrix([[1/sqrt(2), 1/sqrt(2)], [1/sqrt(2), -1/sqrt(2)]])
mode_coeff = simplify(U * coeff)
assert mode_coeff == Matrix([0, 8*sqrt(2)])

# Equivalent average/half-difference coordinates c=(x+y)/2, d=(x-y)/2.
# Tail numerator = 8x-8y = 16d; with full normalization 1/(144 h^2):
# T_tail=d/(9 h^2)=(x-y)/(18 h^2).
assert Fraction(16, 144) == Fraction(1, 9)
assert Fraction(8, 144) == Fraction(1, 18)

# The orthogonal transform is perfectly conditioned.
assert simplify(U.T * U) == Matrix.eye(2)
assert simplify(U.det()**2) == 1

# Symmetric equal-variance covariance model:
# Cov(x,y)=rho*sigma^2. In the orthogonal basis common and differential modes decorrelate exactly.
sigma, rho = symbols('sigma rho', real=True)
Sigma = Matrix([[sigma**2, rho*sigma**2], [rho*sigma**2, sigma**2]])
Sigma_modes = simplify(U * Sigma * U.T)
assert Sigma_modes == Matrix([[sigma**2*(1+rho), 0], [0, sigma**2*(1-rho)]])

# Since T_tail=q_diff/(9*sqrt(2)*h^2),
# Var(T_tail)=sigma^2*(1-rho)/(162 h^4).
# For rho=0 this reduces to sigma^2/(162 h^4).

print('PASS_ITER424_FINAL_PAIR_COMMON_DIFFERENTIAL_MODE_DECOMPOSITION_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING')
print('coefficient_vector_rank11_rank12=[+8,-8]')
print('orthogonal_mode_coefficients=[0,8*sqrt(2)]')
print('common_mode_exactly_null=true')
print('differential_mode_is_only_assembly_relevant_direction=true')
print('T_tail=(F11-F12)/(18*h^2)=d/(9*h^2)')
print('orthogonal_transform_condition_number=1')
print('symmetric_covariance_modes=diag(sigma^2*(1+rho),sigma^2*(1-rho))')
print('Var(T_tail)=sigma^2*(1-rho)/(162*h^4)')
print('u-v_non_equivalence_guardrail=both_final_coordinates_remain_mandatory')
