#!/usr/bin/env python3
"""Iteration 644: prospective external-tensor transport contract for closed-Gamma3.

This gate is frozen before any numerator-weighted cut output is evaluated.
It first proves that covariance + the Iter368 anchor do NOT uniquely determine
h_s(s), h_a(s), h_b(s): an s-dependent common O(2) little-group rotation about
the spatial q_a direction preserves the entire closed-Gamma3 momentum family
and can satisfy theta(1)=0 while changing generic anchor tensors away from s=1.

After classifying that residual freedom, this iteration prospectively defines
MSSC001-CLOSED-GAMMA3-TENSOR-TRANSPORT-V1: use the canonical q_s rest-frame
trajectory in the fixed anchor scattering plane and zero transverse twist; hold
all tetrad components of each Iter368 symmetric metric probe fixed. In the
exact Iter368 coordinate frame this is numerically h_i(s)=h_i(1), but that fact
is now a pre-result versioned observable definition, not a post-hoc shortcut.

No TT/transversality or unit-normalization condition is imposed because the
same-parent Iter368 probes are arbitrary symmetric metric perturbations created
from RNG seed 319; imposing new gauge conditions would change the observable.
"""
from __future__ import annotations
import json, math, pathlib
import numpy as np

ITERATION=644
ROOT=pathlib.Path(__file__).resolve().parents[2]
T0=0.14
U0=0.34
S0=1.0
CUT_THRESHOLD=1.96

ETA=np.diag([1.0,-1.0,-1.0,-1.0])
E0=np.array([1.0,0.0,0.0,0.0])
E1=np.array([0.0,1/math.sqrt(2),1/math.sqrt(2),0.0])
E2=np.array([0.0,1/math.sqrt(2),-1/math.sqrt(2),0.0])
E3=np.array([0.0,0.0,0.0,1.0])
TETRAD=np.stack([E0,E1,E2,E3])


def mdot(a,b):
    return float(np.asarray(a)@ETA@np.asarray(b))


def momenta(s):
    """Canonical fixed-(t0,u0) closed-Gamma3 representative.

    q_s is future timelike and at rest; q_a spatial direction is frozen to the
    exact Iter368 anchor direction. The branch is chosen continuously through
    s0=1 and is valid where the Kallen spatial momentum is real.
    """
    rs=math.sqrt(float(s))
    ea=(U0-float(s)-T0)/(2*rs)
    k2=ea*ea-T0
    if k2 < -1e-14:
        raise ValueError(f'closed-Gamma3 representative not real at s={s}: k2={k2}')
    k=math.sqrt(max(k2,0.0))
    qs=np.array([rs,0.0,0.0,0.0])
    qa=ea*E0+k*E1
    qb=-qs-qa
    return qs,qa,qb,k2


def anchor_tensors():
    rng=np.random.default_rng(319)
    out=[]
    for _ in range(3):
        x=rng.normal(size=(4,4))
        out.append(0.12*(x+x.T)/2.0)
    return out


def little_group_rotation(theta):
    """Proper spatial rotation about anchor E1; leaves qs,qa,qb invariant."""
    axis=E1[1:]
    x,y,z=axis
    K=np.array([[0.0,-z,y],[z,0.0,-x],[-y,x,0.0]])
    c=math.cos(theta); ss=math.sin(theta)
    R3=c*np.eye(3)+(1-c)*np.outer(axis,axis)+ss*K
    L=np.eye(4); L[1:,1:]=R3
    return L


def transport_v1(s, hs):
    # Zero-twist tetrad-component transport. The chosen tetrad is constant on
    # this canonical representative, hence the coordinate matrices are fixed.
    _=momenta(s)
    return [h.copy() for h in hs]


failures=[]
hs=anchor_tensors()
qs0,qa0,qb0,k20=momenta(S0)
expected_qs=np.array([1.0,0.0,0.0,0.0])
expected_qa=np.array([-0.4,0.1,0.1,0.0])
expected_qb=np.array([-0.6,-0.1,-0.1,0.0])
anchor_err=max(np.max(np.abs(qs0-expected_qs)),np.max(np.abs(qa0-expected_qa)),np.max(np.abs(qb0-expected_qb)))
if anchor_err>2e-15: failures.append(f'anchor momentum recovery drift {anchor_err}')

# Tetrad orthonormality in +---.
gram=TETRAD@ETA@TETRAD.T
tetrad_err=float(np.max(np.abs(gram-ETA)))
if tetrad_err>2e-15: failures.append(f'tetrad orthonormality drift {tetrad_err}')

# Verify the physical cut region representative and invariants at two points.
kin_checks=[]
for s in (S0,CUT_THRESHOLD,2.0,3.0):
    qs,qa,qb,k2=momenta(s)
    inv=[mdot(qs,qs),mdot(qa,qa),mdot(qb,qb)]
    closure=float(np.max(np.abs(qs+qa+qb)))
    ierr=max(abs(inv[0]-s),abs(inv[1]-T0),abs(inv[2]-U0))
    if closure>2e-15 or ierr>2e-14: failures.append(f'kinematic drift at s={s}: closure={closure}, ierr={ierr}')
    kin_checks.append({'s':s,'q_s':qs.tolist(),'q_a':qa.tolist(),'q_b':qb.tolist(),'k2':k2,
                       'invariants':inv,'closure_max_abs':closure})

