#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 312.

Repair/validation gate for Iteration 311 determinant e=0,c<=3 cubic logdet
operator topology. Iteration 311's degree-6 polynomial fit at |t|<=6e-4 was
numerically ill-conditioned for the cubic coefficient. This gate keeps the
same frozen analytic identity and checks it independently using 80-digit
arithmetic plus a symmetric third-coefficient stencil with Richardson
cancellation of the leading O(h^2) contamination.

No physical H1/H2/H3 or ghost component kernels are invented here.
"""
import json
import numpy as np
import mpmath as mp

rng=np.random.default_rng(311)
n=6
H0=rng.normal(size=(n,n)); H0=H0.T@H0+2*np.eye(n)
H1=rng.normal(size=(n,n)); H2=rng.normal(size=(n,n)); H3=rng.normal(size=(n,n))

mp.mp.dps=80
def M(a):
    return mp.matrix([[mp.mpf(repr(float(x))) for x in row] for row in a])
M0,M1,M2,M3=map(M,(H0,H1,H2,H3))
G0=M0**-1
tr=lambda A: sum(A[i,i] for i in range(A.rows))
T1=tr(G0*M3)
T12a=tr(G0*M1*G0*M2)
T12b=tr(G0*M2*G0*M1)
T111=tr(G0*M1*G0*M1*G0*M1)
cubic_formula=T1-mp.mpf('0.5')*(T12a+T12b)+mp.mpf(1)/3*T111
mixed_cyclic_abs=abs(T12a-T12b)

def logdet(t):
    H=M0+t*M1+t*t*M2+t**3*M3
    d=mp.det(H)
    if d <= 0:
        raise RuntimeError('nonpositive determinant in audit stencil')
    return mp.log(d)

def cubic_stencil(h):
    return (logdet(2*h)-2*logdet(h)+2*logdet(-h)-logdet(-2*h))/(12*h**3)

h=mp.mpf('0.002')
a_h=cubic_stencil(h)
a_h2=cubic_stencil(h/2)
cubic_richardson=(4*a_h2-a_h)/3
absolute_residual=abs(cubic_richardson-cubic_formula)
relative_residual=absolute_residual/max(mp.mpf(1),abs(cubic_formula))
thresholds={'cubic_absolute_max':'1e-9','mixed_cyclic_absolute_max':'1e-50'}
passed=(absolute_residual <= mp.mpf(thresholds['cubic_absolute_max']) and
        mixed_cyclic_abs <= mp.mpf(thresholds['mixed_cyclic_absolute_max']))
classification=('PASS_DETERMINANT_E0C3_EXACT_CUBIC_LOGDET_OPERATOR_TOPOLOGY_HIGH_PRECISION_AUDIT__PHYSICAL_COMPONENTS_REMAIN_BLOCKED'
                if passed else 'FAIL_DETERMINANT_E0C3_HIGH_PRECISION_CUBIC_LOGDET_AUDIT')

def s(x): return mp.nstr(x,50)
result={
 'iteration':312,
 'model_readiness_percent':24,
 'scientific_gate_pass':bool(passed),
 'classification':classification,
 'candidate_residual':False,
 'iteration311_disposition':'NUMERICAL_AUDIT_FAILED_DUE_TO_ILL_CONDITIONED_SMALL_T_POLYFIT__NOT_SCIENTIFIC_IDENTITY_REFUTATION',
 'exact_cubic_identity':{
   'operator':'H=H0+t H1+t^2 H2+t^3 H3+O(t^4)',
   'green':'G0=H0^{-1}',
   'coefficient':'Tr(G0 H3) - 1/2 Tr(G0 H1 G0 H2) - 1/2 Tr(G0 H2 G0 H1) + 1/3 Tr(G0 H1 G0 H1 G0 H1)',
   'cyclic_reduced':'Tr(G0 H3) - Tr(G0 H1 G0 H2) + 1/3 Tr((G0 H1)^3)'
 },
 'high_precision_audit':{
   'mp_dps':mp.mp.dps,'h':s(h),'cubic_formula':s(cubic_formula),
   'cubic_stencil_h':s(a_h),'cubic_stencil_h_over_2':s(a_h2),
   'cubic_richardson':s(cubic_richardson),
   'absolute_residual':s(absolute_residual),'relative_residual':s(relative_residual),
   'mixed_cyclic_absolute_residual':s(mixed_cyclic_abs),'thresholds':thresholds
 },
 'physical_component_status':{
   'graviton_H1_H2_H3':'BLOCKED_COMPONENT_FORMULAS_NOT_SUPPLIED_BY_THIS_GATE',
   'ghost_operator_N1_N2_N3':'BLOCKED_COMPONENT_FORMULAS_NOT_SUPPLIED_BY_THIS_GATE',
   'source_contact_completion':'BLOCKED_DOWNSTREAM'
 },
 'guardrails':['UNSUPPORTED_COMPONENT_KERNELS_BLOCKED_NOT_ZERO_FILLED','NO_BLIND_HEAVY_FULL_C5','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003_FISHER_RESOURCES'],
 'next_gate':'freeze same-parent determinant graviton/ghost H1,H2,H3 component conventions and routing in D=4 Lambda=0 a=-1/2; if formulas are unavailable in repository authority, record BLOCKED and pursue another independent permitted prerequisite.'
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
