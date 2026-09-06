from fractions import Fraction

# Exact Gram entries retained from Iteration 510 for the 28-coordinate
# frozen BASE/HALF union, in units of 1/h^4.
base_var = Fraction(4225, 5184)
half_var = Fraction(4225, 324)
cov = Fraction(4, 81)
delta_var = base_var + half_var - 2 * cov

# sqrt(base_var*half_var) is exactly 4225/1296.
corr = cov / Fraction(4225, 1296)

assert corr == Fraction(64, 4225)
assert delta_var == Fraction(23771, 1728)
assert cov > 0

print({
    "classification": "PASS_BASE_HALF_SHARED_NODE_COVARIANCE_EXACT__NON_PROMOTING",
    "base_variance_factor": str(base_var),
    "half_variance_factor": str(half_var),
    "base_half_covariance_factor": str(cov),
    "base_half_correlation": str(corr),
    "delta_variance_factor": str(delta_var),
})
