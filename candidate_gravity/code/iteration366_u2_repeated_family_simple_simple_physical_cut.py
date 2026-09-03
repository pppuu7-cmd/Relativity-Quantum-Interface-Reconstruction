#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 366.

Physical normalized cut integration of the 18 timelike simple-simple channels in
repeated (2,1,1) U2 families.  The unique double-pole group is uncut.

Parent authority:
- Iteration 359 identifies the repeated-family topology and typed channels.
- Iteration 365 proves all 18 target channels are full-sphere REGULAR and validates
  direct uncut D^-2 against the auxiliary-mass derivative representation.
- Iteration 337 fixes the repository massless two-particle normalization
  D_s I = - sphere_mean(integrand after the two cut denominators are stripped).

Each channel is integrated directly with the two repeated denominators retained.
On the same high angular grid an independent auxiliary-mass representation of the
uncut double-pole factor is evaluated and required to agree.  Low/high and
half-phi-shift grids provide the angular convergence check.
"""
from __future__ import annotations
import contextlib, io, json, math, runpy
from collections import defaultdict
from pathlib import Path
import numpy as np

ITERATION=366
ROOT=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    P355=runpy.run_path(str(ROOT/'iteration355_u2_heldout_physical_numerator_transport.py'),run_name='iteration366_parent355')
    P359=runpy.run_path(str(ROOT/'iteration359_u2_repeated_pole_derivative_contract.py'),run_name='iteration366_parent359')
    P365=runpy.run_path(str(ROOT/'iteration365_u2_repeated_family_simple_simple_prerequisite.py'),run_name='iteration366_parent365')

if not P365['result']['scientific_gate_pass']:
    raise RuntimeError('iteration365_parent_not_authoritative')
if P365['result']['census']['typed_simple_simple_channels_in_repeated_families']!=18 or P365['result']['census']['BLOCKED']!=0:
    raise RuntimeError(('iteration365_not_all_regular',P365['result']['census']))

raw=P355['raw']; enumerate_subterms=P355['enumerate_subterms']; mdot=P355['mdot']; prop_den=P355['prop_den']
PREF=np.array([.43,-.27,.39,.21],dtype=float)
CONV_TOL=2e-5
REP_TOL=2e-8
SHELL_TOL=2e-10
AUX_H=1e-5


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


def central4_derivative(fun,h):
    return (fun(-2*h)-8.0*fun(-h)+8.0*fun(h)-fun(2*h))/(12.0*h)


def channel_integral(fam,ch,nz,nphi,phi_shift=0.0,need_aux=False):
    route=int(fam['route']); subterm=int(fam['subterm'])
    sref=enumerate_subterms(raw[route],PREF)[subterm]
    species=[sp for sp,_ in sref['props']]
    offsets=[np.asarray(k,float)-PREF for _,k in sref['props']]
    groups=fam['groups']; ia,ib=map(int,ch['group_pair'])
    if int(groups[ia]['multiplicity'])!=1 or int(groups[ib]['multiplicity'])!=1:
        raise RuntimeError(('target_not_simple_simple',route,subterm,ia,ib))
    repeated=[i for i,g in enumerate(groups) if int(g['multiplicity'])==2]
    if len(repeated)!=1: raise RuntimeError(('bad_repeated_group_count',route,subterm))
    rg=repeated[0]
    if rg in (ia,ib): raise RuntimeError(('repeated_group_cut_unexpectedly',route,subterm,rg,ia,ib))
    cmem=[int(groups[ia]['members'][0]),int(groups[ib]['members'][0])]
    rmem=list(map(int,groups[rg]['members']))
    if len(rmem)!=2: raise RuntimeError(('bad_repeated_members',route,subterm,rmem))
    a=offsets[cmem[0]]; b=offsets[cmem[1]]; q=b-a
    s=float(-np.real(mdot(q)))
    if s<=1e-12: raise RuntimeError(('non_timelike_channel',route,subterm,s))
    basis=transverse_basis(q); rho=math.sqrt(s)/2.0
    cut_sign=species_sign(species[cmem[0]])*species_sign(species[cmem[1]])
    rep_sign=species_sign(species[rmem[0]])*species_sign(species[rmem[1]])
    excluded=set(cmem); repeated_set=set(rmem)

    zs,ws=np.polynomial.legendre.leggauss(nz)
    direct_total=0j; aux_total=0j; max_shell=0.0; min_uncut=float('inf'); max_point_rep_err=0.0
    for z,wz in zip(zs,ws):
        rr=math.sqrt(max(0.0,1.0-float(z)*float(z)))
        direct_row=0j; aux_row=0j
        for m in range(nphi):
            phi=2.0*math.pi*(m+phi_shift)/nphi
            n=np.array([rr*math.cos(phi),rr*math.sin(phi),float(z)])
            unit=n[0]*basis[0]+n[1]*basis[1]+n[2]*basis[2]
            p=-a-0.5*q+rho*unit
            ss=enumerate_subterms(raw[route],p)[subterm]
            props=ss['props']; num=complex(ss['numerator_trace'])
            k1=np.asarray(props[cmem[0]][1],float); k2=np.asarray(props[cmem[1]][1],float)
            max_shell=max(max_shell,abs(complex(mdot(k1))),abs(complex(mdot(k2))))

            d_all=1+0j; d_other=1+0j
            for u,(sp,k) in enumerate(props):
                if u in excluded: continue
                du=complex(prop_den(sp,k)); min_uncut=min(min_uncut,abs(du)); d_all*=du
                if u not in repeated_set: d_other*=du
            if abs(d_all)<1e-10: raise RuntimeError(('uncut_pole_encountered',route,subterm,abs(d_all)))
            direct_integrand=cut_sign*num/d_all
            direct_row += direct_integrand

            if need_aux:
                # Common unsigned D=k^2 of the repeated group.  The stripped
                # denominator product is (s1*s2) D^2, hence inverse factor is
                # (s1*s2)/D^2 = -(s1*s2) d_mu [1/(D+mu)]|0.
                kr=np.asarray(props[rmem[0]][1],float)
                D=complex(mdot(kr))
                aux_rep=-rep_sign*central4_derivative(lambda mu: 1.0/(D+mu),AUX_H)
                direct_rep=rep_sign/(D*D)
                point_err=abs(aux_rep-direct_rep)/max(1.0,abs(aux_rep),abs(direct_rep))
                max_point_rep_err=max(max_point_rep_err,float(point_err))
                aux_integrand=cut_sign*num*aux_rep/d_other
                aux_row += aux_integrand
        direct_total += float(wz)*(direct_row/nphi)
        if need_aux: aux_total += float(wz)*(aux_row/nphi)
    direct=-0.5*direct_total
    aux=-0.5*aux_total if need_aux else None
    return direct,aux,max_shell,min_uncut,max_point_rep_err,s,rg


records=[]; by_bucket=defaultdict(list); max_conv=0.0; max_rep=0.0; max_shell=0.0; min_uncut=float('inf'); blocked=0
for fam in P359['result']['families']:
    groups=fam['groups']
    if sorted(int(g['multiplicity']) for g in groups)!=[1,1,2]: continue
    for ch in fam['timelike_distinct_group_channels']:
        if not ch['ordinary_simple_pair']: continue
        low,_,es1,mu1,_,s,rg=channel_integral(fam,ch,6,12,0.0,False)
        high,aux,es2,mu2,rep2,_,_=channel_integral(fam,ch,8,16,0.0,True)
        shifted,_,es3,mu3,_,_,_=channel_integral(fam,ch,8,16,0.5,False)
        scale=max(1.0,abs(low),abs(high),abs(shifted),abs(aux))
        conv=float(max(abs(high-low),abs(high-shifted))/scale)
        rep_agree=float(abs(high-aux)/scale)
        shell=max(es1,es2,es3)
        status='CONVERGED' if conv<=CONV_TOL and rep_agree<=REP_TOL and rep2<=REP_TOL and shell<=SHELL_TOL else 'BLOCKED_CONVERGENCE'
        if status!='CONVERGED': blocked+=1
        max_conv=max(max_conv,conv); max_rep=max(max_rep,rep_agree,rep2); max_shell=max(max_shell,shell); min_uncut=min(min_uncut,mu1,mu2,mu3)
        q2=float(ch['q2']); key=round(q2,12)
        rec={'route':int(fam['route']),'subterm':int(fam['subterm']),'group_pair':list(map(int,ch['group_pair'])),
             'repeated_group':int(rg),'q2':q2,'status':status,
             'D_s_TrU2_simple_simple_direct_high':[float(high.real),float(high.imag)],
             'D_s_TrU2_simple_simple_direct_low':[float(low.real),float(low.imag)],
             'D_s_TrU2_simple_simple_direct_high_phi_shifted':[float(shifted.real),float(shifted.imag)],
             'D_s_TrU2_simple_simple_aux_high':[float(aux.real),float(aux.imag)],
             'scaled_angular_convergence_error':conv,'scaled_direct_vs_aux_integral_error':rep_agree,
             'max_pointwise_repeated_factor_scaled_error':rep2,'max_cut_shell_abs_error':shell,
             'minimum_sampled_uncut_abs_denominator':min(mu1,mu2,mu3)}
        records.append(rec); by_bucket[key].append(rec)

by_q2={}
for q2,recs in sorted(by_bucket.items()):
    vals=[complex(*r['D_s_TrU2_simple_simple_direct_high']) for r in recs if r['status']=='CONVERGED']
    sm=sum(vals,0j)
    by_q2[str(q2)]={'channel_count':len(recs),'converged_channel_count':len(vals),
                    'D_s_TrU2_simple_simple_in_repeated_families_sum':[float(sm.real),float(sm.imag)] if len(vals)==len(recs) else None,
                    'status':'CONVERGED' if len(vals)==len(recs) else 'BLOCKED_PARTIAL'}

classified=bool(len(records)==18 and len(by_q2)==3 and max_shell<=SHELL_TOL)
all_converged=bool(classified and blocked==0 and max_conv<=CONV_TOL and max_rep<=REP_TOL)
classification=('PASS_U2_REPEATED_FAMILY_SIMPLE_SIMPLE_18_PHYSICAL_CUTS__ALL_CONVERGED__DIRECT_AUX_AGREE'
                if all_converged else
                'PASS_U2_REPEATED_FAMILY_SIMPLE_SIMPLE_PHYSICAL_CLASSIFICATION__SOME_BLOCKED'
                if classified else 'FAIL_U2_REPEATED_FAMILY_SIMPLE_SIMPLE_PHYSICAL_GATE')
result={'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':classified,'candidate_residual':False,
        'classification':classification,
        'census':{'typed_simple_simple_channels':len(records),'CONVERGED':len(records)-blocked,'BLOCKED_CONVERGENCE':blocked,
                  'q2_buckets':len(by_q2),'max_scaled_angular_convergence_error':max_conv,
                  'max_direct_vs_aux_scaled_error':max_rep,'max_cut_shell_abs_error':max_shell,
                  'minimum_sampled_uncut_abs_denominator':min_uncut},
        'thresholds':{'angular_convergence':CONV_TOL,'direct_vs_aux_representation':REP_TOL,'cut_shell':SHELL_TOL},
        'normalization':'D_s = -sphere_mean after stripping the two massless simple cut denominators; the uncut double pole is retained directly and cross-checked by auxiliary-mass differentiation',
        'by_q2':by_q2,'channels':records,
        'scope':'18_SIMPLE_SIMPLE_TIMELIKE_CUTS_IN_REPEATED_211_FAMILIES__PHYSICAL_NORMALIZED_INTEGRATION',
        'guardrails':['DOUBLE_POLE_UNCUT_AND_RETAINED','DIRECT_D_MINUS2_PRIMARY','AUXILIARY_DERIVATIVE_INDEPENDENT_CROSSCHECK',
                      'DISTINCT_Q2_NOT_SUMMED','NO_EFFECTIVE_ACTION_WEIGHT_FOLDING','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
        'next_gate':('once Iteration364 is authoritative, combine Iteration361 ordinary-simple, Iteration364 cut-through-double-pole, and this 18-channel sector q2-by-q2 to freeze complete normalized Tr U2 discontinuity; do not include Tr U1^2 or effective-action coefficients in that Tr U2 sum' if all_converged else 'resolve only blocked channels without weakening frozen thresholds')}
print(json.dumps(result,indent=2,sort_keys=True))
if not classified: raise SystemExit(2)
