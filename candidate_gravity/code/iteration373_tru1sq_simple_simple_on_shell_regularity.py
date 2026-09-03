#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 373.

On-shell regularity and analytic uncut-denominator separation gate for the six
ordinary simple-simple timelike Tr(U1^2) channels frozen by Iteration 372.

The physical routed integrand and raw scalar denominator word come unchanged
from Iteration 370.  For each simple-simple channel we:
  * construct the exact massless two-particle cut sphere in (-,+,+,+);
  * certify every uncut unique denominator group by its exact affine range on
    that sphere;
  * approach both cut shells simultaneously by symmetric radial deformations
    and test convergence of the fully stripped physical traced numerator.

No discontinuity integral is performed. Channels containing a double cut pole
remain outside this gate and ordinary-simple Cutkosky substitution remains
forbidden for them.
"""
from __future__ import annotations
import contextlib, io, json, math, runpy
from pathlib import Path
import numpy as np

ITERATION=373
ROOT=Path(__file__).resolve().parent
SRC370=ROOT/'iteration370_tru1sq_timelike_numerator_transport.py'
src=SRC370.read_text().split('rows=[]',1)[0]
ns={'__name__':'iteration373_parent370','__file__':str(SRC370)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src,str(SRC370),'exec'),ns,ns)
    P372=runpy.run_path(str(ROOT/'iteration372_tru1sq_timelike_cut_support_topology.py'),run_name='iteration373_parent372')
ETA=ns['ETA']; LEGS=ns['LEGS']; second_specs=ns['second_specs']; denominator_shifts=ns['denominator_shifts']; stripped=ns['stripped']; vk=ns['vk']

TIMELIKE_TOL=2e-12
UNCUT_SEPARATION_TOL=1e-10
CUT_SHELL_TOL=2e-10
MID_CONVERGENCE_MAX=5e-2
HS=[2.0e-3,1.0e-3,5.0e-4]
NUMERATOR_FINITE_LIMIT=1e100
ROUND=12


def mdot(v):
    z=np.asarray(v,complex)
    return complex(z@ETA@z)

def mbilin(a,b):
    a=np.asarray(a,float); b=np.asarray(b,float)
    return float(-a[0]*b[0]+np.dot(a[1:],b[1:]))

def mproj_orth(v,q):
    q=np.asarray(q,float); q2=float(np.real(mdot(q)))
    return np.asarray(v,float)-q*(mbilin(v,q)/q2)

def transverse_basis(q):
    seeds=[np.array([0.,1.,0.,0.]),np.array([0.,0.,1.,0.]),np.array([0.,0.,0.,1.]),
           np.array([1.,0.,0.,0.]),np.array([1.,1.,0.,0.]),np.array([1.,0.,1.,0.])]
    basis=[]
    for s in seeds:
        v=mproj_orth(s,q)
        for e in basis:
            v=v-mbilin(v,e)*e
        n2=float(np.real(mdot(v)))
        if n2>1e-12:
            basis.append(v/math.sqrt(n2))
        if len(basis)==3:
            break
    if len(basis)!=3:
        raise RuntimeError('could_not_construct_timelike_transverse_basis')
    gram=np.array([[mbilin(a,b) for b in basis] for a in basis])
    if np.max(np.abs(gram-np.eye(3)))>2e-10:
        raise RuntimeError(('bad_transverse_gram',gram.tolist()))
    if max(abs(mbilin(e,q)) for e in basis)>2e-10:
        raise RuntimeError('basis_not_q_orthogonal')
    return basis

def directions():
    out=[]
    for a in np.eye(3):
        out.extend([a.copy(),-a.copy()])
    phi=(1+math.sqrt(5.0))/2.0
    for k in range(6):
        z=1.0-2.0*(k+0.5)/6.0; r=math.sqrt(max(0.0,1.0-z*z)); ang=2.0*math.pi*k/phi
        out.append(np.array([r*math.cos(ang),r*math.sin(ang),z]))
    return out
DIRS=directions()

def analytic_uncut_range(c,a,q):
    q2=float(np.real(mdot(q))); rho=math.sqrt(-q2)/2.0
    d=np.asarray(c,float)-np.asarray(a,float); w=d-0.5*np.asarray(q,float)
    wperp=mproj_orth(w,q); wp2=max(0.0,float(np.real(mdot(wperp))))
    center=float(np.real(mdot(w)))+rho*rho
    amp=2.0*rho*math.sqrt(wp2)
    lo=center-amp; hi=center+amp
    min_abs=0.0 if lo<=0.0<=hi else min(abs(lo),abs(hi))
    return lo,hi,min_abs

def rowset():
    out=[]
    for singleton in LEGS:
        pair=tuple(x for x in LEGS if x!=singleton)
        for i,spec in enumerate(second_specs(pair)):
            r={'class_id':len(out)+1,'singleton_leg':singleton,'pair_legs':pair,'spec_index':i,'spec':spec}
            r['shifts']=denominator_shifts(r)
            out.append(r)
    return out

rows={r['class_id']:r for r in rowset()}
simple_channels=[c for c in P372['channels'] if c['singularity_type']=='simple-simple']
if len(simple_channels)!=6:
    raise RuntimeError(('simple_simple_census_changed',len(simple_channels)))

records=[]; regular=0; blocked=0; max_shell_error=0.0; global_min_uncut=float('inf'); max_conv=0.0
for ch in simple_channels:
    row=rows[int(ch['class_id'])]
    a=np.asarray(ch['shift_i'],float); b=np.asarray(ch['shift_j'],float); q=b-a
    q2=float(np.real(mdot(q)))
    if not q2 < -TIMELIKE_TOL:
        raise RuntimeError(('non_timelike_parent_channel',ch['class_id'],q2))
    rho=math.sqrt(-q2)/2.0; basis=transverse_basis(q)

    mult={}
    for s in row['shifts']:
        mult.setdefault(vk(s),0); mult[vk(s)]+=1
    if mult.get(vk(a))!=1 or mult.get(vk(b))!=1:
        raise RuntimeError(('iteration372_simple_simple_multiplicity_mismatch',ch['class_id'],mult.get(vk(a)),mult.get(vk(b))))

    uncut=[]; separated=True
    for key,m in sorted(mult.items()):
        c=np.asarray(key,float)
        if key in (vk(a),vk(b)):
            continue
        lo,hi,min_abs=analytic_uncut_range(c,a,q)
        global_min_uncut=min(global_min_uncut,min_abs)
        ok=bool(min_abs>UNCUT_SEPARATION_TOL); separated=separated and ok
        uncut.append({'shift':c.tolist(),'multiplicity':int(m),'r2_range':[lo,hi],
                      'minimum_abs_r2':min_abs,'separated_from_zero':ok})

    direction_scans=[]; finite=True; local_shell_error=0.0; local_max_conv=0.0
    for n in DIRS:
        v=rho*(n[0]*basis[0]+n[1]*basis[1]+n[2]*basis[2])
        p0=-a-0.5*q+v
        local_shell_error=max(local_shell_error,abs(mdot(p0+a)),abs(mdot(p0+b)))
        mids=[]; endpoint_scales=[]
        for h in HS:
            vals=[]
            for sign in (+1,-1):
                ph=-a-0.5*q+(1.0+sign*h)*v
                z,_=stripped(row,ph)
                z=complex(z)
                finite=finite and np.isfinite(z.real) and np.isfinite(z.imag) and abs(z)<NUMERATOR_FINITE_LIMIT
                vals.append(z)
            mids.append(0.5*(vals[0]+vals[1])); endpoint_scales.extend(abs(z) for z in vals)
        scale=max(endpoint_scales+[abs(z) for z in mids]+[1e-30])
        conv=float(abs(mids[-1]-mids[-2])/scale)
        local_max_conv=max(local_max_conv,conv)
        direction_scans.append({'direction':n.tolist(),'fine_midpoint':[float(mids[-1].real),float(mids[-1].imag)],
                                'fine_mid_convergence_scaled':conv,'scale':float(scale)})
    max_shell_error=max(max_shell_error,float(local_shell_error)); max_conv=max(max_conv,local_max_conv)
    if finite and separated and local_shell_error<=CUT_SHELL_TOL and local_max_conv<=MID_CONVERGENCE_MAX:
        status='REGULAR'; regular+=1
    else:
        status='BLOCKED'; blocked+=1
    records.append({'class_id':int(ch['class_id']),'q_squared':float(ch['q_squared']),
                    'cut_shifts':[a.tolist(),b.tolist()],'status':status,
                    'cut_shell_max_abs_error':float(local_shell_error),
                    'max_stripped_numerator_midpoint_convergence_scaled':float(local_max_conv),
                    'stripped_numerator_finite_on_all_samples':bool(finite),
                    'all_uncut_denominator_groups_analytically_separated':bool(separated),
                    'uncut_denominator_groups':uncut,'direction_scans':direction_scans})

execution_valid=bool(len(records)==6 and regular+blocked==6 and max_shell_error<=CUT_SHELL_TOL)
classification=('PASS_TRU1SQ_SIMPLE_SIMPLE_ON_SHELL_REGULARITY_AND_UNCUT_SEPARATION__REGULAR_%d__BLOCKED_%d'%(regular,blocked)
                if execution_valid else 'FAIL_TRU1SQ_SIMPLE_SIMPLE_REGULARITY_EXECUTION_GATE')
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':execution_valid,'candidate_residual':False,
 'classification':classification,
 'scope':'TRU1SQ_SIMPLE_SIMPLE_TIMELIKE_ON_SHELL_REGULARITY_AND_UNCUT_SEPARATION_ONLY__NO_DISCONTINUITY_INTEGRATION',
 'authoritative_inputs':['Iteration 370 physical routed numerator/denominator families','Iteration 371 physical double-pole authority','Iteration 372 57-channel singularity classification'],
 'thresholds':{'timelike_q2_max':-TIMELIKE_TOL,'uncut_denominator_min_abs_r2':UNCUT_SEPARATION_TOL,
               'cut_shell_max_abs_error':CUT_SHELL_TOL,'symmetric_radial_relative_steps':HS,
               'stripped_numerator_midpoint_convergence_scaled_max':MID_CONVERGENCE_MAX},
 'counts':{'iteration372_simple_simple_channels':6,'REGULAR':regular,'BLOCKED':blocked,
           'channels_by_q_squared':{str(q):sum(abs(float(r['q_squared'])-q)<1e-12 for r in records) for q in (-1.0,-0.34,-0.14)}},
 'maximum_cut_shell_abs_error':float(max_shell_error),'minimum_certified_uncut_abs_r2':float(global_min_uncut),
 'maximum_stripped_numerator_midpoint_convergence_scaled':float(max_conv),'channels':records,
 'guardrails':['ONLY_ITERATION372_SIMPLE_SIMPLE_CHANNELS','DOUBLE_POLE_CHANNELS_EXCLUDED','ANALYTIC_UNCUT_DENOMINATOR_RANGE_NOT_SAMPLED_ZERO_TEST',
               'SYMMETRIC_OFF_SHELL_LIMIT_FOR_STRIPPED_PHYSICAL_NUMERATOR','BLOCKED_IS_NOT_ZERO','NO_CUT_INTEGRATION','NO_SOURCE_BORN_SUBTRACTION',
               'NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],
 'next_gate':('if all six channels are REGULAR, perform normalized q2-resolved Tr U1^2 discontinuity for simple-simple channels using frozen determinant/U2 normalization conventions; keep all 51 channels containing double poles BLOCKED pending exact auxiliary-mass derivative/distributional validation for simple-double and double-double multiplicities. If any channel is BLOCKED, resolve only that channel without threshold weakening.')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not execution_valid:
    raise SystemExit(2)
