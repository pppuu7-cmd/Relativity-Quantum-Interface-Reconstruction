#!/usr/bin/env python3
from fractions import Fraction
import json

# Structural same-parent CTP/r-a gate.  No Candidate/native values are read.
# Ordering is (r,a), with the frozen Iter627 propagator matrix
# G = [[G_K,G_R],[G_A,0]].  From
# 1/2(phi_+ K[h_+] phi_+ - phi_- K[h_-] phi_-),
# h_r insertion gives V_r=[[0,V],[V,0]], while one h_a insertion gives
# V_a=[[V,0],[0,V/4]].  We suppress the common metric vertex tensor V and
# compute only causal-component support.  Every retarded gravitational arr
# closed scalar-loop family must contain exactly one G_K factor.

# Polynomial in (K,R,A): dict[(eK,eR,eA)] -> Fraction.
def padd(x,y):
    z=dict(x)
    for m,c in y.items(): z[m]=z.get(m,Fraction(0))+c
    return {m:c for m,c in z.items() if c}
def pmul(x,y):
    z={}
    for (i,j,k),a in x.items():
      for (u,v,w),b in y.items():
        m=(i+u,j+v,k+w); z[m]=z.get(m,Fraction(0))+a*b
    return {m:c for m,c in z.items() if c}
def pscale(x,s): return {m:c*s for m,c in x.items() if c*s}
def pconst(x): return {(0,0,0):Fraction(x)} if x else {}
def psym(which):
    return { {'K':(1,0,0),'R':(0,1,0),'A':(0,0,1)}[which]: Fraction(1)}
Z={}
K,R,A=psym('K'),psym('R'),psym('A')
G=[[K,R],[A,Z]]
Vr=[[Z,pconst(1)],[pconst(1),Z]]
Va=[[pconst(1),Z],[Z,pconst(Fraction(1,4))]]
def mm(X,Y):
    return [[padd(pmul(X[i][0],Y[0][j]),pmul(X[i][1],Y[1][j])) for j in range(2)] for i in range(2)]
def tr(X): return padd(X[0][0],X[1][1])
def chain(vertices):
    X=G
    for n,V in enumerate(vertices):
        X=mm(X,V)
        if n != len(vertices)-1: X=mm(X,G)
    return tr(X)
def fmt(p):
    names=[]
    for (ek,er,ea),c in sorted(p.items()):
        factors=[]
        for name,e in [('G_K',ek),('G_R',er),('G_A',ea)]:
            if e: factors.append(name if e==1 else f'{name}^{e}')
        mono='*'.join(factors) if factors else '1'
        if c==1: names.append(mono)
        elif c==-1: names.append('-'+mono)
        else: names.append(f'{c.numerator}/{c.denominator}*{mono}' if c.denominator!=1 else f'{c.numerator}*{mono}')
    return ' + '.join(names).replace('+ -','- ') if names else '0'

contact=chain([Va])
mixed_ar=chain([Va,Vr])
mixed_ra=chain([Vr,Va])
cubic=[chain(seq) for seq in ([Va,Vr,Vr],[Vr,Va,Vr],[Vr,Vr,Va])]
expected_contact={(1,0,0):Fraction(1)}
expected_mixed={(1,1,0):Fraction(1),(1,0,1):Fraction(1)}
expected_cubic={(1,2,0):Fraction(1),(1,1,1):Fraction(1),(1,0,2):Fraction(1)}
failures=[]
if contact!=expected_contact: failures.append('contact causal trace mismatch')
if mixed_ar!=expected_mixed or mixed_ra!=expected_mixed: failures.append('mixed causal trace mismatch')
if any(x!=expected_cubic for x in cubic): failures.append('cubic causal trace mismatch')
# Exact invariant: all monomials have one and only one Keldysh factor.
for label,p in [('contact',contact),('mixed_ar',mixed_ar),('mixed_ra',mixed_ra)]+[(f'cubic_{i}',p) for i,p in enumerate(cubic)]:
    if not p or any(m[0]!=1 for m in p): failures.append(f'{label} does not require exactly one G_K')

result={
  'iteration':630,
  'date':'2026-09-09',
  'scientific_gate_pass':not failures,
  'candidate_residual':False,
  'classification':'PASS_ITER630_CLOSED_RETARDED_GRAVITATIONAL_SCALAR_LOOP_REQUIRES_KELDYSH_COMPONENT__OPEN_GR_COEFFICIENTS_NOT_DIRECT_1PI_AUTHORITY__NON_RESIDUAL' if not failures else 'FAIL_ITER630_CLOSED_RETARDED_LOOP_CAUSAL_ALGEBRA',
  'frozen_inputs':{
    'iter627_propagator_matrix':'G_ra_basis=[[G_K,G_R],[G_A,0]]',
    'r_vertex':'V_r=[[0,V],[V,0]]',
    'one_a_vertex':'V_a=[[V,0],[0,V/4]]',
    'retarded_gravitational_component':'one h_a and two h_r insertions (arr plus cyclic placements)',
    'iter613_trajectory':'PRESERVED_NOT_EVALUATED_HERE'
  },
  'closed_trace_causal_support':{
    'K3_one_a_contact':fmt(contact),
    'K1K2_one_a_one_r':fmt(mixed_ar),
    'K1K2_reverse_order':fmt(mixed_ra),
    'K1cubed_arr':fmt(cubic[0]),
    'K1cubed_rar':fmt(cubic[1]),
    'K1cubed_rra':fmt(cubic[2])
  },
  'exact_consequence':'Every closed retarded scalar-loop family carries exactly one G_K. Therefore the Iter628 open scalar response, whose internal lines are induced G_R, cannot be reweighted into gravitational retarded Gamma3 by any family-independent or root-wise normalization.',
  'required_new_authority':'same-parent scalar Keldysh/statistical component G_K (state/boundary-condition normalization) and its relation to G_R/G_A must be frozen before numerical closed-loop pole/cut coefficients can be computed',
  'iter628_retarded_pole_data':'PRESERVED_AS_OPEN_RESPONSE_AUTHORITY__NOT_DIRECTLY_REUSED_AS_CLOSED_1PI',
  'source_born_subtraction':'NOT_PERFORMED',
  'native_projection':'NOT_PERFORMED',
  'candidate_values_used':False,
  'N_native_fit':False,
  'zero_fill':False,
  'failures':failures,
  'MODEL_READINESS':'24%',
  'readiness_change':'0 percentage points',
  'next_gate':'Iteration631: authority audit/prospective freeze of the same-parent MSSC001 scalar state and G_K component in the Iter627 CTP convention; only then evaluate closed retarded Gamma3 pole/cut support on the Iter613 trajectory.'
}
print(json.dumps(result,indent=2))
if failures: raise SystemExit('\n'.join(failures))
