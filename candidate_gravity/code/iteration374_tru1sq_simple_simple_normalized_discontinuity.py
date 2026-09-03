#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 374.

Repository-normalized q^2-resolved discontinuity of ONLY the six physical
simple-simple Tr(U1^2) channels certified REGULAR by Iteration 373.

Frozen authority inherited without re-fitting:
- Iteration 370: physical routed traced integrand and raw scalar denominator word.
- Iteration 372: exactly six simple-simple timelike channels, two at each q^2.
- Iteration 373: all six are full-sphere REGULAR; uncut groups are analytically
  separated from zero.
- Iteration 337: for an ordinary massless two-simple-line cut,
      D_s I[F] = - sphere_mean(F).
- Reduced one-loop convention: the separate effective-action coefficient of
  Tr(U1^2) is -i/4.  It is NOT folded into the Tr(U1^2) coordinate here.

Because the physical traced numerator is defined as the off-shell stripped
limit, each angular point uses symmetric radial deformations at frozen scales
2e-3, 1e-3, 5e-4 and an even-error Richardson extrapolation.  Angular
integration is independently checked by low/high and half-step shifted phi grids.

No double-cut-pole channel is evaluated.  Distinct q^2 discontinuity variables
are never summed together.
"""
from __future__ import annotations
import contextlib, io, json, math, runpy
from collections import defaultdict
from pathlib import Path
import numpy as np

ITERATION=374
ROOT=Path(__file__).resolve().parent
SRC370=ROOT/'iteration370_tru1sq_timelike_numerator_transport.py'
src=SRC370.read_text().split('rows=[]',1)[0]
ns={'__name__':'iteration374_parent370','__file__':str(SRC370)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src,str(SRC370),'exec'),ns,ns)
    P372=runpy.run_path(str(ROOT/'iteration372_tru1sq_timelike_cut_support_topology.py'),run_name='iteration374_parent372')
    P373=runpy.run_path(str(ROOT/'iteration373_tru1sq_simple_simple_on_shell_regularity.py'),run_name='iteration374_parent373')
ETA=ns['ETA']; LEGS=ns['LEGS']; second_specs=ns['second_specs']; denominator_shifts=ns['denominator_shifts']; stripped=ns['stripped']; vk=ns['vk']

ANGULAR_CONVERGENCE_TOL=2e-5
CUT_SHELL_TOL=2e-10
UNCUT_MIN_TOL=1e-10
RADIAL_EXTRAP_TOL=5e-4
HS=(2.0e-3,1.0e-3,5.0e-4)
NONZERO_TOL=1e-10

if not (P373['result']['scientific_gate_pass'] and P373['result']['counts']['REGULAR']==6 and P373['result']['counts']['BLOCKED']==0):
    raise RuntimeError(('iteration373_not_all_regular',P373['result']['counts']))


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
        for e in basis: v=v-mbilin(v,e)*e
        n2=float(np.real(mdot(v)))
        if n2>1e-12: basis.append(v/math.sqrt(n2))
        if len(basis)==3: break
    if len(basis)!=3: raise RuntimeError('could_not_construct_timelike_transverse_basis')
    return basis

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
if len(simple_channels)!=6: raise RuntimeError(('simple_simple_census_changed',len(simple_channels)))


def stripped_limit(row,p0,a,q,v):
    mids=[]
    for h in HS:
        vals=[]
        for sign in (+1,-1):
            ph=-a-0.5*q+(1.0+sign*h)*v
            z,_=stripped(row,ph)
            vals.append(complex(z))
        mids.append(0.5*(vals[0]+vals[1]))
    # Symmetric midpoint has leading even h^2 error. Richardson eliminates it.
    ext_coarse=(4.0*mids[1]-mids[0])/3.0
    ext_fine=(4.0*mids[2]-mids[1])/3.0
    scale=max(1.0,abs(ext_fine),abs(ext_coarse),*(abs(z) for z in mids))
    err=float(abs(ext_fine-ext_coarse)/scale)
    return ext_fine,err


def sphere_mean(ch,nz,nphi,phi_shift=0.0):
    row=rows[int(ch['class_id'])]
    a=np.asarray(ch['shift_i'],float); b=np.asarray(ch['shift_j'],float); q=b-a
    q2=float(np.real(mdot(q))); rho=math.sqrt(-q2)/2.0; basis=transverse_basis(q)
    mult={}
    for s in row['shifts']:
        mult.setdefault(vk(s),0); mult[vk(s)]+=1
    if mult.get(vk(a))!=1 or mult.get(vk(b))!=1:
        raise RuntimeError(('cut_groups_not_simple',ch['class_id'],mult.get(vk(a)),mult.get(vk(b))))
    zs,ws=np.polynomial.legendre.leggauss(nz)
    total=0j; max_shell=0.0; min_uncut=float('inf'); max_radial=0.0
    for z,wz in zip(zs,ws):
        rr=math.sqrt(max(0.0,1.0-float(z)*float(z))); row_sum=0j
        for m in range(nphi):
            phi=2.0*math.pi*(m+phi_shift)/nphi
            n=np.array([rr*math.cos(phi),rr*math.sin(phi),float(z)])
            v=rho*(n[0]*basis[0]+n[1]*basis[1]+n[2]*basis[2])
            p0=-a-0.5*q+v
            max_shell=max(max_shell,abs(mdot(p0+a)),abs(mdot(p0+b)))
            num,raderr=stripped_limit(row,p0,a,q,v); max_radial=max(max_radial,raderr)
            d=1+0j
            for s in row['shifts']:
                if vk(s) in (vk(a),vk(b)): continue
                du=mdot(p0+np.asarray(s,float)); min_uncut=min(min_uncut,abs(du)); d*=du
            if abs(d)<UNCUT_MIN_TOL: raise RuntimeError(('uncut_pole_encountered',ch['class_id'],abs(d)))
            row_sum += num/d
        total += float(wz)*(row_sum/nphi)
    return 0.5*total,max_shell,min_uncut,max_radial

records=[]; by_q=defaultdict(list); blocked=0; max_conv=0.0; max_shell=0.0; min_uncut=float('inf'); max_radial=0.0
for ch in simple_channels:
    low,es1,mu1,re1=sphere_mean(ch,6,12,0.0)
    high,es2,mu2,re2=sphere_mean(ch,8,16,0.0)
    shifted,es3,mu3,re3=sphere_mean(ch,8,16,0.5)
    scale=max(1.0,abs(low),abs(high),abs(shifted))
    conv=float(max(abs(high-low),abs(high-shifted))/scale)
    shell=max(es1,es2,es3); radial=max(re1,re2,re3); umin=min(mu1,mu2,mu3)
    status='CONVERGED' if conv<=ANGULAR_CONVERGENCE_TOL and shell<=CUT_SHELL_TOL and radial<=RADIAL_EXTRAP_TOL and umin>UNCUT_MIN_TOL else 'BLOCKED_CONVERGENCE'
    blocked += int(status!='CONVERGED')
    max_conv=max(max_conv,conv); max_shell=max(max_shell,shell); max_radial=max(max_radial,radial); min_uncut=min(min_uncut,umin)
    ds=-high  # Iteration 337: repository normalized ordinary-simple cut bridge.
    q2=float(ch['q_squared']); key=round(q2,12)
    rec={'class_id':int(ch['class_id']),'q_squared':q2,'cut_shifts':[ch['shift_i'],ch['shift_j']],
         'status':status,'sphere_mean_low':[float(low.real),float(low.imag)],
         'sphere_mean_high':[float(high.real),float(high.imag)],
         'sphere_mean_high_phi_shifted':[float(shifted.real),float(shifted.imag)],
         'D_s_TrU1sq_channel':[float(ds.real),float(ds.imag)],
         'scaled_angular_convergence_error':conv,'max_radial_richardson_scaled_error':radial,
         'max_cut_shell_abs_error':shell,'minimum_sampled_uncut_abs_denominator':umin}
    records.append(rec); by_q[key].append(rec)

by_q2={}
for q2,recs in sorted(by_q.items()):
    vals=[complex(*r['D_s_TrU1sq_channel']) for r in recs if r['status']=='CONVERGED']
    complete=len(vals)==len(recs)
    sm=sum(vals,0j)
    if not complete: cls='BLOCKED_PARTIAL'
    elif abs(sm)<=NONZERO_TOL: cls='SCOPED_CANCELLATION'
    else: cls='NONZERO'
    by_q2[str(q2)]={'channel_count':len(recs),'converged_channel_count':len(vals),
                    'D_s_TrU1sq_simple_simple_sum':[float(sm.real),float(sm.imag)] if complete else None,
                    'classification':cls}

execution_valid=bool(len(records)==6 and len(by_q2)==3 and max_shell<=CUT_SHELL_TOL)
all_converged=bool(execution_valid and blocked==0 and max_conv<=ANGULAR_CONVERGENCE_TOL and max_radial<=RADIAL_EXTRAP_TOL and min_uncut>UNCUT_MIN_TOL)
classification=('PASS_TRU1SQ_SIMPLE_SIMPLE_NORMALIZED_DISCONTINUITY__ALL_6_CONVERGED' if all_converged else
                'PASS_TRU1SQ_SIMPLE_SIMPLE_NORMALIZED_DISCONTINUITY_CLASSIFICATION__SOME_BLOCKED' if execution_valid else
                'FAIL_TRU1SQ_SIMPLE_SIMPLE_NORMALIZED_DISCONTINUITY_EXECUTION_GATE')
result={'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':execution_valid,'candidate_residual':False,
        'classification':classification,
        'scope':'ONLY_6_ITERATION373_REGULAR_SIMPLE_SIMPLE_TRU1SQ_CHANNELS__NORMALIZED_Q2_RESOLVED_DISCONTINUITY',
        'census':{'typed_channels':len(records),'CONVERGED':len(records)-blocked,'BLOCKED_CONVERGENCE':blocked,'q2_buckets':len(by_q2),
                  'max_scaled_angular_convergence_error':max_conv,'max_radial_richardson_scaled_error':max_radial,
                  'max_cut_shell_abs_error':max_shell,'minimum_sampled_uncut_abs_denominator':min_uncut},
        'thresholds':{'angular_convergence_scaled_max':ANGULAR_CONVERGENCE_TOL,'radial_richardson_scaled_max':RADIAL_EXTRAP_TOL,
                      'cut_shell_abs_max':CUT_SHELL_TOL,'uncut_abs_min':UNCUT_MIN_TOL,'nonzero_abs_min':NONZERO_TOL,
                      'symmetric_radial_relative_steps':list(HS)},
        'quadrature':{'low':{'gauss_legendre_z':6,'periodic_phi':12},'high':{'gauss_legendre_z':8,'periodic_phi':16},
                      'independent_phase_check':'high phi grid shifted by half step'},
        'normalization':'ITERATION337_D_s_I_EQUALS_MINUS_SPHERE_MEAN',
        'effective_action_weight':'NOT_FOLDED__REDUCED_ONE_LOOP_MINUS_I_OVER_4_TRU1SQ_SEPARATE',
        'by_q2':by_q2,'channels':records,
        'guardrails':['ITERATION373_REGULAR_CHANNELS_ONLY','51_DOUBLE_POLE_CHANNELS_EXCLUDED','DISTINCT_Q2_NOT_SUMMED',
                      'NO_EFFECTIVE_ACTION_WEIGHT_FOLDING','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],
        'next_gate':('if all six converge, freeze the three q2-resolved simple-simple TrU1sq coordinates; independently derive and validate auxiliary-mass derivative/distributional cut formulae for the 36 simple-double and 15 double-double channels before any full TrU1sq assembly. Do not combine with TrU2 until both operators are complete.' if all_converged else 'resolve only blocked simple-simple channels with stronger quadrature or analytic angular reduction without weakening thresholds')}
print(json.dumps(result,indent=2,sort_keys=True))
if not execution_valid: raise SystemExit(2)
