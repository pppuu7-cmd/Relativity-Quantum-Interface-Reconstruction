#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 363.

Physical channel-resolved evaluation of the 48 distinct-group U2 timelike cut
channels whose cut itself passes through the unique double-pole momentum group.

Authorities:
- Iteration 359: every repeated family has exactly one multiplicity-2 group and
  repeated cut channels require one auxiliary-mass-squared derivative.
- Iteration 362: the sign/order/normalization of
      1/(D+i0)^2 = - d/d(mu2) 1/(D+mu2+i0)|0
  is independently validated on smooth distributions.
- Iteration 337: repository simple two-particle cut normalization.

For one massive auxiliary cut line (m1^2=mu2) and one massless cut line, with
s=-q^2>0, the normalized simple-cut coordinate acquires the exact two-body
phase-space factor beta=(s-mu2)/s.  The loop shell is parameterized covariantly
by alpha=-(s+mu2)/(2s), rho=(s-mu2)/(2 sqrt(s)).

The auxiliary derivative is evaluated pointwise on identical angular nodes using
a fourth-order one-sided stencil.  This avoids subtracting independently
integrated nearly equal numbers.  No negative mu2/tachyonic continuation is used.

This iteration evaluates only the 48 cut-through-double-pole channels.  The 18
simple-simple cuts inside (2,1,1) repeated families remain a separate next gate.
"""
from __future__ import annotations
import contextlib, io, json, math, runpy
from collections import defaultdict
from pathlib import Path
import numpy as np

ITERATION=363
ROOT=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    P355=runpy.run_path(str(ROOT/'iteration355_u2_heldout_physical_numerator_transport.py'),run_name='iteration363_parent355')
    P359=runpy.run_path(str(ROOT/'iteration359_u2_repeated_pole_derivative_contract.py'),run_name='iteration363_parent359')
    P362=runpy.run_path(str(ROOT/'iteration362_u2_repeated_pole_distribution_oracle.py'),run_name='iteration363_parent362')

if not (P359['result']['scientific_gate_pass'] and P362['result']['scientific_gate_pass']):
    raise RuntimeError('required_repeated_pole_authority_not_passed')

raw=P355['raw']; enumerate_subterms=P355['enumerate_subterms']; mdot=P355['mdot']; prop_den=P355['prop_den']
PREF=np.array([.43,-.27,.39,.21],dtype=float)
CONV_TOL=2e-5
SHELL_TOL=2e-10
HREL=2e-4

def mbilin(a,b):
    a=np.asarray(a); b=np.asarray(b)
    return -a[0]*b[0]+np.dot(a[1:],b[1:])

def transverse_basis(q):
    q=np.asarray(q,float); q2=float(np.real(mdot(q)))
    seeds=[np.array([0.,1.,0.,0.]),np.array([0.,0.,1.,0.]),np.array([0.,0.,0.,1.]),np.array([1.,0.,0.,0.]),np.array([1.,1.,0.,0.])]
    out=[]
    for seed in seeds:
        v=seed-q*(float(np.real(mbilin(seed,q)))/q2)
        for e in out: v=v-float(np.real(mbilin(v,e)))*e
        n2=float(np.real(mdot(v)))
        if n2>1e-12: out.append(v/math.sqrt(n2))
        if len(out)==3: break
    if len(out)!=3: raise RuntimeError('transverse_basis_failure')
    return out

def species_sign(sp):
    if sp=='ghost': return -1.0
    if sp=='graviton': return 1.0
    raise ValueError(sp)

def group_sign(species,members):
    z=1.0
    for u in members: z*=species_sign(species[u])
    return z

def deriv4_forward(vals,h):
    # f'(0) from f(0),f(h),...,f(4h), O(h^4).
    return (-25.0*vals[0]+48.0*vals[1]-36.0*vals[2]+16.0*vals[3]-3.0*vals[4])/(12.0*h)

def channel_value(fam,ch,nz,nphi,hrel,phi_shift=0.0):
    route=int(fam['route']); subterm=int(fam['subterm'])
    sref=enumerate_subterms(raw[route],PREF)[subterm]
    species=[sp for sp,_ in sref['props']]
    offsets=[np.asarray(k,float)-PREF for _,k in sref['props']]
    gi,gj=map(int,ch['group_pair'])
    groups=fam['groups']
    if groups[gi]['multiplicity']==2:
        rg,og=gi,gj
    elif groups[gj]['multiplicity']==2:
        rg,og=gj,gi
    else:
        raise RuntimeError(('channel_does_not_cut_repeated_group',route,subterm,ch))
    rmem=list(map(int,groups[rg]['members'])); omem=list(map(int,groups[og]['members']))
    if len(rmem)!=2 or len(omem)!=1:
        raise RuntimeError(('unexpected_group_multiplicity',len(rmem),len(omem)))
    a=offsets[rmem[0]]; b=offsets[omem[0]]; q=b-a
    s=float(-np.real(mdot(q)))
    if not s>1e-12: raise RuntimeError(('non_timelike_channel',s))
    basis=transverse_basis(q)
    h=hrel*s
    mus=np.arange(5,dtype=float)*h
    cut_sign=group_sign(species,rmem)*group_sign(species,omem)
    excluded=set(rmem+omem)
    zs,ws=np.polynomial.legendre.leggauss(nz)
    total=0j; max_shell=0.0; min_uncut=float('inf')
    for z,wz in zip(zs,ws):
        rr=math.sqrt(max(0.0,1.0-float(z)*float(z)))
        row=0j
        for m in range(nphi):
            phi=2.0*math.pi*(m+phi_shift)/nphi
            n=np.array([rr*math.cos(phi),rr*math.sin(phi),float(z)])
            unit=n[0]*basis[0]+n[1]*basis[1]+n[2]*basis[2]
            gv=[]
            for mu2 in mus:
                beta=(s-mu2)/s
                alpha=-(s+mu2)/(2.0*s)
                rho=(s-mu2)/(2.0*math.sqrt(s))
                p=-a+alpha*q+rho*unit
                ss=enumerate_subterms(raw[route],p)[subterm]
                props=ss['props']; num=complex(ss['numerator_trace'])
                kr=np.asarray(props[rmem[0]][1],float)
                ko=np.asarray(props[omem[0]][1],float)
                max_shell=max(max_shell,abs(complex(mdot(kr))+mu2),abs(complex(mdot(ko))))
                d=1+0j
                for u,(sp,k) in enumerate(props):
                    if u in excluded: continue
                    du=complex(prop_den(sp,k)); min_uncut=min(min_uncut,abs(du)); d*=du
                if abs(d)<1e-10: raise RuntimeError(('uncut_pole_encountered',route,subterm,rg,og,mu2,abs(d)))
                # J_simple(mu2) = - mean[ beta * cut_sign * num / D_uncut ].
                # Repeated coordinate = -dJ_simple/dmu2 = + mean[d(...)/dmu2].
                gv.append(beta*cut_sign*num/d)
            row += deriv4_forward(gv,h)
        total += float(wz)*(row/nphi)
    return 0.5*total,max_shell,min_uncut,s,h,cut_sign,rg,og

records=[]; groups_q2=defaultdict(list); max_conv=0.0; max_shell=0.0; min_uncut=float('inf'); blocked=0
for fam in P359['records']:
    for ch in fam['timelike_distinct_group_channels']:
        if not ch['repeated_pole_reduction_required']: continue
        low,es1,mu1,s,h,sgn,rg,og=channel_value(fam,ch,6,12,HREL,0.0)
        high,es2,mu2,_,_,_,_,_=channel_value(fam,ch,8,16,HREL,0.0)
        shifted,es3,mu3,_,_,_,_,_=channel_value(fam,ch,8,16,HREL,0.5)
        halfstep,es4,mu4,_,h2,_,_,_=channel_value(fam,ch,8,16,HREL/2.0,0.0)
        scale=max(1.0,abs(low),abs(high),abs(shifted),abs(halfstep))
        conv=max(abs(high-low),abs(high-shifted),abs(high-halfstep))/scale
        status='CONVERGED' if conv<=CONV_TOL and max(es1,es2,es3,es4)<=SHELL_TOL else 'BLOCKED_CONVERGENCE'
        if status!='CONVERGED': blocked+=1
        max_conv=max(max_conv,float(conv)); max_shell=max(max_shell,es1,es2,es3,es4); min_uncut=min(min_uncut,mu1,mu2,mu3,mu4)
        q2=float(ch['q2']); key=round(q2,12)
        rec={'route':int(fam['route']),'subterm':int(fam['subterm']),'group_pair':list(map(int,ch['group_pair'])),
             'repeated_group':rg,'other_cut_group':og,'q2':q2,'status':status,'cut_algebraic_sign':sgn,
             'aux_h_mu2':h,'aux_h_mu2_half':h2,
             'D_s_TrU2_repeated_channel_low':[float(low.real),float(low.imag)],
             'D_s_TrU2_repeated_channel_high':[float(high.real),float(high.imag)],
             'D_s_TrU2_repeated_channel_high_phi_shifted':[float(shifted.real),float(shifted.imag)],
             'D_s_TrU2_repeated_channel_halfstep':[float(halfstep.real),float(halfstep.imag)],
             'scaled_convergence_error':float(conv),'max_cut_shell_abs_error':max(es1,es2,es3,es4),
             'minimum_sampled_uncut_abs_denominator':min(mu1,mu2,mu3,mu4)}
        records.append(rec); groups_q2[key].append(rec)

by_q2={}
for q2,recs in sorted(groups_q2.items()):
    vals=[complex(*r['D_s_TrU2_repeated_channel_high']) for r in recs if r['status']=='CONVERGED']
    sm=sum(vals,0j)
    by_q2[str(q2)]={'channel_count':len(recs),'converged_channel_count':len(vals),
                    'D_s_TrU2_cut_through_repeated_sum':[float(sm.real),float(sm.imag)] if len(vals)==len(recs) else None,
                    'status':'CONVERGED' if len(vals)==len(recs) else 'BLOCKED_PARTIAL'}

resolved=bool(len(records)==48 and blocked==0 and len(groups_q2)==3 and max_shell<=SHELL_TOL and max_conv<=CONV_TOL)
classification=('PASS_U2_REPEATED_CUT_AUX_MASS_PHYSICAL_48_CHANNELS_ALL_CONVERGED' if resolved else
                'PASS_U2_REPEATED_CUT_AUX_MASS_PHYSICAL_CLASSIFICATION_WITH_BLOCKED_CHANNELS' if len(records)==48 else
                'FAIL_U2_REPEATED_CUT_AUX_MASS_PHYSICAL_GATE')
result={'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':bool(len(records)==48 and len(groups_q2)==3 and max_shell<=SHELL_TOL),
        'candidate_residual':False,'classification':classification,
        'census':{'typed_cut_through_repeated_channels':len(records),'CONVERGED':len(records)-blocked,'BLOCKED_CONVERGENCE':blocked,
                  'q2_buckets':len(groups_q2),'max_scaled_convergence_error':max_conv,'max_cut_shell_abs_error':max_shell,
                  'minimum_sampled_uncut_abs_denominator':min_uncut},
        'derivative':{'variable':'auxiliary_mass_squared_mu2','stencil':'fourth_order_forward_0_to_4h_pointwise_before_angular_average',
                      'h_relative_to_s':HREL,'independent_halfstep_relative_to_s':HREL/2.0,'negative_mu2_used':False},
        'normalization':'D_s_repeated = -d_mu2 D_s_simple_massive = sphere_mean[d_mu2(beta*cut_sign*num/D_uncut)] at mu2=0',
        'by_q2':by_q2,'channels':records,
        'scope':'48_DISTINCT_GROUP_TIMELIKE_CHANNELS_CUTTING_UNIQUE_DOUBLE_POLE_ONLY',
        'guardrails':['ITERATION359_REPEATED_CHANNELS_ONLY','ITERATION362_DISTRIBUTION_ORACLE_REQUIRED','POINTWISE_AUX_DERIVATIVE_BEFORE_AVERAGE',
                      'DISTINCT_Q2_NOT_SUMMED','18_SIMPLE_SIMPLE_CHANNELS_IN_REPEATED_FAMILIES_NOT_INCLUDED','NO_EFFECTIVE_ACTION_WEIGHT_FOLDING',
                      'NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],
        'next_gate':('if all 48 channels converge, evaluate the remaining 18 simple-simple distinct-group cuts in the (2,1,1) repeated families with the unique double pole left uncut (direct squared denominator, plus auxiliary-derivative cross-check); then combine only within each q2 bucket with Iteration361 and the 48-channel repeated-cut sector')}
print(json.dumps(result,indent=2,sort_keys=True))
if not result['scientific_gate_pass']:
    raise SystemExit(2)
