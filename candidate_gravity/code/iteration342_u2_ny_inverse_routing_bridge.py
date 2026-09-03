#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 342.

Same-parent N/Y inverse-routing bridge for the Vilkovisky U2 operator.

Primary relations (Giacchini, de Paula Netto & Shapiro 2020):
  hat N^a_b = Y^{a g} N_{g b},
with the gravity gauge of Eq. (48) implying, relative to the generic
S_GF=-1/2 chi^a Y_ab chi^b convention,
  Y_ab=-g_ab,  Y^{ab}=-g^{ab}.
Eq. (57) gives the corresponding ghost Green object and fixes the flat sign.

At a=-1/2 the frozen RQIR same-parent minimal ghost operator is exactly the
Iteration-317 operator hat N = delta Box + R.  This gate imports only its
already-validated physical N0/N1 background coefficients and tests the inverse
routing on a two-momentum block {p,p+q}.  It freezes no U2 numerator by itself.
"""
from __future__ import annotations
import contextlib, io, json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
# Load only the frozen physical polynomial ghost construction, stopping before
# Iteration 317's independent direct-geometry fit executes.
src=(ROOT/'iteration317_det_ghost_three_mode_routing.py').read_text()
prefix=src.split('# Independent exact-geometry oracle',1)
if len(prefix)!=2:
    raise RuntimeError('Iteration-317 authority boundary changed; refuse implicit rebase')
ns={'__name__':'iteration342_frozen_ghost_parent','__file__':str(ROOT/'iteration317_det_ghost_three_mode_routing.py')}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(prefix[0],'iteration342_frozen_ghost_parent','exec'),ns,ns)

D=ns['D']; eta=np.asarray(ns['eta'],complex); p=np.asarray(ns['p'],float)
qs=[np.asarray(x,float) for x in ns['qs']]; hs=[np.asarray(x,complex) for x in ns['hs']]
N=ns['N']; G=ns['G']; ZERO=ns['ZERO']
mode=(1,0,0); q=qs[0]; N1=np.asarray(N[mode],complex)

def mdot(a,b):
    return complex(np.asarray(a,complex)@eta@np.asarray(b,complex))

def hatN0(k):
    # Iteration-317 flat identity: Box exp(i k.x) = -k^2 exp(i k.x).
    return -mdot(k,k)*np.eye(D,dtype=complex)

def maxabs(x): return float(np.max(np.abs(x)))

N0p=hatN0(p); N0pq=hatN0(p+q)
flat_parent_error=maxabs(np.asarray(N[ZERO],complex)-N0p)
Q0p=np.linalg.inv(N0p); Q0pq=np.linalg.inv(N0pq)
Q1=-Q0pq@N1@Q0p

# Independent shifted left/right inverse equations at first background order.
left_inverse_res=N0pq@Q1+N1@Q0p
right_inverse_res=Q1@N0p+Q0pq@N1
left_inverse_error=maxabs(left_inverse_res)
right_inverse_error=maxabs(right_inverse_res)

# Two-momentum block representation.  Lower-left blocks carry the physical
# background mode q: input p -> output p+q.
Z=np.zeros((D,D),complex)
def block(A00,A01,A10,A11): return np.block([[A00,A01],[A10,A11]])
Hat=block(N0p,Z,N1,N0pq)
Q_direct=np.linalg.inv(Hat)
Q_expected=block(Q0p,Z,Q1,Q0pq)
q_block_error=maxabs(Q_direct-Q_expected)

# Gauge metric.  Generic paper convention plus Eq.(48) gives Y_lower=-g,
# Y_upper=-g^{-1}.  G[mode] is the frozen inverse-metric first coefficient.
Yup0=-eta
Yup1=-np.asarray(G[mode],complex)
Ylow0=-eta
Ylow1=-hs[0]
Yup=block(Yup0,Z,Yup1,Yup0)
Ylow=block(Ylow0,Z,Ylow1,Ylow0)
y_inverse_error=maxabs(Yup@Ylow-np.eye(2*D))
y_inverse_error=max(y_inverse_error,maxabs(Ylow@Yup-np.eye(2*D)))

# From hatN=Yup*N_lower, infer N_lower=Ylow*hatN and invert independently.
Nlower=Ylow@Hat
Nupper_direct=np.linalg.inv(Nlower)
Nupper_from_QY=Q_direct@Yup
nupper_bridge_error=maxabs(Nupper_direct-Nupper_from_QY)

# Exact companion identity entering the right side of U2:
# N^{a d} Y_{d b} = hatN^{-1 a}_b.
right_NY_error=maxabs(Nupper_direct@Ylow-Q_direct)

# First-order routed formula for the left U2 N factor, extracted independently
# from the block product Q*Yup.
L0=Q0p@Yup0
L1=Q0pq@Yup1+Q1@Yup0
left_block_formula_error=maxabs(Nupper_from_QY[:D,:D]-L0)
left_block_formula_error=max(left_block_formula_error,maxabs(Nupper_from_QY[D:,:D]-L1))

# Eq.(57) flat calibration: N^{ab}=-g^{ab}/Box; Box eigenvalue=-p^2.
p2=mdot(p,p)
eq57_flat=-eta/(-p2)
eq57_flat_error=maxabs(L0-eq57_flat)

thresholds={
 'flat_parent_abs_max':1e-12,
 'inverse_identity_abs_max':2e-11,
 'block_inverse_abs_max':2e-11,
 'Y_inverse_abs_max':2e-12,
 'NY_bridge_abs_max':2e-11,
 'Eq57_flat_abs_max':2e-12,
}
passed=(flat_parent_error<=thresholds['flat_parent_abs_max'] and
        left_inverse_error<=thresholds['inverse_identity_abs_max'] and
        right_inverse_error<=thresholds['inverse_identity_abs_max'] and
        q_block_error<=thresholds['block_inverse_abs_max'] and
        y_inverse_error<=thresholds['Y_inverse_abs_max'] and
        nupper_bridge_error<=thresholds['NY_bridge_abs_max'] and
        right_NY_error<=thresholds['NY_bridge_abs_max'] and
        left_block_formula_error<=thresholds['NY_bridge_abs_max'] and
        eq57_flat_error<=thresholds['Eq57_flat_abs_max'])

result={
 'iteration':342,
 'model_readiness_percent':24,
 'scientific_gate_pass':bool(passed),
 'classification':('PASS_U2_SAME_PARENT_NY_INVERSE_ROUTING_BRIDGE_WITH_PHYSICAL_GHOST_N1__FIRST_BACKGROUND_TRU2_ASSEMBLY_AUTHORIZED_NEXT'
                   if passed else 'FAIL_U2_NY_INVERSE_ROUTING_BRIDGE'),
 'candidate_residual':False,
 'primary_authority':{
   'paper':'Giacchini-de Paula Netto-Shapiro 2020 arXiv:2006.04217v4',
   'relations':['hatN=Yupper*Nlower','Ylower=-g','Yupper=-g^{-1}','Eq57 ghost Green expansion']
 },
 'frozen_parent':{'ghost_operator':'Iteration317 hatN=delta Box+R','D':4,'Lambda':0,'a':'-1/2','mode':list(mode),'p':p.tolist(),'q':q.tolist()},
 'routing':{
   'Q0':'hatN0(p)^{-1}',
   'Q1':'-Q0(p+q) @ hatN1(q;p) @ Q0(p)',
   'left_N0':'Q0(p) @ Yupper0',
   'left_N1':'Q0(p+q) @ Yupper1(q) + Q1(q;p) @ Yupper0',
   'right_NY':'Q = hatN^{-1}'
 },
 'validation':{
   'flat_parent_error':flat_parent_error,
   'left_inverse_error':left_inverse_error,
   'right_inverse_error':right_inverse_error,
   'two_momentum_block_inverse_error':q_block_error,
   'Yupper_Ylower_inverse_error':y_inverse_error,
   'Nupper_equals_QYupper_error':nupper_bridge_error,
   'Nupper_Ylower_equals_Q_error':right_NY_error,
   'left_first_order_block_formula_error':left_block_formula_error,
   'Eq57_flat_sign_error':eq57_flat_error,
   'thresholds':thresholds
 },
 'status':{
   'physical_A1_A2':'FROZEN_FROM_ITERATION341',
   'N_Y_inverse_routing':'FROZEN_EXECUTABLE' if passed else 'FAIL_PRESERVE',
   'Hinv_VD_sign':'FROZEN_FROM_ITERATION340_MINUS_KINV',
   'first_background_TrU2_assembly':'AUTHORIZED_NEXT' if passed else 'BLOCKED'
 },
 'guardrails':['ITERATION340_A_TRANSPOSE_A_ORIENTATION_BINDING','ITERATION340_HINV_VD_MINUS_KINV_BINDING','NO_DOUBLE_GHOST_INVERSE_OR_Y_FACTOR','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],
 'next_gate':'assemble the complete first-background-order physical Tr U2 from the six typed Iteration309 derivative sites using Iteration341 A1/A2, this N/Y bridge, the Iteration339 shifted graviton inverse routing with Iteration340 Hinv_VD=-K^-1, and independently validate route/trace closure before any cut integration'
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
