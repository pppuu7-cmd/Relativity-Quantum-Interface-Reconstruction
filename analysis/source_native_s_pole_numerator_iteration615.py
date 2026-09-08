#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 615.

Evaluate the source-side numerator/sign data at the six simple internal scalar
pole support points frozen by Iter614, using only the prospectively frozen
MSSC001-NATIVE-S-KIN-V1 trajectory from Iter613 and the unchanged Iter594/605
same-action 13-family cubic source object.

Scope is deliberately narrow:
  * retained routed *internal* scalar denominators only (Iter609/614 scope),
  * no source/Born subtraction,
  * no native Y/T_cut normalization or sign fit,
  * no comparator quotient, ANSATZ-003, Fisher, or resources.

For a simple routed denominator D_A(s), with the Iter608 prescription
  Disc[1/(D_A+i0)] = -2*pi*i*delta(D_A),
the source-side normalized discontinuity coefficient is
  - C_A(s_r) / |partial_s D_A(s_r)|,
where C_A is the finite coefficient multiplying 1/D_A in the full Iter594
source response.  This script computes C_A as the sum of the one relevant
K1/K2 placement and the two relevant ordered K1^3 chains, including the
frozen overall minus sign of the K1^3 family.
"""
from __future__ import annotations
import contextlib, io, itertools, json, math
from pathlib import Path
import numpy as np

ITERATION=615
ROOT=Path(__file__).resolve().parents[1]
CROOT=ROOT/'candidate_gravity'/'code'
ETA=np.diag([1.,-1.,-1.,-1.])
MASS=0.7
LEGS=('s','a','b')
ROOT_TOL=2e-12
# Iter614 authoritative values, used as regression targets rather than tuned.
SUPPORT=[
 ('s','-',0.09,2.333333333333333),
 ('s','-',2.89,0.4117647058823529),
 ('a','+',1.241314274283428,0.6409796081665314),
 ('a','-',0.09868572571657197,2.273306106119183),
 ('b','+',1.726971411425142,0.54342862858286),
 ('b','-',0.013028588574858,6.25657137141714),
]


def mdot(v):
    v=np.asarray(v,float); return float(v@ETA@v)


def first_coeff(h):
    H=ETA@h; trH=float(np.trace(H))
    return 0.5*trH*ETA-ETA@h@ETA,0.5*trH


def mixed_coeff(h1,h2):
    H1=ETA@h1; H2=ETA@h2
    t1=float(np.trace(H1)); t2=float(np.trace(H2))
    bs=t1*t2/4.0-float(np.trace(H1@H2))/2.0
    bt=(ETA@h1@ETA@h2@ETA + ETA@h2@ETA@h1@ETA
        -0.5*t1*(ETA@h2@ETA)-0.5*t2*(ETA@h1@ETA)+bs*ETA)
    return bt,bs


def K1(h,pp,p):
    a1,b1=first_coeff(h)
    return -float((ETA@pp)@a1@(ETA@p))+MASS*MASS*b1


def K2(h1,h2,pp,p):
    bt,bs=mixed_coeff(h1,h2)
    return -float((ETA@pp)@bt@(ETA@p))+MASS*MASS*bs


def denom(q,branch,s):
    w=math.sqrt(s)
    # D^+ is p0+q, D^- is p0-q.
    return MASS*MASS-s-mdot(q)+((-2.0 if branch=='+' else 2.0)*w*q[0])


def main():
    failures=[]
    # Inherit the exact Iter368/588 fixture rather than retyping q or h.
    p368=CROOT/'iteration368_tru1sq_timelike_full_prepruning_routing.py'
    src=p368.read_text(); marker='# Cache expensive same-parent blocks by routed loop momentum.'
    if src.count(marker)!=1:
        raise SystemExit('iteration368 setup boundary drift')
    ns={'__name__':'iteration615_parent368_fixture','__file__':str(p368)}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(src.split(marker,1)[0],str(p368),'exec'),ns,ns)
    M=ns['M']
    qs={x:np.asarray(M[x][0],float) for x in LEGS}
    hs={x:np.asarray(M[x][1],float) for x in LEGS}
    closure=float(np.max(np.abs(sum((qs[x] for x in LEGS),np.zeros(4)))))
    if closure>1e-14: failures.append(f'fixture closure drift {closure}')

    rows=[]
    for leg,branch,s,jac in SUPPORT:
        p0=np.array([math.sqrt(s),0.,0.,0.])
        g0=1.0/(MASS*MASS-s)
        droot=denom(qs[leg],branch,s)
        if abs(droot)>ROOT_TOL:
            failures.append(f'{leg}{branch} Iter614 root regression failed: {droot}')
        pair=tuple(x for x in LEGS if x!=leg)

        # The single K1/K2 placement carrying this denominator.
        if branch=='-':
            # Pair acts first: p0 -> p0+q_pair = p0-q_leg.
            pint=p0+qs[pair[0]]+qs[pair[1]]
            pair_coeff=(g0*g0*K1(hs[leg],p0,pint)
                        *K2(hs[pair[0]],hs[pair[1]],pint,p0))
            pair_orientation='K1_after_K2__internal_p0_minus_q_singleton'
        else:
            # Singleton acts first: p0 -> p0+q_leg.
            pint=p0+qs[leg]
            pair_coeff=(g0*g0*K2(hs[pair[0]],hs[pair[1]],p0,pint)
                        *K1(hs[leg],pint,p0))
            pair_orientation='K2_after_K1__internal_p0_plus_q_singleton'

        triple_rows=[]
        for perm in itertools.permutations(LEGS):
            p1=p0+qs[perm[0]]
            p2=p1+qs[perm[1]]
            d1=MASS*MASS-mdot(p1)
            d2=MASS*MASS-mdot(p2)
            kvals=(K1(hs[perm[0]],p1,p0),
                   K1(hs[perm[1]],p2,p1),
                   K1(hs[perm[2]],p0,p2))
            match=(branch=='+' and perm[0]==leg) or (branch=='-' and perm[2]==leg)
            if not match: continue
            vanishing=d1 if branch=='+' else d2
            other=d2 if branch=='+' else d1
            if abs(vanishing)>ROOT_TOL:
                failures.append(f'{leg}{branch} chain {perm} wrong vanishing denominator {vanishing}')
            if abs(other)<=ROOT_TOL:
                failures.append(f'{leg}{branch} chain {perm} simultaneous second pole {other}')
            # Full Iter594 identity subtracts the ordered K1^3 family.
            coeff=-g0*g0*float(np.prod(kvals))/other
            triple_rows.append({'order':list(perm),'coefficient_with_frozen_family_minus':float(coeff),
                                'other_internal_denominator':float(other)})

        if len(triple_rows)!=2:
            failures.append(f'{leg}{branch}: expected two K1^3 chains, got {len(triple_rows)}')
        triple_sum=float(sum(x['coefficient_with_frozen_family_minus'] for x in triple_rows))
        total=float(pair_coeff+triple_sum)
        source_Ds=float(-total/jac)  # Iter608 + Iter205 D_s normalization only.
        rows.append({
          'leg':leg,'branch':branch,'s_root':float(s),'abs_dD_ds':float(jac),
          'root_regression_abs_D':float(abs(droot)),
          'K1K2_orientation':pair_orientation,
          'K1K2_finite_coefficient':float(pair_coeff),
          'K1cubed_rows':triple_rows,
          'K1cubed_finite_coefficient_sum':triple_sum,
          'full_internal_pole_finite_coefficient_C':total,
          'source_Ds_delta_weight_minus_C_over_abs_dD':source_Ds,
          'all_other_internal_denominators_finite':all(abs(x['other_internal_denominator'])>ROOT_TOL for x in triple_rows),
        })

    classification=('PASS_ITER615_FROZEN_NATIVE_S_INTERNAL_SCALAR_POLE_NUMERATOR_AND_SOURCE_DS_SIGN_AUDIT__NON_RESIDUAL'
                    if not failures else 'FAIL_ITER615_NATIVE_S_INTERNAL_SCALAR_POLE_NUMERATOR_AUDIT')
    result={
      'iteration':ITERATION,'date':'2026-09-08','model_readiness_percent':24,
      'classification':classification,'scientific_gate_pass':not failures,'failures':failures,
      'contract':'MSSC001-NATIVE-S-KIN-V1',
      'parent_authorities':['Iter608 scalar-pole distribution law','Iter613 prospective native-s kinematic completion',
                            'Iter614 simple-root/Jacobian support','Iter594/605 full same-action 13-family source object'],
      'fixture_q':{x:qs[x].tolist() for x in LEGS},'fixture_momentum_closure_max_abs':closure,
      'rows':rows,
      'distribution_convention':'D_s=Disc_s/(2*pi*i); Disc[1/(D+i0)]=-2*pi*i*delta(D), hence source-side simple-pole weight=-C/|dD/ds|',
      'scope':'routed internal scalar-pole numerator/sign audit only; common external endpoint factors are not reclassified in the Iter609/614 internal-line projector scope',
      'all_13_source_families_retained':True,'zero_fill':False,
      'source_born_subtraction':'NOT_PERFORMED','native_Y_over_Tcut_binding':'BLOCKED',
      'candidate_residual':False,'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
      'readiness_change':'0 percentage points; numerator/sign data close a mapping subgate but no complete stable model-level rubric sector closes',
      'next_gate_if_pass':'prospectively bind the source-side delta weights to the frozen Iter205/Iter582 native Y/T_cut coordinate, including sign/normalization and explicit treatment of external/amputation convention, before any Source/Born subtraction or comparator quotient'
    }
    out=ROOT/'candidate_gravity'/'results'; out.mkdir(parents=True,exist_ok=True)
    (out/'iteration615_native_s_internal_pole_numerators.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    if failures: raise SystemExit(2)

if __name__=='__main__': main()
