#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 364.

Physical normalized evaluation of the 48 U2 timelike channels whose cut passes
through the unique double-pole momentum group.

Frozen parents:
- Iteration 359: exactly one multiplicity-2 momentum group per repeated family;
  48 distinct-group timelike channels cut that group and need one mu^2 derivative.
- Iteration 362: auxiliary-mass derivative/distributional sign and normalization.
- Iteration 363: all 48 channels remain REGULAR for mu^2 in {-1e-5,0,+1e-5},
  with analytic full-sphere uncut-pole separation.
- Iteration 337: massless simple-cut normalization D_s I = - sphere_mean.

For a repeated group chosen as cut leg 1 and the other cut group as massless leg 2,
let s=-q^2>0 and m1^2=mu2, m2^2=0.  The two-body phase-space ratio to the
massless reference is beta=(s-mu2)/s.  The on-shell repeated-leg momentum is
p1=alpha q+rho n with
    alpha=-(s+mu2)/(2s),
    rho=(s-mu2)/(2 sqrt(s)),
and loop momentum k=p1-a.

If G(mu2,n)=beta * algebraic_cut_sign * numerator / uncut_denominators, then
D_s I_simple(mu2)=-<G>, while the double-pole identity implies
D_s I_repeated=-d_mu2 D_s I_simple = <d_mu2 G>|_0.

We differentiate pointwise on identical angular nodes with the fourth-order
symmetric stencil, and compare h vs h/2 plus independent angular resolution and
half-phi-grid shift.  Symmetric probes stay within the Iteration-363 certified
|mu2|<=1e-5 envelope.

