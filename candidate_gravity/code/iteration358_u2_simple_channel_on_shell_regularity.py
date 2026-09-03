#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 358.

Evaluate only the 12 ordinary-simple U2 families authorized by Iteration 357.
For each of their 36 typed timelike two-line channels:
  * construct the exact massless two-particle cut sphere in signature (-,+,+,+);
  * certify every uncut propagator by its analytic affine range on that sphere;
  * evaluate the already stripped physical traced numerator on deterministic
    on-shell directions as a regularity cross-check.

Repeated-pole families are not evaluated here. No discontinuity integration is
performed. Unsupported/ambiguous channels are BLOCKED, never zero-filled.
"""
from __future__ import annotations
import contextlib, io, json, math, runpy
from pathlib import Path
import numpy as np

ITERATION = 358
ROOT = Path(__file__).resolve().parent

with contextlib.redirect_stdout(io.StringIO()):
    P355 = runpy.run_path(str(ROOT/'iteration355_u2_heldout_physical_numerator_transport.py'), run_name='iteration358_parent355')
    P356 = runpy.run_path(str(ROOT/'iteration356_u2_family_origin_topology_classification.py'), run_name='iteration358_parent356')
    P357 = runpy.run_path(str(ROOT/'iteration357_u2_simple_vs_repeated_pole_cut_contract.py'), run_name='iteration358_parent357')

raw = P355['raw']
enumerate_subterms = P355['enumerate_subterms']
mdot = P355['mdot']

TIMELIKE_TOL = 2e-12
UNCUT_SEPARATION_TOL = 1e-10
NUMERATOR_FINITE_LIMIT = 1e100
PREF = np.array([.43, -.27, .39, .21], dtype=float)


def bdot(a,b):
    """Bilinear Minkowski product recovered from frozen quadratic mdot."""
    a=np.asarray(a,float); b=np.asarray(b,float)
    return 0.5*(mdot(a+b)-mdot(a)-mdot(b))


def mproj_orth(v, q):
    q2 = float(np.real(mdot(q)))
    return np.asarray(v, float) - np.asarray(q, float) * (float(np.real(bdot(v, q))) / q2)


def transverse_basis(q):
    seeds = [np.array([0.,1.,0.,0.]),np.array([0.,0.,1.,0.]),np.array([0.,0.,0.,1.]),
             np.array([1.,0.,0.,0.]),np.array([1.,1.,0.,0.]),np.array([1.,0.,1.,0.])]
    basis=[]
    for s in seeds:
        v=mproj_orth(s,q)
        for e in basis: v=v-float(np.real(bdot(v,e)))*e
        n2=float(np.real(mdot(v)))
        if n2>1e-12: basis.append(v/math.sqrt(n2))
        if len(basis)==3: break
    if len(basis)!=3: raise RuntimeError('could_not_construct_timelike_transverse_basis')
    gram=np.array([[float(np.real(bdot(a,b))) for b in basis] for a in basis])
    if np.max(np.abs(gram-np.eye(3)))>2e-10: raise RuntimeError(('bad_transverse_gram',gram.tolist()))
    if max(abs(float(np.real(bdot(e,q)))) for e in basis)>2e-10: raise RuntimeError('basis_not_q_orthogonal')
    return basis


def directions():
    out=[]
    for a in np.eye(3): out += [a.copy(),-a.copy()]
    n=32; phi=(1+math.sqrt(5.0))/2.0
    for k in range(n):
        z=1.0-2.0*(k+0.5)/n; r=math.sqrt(max(0.0,1.0-z*z)); ang=2.0*math.pi*k/phi
        out.append(np.array([r*math.cos(ang),r*math.sin(ang),z]))
    return out

DIRS=directions()


def analytic_uncut_range(c,a,q):
    q2=float(np.real(mdot(q))); rho=math.sqrt(-q2)/2.0
    d=np.asarray(c,float)-np.asarray(a,float); w=d-0.5*np.asarray(q,float)
    wperp=mproj_orth(w,q); wp2=max(0.0,float(np.real(mdot(wperp))))
    center=float(np.real(mdot(w)))+rho*rho; amp=2.0*rho*math.sqrt(wp2)
    lo=center-amp; hi=center+amp
    min_abs=0.0 if lo<=0.0<=hi else min(abs(lo),abs(hi))
    return lo,hi,min_abs

simple_records=[r for r in P356['records'] if not r['has_repeated_pole_momentum']]
if len(simple_records)!=12: raise RuntimeError(('simple_family_census_changed',len(simple_records)))

channels=[]; regular=zero=blocked=0; max_shell_error=0.0; min_certified_uncut=float('inf')
for fam in simple_records:
    route=int(fam['route']); subterm=int(fam['subterm'])
    sref=enumerate_subterms(raw[route],PREF)[subterm]
    offsets=[np.asarray(k,float)-PREF for _,k in sref['props']]; species=[sp for sp,_ in sref['props']]
    for ch in fam['timelike_pair_channels']:
        i=int(ch['i']); j=int(ch['j']); a=offsets[i]; b=offsets[j]; q=b-a
        q2=float(np.real(mdot(q)))
        if not q2 < -TIMELIKE_TOL: raise RuntimeError(('parent_channel_not_timelike',route,subterm,i,j,q2))
        rho=math.sqrt(-q2)/2.0; basis=transverse_basis(q)
        uncut=[]; separated=True
        for u,c in enumerate(offsets):
            if u in (i,j): continue
            lo,hi,min_abs=analytic_uncut_range(c,a,q); min_certified_uncut=min(min_certified_uncut,min_abs)
            ok=bool(min_abs>UNCUT_SEPARATION_TOL); separated=separated and ok
            uncut.append({'index':u,'species':species[u],'r2_range':[lo,hi],'minimum_abs_r2':min_abs,'separated_from_zero':ok})
        vals=[]; finite=True; local_shell_error=0.0
        for n in DIRS:
            v=rho*(n[0]*basis[0]+n[1]*basis[1]+n[2]*basis[2]); p=-a-0.5*q+v
            ss=enumerate_subterms(raw[route],p)[subterm]; z=complex(ss['numerator_trace'])
            if not (np.isfinite(z.real) and np.isfinite(z.imag) and abs(z)<NUMERATOR_FINITE_LIMIT): finite=False
            vals.append(z); props=ss['props']
            local_shell_error=max(local_shell_error,float(abs(complex(mdot(props[i][1])))),float(abs(complex(mdot(props[j][1])))))
        max_shell_error=max(max_shell_error,local_shell_error)
        max_num=max((abs(z) for z in vals),default=0.0); min_num=min((abs(z) for z in vals),default=0.0)
        if finite and separated: status='REGULAR'; regular+=1
        else: status='BLOCKED'; blocked+=1
        channels.append({'route':route,'subterm':subterm,'cut_pair':[i,j],'q2':q2,'status':status,
                         'numerator_structure':'STRIPPED_LOCAL_POLYNOMIAL_MATRIX_PRODUCT',
                         'numerator_sample_count':len(vals),'numerator_sample_abs_min':min_num,'numerator_sample_abs_max':max_num,
                         'numerator_finite_on_all_samples':finite,'cut_shell_max_abs_error':local_shell_error,
                         'uncut_denominators':uncut,'all_uncut_denominators_analytically_separated':separated})

passed=bool(len(channels)==36 and regular+zero+blocked==36 and max_shell_error<=2e-10)
result={'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':passed,'candidate_residual':False,
 'classification':('PASS_U2_ORDINARY_SIMPLE_CHANNEL_ON_SHELL_REGULARITY_AND_UNCUT_DENOMINATOR_CLASSIFICATION' if passed else 'FAIL_U2_ORDINARY_SIMPLE_CHANNEL_ON_SHELL_DIAGNOSTIC_GATE'),
 'census':{'ordinary_simple_families':12,'typed_channels':len(channels),'REGULAR':regular,'ZERO':zero,'BLOCKED':blocked,
           'max_cut_shell_abs_error':max_shell_error,'minimum_certified_uncut_abs_r2':min_certified_uncut},
 'thresholds':{'timelike_pair_q2_max':-TIMELIKE_TOL,'uncut_denominator_min_abs_r2':UNCUT_SEPARATION_TOL,'cut_shell_max_abs_error':2e-10},
 'channels':channels,'scope':'ORDINARY_SIMPLE_U2_ON_SHELL_DIAGNOSTICS_ONLY__NO_DISCONTINUITY_INTEGRATION',
 'guardrails':['ITERATION357_SIMPLE_ONLY','REPEATED_POLE_FAMILIES_NOT_EVALUATED','ANALYTIC_UNCUT_DENOMINATOR_RANGE_NOT_SAMPLED_ZERO_TEST','NO_ZERO_FROM_NUMERICAL_SAMPLING','UNSUPPORTED_IS_BLOCKED_NOT_ZERO','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],
 'next_gate':'for REGULAR ordinary-simple channels only, perform normalized channel-resolved Tr U2 discontinuity using frozen Iterations 336-338 normalization; keep BLOCKED simple channels separate and all 30 repeated-pole families BLOCKED pending explicit derivative/distributional reduction'}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)

# Workflow-registration trigger marker; no scientific content changed.
