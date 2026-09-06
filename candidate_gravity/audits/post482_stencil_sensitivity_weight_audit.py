from fractions import Fraction

# Diagnostic-only audit of frozen central4 x central4 mixed-derivative stencil
# sensitivity across the Iteration-455 source-order manifest.
# It does not change source order, thresholds, estimator, or scientific authority.

c = [Fraction(1,12), Fraction(-2,3), Fraction(2,3), Fraction(-1,12)]
L1_TOTAL = sum(abs(x) for x in c) ** 2
assert L1_TOTAL == Fraction(9,4)

W = {(i,j): c[i]*c[j] for i in range(4) for j in range(4)}

# BASE rank == BASE local index for ranks 0..15.
base_certified_ranks = list(range(12))
base_active_rank = 12
base_tail_ranks = [12,13,14,15]
base_cert_abs = sum(abs(W[divmod(r,4)]) for r in base_certified_ranks)
base_tail_abs = sum(abs(W[divmod(r,4)]) for r in base_tail_ranks)
assert base_cert_abs == Fraction(17,8)
assert base_tail_abs == Fraction(1,8)
assert base_cert_abs + base_tail_abs == L1_TOTAL

# HALF corners overlap exact BASE coordinates at manifest ranks 5,6,9,10.
# In the HALF stencil those coordinates are local indices 0,3,12,15.
half_shared = {5:0, 6:3, 9:12, 10:15}
half_cert_abs = sum(abs(W[divmod(local,4)]) for local in half_shared.values())
assert half_cert_abs == Fraction(1,36)

# HALF-exclusive manifest ranks and their HALF local indices.
half_tail = {
    16:1, 17:2, 18:4, 19:5, 20:6, 21:7,
    22:8, 23:9, 24:10, 25:11, 26:13, 27:14,
}
half_tail_abs = sum(abs(W[divmod(local,4)]) for local in half_tail.values())
assert half_cert_abs + half_tail_abs == L1_TOTAL

half_peak_ranks = [19,20,23,24]
half_peak_abs = sum(abs(W[divmod(half_tail[r],4)]) for r in half_peak_ranks)
assert half_peak_abs == Fraction(16,9)

# If rank12 passes, its BASE absolute weight contribution is 1/144.
rank12_abs = abs(W[divmod(12,4)])
assert rank12_abs == Fraction(1,144)
base_after_rank12_abs = base_cert_abs + rank12_abs

print('L1 stencil weight total per assembly =', L1_TOTAL)
print('BASE certified through rank11 =', base_cert_abs, float(base_cert_abs/L1_TOTAL))
print('BASE after rank12 if PASS =', base_after_rank12_abs, float(base_after_rank12_abs/L1_TOTAL))
print('HALF certified via shared corners =', half_cert_abs, float(half_cert_abs/L1_TOTAL))
print('HALF peak ranks 19,20,23,24 =', half_peak_abs, float(half_peak_abs/L1_TOTAL))
print('PASS: occurrence coverage and stencil-sensitivity coverage are distinct diagnostics')
print('PASS: no source-order or threshold change')
