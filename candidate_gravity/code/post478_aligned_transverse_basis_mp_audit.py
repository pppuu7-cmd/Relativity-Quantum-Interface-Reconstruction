#!/usr/bin/env python3
"""Post-Iteration-478 aligned transverse-basis MP reconstruction audit.

Iteration 478 closed MP80/120 arithmetic for alpha,rho,beta,p,cc,aa when the
Iteration431/407 source vectors and aligned basis are treated as frozen decimal
inputs.  This collision-safe gate moves the precision boundary one layer
upstream: reconstruct the complete transverse basis and the Iteration407
aligned (e1,e2,e3) basis directly at MP80/MP120 from the frozen physical source
shift vectors and the repository Minkowski metric.

No mass support, numerator, routing, estimator, threshold or physical promotion
is changed.  PASS is precision/provenance only.
"""
from __future__ import annotations
import contextlib, io, json, time
from pathlib import Path
import numpy as np
import mpmath as mp

ROOT = Path(__file__).resolve().parent
MP_LEVELS = (80, 120)
MP_LIMIT = mp.mpf('1e-30')
ASSEMBLY_REFERENCE = mp.mpf('2e-6')
PHYSICAL_REFERENCE = mp.mpf('2e-5')

# Bind latest canonical geometry closure fail-closed.
R = ROOT.parent / 'results'
geo_candidates = [
    R/'iteration478_frozen_basis_geometry_mp_raw_consumed.json',
    R/'iteration478_geometry_mp_raw_consumed.json',
    R/'iteration478_frozen_basis_geometry_mp_audit.json',
]
geo = None
for p in geo_candidates:
    if p.exists():
        o = json.loads(p.read_text())
        if o.get('scientific_gate_pass') is True or o.get('scientific_result',{}).get('scientific_gate_pass') is True:
            geo = o; break
if geo is None:
    # Canonical authority can also be represented only through recovery/current
    # front while filenames evolve.  Bind CURRENT_QG_FRONT text as a strict
    # fallback and require explicit Iteration 478 geometry PASS wording.
    front = (ROOT.parent/'recovery/CURRENT_QG_FRONT.md').read_text()
    required = ['Latest authoritative research iteration: **Iteration 478**',
                'PASS_FROZEN_BASIS_GEOMETRY_ARITHMETIC_MP80_MP120']
    if not all(x in front for x in required):
        raise SystemExit('iteration478_geometry_prerequisite_not_found')

# Load exact same specialized index2 source construction as Iter431, stopping
# before its diagnostic execution.
p431 = ROOT/'iteration431_channel2_cut_kinematic_h1_sensitivity.py'
s431 = p431.read_text(); marker = 'records=[]; max_delta=0.0; max_raderr=0.0'
if s431.count(marker) != 1:
    raise SystemExit(('iteration431_boundary_drift', s431.count(marker)))
C = {'__name__':'post478_basis_parent431','__file__':str(p431)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(s431.split(marker,1)[0], str(p431), 'exec'), C, C)
ns407 = C['ns407']
if int(C['ch']['class_id']) != 3 or abs(float(C['q2']) + 1.0) > 1e-12:
    raise SystemExit(('target_identity_drift', C['ch']['class_id'], C['q2']))

# Frozen source vectors.  For this physical fixture they descend from the exact
# decimal TIMELIKE_Q vectors of Iteration368; convert their stored decimal float
# representations into MP rather than doing any further binary arithmetic.
a_np = np.asarray(ns407['a'], float)
b_np = np.asarray(ns407['b'], float)
c_np = np.asarray(ns407['c'], float)
q_np = np.asarray(ns407['q'], float)
ETA_np = np.asarray(C['ETA'], float)
e_bin = [np.asarray(ns407['e1'],float), np.asarray(ns407['e2'],float), np.asarray(ns407['e3'],float)]

SEEDS = [
    [0.,1.,0.,0.], [0.,0.,1.,0.], [0.,0.,0.,1.],
    [1.,0.,0.,0.], [1.,1.,0.,0.], [1.,0.,1.,0.],
]


def mpr(x): return mp.mpf(repr(float(x)))
def vec(x): return [mpr(t) for t in x]
def eta_mp(): return [[mpr(ETA_np[i,j]) for j in range(4)] for i in range(4)]
def add(a,b): return [a[i]+b[i] for i in range(4)]
def sub(a,b): return [a[i]-b[i] for i in range(4)]
def scale(s,a): return [s*a[i] for i in range(4)]
def bil(a,b,E): return sum(a[i]*E[i][j]*b[j] for i in range(4) for j in range(4))
def norm_scaled(a,b):
    return max(abs(a[i]-b[i]) for i in range(4))/max([mp.mpf(1)]+[abs(x) for x in a]+[abs(x) for x in b])


