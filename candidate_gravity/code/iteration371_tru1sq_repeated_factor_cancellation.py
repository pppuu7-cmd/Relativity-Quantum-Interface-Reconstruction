#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 371.

Targeted physical test of apparent repeated raw denominator factors in all 21
physically distinct timelike Tr(U1^2) cyclic classes.

Iteration 370 proved that none of the six denominator-only multi-member
candidates has equivalent transported physical numerator, so all 21 classes
remain distinct.  Here each repeated shift (multiplicity two) is approached on
its massless shell from symmetric off-shell points.  The full physical traced
integrand is multiplied by the complete raw scalar denominator product to form
its stripped numerator.  Symmetric shell limits determine whether the numerator
cancels a repeated factor or whether the double pole survives.

No Cutkosky integration is performed.
"""
from __future__ import annotations
import contextlib, io, json, math
from pathlib import Path
import numpy as np

ITERATION=371
ROOT=Path(__file__).resolve().parent
SRC370=ROOT/'iteration370_tru1sq_timelike_numerator_transport.py'
src=SRC370.read_text().split('rows=[]',1)[0]
ns={'__name__':'iteration371_parent','__file__':str(SRC370)}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(src,str(SRC370),'exec'),ns,ns)
ETA=ns['ETA']; M=ns['M']; LEGS=ns['LEGS']; second_specs=ns['second_specs']; denominator_shifts=ns['denominator_shifts']; stripped=ns['stripped']; vk=ns['vk']

E=0.73
HS=[2.0e-3,1.0e-3,5.0e-4]
OTHER_DENOM_MIN=2e-2
MID_CONVERGENCE_MAX=5e-2
CANCEL_RATIO_MAX=2e-2
SURVIVE_RATIO_MIN=2e-1

# Deterministic angular candidates; directions are used only if all non-target
# denominator groups stay safely away from their shells at epsilon=0.
DIRS=[]
golden=(1+5**0.5)/2
for i in range(24):
    z=1-2*(i+0.5)/24; phi=2*math.pi*i/golden
    r=math.sqrt(max(0.,1-z*z)); DIRS.append(np.array([r*math.cos(phi),r*math.sin(phi),z]))

def dval(v): return float(np.real(np.asarray(v,float)@ETA@np.asarray(v,float)))
def rowset():
    out=[]
    for singleton in LEGS:
      pair=tuple(x for x in LEGS if x!=singleton)
      for i,spec in enumerate(second_specs(pair)):
        r={'class_id':len(out)+1,'singleton_leg':singleton,'pair_legs':pair,'spec_index':i,'spec':spec}
        r['shifts']=denominator_shifts(r); out.append(r)
    return out

def repeated_groups(shifts):
    m={}
    for s in shifts: m.setdefault(vk(s),[]).append(s)
    return [(np.array(k,float),len(v)) for k,v in m.items() if len(v)>1]

def safe_directions(row,target):
    uniq={vk(s):np.array(s,float) for s in row['shifts']}
    ans=[]
    for n in DIRS:
        k=np.r_[E,E*n]; p=k-target
        others=[abs(dval(p+s)) for key,s in uniq.items() if np.max(np.abs(s-target))>1e-12]
        md=min(others) if others else float('inf')
        if md>=OTHER_DENOM_MIN:
            ans.append((n,md))
            if len(ans)==2: break
    return ans

def shell_scan(row,target,n):
    mids=[]; endpoints=[]
    for h in HS:
        vals=[]
        for sign in (+1,-1):
            k=np.r_[E*(1+sign*h),E*n]; p=k-target
            N,_=stripped(row,p); vals.append(N)
        mid=.5*(vals[0]+vals[1]); mids.append(mid); endpoints.append(vals)
    scale=max([abs(z) for pair in endpoints for z in pair]+[1e-30])
    fine_ratio=float(abs(mids[-1])/scale)
    conv=float(abs(mids[-1]-mids[-2])/scale)
    return {'midpoints':[[float(z.real),float(z.imag)] for z in mids],
            'fine_endpoints':[[float(z.real),float(z.imag)] for z in endpoints[-1]],
            'scale':float(scale),'fine_mid_over_endpoint_scale':fine_ratio,
            'fine_mid_convergence_scaled':conv}

rows=rowset(); tests=[]; blocked=0; cancelled=0; survived=0
for row in rows:
    reps=repeated_groups(row['shifts']); assert reps
    for target,mult in reps:
        assert mult==2
        safe=safe_directions(row,target)
        if len(safe)<2:
            tests.append({'class_id':row['class_id'],'target_shift':target.tolist(),'multiplicity':mult,'status':'BLOCKED_NO_TWO_SAFE_SHELL_DIRECTIONS'})
            blocked+=1; continue
        scans=[]
        for n,sep in safe:
            s=shell_scan(row,target,n); s['direction']=n.tolist(); s['other_denominator_min_at_shell']=sep; scans.append(s)
        ratios=[s['fine_mid_over_endpoint_scale'] for s in scans]; convs=[s['fine_mid_convergence_scaled'] for s in scans]
        if max(convs)>MID_CONVERGENCE_MAX:
            status='BLOCKED_SHELL_LIMIT_CONVERGENCE'; blocked+=1
        elif max(ratios)<=CANCEL_RATIO_MAX:
            status='CANCELS_AT_LEAST_ONE_REPEATED_FACTOR'; cancelled+=1
        elif min(ratios)>=SURVIVE_RATIO_MIN:
            status='DOUBLE_POLE_NUMERATOR_SURVIVES'; survived+=1
        else:
            status='BLOCKED_INTERMEDIATE_CANCELLATION_RATIO'; blocked+=1
        tests.append({'class_id':row['class_id'],'target_shift':target.tolist(),'multiplicity':mult,'status':status,'scans':scans,
                      'max_mid_convergence_scaled':max(convs),'min_cancellation_ratio':min(ratios),'max_cancellation_ratio':max(ratios)})

# A completed typed classification, including explicit BLOCKED cases, is valid
# authority. BLOCKED is never silently promoted or zero-filled.
execution_valid=bool(len(tests)>0 and cancelled+survived+blocked==len(tests))
classification='PASS_TRU1SQ_REPEATED_FACTOR_PHYSICAL_CANCELLATION_CLASSIFICATION__SURVIVE_%d__CANCEL_%d__BLOCKED_%d'%(survived,cancelled,blocked)
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':execution_valid,'candidate_residual':False,
 'classification':classification,
 'scope':'PHYSICAL_REPEATED_FACTOR_CANCELLATION_CLASSIFICATION_ONLY__NO_CUT_INTEGRATION',
 'thresholds':{'shell_energy':E,'symmetric_relative_energy_steps':HS,'other_denominator_abs_min':OTHER_DENOM_MIN,
               'midpoint_convergence_scaled_max':MID_CONVERGENCE_MAX,'cancellation_ratio_max':CANCEL_RATIO_MAX,'survival_ratio_min':SURVIVE_RATIO_MIN},
 'counts':{'physical_classes':21,'repeated_factor_tests':len(tests),'double_pole_survives':survived,'cancelled_at_least_one_power':cancelled,'blocked':blocked},
 'tests':tests,
 'guardrails':['ALL_21_CLASSES_REMAIN_DISTINCT_AFTER_ITERATION370','BLOCKED_IS_NOT_ZERO','NO_SIMPLE_OR_REPEATED_CUT_FORMULA_FOR_BLOCKED_TESTS',
               'NO_CUT_INTEGRATION','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':('freeze only unblocked physical pole orders; classify timelike two-line cut support separately for surviving simple/repeated families; any BLOCKED shell-limit cases require targeted analytic or higher-precision resolution before cut integration')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not execution_valid: raise SystemExit(2)
