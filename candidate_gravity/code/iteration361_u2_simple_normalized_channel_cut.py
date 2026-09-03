#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 361.

Compute the repository-normalized channel-resolved ordinary-simple Tr U2 cut for
only the 36 channels certified REGULAR by Iteration 360.  The frozen Iteration
337 bridge is D_s I[F] = - sphere_mean(F).  Physical ghost/graviton algebraic
propagator signs from the Iteration-355 stripped decomposition are retained
explicitly. Distinct external q^2 discontinuity variables are never summed.

This gate does not touch repeated poles, does not fold in the separate +i/2
connection effective-action coefficient, and does not perform Source/Born
subtraction or comparator promotion.
"""
from __future__ import annotations
import contextlib, io, json, math, runpy
from collections import defaultdict
from pathlib import Path
import numpy as np

ITERATION=361
ROOT=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    P355=runpy.run_path(str(ROOT/'iteration355_u2_heldout_physical_numerator_transport.py'),run_name='iteration361_parent355')
    P360=runpy.run_path(str(ROOT/'iteration360_u2_simple_channel_on_shell_regularity_v2.py'),run_name='iteration361_parent360')

raw=P355['raw']; enumerate_subterms=P355['enumerate_subterms']; mdot=P355['mdot']; prop_den=P355['prop_den']
PREF=np.array([.43,-.27,.39,.21],dtype=float)
CONVERGENCE_TOL=2e-5  # no weaker than the frozen direct-cut angular authority used in the determinant branch
SHELL_TOL=2e-10

# Fail closed if Iteration 360 is not exactly the expected all-REGULAR authority.
c360=P360['result']['census']
if not (P360['result']['scientific_gate_pass'] and c360['typed_channels']==36 and c360['REGULAR']==36 and c360['BLOCKED']==0):
    raise RuntimeError(('iteration360_not_all_regular',c360))


def mbilin(a,b):
    a=np.asarray(a); b=np.asarray(b)
    return -a[0]*b[0]+np.dot(a[1:],b[1:])

def mproj_orth(v,q):
    q2=float(np.real(mdot(q)))
    return np.asarray(v,float)-np.asarray(q,float)*(float(np.real(mbilin(v,q)))/q2)

def transverse_basis(q):
    seeds=[np.array([0.,1.,0.,0.]),np.array([0.,0.,1.,0.]),np.array([0.,0.,0.,1.]),np.array([1.,0.,0.,0.]),np.array([1.,1.,0.,0.])]
    basis=[]
    for s in seeds:
        v=mproj_orth(s,q)
        for e in basis: v=v-float(np.real(mbilin(v,e)))*e
        n2=float(np.real(mdot(v)))
        if n2>1e-12: basis.append(v/math.sqrt(n2))
        if len(basis)==3: break
    if len(basis)!=3: raise RuntimeError('transverse_basis_failure')
    return basis

def species_sign(sp):
    # Iteration 355: ghost denominator = -p^2, graviton denominator = +p^2.
    if sp=='ghost': return -1.0
    if sp=='graviton': return 1.0
    raise ValueError(sp)

def sphere_mean(route,subterm,i,j,offsets,species,nz,nphi,phi_shift=0.0):
    a=offsets[i]; b=offsets[j]; q=b-a; q2=float(np.real(mdot(q)))
    rho=math.sqrt(-q2)/2.0; basis=transverse_basis(q)
    zs,ws=np.polynomial.legendre.leggauss(nz)
    total=0j; max_shell=0.0; min_uncut=float('inf')
    cut_alg_sign=species_sign(species[i])*species_sign(species[j])
    for z,wz in zip(zs,ws):
        r=math.sqrt(max(0.0,1.0-float(z)*float(z)))
        row=0j
        for m in range(nphi):
            phi=2.0*math.pi*(m+phi_shift)/nphi
            n=np.array([r*math.cos(phi),r*math.sin(phi),float(z)])
            v=rho*(n[0]*basis[0]+n[1]*basis[1]+n[2]*basis[2])
            p=-a-0.5*q+v
            ss=enumerate_subterms(raw[route],p)[subterm]
            props=ss['props']; num=complex(ss['numerator_trace'])
            max_shell=max(max_shell,float(abs(complex(mdot(props[i][1])))),float(abs(complex(mdot(props[j][1])))))
            d=1+0j
            for u,(sp,k) in enumerate(props):
                if u in (i,j): continue
                du=complex(prop_den(sp,k)); min_uncut=min(min_uncut,abs(du)); d*=du
            if abs(d)<1e-10: raise RuntimeError(('uncut_pole_encountered',route,subterm,i,j,abs(d)))
            row += cut_alg_sign*num/d
        total += float(wz)*(row/nphi)
    # 1/(4pi) int dphi dz = 1/2 * GaussLegendre_z(mean_phi)
    return 0.5*total,max_shell,min_uncut,cut_alg_sign

records=[]; converged=0; blocked=0; max_conv=0.0; max_shell=0.0; min_uncut=float('inf')
groups=defaultdict(list)
for parent in P360['result']['channels']:
    if parent['status']!='REGULAR': continue
    route=int(parent['route']); subterm=int(parent['subterm']); i,j=map(int,parent['cut_pair'])
    sref=enumerate_subterms(raw[route],PREF)[subterm]
    offsets=[np.asarray(k,float)-PREF for _,k in sref['props']]; species=[sp for sp,_ in sref['props']]
    low,es1,mu1,sgn=sphere_mean(route,subterm,i,j,offsets,species,6,12,0.0)
    high,es2,mu2,_=sphere_mean(route,subterm,i,j,offsets,species,8,16,0.0)
    shifted,es3,mu3,_=sphere_mean(route,subterm,i,j,offsets,species,8,16,0.5)
    scale=max(1.0,abs(high),abs(low),abs(shifted))
    conv=max(abs(high-low),abs(high-shifted))/scale
    max_conv=max(max_conv,float(conv)); max_shell=max(max_shell,es1,es2,es3); min_uncut=min(min_uncut,mu1,mu2,mu3)
    status='CONVERGED' if conv<=CONVERGENCE_TOL and max(es1,es2,es3)<=SHELL_TOL else 'BLOCKED_CONVERGENCE'
    if status=='CONVERGED': converged+=1
    else: blocked+=1
    ds=-high  # frozen Iteration-337 normalized simple-cut bridge
    q2=float(parent['q2']); qkey=round(q2,12)
    rec={'route':route,'subterm':subterm,'cut_pair':[i,j],'species_pair':[species[i],species[j]],'cut_algebraic_sign':sgn,
         'q2':q2,'status':status,'sphere_mean_low':[float(low.real),float(low.imag)],
         'sphere_mean_high':[float(high.real),float(high.imag)],'sphere_mean_high_phi_shifted':[float(shifted.real),float(shifted.imag)],
         'scaled_convergence_error':float(conv),'D_s_TrU2_channel':[float(ds.real),float(ds.imag)],
         'max_cut_shell_abs_error':max(es1,es2,es3),'minimum_sampled_uncut_abs_denominator':min(mu1,mu2,mu3)}
    records.append(rec); groups[qkey].append(rec)

# Aggregate only within the same discontinuity variable q^2. Never sum across q^2 buckets.
by_q2={}
for q2,recs in sorted(groups.items()):
    vals=[complex(*r['D_s_TrU2_channel']) for r in recs if r['status']=='CONVERGED']
    s=sum(vals,0j)
    by_q2[str(q2)]={'channel_count':len(recs),'converged_channel_count':len(vals),
                    'D_s_TrU2_simple_sector_sum':[float(s.real),float(s.imag)] if len(vals)==len(recs) else None,
                    'status':'CONVERGED' if len(vals)==len(recs) else 'BLOCKED_PARTIAL'}

# Scientific gate PASS means the requested fail-closed classification completed;
# individual channels may legitimately remain convergence-BLOCKED.
resolved=bool(len(records)==36 and converged+blocked==36 and len(groups)==3 and np.isfinite(max_conv) and max_shell<=SHELL_TOL)
classification=('PASS_U2_SIMPLE_NORMALIZED_CHANNEL_CUT_CLASSIFICATION__ALL_CONVERGED' if resolved and blocked==0 else
                'PASS_U2_SIMPLE_NORMALIZED_CHANNEL_CUT_CLASSIFICATION__SOME_CHANNELS_CONVERGENCE_BLOCKED' if resolved else
                'FAIL_U2_SIMPLE_NORMALIZED_CHANNEL_CUT_GATE')
result={'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':resolved,'candidate_residual':False,
        'classification':classification,
        'census':{'typed_channels':len(records),'CONVERGED':converged,'BLOCKED_CONVERGENCE':blocked,'q2_buckets':len(groups),
                  'max_scaled_convergence_error':max_conv,'max_cut_shell_abs_error':max_shell,'minimum_sampled_uncut_abs_denominator':min_uncut},
        'quadrature':{'low':{'gauss_legendre_z':6,'periodic_phi':12},'high':{'gauss_legendre_z':8,'periodic_phi':16},
                      'independent_phase_check':'high phi grid shifted by half-step','scaled_convergence_max':CONVERGENCE_TOL},
        'normalization':'ITERATION337_D_s_I_EQUALS_MINUS_SPHERE_MEAN','effective_action_weight':'NOT_FOLDED__ITERATION308_PLUS_I_OVER_2_TRU2_SEPARATE',
        'by_q2':by_q2,'channels':records,
        'scope':'ORDINARY_SIMPLE_U2_NORMALIZED_CHANNEL_RESOLVED_CUT_ONLY__DISTINCT_Q2_NOT_SUMMED',
        'guardrails':['ITERATION360_REGULAR_CHANNELS_ONLY','GHOST_GRAVITON_PROPAGATOR_SIGNS_EXPLICIT','REPEATED_POLES_NOT_EVALUATED',
                      'DISTINCT_Q2_DISCONTINUITIES_NOT_SUMMED','NO_EFFECTIVE_ACTION_WEIGHT_FOLDING','NO_SOURCE_BORN_SUBTRACTION',
                      'NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],
        'next_gate':('if all channels CONVERGED, freeze the three q2-resolved ordinary-simple TrU2 coordinates and proceed independently to the Iteration359 repeated-pole auxiliary-mass derivative/distributional validation; '
                     'if any channel is BLOCKED_CONVERGENCE, resolve only those channels with a demonstrably stronger quadrature or analytic angular reduction without weakening the threshold')}
print(json.dumps(result,indent=2,sort_keys=True))
if not resolved: raise SystemExit(2)