def reconstruct(dps):
    with mp.workdps(dps):
        E=eta_mp(); a=vec(a_np); b=vec(b_np); c=vec(c_np); q=sub(b,a)
        q2=bil(q,q,E)
        if q2 >= 0: raise RuntimeError(('q_not_timelike', mp.nstr(q2,30)))
        def proj(v): return sub(v, scale(bil(v,q,E)/q2, q))
        base=[]
        for s0 in SEEDS:
            v=proj(vec(s0))
            for e in base: v=sub(v,scale(bil(v,e,E),e))
            n2=bil(v,v,E)
            if n2 > mp.mpf('1e-40'): base.append(scale(1/mp.sqrt(n2),v))
            if len(base)==3: break
        if len(base)!=3: raise RuntimeError('mp_transverse_basis_failed')
        rvec=proj(sub(c,a)); r2=bil(rvec,rvec,E)
        if r2 <= mp.mpf('1e-40'): raise RuntimeError('mp_aligned_e3_degenerate')
        e3=scale(1/mp.sqrt(r2),rvec)
        es=[]
        for seed in base:
            v=sub(seed,scale(bil(seed,e3,E),e3))
            for e in es: v=sub(v,scale(bil(v,e,E),e))
            n2=bil(v,v,E)
            if n2 > mp.mpf('1e-40'): es.append(scale(1/mp.sqrt(n2),v))
            if len(es)==2: break
        if len(es)!=2: raise RuntimeError('mp_aligned_e12_failed')
        e1,e2=es
        G=[[bil(x,y,E) for y in (e1,e2,e3)] for x in (e1,e2,e3)]
        qorth=[bil(q,e,E) for e in (e1,e2,e3)]
        return {'q2':q2,'e':[e1,e2,e3],'gram':G,'qorth':qorth,'r2':r2}

start=time.perf_counter(); outp={d:reconstruct(d) for d in MP_LEVELS}
with mp.workdps(150):
    m80,m120=outp[80],outp[120]
    cross=max(norm_scaled(m80['e'][i],m120['e'][i]) for i in range(3))
    binary=max(norm_scaled([mpr(x) for x in e_bin[i]],m120['e'][i]) for i in range(3))
    gram80=max(abs(m80['gram'][i][j]-(1 if i==j else 0)) for i in range(3) for j in range(3))
    gram120=max(abs(m120['gram'][i][j]-(1 if i==j else 0)) for i in range(3) for j in range(3))
    qorth120=max(abs(x) for x in m120['qorth'])
    q2cross=abs(m80['q2']-m120['q2'])/max(1,abs(m80['q2']),abs(m120['q2']))
    finite=all(mp.isfinite(x) for lev in outp.values() for e in lev['e'] for x in e)
    passed=bool(finite and cross<=MP_LIMIT and q2cross<=MP_LIMIT)
    material_assembly=bool(binary>ASSEMBLY_REFERENCE); material_physical=bool(binary>PHYSICAL_REFERENCE)
    result={
      'stage':'POST478_ALIGNED_TRANSVERSE_BASIS_MP_AUDIT__COLLISION_SAFE',
      'classification':('PASS_ALIGNED_TRANSVERSE_BASIS_MP80_MP120__BINARY_DRIFT_DIAGNOSTIC_ONLY_NON_PROMOTING' if passed else 'BLOCKED_ALIGNED_TRANSVERSE_BASIS_MP__NON_PROMOTING'),
      'scientific_gate_pass':passed,'promotes_physical_coordinate':False,
      'MODEL_READINESS':'24%','readiness_change_pp':0,
      'target':{'double_double_index':2,'class_id':3,'q_squared':-1.0},
      'scope':'RECONSTRUCT_TRANSVERSE_BASIS_AND_ITER407_ALIGNED_E1_E2_E3_FROM_FROZEN_SOURCE_SHIFTS_AT_MP80_MP120',
      'frozen':{'precision_digits':[80,120],'source_vectors':'a,b,c from Iter407/index2 specialized source; underlying Iter368 TIMELIKE_Q decimal fixture','seed_order':SEEDS,'metric':'repository ETA'},
      'thresholds':{'mp80_vs_mp120_scaled_max':'1e-30','assembly_reference_diagnostic_only':'2e-6','physical_reference_diagnostic_only':'2e-5','all_finite':True},
      'observed':{
        'mp80_vs_mp120_scaled_basis_max':mp.nstr(cross,30),
        'mp80_vs_mp120_scaled_q2':mp.nstr(q2cross,30),
        'binary64_vs_mp120_scaled_basis_max':mp.nstr(binary,30),
        'mp80_gram_max_abs_error':mp.nstr(gram80,30),
        'mp120_gram_max_abs_error':mp.nstr(gram120,30),
        'mp120_q_orthogonality_max_abs':mp.nstr(qorth120,30),
        'binary_basis_drift_material_relative_to_2e-6':material_assembly,
        'binary_basis_drift_material_relative_to_2e-5':material_physical,
        'all_finite':finite,'runtime_seconds':time.perf_counter()-start,
        'mp120_basis':[[mp.nstr(x,50) for x in e] for e in m120['e']],
        'binary_basis':[[float(x) for x in e] for e in e_bin],
      },
      'interpretation':[
        'PASS closes arithmetic precision of the Iter407 transverse/aligned basis construction from frozen physical source shifts.',
        'Binary64-vs-MP120 basis drift is diagnostic only and cannot alter frozen thresholds.',
        'This does not certify upstream random metric-perturbation tensors because they do not enter the cut basis; it also does not substitute for full-F or BASE/HALF assembly closure.'
      ],
      'next_gate_if_pass':'treat cut-geometry/basis precision as closed at the frozen source-shift scope; continue deterministic mass-support queue and prepare independent MP80/MP120 full-F spectral assembly from locally certified samples',
      'next_gate_if_blocked':'localize transverse projection, seed Gram-Schmidt, e3 alignment, or e1/e2 projection at the same frozen source vectors without changing support or thresholds',
      'guardrails':['ITERATION478_GEOMETRY_PASS_REQUIRED','NO_SUPPORT_REORDERING','NO_ACTIVE_RANK11_DUPLICATION','NO_THRESHOLD_CHANGE','NO_PHYSICAL_DS_PROMOTION','NO_ANSATZ003','NO_FISHER_RESOURCES']
    }
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
