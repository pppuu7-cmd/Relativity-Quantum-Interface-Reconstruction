#!/usr/bin/env python3
"""Iteration 615: source numerator/sign audit on Iter614 simple roots.

Inputs are frozen: Iter613 MSSC001-NATIVE-S-KIN-V1, Iter614 root/Jacobian
support, Iter594 full 13-family routed MSSC source identity, and Iter608
normalized scalar-pole discontinuity D G = -delta(m^2-r^2).

This gate evaluates only the internal scalar-pole distribution coefficients of
the unchanged source tree.  It does not bind the result to native Y/T_cut or
Iter582, and it performs no Source/Born subtraction or comparator quotient.
"""
from __future__ import annotations
import itertools, json, math
from pathlib import Path
import numpy as np

ITERATION=615
ETA=np.diag([1.,-1.,-1.,-1.])
MASS=0.7
LEGS=('s','a','b')
Q={'s':np.array([1.,0.,0.,0.]),
   'a':np.array([-.4,.1,.1,0.]),
   'b':np.array([-.6,-.1,-.1,0.])}
rng=np.random.default_rng(319)
H={}
for x in LEGS:
    z=rng.normal(size=(4,4)); H[x]=0.12*(z+z.T)/2.0
ROOTS={('s','-'):[0.09,2.89],
       ('a','+'):[1.241314274283428],('a','-'):[0.09868572571657197],
       ('b','+'):[1.726971411425142],('b','-'):[0.013028588574858]}
TOL=1e-11

def mdot(v): return float(v@ETA@v)
def first_coeff(h):
    HH=ETA@h; tr=float(np.trace(HH))
    return 0.5*tr*ETA-ETA@h@ETA,0.5*tr
def mixed_coeff(h1,h2):
    H1=ETA@h1; H2=ETA@h2
    t1=float(np.trace(H1)); t2=float(np.trace(H2))
    bs=t1*t2/4.0-float(np.trace(H1@H2))/2.0
    bt=(ETA@h1@ETA@h2@ETA+ETA@h2@ETA@h1@ETA
        -0.5*t1*(ETA@h2@ETA)-0.5*t2*(ETA@h1@ETA)+bs*ETA)
    return bt,bs
def K1(h,pp,p):
    a,b=first_coeff(h); return -float((ETA@pp)@a@(ETA@p))+MASS*MASS*b
def K2(h1,h2,pp,p):
    a,b=mixed_coeff(h1,h2); return -float((ETA@pp)@a@(ETA@p))+MASS*MASS*b
def G(p): return 1.0/(MASS*MASS-mdot(p))
def p0(s): return np.array([math.sqrt(s),0.,0.,0.])
def jac(leg,sign,s):
    w=math.sqrt(s); q0=Q[leg][0]
    return abs(-1.0-q0/w if sign=='+' else -1.0+q0/w)

def pair_cut(leg,sign,s):
    p=p0(s); g0=G(p); pair=tuple(x for x in LEGS if x!=leg)
    if sign=='-':
        r=p-Q[leg]
        numerator=K1(H[leg],p,r)*K2(H[pair[0]],H[pair[1]],r,p)
    else:
        r=p+Q[leg]
        numerator=K2(H[pair[0]],H[pair[1]],p,r)*K1(H[leg],r,p)
    # Iter594 pair family has + sign; normalized Iter608 D G = -delta(D).
    return {'family':'K1K2','numerator_without_cut_G':numerator,
            'coefficient':-(g0*g0)*numerator/jac(leg,sign,s)}

def triple_cut(perm,root_leg,root_sign,s):
    i,j,k=perm; p=p0(s); g0=G(p)
    p1=p+Q[i]; p2=p1+Q[j]
    if (root_leg,root_sign)==(i,'+'):
        other_D=MASS*MASS-mdot(p2)
        numerator=K1(H[i],p1,p)*K1(H[j],p2,p1)*G(p2)*K1(H[k],p,p2)
    elif (root_leg,root_sign)==(k,'-'):
        other_D=MASS*MASS-mdot(p1)
        numerator=K1(H[i],p1,p)*G(p1)*K1(H[j],p2,p1)*K1(H[k],p,p2)
    else:
        return None
    # Iter594 full source subtracts K1^3; Iter608 cut contributes another minus.
    coeff=(g0*g0)*numerator/jac(root_leg,root_sign,s)
    return {'family':'K1cubed','permutation':list(perm),'other_internal_D':other_D,
            'numerator_including_other_finite_G':numerator,'coefficient':coeff}

