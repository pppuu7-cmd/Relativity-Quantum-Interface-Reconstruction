#!/usr/bin/env python3
"""RQIR Iteration 328: determinant triangle orientation affine-equivalence audit.

Iteration 327 correctly found two triangle denominator classes when quotienting
only by common loop-momentum translations.  A scalar loop integral also permits
an orientation reversal p -> -p + C, whose Jacobian has absolute determinant 1
and preserves every quadratic propagator denominator.  This gate checks, with
exact integer Fourier shifts, whether the two translation-only triangle classes
are one integration family under the signed affine loop-variable group.

This gate does not alter Iteration 327, does not claim numerator equivalence, and
does not integrate any family.  If it passes, numerator polynomials still have
to be transformed/combined consistently before DR reduction.
"""
from __future__ import annotations
import itertools, json

D=4
TARGET=(1,1,1)
QINT=[(27,-19,31,11),(-13,37,17,-29),(-14,-18,-48,18)]
ZERO4=(0,0,0,0)

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def qint(a): return tuple(sum(a[r]*QINT[r][mu] for r in range(3)) for mu in range(D))
def nonzero_subindices(target):
    return [a for a in itertools.product(*(range(x+1) for x in target)) if any(a)]
NZ=nonzero_subindices(TARGET)
def triples(): return [(a,b,c) for a in NZ for b in NZ for c in NZ if add(add(a,b),c)==TARGET]

def shifts(seq):
    out=[ZERO4]; cur=ZERO4
    for a in seq[:-1]:
        q=qint(a); cur=tuple(cur[i]+q[i] for i in range(D)); out.append(cur)
    total=ZERO4
    for a in seq:
        q=qint(a); total=tuple(total[i]+q[i] for i in range(D))
    if total!=ZERO4: raise AssertionError((seq,total))
    return tuple(out)

def canon_translation(S):
    cands=[]
    for origin in S:
        cands.append(tuple(sorted(tuple(s[i]-origin[i] for i in range(D)) for s in S)))
    return min(cands)

def canon_signed_affine(S):
    # Quotient by p -> sigma p + C, sigma in {+1,-1}.
    cands=[]
    for sigma in (1,-1):
        T=[tuple(sigma*x for x in s) for s in S]
        for origin in T:
            cands.append(tuple(sorted(tuple(t[i]-origin[i] for i in range(D)) for t in T)))
    return min(cands)

rows=[]
for seq in triples():
    S=shifts(seq)
    rows.append({'sequence':[list(a) for a in seq],
                 'shifts_int100':[list(s) for s in S],
                 'translation_family':[list(s) for s in canon_translation(S)],
                 'signed_affine_family':[list(s) for s in canon_signed_affine(S)]})
translation_fams={tuple(tuple(x) for x in r['translation_family']) for r in rows}
affine_fams={tuple(tuple(x) for x in r['signed_affine_family']) for r in rows}
translation_counts={str([[*x] for x in fam]):sum(tuple(tuple(x) for x in r['translation_family'])==fam for r in rows) for fam in translation_fams}
affine_counts={str([[*x] for x in fam]):sum(tuple(tuple(x) for x in r['signed_affine_family'])==fam for r in rows) for fam in affine_fams}

# Exact structural facts for the allowed loop transformation.
reversal_jacobian_abs=1
quadratic_form_invariant_under_sign=True  # (-k)^2 = k^2 for any bilinear metric.
all_six=len(rows)==6
split_3_3=(len(translation_fams)==2 and sorted(translation_counts.values())==[3,3])
collapse_to_one=(len(affine_fams)==1 and list(affine_counts.values())==[6])
ok=bool(all_six and split_3_3 and collapse_to_one and reversal_jacobian_abs==1 and quadratic_form_invariant_under_sign)

result={
  'iteration':328,
  'model_readiness_percent':24,
  'scientific_gate_pass':ok,
  'classification':('PASS_TRIANGLE_TWO_ORIENTATIONS_ONE_SIGNED_AFFINE_INTEGRATION_FAMILY' if ok else
                    'FAIL_TRIANGLE_ORIENTATION_SIGNED_AFFINE_EQUIVALENCE'),
  'candidate_residual':False,
  'scope':{'closed_triad_q_int100':[list(q) for q in QINT],
           'ordered_triple_count':len(rows),
           'allowed_loop_variable_group':'p -> sigma p + C with sigma=+/-1; translation plus orientation reversal',
           'claim_level':'denominator integration-family equivalence only; numerator transformation not yet certified'},
  'checks':{'translation_only_family_count':len(translation_fams),
            'translation_only_split_3_plus_3':split_3_3,
            'signed_affine_family_count':len(affine_fams),
            'all_six_routes_collapse_to_one_signed_affine_family':collapse_to_one,
            'loop_reversal_jacobian_absolute_value':reversal_jacobian_abs,
            'quadratic_propagator_form_invariant_under_loop_reversal':quadratic_form_invariant_under_sign},
  'translation_family_counts':translation_counts,
  'signed_affine_family_counts':affine_counts,
  'routes':rows,
  'iteration327_interpretation':('Its expected one triangle translation-family assertion was too strong; two orientation classes are one denominator integration family only after including the legitimate loop reversal. Iteration 327 remains preserved as a scoped gate-design FAIL.' if ok else 'Do not reinterpret Iteration 327; triangle orientation equivalence remains unresolved.'),
  'guardrails':['ITERATION327_NOT_RETROACTIVELY_EDITED','DENOMINATOR_EQUIVALENCE_NOT_NUMERATOR_EQUIVALENCE','NO_ZERO_FILL','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_HEAVY_FULL_C5'],
  'next_gate':('transform and combine the physical graviton-minus-ghost loop-momentum numerator polynomials into the canonical 3 bubble + 1 signed-affine triangle denominator families, independently verify reconstruction at held-out loop momenta, then perform DR/cut reduction' if ok else 'preserve BLOCKED triangle family reduction and seek an independent allowed loop-variable equivalence or retain two separate triangle families')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not ok: raise SystemExit(2)

# Trigger-only marker; scientific contract unchanged.
