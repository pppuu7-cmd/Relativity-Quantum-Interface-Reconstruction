#!/usr/bin/env python3
"""Iteration 655: prospectively freeze the exact soft T_cut kinematics.

No cut values are evaluated. This gate only fixes a non-Candidate-tuned soft
trajectory, tensor transport, hard invariant, and order of operations.
"""
from pathlib import Path
import json, math

ROOT=Path(__file__).resolve().parents[2]
failures=[]
d654=json.loads((ROOT/'candidate_gravity/results/iteration654_soft_target_vs_finite_family_compatibility_audit.json').read_text())
d653=json.loads((ROOT/'candidate_gravity/results/iteration653_closed_sk_gamma2_gamma3_ward_contract.json').read_text())
d205=json.loads((ROOT/'results/linked_nonanalytic_cut_protocol_iteration205.json').read_text())

if d654.get('scientific_gate_pass') is not True:
    failures.append('Iter654 raw-valid blocker authority missing')
if d653.get('parent',{}).get('contract_id')!='MSSC001-CLOSED-SK-GAMMA2-GAMMA3-WARD-V1':
    failures.append('Iter653 normalized parent drift')
if d205.get('proposed_coordinate')!='T_cut = D Gamma3_ret,soft - W[D K2] in one source-completed convention':
    failures.append('Iter205 target drift')

# +--- signature. The choice is prospective and independent of Candidate values.
def mink(q):
    return q[0]*q[0]-q[1]*q[1]-q[2]*q[2]-q[3]*q[3]
def add(*vs):
    return [sum(x) for x in zip(*vs)]
def norm(v):
    return math.sqrt(sum(x*x for x in v))

n=[1.0,0.0,0.0,1.0]                 # fixed future-directed null soft direction
rt2=math.sqrt(2.0)
eplus=[[0.0]*4 for _ in range(4)]
eplus[1][1]=1.0/rt2
eplus[2][2]=-1.0/rt2                 # fixed TT + polarization

checks=[]
for s in (2.0,3.0,5.0):             # audit points only; not a physics grid
    p=[math.sqrt(s),0.0,0.0,0.0]
    for eps in (1e-1,1e-2,1e-3):
        q=[eps*x for x in n]
        r=[-(p[i]+q[i]) for i in range(4)]
        closure=add(q,p,r)
        # contractions q^mu e_{mu nu}; all nonzero e components are x/y.
        trans_soft=max(abs(sum(q[mu]*eplus[mu][nu] for mu in range(4))) for nu in range(4))
        trans_p=max(abs(sum(p[mu]*eplus[mu][nu] for mu in range(4))) for nu in range(4))
        trans_r=max(abs(sum(r[mu]*eplus[mu][nu] for mu in range(4))) for nu in range(4))
        row={
          's':s,'epsilon':eps,'q_soft':q,'p_hard':p,'q_other':r,
          'q_soft_sq':mink(q),'p_hard_sq':mink(p),'q_other_sq':mink(r),
          'closure_max_abs':max(abs(x) for x in closure),
          'q_other_plus_p_euclidean_norm':norm(add(r,p)),
          'expected_soft_distance':eps*norm(n),
          'polarization_transversality_max_abs':max(trans_soft,trans_p,trans_r)
        }
        checks.append(row)
        if abs(row['q_soft_sq'])>1e-13 or abs(row['p_hard_sq']-s)>1e-13:
            failures.append('kinematic invariant failure')
        if row['closure_max_abs']>1e-13:
            failures.append('momentum closure failure')
        if abs(row['q_other_plus_p_euclidean_norm']-row['expected_soft_distance'])>1e-13:
            failures.append('soft-limit scaling failure')
        if row['polarization_transversality_max_abs']>1e-13:
            failures.append('TT transport failure')

result={
 'iteration':655,
 'date':'2026-09-09',
 'classification':('PASS_ITER655_PROSPECTIVE_SOFT_T_CUT_KINEMATIC_CONTRACT_FROZEN__NO_CUT_VALUES_NON_RESIDUAL' if not failures else 'BLOCKED_ITER655_CONTRACT_VALIDATION_FAILURE__NON_RESIDUAL'),
 'scientific_gate_pass':not failures,
 'contract_id':'MSSC001-CLOSED-SK-SOFT-TCUT-KIN-V1',
 'signature':'+---',
 'soft_leg':{
   'label':'q_soft',
   'definition':'q_soft(epsilon)=epsilon*n',
   'n':[1.0,0.0,0.0,1.0],
   'n_squared':0.0,
   'limit':'epsilon -> 0+',
   'polarization':'e_plus with e_xx=+1/sqrt(2), e_yy=-1/sqrt(2), all other components zero'
 },
 'hard_channel':{
   'momentum':'p(s)=(sqrt(s),0,0,0)',
   'invariant':'s=p^2',
   'ordinary_cut_threshold':'s=4*m_phi^2=1.96',
   'working_domain':'s>1.96; threshold itself is excluded from any limit-commutation claim'
 },
 'third_leg':{
   'definition':'q_other(epsilon,s)=-p(s)-q_soft(epsilon)',
   'soft_limit':'q_other -> -p'
 },
 'tensor_transport':{
   'soft':'fixed e_plus',
   'hard_p':'fixed e_plus',
   'other':'fixed e_plus',
   'status':'transverse and traceless for the chosen p,n,q_other trajectory; no Candidate-value tuning'
 },
 'order_of_operations':{
   'frozen_order':['hold epsilon>0 fixed','take D_s=Disc_s/(2*pi*i) in the hard invariant s','extract the prescribed soft coefficient / epsilon->0+ limit'],
   'commutation_claim':'NO_GLOBAL_COMMUTATION_CLAIM. Any interchange of D_s and epsilon->0 requires a separate uniformity proof on a stated compact domain away from threshold/Landau singularities.'
 },
 'parent':d653.get('parent'),
 'candidate_residual':False,
 'MODEL_READINESS':'24%',
 'readiness_change':'0 percentage points',
 'source_born_subtraction':'NOT_PERFORMED',
 'native_Y_Tcut_projection':'NOT_PERFORMED',
 'comparator_quotient':'NOT_PERFORMED',
 'zero_fill':False,
 'ANSATZ_003':'FORBIDDEN',
 'Fisher_resources':'FORBIDDEN',
 'checks':checks,
 'failures':sorted(set(failures)),
 'next_gate':'Iteration656: using only MSSC001-CLOSED-SK-SOFT-TCUT-KIN-V1 and Iter653 parent normalization, derive the epsilon-leading closed-SK Gamma2 Ward image W[D_s K2] and Gamma3 soft-cut integrand/topology before any numerical integration; classify pole/cut origin and remain fail-closed on unsupported contact/transverse terms.'
}
out=ROOT/'candidate_gravity/results/iteration655_soft_tcut_kinematic_contract.json'
out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
if failures: raise SystemExit(2)