def main():
    failures=[]; rows=[]
    for key,ss in ROOTS.items():
        leg,sign=key
        for s in ss:
            pair=pair_cut(leg,sign,s)
            triples=[]
            for perm in itertools.permutations(LEGS):
                z=triple_cut(perm,leg,sign,s)
                if z is not None: triples.append(z)
            if len(triples)!=2: failures.append(f'{leg}{sign}@{s}: expected two K1^3 contributors, got {len(triples)}')
            min_other=min(abs(z['other_internal_D']) for z in triples)
            if min_other<=TOL: failures.append(f'{leg}{sign}@{s}: coincident/repeated internal pole {min_other}')
            total=float(pair['coefficient']+sum(z['coefficient'] for z in triples))
            if not np.isfinite(total): failures.append(f'{leg}{sign}@{s}: nonfinite total')
            rows.append({'root_denominator':f'D_{leg}^{sign}','s':s,'abs_jacobian':jac(leg,sign,s),
                         'pair_contribution':pair,'K1cubed_contributions':triples,
                         'minimum_abs_other_internal_D':min_other,
                         'aggregate_normalized_internal_scalar_cut_coefficient':total})
    rows.sort(key=lambda r:r['s'])
    classification=('PASS_ITER615_FROZEN_NATIVE_S_INTERNAL_SCALAR_POLE_SOURCE_COEFFICIENT_AUDIT__NON_NORMALIZED_NON_RESIDUAL'
                    if not failures else 'FAIL_ITER615_FROZEN_NATIVE_S_INTERNAL_SCALAR_POLE_SOURCE_COEFFICIENT_AUDIT')
    out={
      'iteration':ITERATION,'date':'2026-09-08','model_readiness_percent':24,
      'classification':classification,'scientific_gate_pass':not failures,'failures':failures,
      'inputs':['Iter594 exact 13-family source identity','Iter605 Ward PASS','Iter608 normalized scalar-pole discontinuity',
                'Iter613 MSSC001-NATIVE-S-KIN-V1','Iter614 simple-root/Jacobian authority'],
      'normalized_cut_sign_rule':'pair: (+ family sign)*(- delta) => minus; K1^3: (- family sign)*(- delta) => plus',
      'root_rows':rows,
      'root_count':len(rows),'all_roots_noncoincident_with_other_internal_denominator':not failures,
      'K3_scalar_pole_distribution':'NO_INTERNAL_SCALAR_POLE_DISTRIBUTION_IN_THIS_SECTOR; not an amplitude-zero claim',
      'D_s_plus_support':'NO_POSITIVE_ROOT; not an amplitude-zero claim',
      'all_13_source_families_retained':True,'zero_fill':False,
      'native_Y_Tcut_binding':'NOT_YET_PERFORMED','iter582_binding':'NOT_YET_PERFORMED',
      'source_born_subtraction':'NOT_PERFORMED','comparator_quotient':'BLOCKED','candidate_residual':False,
      'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
      'readiness_change':'unchanged at 24%; internal source distribution coefficients are now explicit but the native normalization/matched-observable bridge is not yet closed',
      'next_gate_if_pass':'derive the exact native Y=(K2,S_soft2_full)/T_cut sign and normalization binding for these distributional source coefficients and the Iter582 D_s Gamma_e2 coordinate, keeping q2 buckets distinct and performing no Source/Born subtraction'
    }
    path=Path(__file__).resolve().parents[1]/'results'/'iteration615_native_s_source_pole_coefficient_audit.json'
    path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
    if failures: raise SystemExit(2)

if __name__=='__main__': main()
