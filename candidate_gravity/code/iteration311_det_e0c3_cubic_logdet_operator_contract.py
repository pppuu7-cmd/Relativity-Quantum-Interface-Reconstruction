#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 311.

Exact cubic-background operator bookkeeping for the independent determinant
sector e=0,c<=3.  This freezes only the universal logdet expansion topology for
an operator H=H0+H1+H2+H3+..., with G0=H0^{-1}; it does not invent physical
Hn component kernels and does not perform a blind heavy C5 integration.
"""
import json, numpy as np
rng=np.random.default_rng(311)
n=6
H0=rng.normal(size=(n,n)); H0=H0.T@H0+2*np.eye(n)
G0=np.linalg.inv(H0)
H1=rng.normal(size=(n,n)); H2=rng.normal(size=(n,n)); H3=rng.normal(size=(n,n))

# Exact cubic coefficient of Tr log(H0 + t H1 + t^2 H2 + t^3 H3)
# from log(1+X)=X-X^2/2+X^3/3+...
T1=np.trace(G0@H3)
T12a=np.trace(G0@H1@G0@H2)
T12b=np.trace(G0@H2@G0@H1)
T111=np.trace(G0@H1@G0@H1@G0@H1)
cubic_formula=float(T1-0.5*(T12a+T12b)+(1.0/3.0)*T111)
cyclic_mixed_res=float(abs(T12a-T12b))

# Finite-difference/polyfit audit against direct logdet around t=0.
ts=np.array([-3,-2,-1,0,1,2,3],dtype=float)*2e-4
ys=[]
for t in ts:
    H=H0+t*H1+t*t*H2+t**3*H3
    sign,ld=np.linalg.slogdet(H)
    assert sign>0
    ys.append(ld)
coef=np.polynomial.polynomial.polyfit(ts,np.array(ys),6)
cubic_fit=float(coef[3])
rel=float(abs(cubic_fit-cubic_formula)/max(1.0,abs(cubic_formula)))
thresholds={'cubic_relative_max':2e-5,'mixed_cyclic_absolute_max':1e-10}
passed=rel<=thresholds['cubic_relative_max'] and cyclic_mixed_res<=thresholds['mixed_cyclic_absolute_max']

classification=('PASS_DETERMINANT_E0C3_EXACT_CUBIC_LOGDET_OPERATOR_TOPOLOGY_CONTRACT__PHYSICAL_H1_H2_H3_KERNELS_REMAIN_BLOCKED'
                if passed else 'FAIL_DETERMINANT_E0C3_CUBIC_LOGDET_OPERATOR_CONTRACT')
result={
 'iteration':311,
 'model_readiness_percent':24,
 'scientific_gate_pass':bool(passed),
 'classification':classification,
 'candidate_residual':False,
 'exact_cubic_identity':{
   'operator':'H=H0+t H1+t^2 H2+t^3 H3+O(t^4)',
   'green':'G0=H0^{-1}',
   'coefficient':'Tr(G0 H3) - 1/2 Tr(G0 H1 G0 H2) - 1/2 Tr(G0 H2 G0 H1) + 1/3 Tr(G0 H1 G0 H1 G0 H1)',
   'cyclic_reduced':'Tr(G0 H3) - Tr(G0 H1 G0 H2) + 1/3 Tr((G0 H1)^3)'
 },
 'numerical_audit':{
   'cubic_formula':cubic_formula,
   'cubic_fit':cubic_fit,
   'relative_residual':rel,
   'mixed_cyclic_absolute_residual':cyclic_mixed_res,
   'thresholds':thresholds
 },
 'physical_component_status':{
   'graviton_H1_H2_H3':'BLOCKED_COMPONENT_FORMULAS_NOT_SUPPLIED_BY_THIS_GATE',
   'ghost_operator_N1_N2_N3':'BLOCKED_COMPONENT_FORMULAS_NOT_SUPPLIED_BY_THIS_GATE',
   'source_contact_completion':'BLOCKED_DOWNSTREAM'
 },
 'guardrails':[
   'UNSUPPORTED_COMPONENT_KERNELS_BLOCKED_NOT_ZERO_FILLED',
   'NO_BLIND_HEAVY_FULL_C5',
   'NO_SOURCE_BORN_SUBTRACTION',
   'NO_ANSATZ003_FISHER_RESOURCES',
   'NEGATIVE_OR_BLOCKED_COMPONENT_RESULTS_MUST_BE_RETAINED'
 ],
 'next_gate':'freeze same-parent determinant graviton/ghost H1,H2,H3 component conventions and routing in D=4 Lambda=0 a=-1/2 before scoped numerator/cut evaluation; if unavailable, record BLOCKED rather than zero-fill.'
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
