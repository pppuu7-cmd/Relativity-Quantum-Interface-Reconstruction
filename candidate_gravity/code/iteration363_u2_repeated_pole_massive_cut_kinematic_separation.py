#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 363.

For the 48 Iteration-359 timelike channels that cut the unique double-pole group,
classify the auxiliary-mass simple-cut kinematics and analytically certify any
uncut distinct momentum group stays away from its massless pole over the full
cut sphere.  This is a prerequisite gate only; it does not differentiate or
integrate the physical repeated-pole discontinuity.
"""
from __future__ import annotations
import contextlib, io, json, math, runpy
from pathlib import Path
import numpy as np

ITERATION=363
ROOT=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    P359=runpy.run_path(str(ROOT/'iteration359_u2_repeated_pole_derivative_contract.py'),run_name='iteration363_parent359')
mdot=P359['mdot']
MU2_PROBES=[-1e-5,0.0,1e-5]
TIMELIKE_TOL=2e-12
SEP_TOL=1e-10

if not P359['result']['scientific_gate_pass']:
    raise RuntimeError('iteration359_parent_not_authoritative')

def mbilin(a,b):
    a=np.asarray(a,float); b=np.asarray(b,float)
    return float(-a[0]*b[0]+np.dot(a[1:],b[1:]))

def sq(a): return mbilin(a,a)

def full_sphere_uncut_range(a,b,c,m1sq,m2sq):
    # p1=k+a, p2=k+b=p1+q; p1^2=-m1^2, p2^2=-m2^2.
    q=np.asarray(b)-np.asarray(a); q2=sq(q)
    alpha=(m1sq-m2sq-q2)/(2.0*q2)
    rho2=-m1sq-alpha*alpha*q2
    if rho2 < -2e-12:
        return None
    rho=math.sqrt(max(0.0,rho2))
    r=alpha*q+(np.asarray(c)-np.asarray(a))
    rperp=r-q*(mbilin(r,q)/q2)
    rp2=sq(rperp)
    if rp2 < -2e-12:
        return None
    amp=2.0*rho*math.sqrt(max(0.0,rp2))
    center=sq(r)+rho2
    lo=center-amp; hi=center+amp
    if lo>hi: lo,hi=hi,lo
    minabs=0.0 if lo<=0.0<=hi else min(abs(lo),abs(hi))
    return {'range':[lo,hi],'min_abs':minabs,'rho2':rho2,'alpha':alpha}

records=[]; blocked=0; regular=0; min_sep=float('inf'); min_rho2=float('inf')
for fam in P359['result']['families']:
    groups=fam['groups']
    for ch in fam['timelike_distinct_group_channels']:
        if not ch['repeated_pole_reduction_required']:
            continue
        ia,ib=ch['group_pair']; ga,gb=groups[ia],groups[ib]
        ma,mb=ga['multiplicity'],gb['multiplicity']
        if sorted([ma,mb]) != [1,2]:
            records.append({'route':fam['route'],'subterm':fam['subterm'],'group_pair':[ia,ib],'status':'BLOCKED_UNEXPECTED_MULTIPLICITY'})
            blocked+=1; continue
        a=np.asarray(ga['offset'],float); b=np.asarray(gb['offset'],float); q2=sq(b-a)
        probe_records=[]; status='REGULAR'
        for mu2 in MU2_PROBES:
            m1sq=mu2 if ma==2 else 0.0; m2sq=mu2 if mb==2 else 0.0
            # Two-body existence via rho^2 and exact timelike q.
            cut=full_sphere_uncut_range(a,b,a,m1sq,m2sq)
            if cut is None or q2>=-TIMELIKE_TOL or cut['rho2'] < -2e-12:
                status='BLOCKED_KINEMATICS'; probe_records.append({'mu2':mu2,'status':status}); continue
            min_rho2=min(min_rho2,cut['rho2'])
            uncut=[]
            for ic,gc in enumerate(groups):
                if ic in (ia,ib): continue
                rr=full_sphere_uncut_range(a,b,np.asarray(gc['offset'],float),m1sq,m2sq)
                if rr is None:
                    status='BLOCKED_UNCUT_RANGE'; uncut.append({'group':ic,'status':'BLOCKED_RANGE'}); continue
                min_sep=min(min_sep,rr['min_abs'])
                if rr['min_abs']<=SEP_TOL: status='BLOCKED_UNCUT_POLE'
                uncut.append({'group':ic,'multiplicity':gc['multiplicity'],'squared_momentum_range':rr['range'],'min_abs':rr['min_abs']})
            probe_records.append({'mu2':mu2,'status':'REGULAR' if status=='REGULAR' else status,
                                  'rho2':cut['rho2'],'uncut_groups':uncut})
        if status=='REGULAR': regular+=1
        else: blocked+=1
        records.append({'route':fam['route'],'subterm':fam['subterm'],'group_pair':[ia,ib],
                        'multiplicity_pair':[ma,mb],'q2':q2,'status':status,'probes':probe_records})

resolved=(len(records)==48 and regular+blocked==48)
classification=('PASS_U2_REPEATED_POLE_MASSIVE_SIMPLE_CUT_KINEMATIC_AND_UNCUT_SEPARATION__ALL_REGULAR'
                if resolved and blocked==0 else
                'PASS_U2_REPEATED_POLE_MASSIVE_SIMPLE_CUT_KINEMATIC_CLASSIFICATION__SOME_BLOCKED'
                if resolved else 'FAIL_U2_REPEATED_POLE_MASSIVE_SIMPLE_CUT_KINEMATIC_GATE')
result={'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':bool(resolved),
        'candidate_residual':False,'classification':classification,
        'census':{'typed_repeated_channels':len(records),'REGULAR':regular,'BLOCKED':blocked,
                  'minimum_rho2_across_probes':None if not np.isfinite(min_rho2) else min_rho2,
                  'minimum_analytic_uncut_abs_squared_momentum':None if not np.isfinite(min_sep) else min_sep},
        'auxiliary_mass_squared_probes':MU2_PROBES,'uncut_separation_threshold':SEP_TOL,
        'records':records,
        'scope':'REPEATED_POLE_AUXILIARY_MASSIVE_SIMPLE_CUT_KINEMATICS_AND_ANALYTIC_UNCUT_SEPARATION_ONLY',
        'guardrails':['ITERATION362_DISTRIBUTIONAL_ORACLE_REQUIRED','ONE_AUXILIARY_MASS_ON_UNIQUE_DOUBLE_GROUP',
                      'FULL_SPHERE_AFFINE_RANGE_NOT_SAMPLED_ZERO_CERTIFICATE','NO_PHYSICAL_REPEATED_CUT_INTEGRATION_YET',
                      'NO_ZERO_FILL','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
        'next_gate':('if all 48 channels REGULAR, evaluate the simple-massive normalized channel cut at symmetric mu2 values with fixed quadrature, take the frozen negative mu2 derivative at zero, and require derivative convergence plus an independent step-size check; any blocked channel remains isolated for analytic reduction')}
print(json.dumps(result,indent=2,sort_keys=True))
if not resolved: raise SystemExit(2)
