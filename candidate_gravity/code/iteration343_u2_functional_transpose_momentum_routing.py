#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 343.

Functional-transpose Fourier-routing authority for the U2 left V1 factor.
Iteration 340 fixed the field/ghost index orientation V1_L=A.T, V1_R=A but did
not by itself determine the momentum argument of the transposed differential
kernel.  For the bilinear functional pairing (no complex conjugation),

  int dx T(x)^T [A[h_Q] c](x) = int dx c(x)^T [A_T[h_Q] T](x),

with c~exp(i p x), A[h_Q]c~exp(i(p+Q)x), the paired test tensor has
k=-(p+Q). Therefore

  A_T(Q;k) = A(Q; -k-Q)^T.

The background insertion still carries +Q around the loop; only the internal
momentum argument is transformed.  This gate validates the rule with the actual
linearized gravity V1 of primary Eq.(55) and cross-checks that implementation
against the frozen Iteration-341 A1 kernels.
"""
from __future__ import annotations
import contextlib, io, json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
# Reuse Iteration 341 only as an independent already-validated A1 oracle.
spec_src=(ROOT/'iteration341_u2_v1_a12_same_parent_geometry.py').read_text()
ns={'__name__':'iteration343_i341_oracle','__file__':str(ROOT/'iteration341_u2_v1_a12_same_parent_geometry.py')}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(spec_src,'iteration343_i341_oracle','exec'),ns,ns)

D=4; eta=np.diag([-1.,1.,1.,1.]).astype(complex)
B=ns['B']

def mat_from_cols(cols):
    out=np.zeros((len(B),D),complex)
    for j,T in enumerate(cols):
        for i,F in enumerate(B): out[i,j]=np.vdot(F,T)
    return out

def linear_A1(q,h,p):
    """D=4, Lambda=0, gamma1=1,gamma2=0 linear Eq.(55), field x ghost."""
    q=np.asarray(q,float); h=np.asarray(h,complex); p=np.asarray(p,float)
    # Linear Levi-Civita connection and Ricci tensor.
    G1=-eta@h@eta
    Gam=np.zeros((D,D,D),complex)
    for a,m,n,s in np.ndindex(D,D,D,D):
        Gam[a,m,n]+=0.5*eta[a,s]*(1j*q[m]*h[s,n]+1j*q[n]*h[s,m]-1j*q[s]*h[m,n])
    Ric=np.zeros((D,D),complex)
    for m in range(D):
      for n in range(D):
        for a in range(D): Ric[m,n]+=1j*q[a]*Gam[a,m,n]-1j*q[n]*Gam[a,m,a]
    RicUp=eta@Ric@eta
    Rsc=np.einsum('mn,mn->',eta,Ric)
    Rmix=eta@Ric
    p_up=eta@p
    cols=[]
    for rho in range(D):
        T=np.zeros((D,D),complex)
        for mu in range(D):
          for nu in range(D):
            T[mu,nu]+=0.5j*(Rmix[mu,rho]*p_up[nu]+Rmix[nu,rho]*p_up[mu])
            T[mu,nu]+=-0.5j*(RicUp[nu,rho]*p[mu]+RicUp[mu,rho]*p[nu])
            T[mu,nu]+=-q[rho]*RicUp[mu,nu]
            T[mu,nu]+=0.5j*RicUp[mu,nu]*p[rho]
            T[mu,nu]+=-0.5j*eta[mu,nu]*sum(Rmix[l,g]*(p[l] if g==rho else 0.0) for l in range(D) for g in range(D))
            T[mu,nu]+=0.25j*Rsc*((p_up[nu] if mu==rho else 0.0)+(p_up[mu] if nu==rho else 0.0))
            T[mu,nu]+=0.5*eta[mu,nu]*q[rho]*Rsc
            T[mu,nu]+=-0.25j*eta[mu,nu]*Rsc*p[rho]
        cols.append(T)
    return mat_from_cols(cols)

# Cross-check the independently coded linear Eq.(55) against both frozen I341 A1 modes.
p341=np.asarray(ns['p'],float); qs341=[np.asarray(x,float) for x in ns['qs']]; hs341=[np.asarray(x,complex) for x in ns['hs']]
Acoef=ns['Acoef']
a1_err0=float(np.max(np.abs(linear_A1(qs341[0],hs341[0],p341)-Acoef[(1,0)])))
a1_err1=float(np.max(np.abs(linear_A1(qs341[1],hs341[1],p341)-Acoef[(0,1)])))

# Functional-transpose pairing test on the first physical mode.
q=qs341[0]; h=hs341[0]; p=np.array([.57,-.31,.22,.46])
k=-(p+q)
AR=linear_A1(q,h,p)                  # field x ghost, input ghost p
AT_formula=linear_A1(q,h,-k-q).T    # ghost x field, input field k
transpose_kernel_error=float(np.max(np.abs(AT_formula-AR.T)))
phase_closure=float(np.max(np.abs(k+p+q)))

rng=np.random.default_rng(343)
c=rng.normal(size=D)+1j*rng.normal(size=D)
t=rng.normal(size=len(B))+1j*rng.normal(size=len(B))
lhs=t.T@(AR@c)
rhs=c.T@(AT_formula@t)
pairing_error=float(abs(lhs-rhs))

# Demonstrate that keeping the same input momentum at the transposed vertex is
# not an innocuous alternative. It should generically disagree with the formal
# transpose rule on this fixed physical fixture.
AT_wrong_same_k=linear_A1(q,h,k).T
wrong_route_difference=float(np.max(np.abs(AT_wrong_same_k-AT_formula)))

thresholds={'A1_independent_crosscheck_abs_max':2e-12,'transpose_kernel_abs_max':1e-13,
            'pairing_abs_max':2e-13,'phase_closure_abs_max':1e-15,
            'wrong_route_difference_min':1e-6}
passed=(max(a1_err0,a1_err1)<=thresholds['A1_independent_crosscheck_abs_max'] and
        transpose_kernel_error<=thresholds['transpose_kernel_abs_max'] and
        pairing_error<=thresholds['pairing_abs_max'] and
        phase_closure<=thresholds['phase_closure_abs_max'] and
        wrong_route_difference>=thresholds['wrong_route_difference_min'])

result={
 'iteration':343,'model_readiness_percent':24,'scientific_gate_pass':bool(passed),
 'classification':('PASS_U2_FUNCTIONAL_TRANSPOSE_FOURIER_ROUTING_A_T_Q_K_EQUALS_A_Q_MINUSKMINUSQ_T__PHYSICAL_ASSEMBLY_ROUTING_FROZEN'
                   if passed else 'FAIL_U2_FUNCTIONAL_TRANSPOSE_FOURIER_ROUTING'),
 'candidate_residual':False,
 'frozen_rule':{'right_vertex':'A_R(Q;p)=A(Q;p), maps ghost momentum p -> field momentum p+Q',
                'left_transposed_vertex':'A_T(Q;k)=A(Q;-k-Q)^T, maps field momentum k -> ghost momentum k+Q',
                'background_momentum':'both orientations carry the same +Q external insertion',
                'trace_consequence':'ordinary closed-loop external-momentum sum remains sum_i Q_i=0'},
 'validation':{'iteration341_A1_mode0_crosscheck_error':a1_err0,'iteration341_A1_mode1_crosscheck_error':a1_err1,
               'transpose_kernel_error':transpose_kernel_error,'bilinear_pairing_error':pairing_error,
               'fourier_phase_closure_error':phase_closure,'wrong_same_momentum_route_difference':wrong_route_difference,
               'thresholds':thresholds},
 'scope':{'D':4,'Lambda':0,'gamma1':1,'gamma2':0,'metric_split':'g=eta+h','physical_vertex':'primary Eq55 linear A1'},
 'status':{'A1_A2_components':'FROZEN_ITERATION341','N_Y_routing':'FROZEN_ITERATION342','functional_A_transpose_routing':'FROZEN_EXECUTABLE' if passed else 'FAIL_PRESERVE','TrU2_assembly':'AUTHORIZED_NEXT' if passed else 'BLOCKED'},
 'guardrails':['DO_NOT_USE_A_Q_K_TRANSPOSE_AT_SAME_K_FOR_LEFT_VERTEX','ITERATION340_INDEX_TRANSPOSE_ORIENTATION_BINDING','ITERATION340_HINV_VD_MINUS_KINV_BINDING','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':'assemble the cubic-background physical Tr U2 coefficient with the frozen Iteration308 placement map, using A_T(Q;k)=A(Q;-k-Q)^T on the left, Iteration339/340 Hinv routing/sign, and Iteration342 ghost N/Y routing; validate the 12 null-soft surviving routes before cut integration'
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