This gate covers only the 48 channels that cut the double pole.  The 18 timelike
simple-simple cuts in (2,1,1) repeated families leave the double pole uncut and
remain a separate gate.
"""
from __future__ import annotations
import contextlib, io, json, math, runpy
from collections import defaultdict
from pathlib import Path
import numpy as np

ITERATION=364
ROOT=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    P355=runpy.run_path(str(ROOT/'iteration355_u2_heldout_physical_numerator_transport.py'),run_name='iteration364_parent355')
    P359=runpy.run_path(str(ROOT/'iteration359_u2_repeated_pole_derivative_contract.py'),run_name='iteration364_parent359')
    P363=runpy.run_path(str(ROOT/'iteration363_u2_repeated_pole_massive_cut_kinematic_separation.py'),run_name='iteration364_parent363')

if not P359['result']['scientific_gate_pass']:
    raise RuntimeError('iteration359_parent_not_authoritative')
c363=P363['result']['census']
if not (P363['result']['scientific_gate_pass'] and c363['typed_repeated_channels']==48 and c363['REGULAR']==48 and c363['BLOCKED']==0):
    raise RuntimeError(('iteration363_not_all_regular',c363))

raw=P355['raw']; enumerate_subterms=P355['enumerate_subterms']; mdot=P355['mdot']; prop_den=P355['prop_den']
PREF=np.array([.43,-.27,.39,.21],dtype=float)
CONVERGENCE_TOL=2e-5
SHELL_TOL=2e-10
BASE_H=5.0e-6      # central stencil reaches exactly +/-1e-5
HALF_H=2.5e-6


def mbilin(a,b):
    a=np.asarray(a); b=np.asarray(b)
    return -a[0]*b[0]+np.dot(a[1:],b[1:])


def transverse_basis(q):
    q=np.asarray(q,float); q2=float(np.real(mdot(q)))
    seeds=[np.array([0.,1.,0.,0.]),np.array([0.,0.,1.,0.]),np.array([0.,0.,0.,1.]),np.array([1.,0.,0.,0.]),np.array([1.,1.,0.,0.])]
    basis=[]
    for seed in seeds:
        v=seed-q*(float(np.real(mbilin(seed,q)))/q2)
        for e in basis:
            v=v-float(np.real(mbilin(v,e)))*e
        n2=float(np.real(mdot(v)))
        if n2>1e-12:
            basis.append(v/math.sqrt(n2))
        if len(basis)==3:
            break
    if len(basis)!=3:
        raise RuntimeError('transverse_basis_failure')
    return basis


def species_sign(sp):
    if sp=='ghost': return -1.0
    if sp=='graviton': return 1.0
    raise ValueError(sp)


def group_sign(species,members):
    z=1.0
    for u in members:
        z*=species_sign(species[u])
    return z


def central4(vals,h):
    # vals ordered at [-2h,-h,+h,+2h]
    return (vals[0]-8.0*vals[1]+8.0*vals[2]-vals[3])/(12.0*h)


def channel_derivative(fam,ch,nz,nphi,h,phi_shift=0.0):
    route=int(fam['route']); subterm=int(fam['subterm'])
    sref=enumerate_subterms(raw[route],PREF)[subterm]
    species=[sp for sp,_ in sref['props']]
    offsets=[np.asarray(k,float)-PREF for _,k in sref['props']]
    groups=fam['groups']; gi,gj=map(int,ch['group_pair'])

    # Reorient so the repeated group is always auxiliary-mass leg 1.
    if int(groups[gi]['multiplicity'])==2:
        rg,og=gi,gj
    elif int(groups[gj]['multiplicity'])==2:
        rg,og=gj,gi
    else:
        raise RuntimeError(('cut_does_not_contain_double_group',route,subterm,gi,gj))

    rmem=list(map(int,groups[rg]['members'])); omem=list(map(int,groups[og]['members']))
    if len(rmem)!=2 or len(omem)!=1:
        raise RuntimeError(('unexpected_group_members',route,subterm,len(rmem),len(omem)))

    a=offsets[rmem[0]]; b=offsets[omem[0]]; q=b-a
    s=float(-np.real(mdot(q)))
    if s<=1e-12:
        raise RuntimeError(('non_timelike_q',route,subterm,s))
    basis=transverse_basis(q)
    cut_sign=group_sign(species,rmem)*group_sign(species,omem)
    excluded=set(rmem+omem)
    mus=[-2.0*h,-h,h,2.0*h]
    if max(abs(x) for x in mus)>1.0000001e-5:
        raise RuntimeError(('mu_probe_exceeds_iteration363_envelope',mus))

    zs,ws=np.polynomial.legendre.leggauss(nz)
    total=0j; max_shell=0.0; min_uncut=float('inf')
    for z,wz in zip(zs,ws):
        rr=math.sqrt(max(0.0,1.0-float(z)*float(z)))
        row=0j
        for m in range(nphi):
            phi=2.0*math.pi*(m+phi_shift)/nphi
            n=np.array([rr*math.cos(phi),rr*math.sin(phi),float(z)])
            unit=n[0]*basis[0]+n[1]*basis[1]+n[2]*basis[2]
            values=[]
            for mu2 in mus:
                beta=(s-mu2)/s
                alpha=-(s+mu2)/(2.0*s)
                rho=(s-mu2)/(2.0*math.sqrt(s))
                p=-a+alpha*q+rho*unit
                ss=enumerate_subterms(raw[route],p)[subterm]
                props=ss['props']; num=complex(ss['numerator_trace'])
                # Every member of the repeated group shares the same momentum.
                kr=np.asarray(props[rmem[0]][1],float)
                ko=np.asarray(props[omem[0]][1],float)
                max_shell=max(max_shell,abs(complex(mdot(kr))+mu2),abs(complex(mdot(ko))))
                d=1+0j
                for u,(sp,k) in enumerate(props):
                    if u in excluded:
                        continue
                    du=complex(prop_den(sp,k))
                    min_uncut=min(min_uncut,abs(du))
                    d*=du
                if abs(d)<1e-10:
                    raise RuntimeError(('uncut_pole_encountered',route,subterm,rg,og,mu2,abs(d)))
                values.append(beta*cut_sign*num/d)
            row += central4(values,h)
        total += float(wz)*(row/nphi)
    # 1/(4pi) int dOmega = 1/2 int_{-1}^1 dz mean_phi.
    return 0.5*total,max_shell,min_uncut,s,cut_sign,rg,og


records=[]; by_bucket=defaultdict(list)
max_conv=0.0; max_shell=0.0; min_uncut=float('inf'); blocked=0
for fam in P359['result']['families']:
    for ch in fam['timelike_distinct_group_channels']:
        if not ch['repeated_pole_reduction_required']:
            continue
        low,es1,mu1,s,sgn,rg,og=channel_derivative(fam,ch,6,12,BASE_H,0.0)
        high,es2,mu2,_,_,_,_=channel_derivative(fam,ch,8,16,BASE_H,0.0)
        shifted,es3,mu3,_,_,_,_=channel_derivative(fam,ch,8,16,BASE_H,0.5)
        halfstep,es4,mu4,_,_,_,_=channel_derivative(fam,ch,8,16,HALF_H,0.0)
        scale=max(1.0,abs(low),abs(high),abs(shifted),abs(halfstep))
        conv=float(max(abs(high-low),abs(high-shifted),abs(high-halfstep))/scale)
        shell=max(es1,es2,es3,es4)
        status='CONVERGED' if conv<=CONVERGENCE_TOL and shell<=SHELL_TOL else 'BLOCKED_CONVERGENCE'
        if status!='CONVERGED': blocked+=1
        max_conv=max(max_conv,conv); max_shell=max(max_shell,shell); min_uncut=min(min_uncut,mu1,mu2,mu3,mu4)
        q2=float(ch['q2']); qkey=round(q2,12)
        rec={
            'route':int(fam['route']),'subterm':int(fam['subterm']),
            'group_pair':list(map(int,ch['group_pair'])),'repeated_group':int(rg),'other_cut_group':int(og),
            'q2':q2,'status':status,'cut_algebraic_sign':float(sgn),
            'D_s_TrU2_repeated_high':[float(high.real),float(high.imag)],
            'D_s_TrU2_repeated_low':[float(low.real),float(low.imag)],
            'D_s_TrU2_repeated_high_phi_shifted':[float(shifted.real),float(shifted.imag)],
            'D_s_TrU2_repeated_halfstep':[float(halfstep.real),float(halfstep.imag)],
            'scaled_convergence_error':conv,'max_cut_shell_abs_error':shell,
            'minimum_sampled_uncut_abs_denominator':min(mu1,mu2,mu3,mu4),
        }
        records.append(rec); by_bucket[qkey].append(rec)

by_q2={}
for q2,recs in sorted(by_bucket.items()):
    vals=[complex(*r['D_s_TrU2_repeated_high']) for r in recs if r['status']=='CONVERGED']
    sm=sum(vals,0j)
    by_q2[str(q2)]={
        'channel_count':len(recs),'converged_channel_count':len(vals),
        'D_s_TrU2_cut_through_double_pole_sum':[float(sm.real),float(sm.imag)] if len(vals)==len(recs) else None,
        'status':'CONVERGED' if len(vals)==len(recs) else 'BLOCKED_PARTIAL',
    }

classified=bool(len(records)==48 and len(by_q2)==3 and max_shell<=SHELL_TOL)
all_converged=bool(classified and blocked==0 and max_conv<=CONVERGENCE_TOL)
classification=(
    'PASS_U2_REPEATED_POLE_SYMMETRIC_AUX_DERIVATIVE_48_CHANNELS__ALL_CONVERGED'
    if all_converged else
    'PASS_U2_REPEATED_POLE_SYMMETRIC_AUX_DERIVATIVE_CLASSIFICATION__SOME_CONVERGENCE_BLOCKED'
    if classified else
    'FAIL_U2_REPEATED_POLE_SYMMETRIC_AUX_DERIVATIVE_GATE'
)
result={
    'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':classified,
    'candidate_residual':False,'classification':classification,
    'census':{
        'typed_cut_through_double_pole_channels':len(records),
        'CONVERGED':len(records)-blocked,'BLOCKED_CONVERGENCE':blocked,'q2_buckets':len(by_q2),
        'max_scaled_convergence_error':max_conv,'max_cut_shell_abs_error':max_shell,
        'minimum_sampled_uncut_abs_denominator':min_uncut,
    },
    'derivative':{
        'variable':'auxiliary_mass_squared_mu2',
        'stencil':'fourth_order_symmetric_pointwise_before_angular_average',
        'base_h':BASE_H,'halfstep_h':HALF_H,
        'base_mu2_nodes':[-2*BASE_H,-BASE_H,BASE_H,2*BASE_H],
        'within_iteration363_certified_envelope':True,
    },
    'quadrature':{
        'low':{'gauss_legendre_z':6,'periodic_phi':12},
        'high':{'gauss_legendre_z':8,'periodic_phi':16},
        'independent_phi_check':'high grid shifted by half phi step',
        'convergence_threshold':CONVERGENCE_TOL,
    },
    'normalization':'D_s_repeated = -d_mu2 D_s_simple_massive = sphere_mean[d_mu2(beta*cut_sign*num/D_uncut)] at mu2=0',
    'by_q2':by_q2,'channels':records,
    'scope':'48_TIMELIKE_CHANNELS_WHERE_CUT_PASSES_THROUGH_UNIQUE_DOUBLE_POLE_ONLY',
    'guardrails':[
        'ITERATION363_ALL_REGULAR_REQUIRED','SYMMETRIC_MU2_DERIVATIVE_WITHIN_CERTIFIED_ENVELOPE',
        'POINTWISE_DERIVATIVE_BEFORE_ANGULAR_AVERAGE','DISTINCT_Q2_NOT_SUMMED',
        '18_SIMPLE_SIMPLE_CUTS_WITH_UNCUT_DOUBLE_POLE_NOT_INCLUDED','NO_EFFECTIVE_ACTION_WEIGHT_FOLDING',
        'NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'
    ],
    'next_gate':(
        'if all 48 channels converge, evaluate the 18 remaining simple-simple timelike cuts in repeated (2,1,1) families where the double pole is uncut, using the direct squared denominator and an auxiliary-mass derivative cross-check; then combine only within each q2 bucket with Iteration361 and this cut-through-double-pole sector'
        if all_converged else
        'isolate only convergence-blocked channels and resolve them with stronger angular or analytic reduction without weakening the frozen threshold'
    ),
}
print(json.dumps(result,indent=2,sort_keys=True))
if not classified:
    raise SystemExit(2)
