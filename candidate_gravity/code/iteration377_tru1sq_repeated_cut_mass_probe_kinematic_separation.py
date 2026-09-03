#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 377.

Physical kinematic-separation prerequisite for the 51 repeated-cut Tr(U1^2)
channels frozen by Iteration 372, after Iteration 375 validated the required
simple-double and double-double auxiliary-mass derivative identities.

Probe every double cut group with mu^2 in {-1e-5,0,+1e-5}.  For a two-line cut
with denominator shifts a,b, q=b-a, s=-q^2>0, and cut masses u=mu1^2,v=mu2^2,
use
  alpha=-(s+u-v)/(2s),
  lambda=s^2+u^2+v^2-2su-2sv-2uv,
  rho=sqrt(lambda)/(2sqrt(s)),
  k=-a+alpha q+rho n,  n.q=0, n^2=1.
Every uncut massless denominator is affine over the cut sphere; its exact range
is certified analytically.  No physical discontinuity is integrated here.
"""
from __future__ import annotations
import contextlib, io, json, math, runpy
from collections import Counter
from pathlib import Path
import numpy as np

ITERATION=377
ROOT=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    P372=runpy.run_path(str(ROOT/'iteration372_tru1sq_timelike_cut_support_topology.py'),run_name='iteration377_parent372')
R=P372['result']
if not (R['scientific_gate_pass'] and R['counts']['simple_double_channels']==36 and R['counts']['double_double_channels']==15):
    raise RuntimeError('iteration372_repeated_cut_census_not_authoritative')

ETA=P372['ETA']; shifts=P372['shifts']; vk=P372['vk']; mdot=lambda a,b: float(np.asarray(a,float)@ETA@np.asarray(b,float))
PROBE=1e-5
SEPARATION_MIN=1e-10
SHELL_MAX=2e-12
Q2_MAX=1e-12
LAMBDA_MIN=1e-12

def transverse_basis(q):
    q=np.asarray(q,float); q2=mdot(q,q)
    seeds=[np.array([0.,1.,0.,0.]),np.array([0.,0.,1.,0.]),np.array([0.,0.,0.,1.]),np.array([1.,0.,0.,0.]),np.array([1.,1.,0.,0.])]
    basis=[]
    for seed in seeds:
        v=seed-q*(mdot(seed,q)/q2)
        for e in basis: v=v-mdot(v,e)*e
        n2=mdot(v,v)
        if n2>1e-12: basis.append(v/math.sqrt(n2))
        if len(basis)==3: break
    if len(basis)!=3: raise RuntimeError('transverse_basis_failure')
    return basis

def same_shift(x,y): return bool(np.max(np.abs(np.asarray(x)-np.asarray(y)))<1e-12)

fam_by_id={int(f['class_id']):f for f in R['families']}
rows=[]; status_count=Counter(); type_count=Counter(); q_count=Counter()
global_min=float('inf'); global_shell=0.0; global_q2err=0.0; global_lam=float('inf')
for ch in R['channels']:
    typ=ch['singularity_type']
    if typ=='simple-simple': continue
    fam=fam_by_id[int(ch['class_id'])]
    raw=shifts(tuple(fam['singleton_leg']) if isinstance(fam['singleton_leg'],list) else fam['singleton_leg'], tuple(fam['pair_legs']), fam['spec'])
    mult={}
    for z in raw: mult[vk(z)]=mult.get(vk(z),0)+1
    uniq=[np.array(k,float) for k in sorted(mult)]
    a=np.asarray(ch['shift_i'],float); b=np.asarray(ch['shift_j'],float)
    mi=int(ch['multiplicity_i']); mj=int(ch['multiplicity_j'])
    q=b-a; qsq=mdot(q,q); qerr=abs(qsq-float(ch['q_squared'])); s=-qsq
    basis=transverse_basis(q)
    probes_i=[0.0] if mi==1 else [-PROBE,0.0,PROBE]
    probes_j=[0.0] if mj==1 else [-PROBE,0.0,PROBE]
    minsep=float('inf'); maxshell=0.0; minlam=float('inf'); blocked_reason=None
    probe_rows=[]
    for u in probes_i:
      for v in probes_j:
        lam=s*s+u*u+v*v-2*s*u-2*s*v-2*u*v
        minlam=min(minlam,lam)
        if lam<=LAMBDA_MIN:
            blocked_reason='NONPOSITIVE_KALLEN'; continue
        alpha=-(s+u-v)/(2*s); rho=math.sqrt(lam)/(2*math.sqrt(s))
        # Exact shell identities are direction-independent; sample +/- basis vectors as a numerical regression.
        pshell=0.0
        for e in basis:
          for sg in (-1.0,1.0):
            k=-a+alpha*q+sg*rho*e
            pshell=max(pshell,abs(mdot(k+a,k+a)+u),abs(mdot(k+b,k+b)+v))
        maxshell=max(maxshell,pshell)
        this_min=float('inf')
        for c in uniq:
            if same_shift(c,a) or same_shift(c,b): continue
            base=(c-a)+alpha*q
            center=mdot(base,base)+rho*rho
            comps=np.array([mdot(base,e) for e in basis],float)
            amp=2.0*abs(rho)*float(np.linalg.norm(comps))
            sep=max(abs(center)-amp,0.0)
            this_min=min(this_min,sep); minsep=min(minsep,sep)
        probe_rows.append({'mu1_sq':u,'mu2_sq':v,'kallen':lam,'max_cut_shell_abs_error':pshell,
                           'minimum_analytic_uncut_abs_denominator':this_min})
    if not np.isfinite(minsep): minsep=float('inf')
    if blocked_reason is None and minsep<=SEPARATION_MIN: blocked_reason='UNCUT_DENOMINATOR_RANGE_TOUCHES_ZERO'
    if blocked_reason is None and maxshell>SHELL_MAX: blocked_reason='CUT_SHELL_ERROR'
    if blocked_reason is None and qerr>Q2_MAX: blocked_reason='Q2_FIXTURE_ERROR'
    status='REGULAR' if blocked_reason is None else 'BLOCKED'
    row={'class_id':int(ch['class_id']),'q_squared':float(ch['q_squared']),'singularity_type':typ,
         'multiplicity_i':mi,'multiplicity_j':mj,'shift_i':a.tolist(),'shift_j':b.tolist(),
         'status':status,'blocked_reason':blocked_reason,'minimum_analytic_uncut_abs_denominator':minsep,
         'max_cut_shell_abs_error':maxshell,'q2_abs_error':qerr,'minimum_kallen':minlam,'probes':probe_rows}
    rows.append(row); status_count[status]+=1; type_count[typ]+=1; q_count[str(float(ch['q_squared']))]+=1
    global_min=min(global_min,minsep); global_shell=max(global_shell,maxshell); global_q2err=max(global_q2err,qerr); global_lam=min(global_lam,minlam)

passed=bool(len(rows)==51 and type_count['simple-double']==36 and type_count['double-double']==15 and
            status_count['REGULAR']==51 and status_count['BLOCKED']==0 and global_min>SEPARATION_MIN and
            global_shell<=SHELL_MAX and global_q2err<=Q2_MAX and global_lam>LAMBDA_MIN)
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':passed,'candidate_residual':False,
 'classification':('PASS_TRU1SQ_REPEATED_CUT_MASS_PROBE_KINEMATIC_SEPARATION__REGULAR_51__BLOCKED_0' if passed else 'FAIL_OR_BLOCKED_TRU1SQ_REPEATED_CUT_MASS_PROBE_SEPARATION'),
 'census':{'channels':len(rows),'simple_double':type_count['simple-double'],'double_double':type_count['double-double'],
           'REGULAR':status_count['REGULAR'],'BLOCKED':status_count['BLOCKED'],'by_q_squared':dict(q_count),
           'minimum_analytic_uncut_abs_denominator':global_min,'max_cut_shell_abs_error':global_shell,
           'max_q2_abs_error':global_q2err,'minimum_kallen':global_lam},
 'mass_probe_contract':{'double_group_mu_squared_nodes':[-PROBE,0.0,PROBE],
                        'simple_cut_group_mass_squared':0.0,'double_double_cartesian_probe_grid':True},
 'thresholds':{'uncut_absolute_separation_min':SEPARATION_MIN,'cut_shell_abs_max':SHELL_MAX,'q2_abs_max':Q2_MAX,'kallen_min':LAMBDA_MIN},
 'scope':'KINEMATIC_PREREQUISITE_ONLY__NO_PHYSICAL_REPEATED_CUT_TRU1SQ_INTEGRATION',
 'channels':rows,
 'guardrails':['ITERATION375_DERIVATIVE_IDENTITIES_REQUIRED','SAME_I0_ON_MASS_PROBES','ANALYTIC_FULL_SPHERE_UNCUT_RANGE_NOT_POINT_SAMPLING',
               'NO_ORDINARY_SIMPLE_SUBSTITUTION','DISTINCT_Q2_BUCKETS_NEVER_SUMMED','NO_ZERO_FILL','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':('if PASS, integrate the 36 simple-double channels with one symmetric auxiliary-mass derivative and the 15 double-double channels with a mixed symmetric derivative, using independent step-size and angular convergence checks and preserving the three q2 coordinates separately')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
