from fractions import Fraction

# Published-authority algebraic checks for Giacchini, de Paula Netto, Shapiro,
# Phys. Rev. D 102, 106006 (2020), arXiv:2006.04217.
# This is deliberately only an operator/convention certificate; it does not
# pretend to compute finite CPT3 form factors.

D = 4
a = Fraction(-1, 2)

ghost_nonminimal_coefficient = 1 + 2 * a
field_metric_singular_value = Fraction(-1, D)
field_metric_is_nondegenerate = a != field_metric_singular_value

# Eq. (60), inside the overall factor
# - mu^(D-4)/[(4 pi)^2 (D-4)] int sqrt(|g|) [...].
vd_divergence_target = {
    "Riemann2": Fraction(53, 45),
    "Ricci2": Fraction(-61, 90),
    "R2": Fraction(25, 36),
    "Lambda_R": Fraction(8, 1),
    "Lambda2": Fraction(12, 1),
}

assert ghost_nonminimal_coefficient == 0
assert field_metric_is_nondegenerate

print("D =", D)
print("a =", a)
print("1 + 2 a =", ghost_nonminimal_coefficient)
print("field-space singular value -1/D =", field_metric_singular_value)
print("field-space metric nondegenerate =", field_metric_is_nondegenerate)
print("Eq60 target coefficients =")
for name, value in vd_divergence_target.items():
    print(f"  {name}: {value}")
print("STATUS: PASS_OPERATOR_CONVENTION_ALGEBRA_ONLY")
print("WARNING: full VD one-loop action also contains U1/U2 connection traces; H+N alone are not the off-shell unique action.")
