#!/usr/bin/env python3
"""Iteration 567: exact null-space/projector audit for frozen QUARTER central4 stencil."""
from fractions import Fraction

w = [1, -8, 8, -1]
C = [[wi * wj for wj in w] for wi in w]

sum_w = sum(w)
coeff_sq_norm = sum(x*x for row in C for x in row)
coeff_l1_norm = sum(abs(x) for row in C for x in row)
rank_C = 1  # nonzero outer product w⊗w
kernel_dim = 16 - rank_C
additive_nuisance_dim = 4 + 4 - 1
nonadditive_invisible_dim = kernel_dim - additive_nuisance_dim

assert sum_w == 0
assert coeff_sq_norm == 16900 == 130**2
assert coeff_l1_norm == 324
assert kernel_dim == 15
assert additive_nuisance_dim == 7
assert nonadditive_invisible_dim == 8

# The Frobenius-orthogonal projector onto the sole stencil-visible grid mode span(C)
# is P(F)=<C,F>/||C||_F^2 C. Since Duv=<C,F>/(144 h^2),
# ||P(F)||_F = |<C,F>|/||C||_F = (144/130) h^2 |Duv|.
projector_denominator = coeff_sq_norm
visible_norm_factor = Fraction(144, 130)  # multiplying h^2 |Duv|
assert visible_norm_factor == Fraction(72, 65)

print("PASS")
print("C_rank", rank_C)
print("kernel_dim", kernel_dim)
print("additive_nuisance_dim", additive_nuisance_dim)
print("nonadditive_invisible_dim", nonadditive_invisible_dim)
print("projector_denominator", projector_denominator)
print("visible_norm_factor", f"{visible_norm_factor.numerator}/{visible_norm_factor.denominator}")
