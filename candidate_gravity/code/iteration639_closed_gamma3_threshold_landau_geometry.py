#!/usr/bin/env python3
"""Iteration 639: exact scalar-denominator threshold/Landau geometry on frozen Iter636 family.

Inputs were frozen before this calculation: s=q_s^2>0 variable, t0=0.14,
u0=0.34, q_s+q_a+q_b=0, m_phi=0.7, and the Iter638 exact anchor.
This gate classifies support geometry only. No numerator, normalization, native projection,
Source/Born subtraction, comparator quotient, residual, ANSATZ or Fisher step is performed.
"""
from __future__ import annotations
import hashlib, json, pathlib
import sympy as sp

ROOT=pathlib.Path(__file__).resolve().parents[2]
P638=ROOT/'results'/'iteration638_exact_fixture_code_provenance_audit'/'result.json'
raw638=P638.read_bytes(); r638=json.loads(raw638)
failures=[]
if r638.get('classification')!='PASS_ITER638_UNIQUE_SAME_PARENT_EXACT_FIXTURE_ANCHOR_RECOVERED_FROM_COMMITTED_CODE__NON_RESIDUAL': failures.append('Iter638 prerequisite classification drift')
an=r638.get('recovered_anchor') or {}
for k,v in {'s0':1.0,'t0':0.14,'u0':0.34}.items():
    if abs(float(an.get(k,float('nan')))-v)>2e-15: failures.append(f'Iter638 anchor drift {k}')

s=sp.symbols('s', real=True)
m=sp.Rational(7,10); m2=m*m
t=sp.Rational(14,100); u=sp.Rational(34,100)

# Equal-mass s-channel bubble normal threshold.
bubble_threshold=sp.simplify((2*m)**2)

# Equal-mass triangle Cayley/Landau matrix. Pair (1,2) is separated by q_s,
# pair (2,3) by q_a, pair (3,1) by q_b. Permutations are physically equivalent here.
Y=sp.Matrix([
 [m2, m2-s/2, m2-u/2],
 [m2-s/2, m2, m2-t/2],
 [m2-u/2, m2-t/2, m2]
])
det=sp.factor(Y.det())
expected_det=-sp.Rational(7,10000)*(175*s*s-151*s+7)
if sp.simplify(det-expected_det)!=0: failures.append('Landau determinant polynomial drift')
roots=sp.solve(sp.Eq(det,0),s)
if len(roots)!=2: failures.append(f'Landau root count {len(roots)}')

landau=[]
for r in roots:
    ns=Y.subs(s,r).nullspace()
    if len(ns)!=1:
        failures.append(f'nullspace dimension drift at {r}: {len(ns)}')
        continue
    v=ns[0]; sm=sp.simplify(sum(v))
    if sm==0:
        failures.append(f'zero alpha normalization sum at {r}')
        continue
    alpha=[sp.simplify(x/sm) for x in v]
    vals=[float(sp.N(x,30)) for x in alpha]
    positive=all(x>0 for x in vals)
    landau.append({
      's_exact':str(sp.simplify(r)), 's_numeric':float(sp.N(r,30)),
      'alpha_exact':[str(x) for x in alpha], 'alpha_numeric':vals,
      'all_alpha_strictly_positive':positive,
      'above_s_channel_normal_threshold':bool(float(sp.N(r,30))>=float(bubble_threshold))
    })

positive_roots=[x for x in landau if x['all_alpha_strictly_positive']]
anchor_s=sp.Rational(1,1)
classification=('PASS_ITER639_CLOSED_GAMMA3_SCALAR_GEOMETRY__BUBBLE_THRESHOLD_1P96__NO_POSITIVE_ALPHA_LEADING_TRIANGLE_LANDAU_ROOT__NON_RESIDUAL'
                if not failures and len(positive_roots)==0 else
                'FAIL_ITER639_CLOSED_GAMMA3_THRESHOLD_LANDAU_GEOMETRY')
result={
 'iteration':639,'date':'2026-09-09','scientific_gate_pass':not failures,'candidate_residual':False,
 'classification':classification,'failures':failures,
 'frozen_contract':'MSSC001-CLOSED-GAMMA3-INV-FAMILY-V1',
 'inputs':{'m_phi_exact':'7/10','m_phi':0.7,'t0_exact':'7/50','t0':0.14,'u0_exact':'17/50','u0':0.34,'anchor_s0':1.0,'metric_signature':'+---'},
 'bubble':{'s_channel_normal_threshold_exact':str(bubble_threshold),'s_channel_normal_threshold':float(bubble_threshold),'anchor_s0_above_threshold':bool(anchor_s>=bubble_threshold)},
 'triangle':{'landau_matrix_convention':'Y_ii=m^2; Y_12=m^2-s/2; Y_23=m^2-t/2; Y_31=m^2-u/2',
             'determinant_exact':str(det),'roots':landau,'positive_alpha_leading_roots':positive_roots,
             'ordinary_s_channel_two_scalar_threshold_exact':str(bubble_threshold),'ordinary_s_channel_two_scalar_threshold':float(bubble_threshold)},
 'interpretation':'Along the frozen t0/u0 family the ordinary two-scalar s-channel cut begins at s=4 m_phi^2=1.96. The two real leading-triangle Landau determinant roots are subthreshold and each has mixed-sign normalized Feynman parameters, so neither is positive-alpha physical leading-Landau support on this family. The exact anchor s0=1 is below the ordinary s-channel threshold.',
 'explicit_nonclaims':['not a numerator/discontinuity magnitude','not native Y/T_cut projection','not Source/Born subtraction','not comparator residual','not Candidate-Gravity consistency PASS/FAIL'],
 'candidate_values_used':False,'zero_fill':False,'source_born_subtraction':'NOT_PERFORMED','native_projection':'NOT_PERFORMED','ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
 'MODEL_READINESS':'24%','readiness_change':'0 percentage points',
 'next_gate':'Classify the retarded closed-loop s-channel discontinuity support family-by-family: K3 remains no ordinary finite cut; K1/K2 and K1^3 ordinary s-channel support only for s>=1.96; no positive-alpha leading anomalous triangle root on the frozen t0/u0 family. Then derive the matched native D_s normalization/projector before Source/Born subtraction.'
}
out=ROOT/'results'/'iteration639_closed_gamma3_threshold_landau_geometry'; out.mkdir(parents=True,exist_ok=True)
rp=out/'result.json'; rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
audit={'iteration':639,'result_sha256':hashlib.sha256(rp.read_bytes()).hexdigest(),'failures':failures,
       'classification':('PASS_RAW_AUTHORITY_AUDIT_ITER639_THRESHOLD_LANDAU_GEOMETRY' if not failures and len(positive_roots)==0 else 'FAIL_RAW_AUTHORITY_AUDIT_ITER639_THRESHOLD_LANDAU_GEOMETRY')}
(out/'authority_audit.json').write_text(json.dumps(audit,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
if failures or positive_roots: raise SystemExit(2)