# Construct two admissible continuations that coincide at s0 but differ at s=2.
# theta_0(s)=0 is V1. theta_1(s)=s-s0 proves covariance/anchor non-uniqueness.
s_test=2.0
qs2,qa2,qb2,_=momenta(s_test)
L=little_group_rotation(s_test-S0)
lorentz_err=float(np.max(np.abs(L.T@ETA@L-ETA)))
momentum_stabilizer_err=max(float(np.max(np.abs(L@q-q))) for q in (qs2,qa2,qb2))
if lorentz_err>2e-15: failures.append(f'little-group Lorentz drift {lorentz_err}')
if momentum_stabilizer_err>2e-15: failures.append(f'little-group momentum stabilizer drift {momentum_stabilizer_err}')

rotated=[L@h@L.T for h in hs]
probe_differences=[float(np.max(np.abs(hr-h))) for h,hr in zip(hs,rotated)]
if not all(d>1e-6 for d in probe_differences): failures.append('generic probe did not witness little-group non-uniqueness')

# V1 exact anchor reduction and tensor symmetry.
hv1_anchor=transport_v1(S0,hs)
hv1_cut=transport_v1(CUT_THRESHOLD,hs)
h_anchor_err=max(float(np.max(np.abs(a-b))) for a,b in zip(hv1_anchor,hs))
symmetry_err=max(float(np.max(np.abs(h-h.T))) for h in hv1_cut)
if h_anchor_err>0.0: failures.append(f'V1 anchor tensor drift {h_anchor_err}')
if symmetry_err>1e-15: failures.append(f'V1 symmetry drift {symmetry_err}')

classification=('PASS_ITER644_PROSPECTIVE_EXTERNAL_TENSOR_TRANSPORT_V1__COVARIANCE_ALONE_NONUNIQUE__ZERO_TWIST_TETRAD_COMPONENTS_FROZEN__NON_RESIDUAL'
                if not failures else
                'FAIL_ITER644_EXTERNAL_TENSOR_TRANSPORT_CONTRACT_PREREQUISITE')

result={
 'iteration':ITERATION,
 'date':'2026-09-09',
 'scientific_gate_pass':not failures,
 'candidate_residual':False,
 'classification':classification,
 'contract_id':'MSSC001-CLOSED-GAMMA3-TENSOR-TRANSPORT-V1',
 'failures':failures,
 'authority':{
   'anchor':'Iteration368/588 exact fixture',
   'anchor_s0':S0,'t0':T0,'u0':U0,'ordinary_cut_threshold':CUT_THRESHOLD,
   'anchor_tensor_generation':'np.random.default_rng(319); 0.12*(x+x.T)/2',
   'tensor_role':'arbitrary symmetric metric probes, not TT physical graviton polarizations'
 },
 'canonical_momentum_representative':{
   'q_s':'(sqrt(s),0,0,0)',
   'q_a_energy':'(u0-s-t0)/(2*sqrt(s))',
   'q_a_spatial_direction':'E1=(0,1/sqrt(2),1/sqrt(2),0)',
   'q_a_spatial_magnitude':'sqrt(q_a0^2-t0)',
   'q_b':'-q_s-q_a',
   'kinematic_checks':kin_checks
 },
 'nonuniqueness_certificate':{
   'statement':'covariance+anchor are insufficient: common O(2) rotations about E1 leave all momenta/invariants fixed while changing generic metric probes',
   'residual_freedom_lower_bound':'at least one arbitrary smooth function theta(s) with theta(1)=0',
   'test_s':s_test,
   'lorentz_error':lorentz_err,
   'momentum_stabilizer_error':momentum_stabilizer_err,
   'probe_max_abs_differences':probe_differences
 },
 'frozen_v1':{
   'rule':'zero transverse twist; hold all tetrad components of each anchor metric probe fixed along the canonical trajectory',
   'coordinate_frame_consequence':'h_s(s)=h_s(1), h_a(s)=h_a(1), h_b(s)=h_b(1) in the exact Iter368 frame',
   'status':'prospectively versioned observable definition before numerator-weighted cut evaluation',
   'gauge_condition':'NONE_ADDED',
   'transversality_condition':'NONE_ADDED',
   'normalization_condition':'fixed anchor tetrad components; no new unit normalization',
   'symmetry':'h_{mu nu}=h_{nu mu}',
   'anchor_tensor_max_error':h_anchor_err,
   'symmetry_max_error':symmetry_err
 },
 'guardrails':{
   'candidate_values_used':False,'cut_numerators_evaluated':False,'zero_fill':False,
   'source_born_subtraction':'NOT_PERFORMED','native_projection':'NOT_PERFORMED','comparator_quotient':'NOT_PERFORMED',
   'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN'
 },
 'MODEL_READINESS':'24%',
 'readiness_change':'0 percentage points: a prerequisite observable contract closes, but robust unique residual remains 0/20 and no complete rubric sector closes',
 'next_gate':'Iteration645: using only Iter594 same-parent K1/K2/K3 machinery plus Iter627/632 retarded-state authority and this frozen V1 tensor trajectory, evaluate numerator-weighted ordinary s-channel cut densities family-by-family for K1/K2 and K1^3 on s>=1.96; keep K3 analytic/contact and do not perform native projection or Source/Born subtraction yet.'
}

out=ROOT/'results'/'iteration644_external_tensor_transport_contract'
out.mkdir(parents=True,exist_ok=True)
(out/'result.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
if failures: raise SystemExit(2)
