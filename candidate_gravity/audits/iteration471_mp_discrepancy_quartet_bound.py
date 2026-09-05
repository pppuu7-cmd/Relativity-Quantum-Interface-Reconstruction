from fractions import Fraction

alpha = {
    (1,1): Fraction(4,9),
    (1,2): Fraction(-1,18),
    (2,1): Fraction(-1,18),
    (2,2): Fraction(1,144),
}

# Deterministic exact test data for delta F = F80-F120 on each signed stencil sample.
delta = {}
seed = 1
for a,b in alpha:
    for su,sv in ((1,1),(-1,1),(1,-1),(-1,-1)):
        delta[(a,b,su,sv)] = Fraction(seed * (1 if su*sv > 0 else -1), 137)
        seed += 1

def quartet(a,b):
    return (delta[(a,b,1,1)] - delta[(a,b,-1,1)]
            - delta[(a,b,1,-1)] + delta[(a,b,-1,-1)])

D = sum(alpha[k]*quartet(*k) for k in alpha)
Bq = sum(abs(alpha[k])*abs(quartet(*k)) for k in alpha)
Bs = sum(abs(alpha[k])*sum(abs(delta[(k[0],k[1],su,sv)])
                         for su,sv in ((1,1),(-1,1),(1,-1),(-1,-1)))
         for k in alpha)

assert abs(D) <= Bq <= Bs
assert sum(abs(v) for v in alpha.values()) == Fraction(9,16)

print('DeltaD =', D)
print('B_quartet_delta =', Bq)
print('B_sample_delta =', Bs)
print('PASS: |DeltaD| <= B_quartet_delta <= B_sample_delta')
