#!/usr/bin/env python3
"""RQIR Iteration 329: common-background closed-triad full-cubic H/N routing gate.

This is the executable realization of the prerequisite called "Iteration 328"
in CURRENT_QG_FRONT after Iteration 327 exposed that Iteration 326 combined
separate historical H/N background fixtures.  The number 329 is used only
because a separate denominator-orientation audit was already committed as 328;
that side audit does not satisfy or bypass this prerequisite.

Contract:
* one shared metric background: the frozen Iteration-319 graviton hs fixture;
* one exact closed triad: Iteration-322/324 q3=-(q1+q2);
* one incoming loop momentum p+Q for each of the 19 full-cubic requests;
* graviton H reconstructed from the Iteration-319 frozen parent formulas;
* ghost N reconstructed on exactly the same hs/qs/p parent as Iteration 320;
* both checked against same-parent exact-geometry direct oracles with the
  unchanged Iteration-326 h=2e-4 and order thresholds.

No trace integration, Source/Born subtraction, comparator residual, zero-fill,
ANSATZ promotion, Fisher/resources, or blind full-C5 work occurs here.
"""
from __future__ import annotations
import contextlib, io, itertools, json, re
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
D=4; TARGET=(1,1,1); ZERO=(0,0,0)
QINT=[(27,-19,31,11),(-13,37,17,-29),(-14,-18,-48,18)]
QMODES=[np.array(q,float)/100.0 for q in QINT]
P=np.array([.61,-.33,.24,.52],float)

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def qint(a): return tuple(sum(a[r]*QINT[r][mu] for r in range(3)) for mu in range(D))
def nonzero_subindices(target): return [a for a in itertools.product(*(range(x+1) for x in target)) if any(a)]
NZ=nonzero_subindices(TARGET)
def topology():
    one=[(TARGET,)]
    two=[(a,b) for a in NZ for b in NZ if add(a,b)==TARGET]
    three=[(a,b,c) for a in NZ for b in NZ for c in NZ if add(add(a,b),c)==TARGET]
    return one+two+three

def inventory():
    req=set(); rows=[]
    for seq in topology():
        shift=(0,0,0,0); rr=[]
        for a in seq:
            req.add((shift,a)); rr.append((shift,a))
            q=qint(a); shift=tuple(shift[i]+q[i] for i in range(D))
        if shift!=(0,0,0,0): raise AssertionError((seq,shift))
        rows.append((seq,rr))
    return sorted(req),rows
REQUESTS,ROUTES=inventory()

def load_graviton_parent(p_in):
    """Same Iteration-319 hs, but exact closed qs and routed incoming p."""
    src=(ROOT/'iteration319_det_graviton_three_mode_routing.py').read_text().split('FIT=indices(4)',1)[0]
    pat=r'qs=\[.*?\]\np=np\.array\([^\n]+\)'
    rep='qs=[np.array(x,float) for x in QMODES]\np=P_IN.copy()'
    src,n=re.subn(pat,rep,src,count=1,flags=re.S)
    if n!=1: raise RuntimeError(f'failed Iteration-319 q/p specialization: {n}')
    ns={'QMODES':[x.copy() for x in QMODES],'P_IN':np.array(p_in,float)}
    with contextlib.redirect_stdout(io.StringIO()): exec(compile(src,'iteration319_common_background_prefix','exec'),ns,ns)
    return ns

def build_ghost_same_parent(g):
    """Iteration-320 ghost construction/direct oracle on exactly g's hs/qs/p."""
    D=g['D']; M=g['M']; ZERO=g['ZERO']; eta=g['eta']; hs=g['hs']; qs=g['qs']; p=g['p']; IND=g['IND']
    G=g['G']; Gam=g['Gam']; Ric=g['Ric']; deg=g['deg']; decompositions=g['decompositions']; qsum=g['qsum']
    Rm={}
    for a in IND:
        X=np.zeros((D,D),complex)
        for b,c in decompositions(a): X+=G[b]@Ric[c]
        Rm[a]=X
    D1={a:[1j*p[nu]*np.eye(D) if a==ZERO else Gam[a][:,nu,:].copy() for nu in range(D)] for a in IND}
    S={}
    for a in IND:
        kout=p+qsum(a); aa=[[None]*D for _ in range(D)]
        for mu in range(D):
          for nu in range(D):
            X=1j*kout[mu]*D1[a][nu]
            for b,c in decompositions(a):
              if deg(b)==0: continue
              X+=Gam[b][:,mu,:]@D1[c][nu]
              for rho in range(D): X-=Gam[b][rho,mu,nu]*D1[c][rho]
            aa[mu][nu]=X
        S[a]=aa
    N={}
    for a in IND:
        X=np.zeros((D,D),complex)
        for b,c in decompositions(a):
          for mu in range(D):
           for nu in range(D): X+=G[b][mu,nu]*S[c][mu][nu]
        N[a]=X+Rm[a]
    def ghost_direct(t):
        g0=eta.copy(); dg=np.zeros((D,D,D),complex); d2g=np.zeros((D,D,D,D),complex)
        for r in range(M):
          g0+=t[r]*hs[r]
          for l in range(D): dg[l]+=1j*qs[r][l]*t[r]*hs[r]
          for l in range(D):
           for s in range(D): d2g[l,s]+=-qs[r][l]*qs[r][s]*t[r]*hs[r]
        gi=np.linalg.inv(g0); dgi=np.array([-gi@dg[l]@gi for l in range(D)])
        Ga=np.zeros((D,D,D),complex); dGa=np.zeros((D,D,D,D),complex)
        for A,m,n,s in itertools.product(range(D),repeat=4): Ga[A,m,n]+=0.5*gi[A,s]*(dg[m,s,n]+dg[n,s,m]-dg[s,m,n])
        for l,A,m,n,s in itertools.product(range(D),repeat=5):
          B=dg[m,s,n]+dg[n,s,m]-dg[s,m,n]; dB=d2g[l,m,s,n]+d2g[l,n,s,m]-d2g[l,s,m,n]
          dGa[l,A,m,n]+=0.5*(dgi[l,A,s]*B+gi[A,s]*dB)
        Ric0=np.zeros((D,D),complex)
        for m,n,A in itertools.product(range(D),repeat=3):
          Ric0[m,n]+=dGa[A,A,m,n]-dGa[n,A,m,A]
          for l in range(D): Ric0[m,n]+=Ga[A,A,l]*Ga[l,m,n]-Ga[A,n,l]*Ga[l,m,A]
        Rmix=gi@Ric0; out=np.zeros((D,D),complex)
        for mu in range(D):
          for nu in range(D):
            X=-(p[mu]*p[nu])*np.eye(D)+dGa[mu,:,nu,:]+1j*p[nu]*Ga[:,mu,:]+1j*p[mu]*Ga[:,nu,:]+Ga[:,mu,:]@Ga[:,nu,:]
            for rho in range(D): X-=Ga[rho,mu,nu]*(1j*p[rho]*np.eye(D)+Ga[:,rho,:])
            out+=gi[mu,nu]*X
        return out+Rmix
    return N,ghost_direct

def mixed_fd(direct,a,h):
    active=[r for r,x in enumerate(a) if x]
    if any(x not in (0,1) for x in a) or not active: raise ValueError(a)
    acc=None
    for signs in itertools.product((-1.,1.),repeat=len(active)):
        t=np.zeros(3); w=1.
        for r,s in zip(active,signs): t[r]=s*h; w*=s
        v=np.asarray(direct(t)); acc=w*v if acc is None else acc+w*v
    return acc/(2*h)**len(active)

def validate():
    h=2e-4
    thrH={1:3e-6,2:5e-4,3:1.2e-1}; thrN={1:2e-6,2:3e-4,3:8e-2}
    by_shift={}
    for shift,a in REQUESTS: by_shift.setdefault(shift,[]).append(a)
    rowsH=[]; rowsN=[]; maxH={1:0.,2:0.,3:0.}; maxN={1:0.,2:0.,3:0.}; common=[]
    for shift,targets in sorted(by_shift.items()):
        p_in=P+np.array(shift,float)/100.
        g=load_graviton_parent(p_in); H=g['H']; Hdirect=g['direct']; N,Ndirect=build_ghost_same_parent(g)
        # Explicit identity certificate: both sectors consume these exact same objects.
        common.append({'shift_int100':list(shift),'p_in':[float(x) for x in p_in],
                       'q_modes':[[float(x) for x in q] for q in g['qs']],
                       'h_background_norms':[float(np.linalg.norm(x)) for x in g['hs']]})
        for a in sorted(set(targets)):
            order=sum(a)
            fdH=mixed_fd(Hdirect,a,h); errH=float(np.max(np.abs(fdH-H[a]))); scH=max(1.,float(np.max(np.abs(H[a])))); relH=errH/scH
            fdN=mixed_fd(Ndirect,a,h); errN=float(np.max(np.abs(fdN-N[a]))); scN=max(1.,float(np.max(np.abs(N[a])))); relN=errN/scN
            maxH[order]=max(maxH[order],relH); maxN[order]=max(maxN[order],relN)
            rowsH.append({'shift_int100':list(shift),'multiindex':list(a),'order':order,'scaled_error':relH})
            rowsN.append({'shift_int100':list(shift),'multiindex':list(a),'order':order,'scaled_error':relN})
    passH=all(maxH[k]<thrH[k] for k in (1,2,3)); passN=all(maxN[k]<thrN[k] for k in (1,2,3))
    return {'h':h,'graviton':{'pass':passH,'max_scaled_error_by_order':{str(k):maxH[k] for k in maxH},'threshold_by_order':{str(k):thrH[k] for k in thrH},'requests':rowsH},
            'ghost':{'pass':passN,'max_scaled_error_by_order':{str(k):maxN[k] for k in maxN},'threshold_by_order':{str(k):thrN[k] for k in thrN},'requests':rowsN},
            'shared_parent_samples':common}

val=validate()
qclosure=tuple(sum(q[mu] for q in QINT) for mu in range(D)); qrank=int(np.linalg.matrix_rank(np.array(QINT,float)))
topo_ok=(len(topology())==13 and len(REQUESTS)==19)
shared_ok=all(np.max(np.abs(np.array(x['q_modes'])-np.array(QMODES)))<1e-15 for x in val['shared_parent_samples'])
nonzero_shift=any(any(x for x in s) for s,a in REQUESTS)
ok=bool(qclosure==(0,0,0,0) and qrank==2 and topo_ok and shared_ok and nonzero_shift and val['graviton']['pass'] and val['ghost']['pass'])
result={
 'iteration':329,'model_readiness_percent':24,'scientific_gate_pass':ok,
 'classification':('PASS_COMMON_BACKGROUND_CLOSED_TRIAD_PHYSICAL_HN_FULL_CUBIC_ROUTING_CERTIFICATE' if ok else 'FAIL_COMMON_BACKGROUND_CLOSED_TRIAD_PHYSICAL_HN_FULL_CUBIC_ROUTING_CERTIFICATE'),
 'candidate_residual':False,
 'iteration_numbering_note':'executes the common-background prerequisite named Iteration 328 in authoritative Iteration-327 recovery; numbered 329 only to preserve an already-committed independent denominator-orientation Iteration 328 without retroactive edits',
 'scope':{'closed_triad_q_int100':[list(q) for q in QINT],'q_total_int100':list(qclosure),'q_rank':qrank,'full_cubic_sequence_count':len(topology()),'unique_routed_requests':len(REQUESTS),'shared_metric_background':'Iteration-319 hs used identically for H and N','ghost_construction':'Iteration-320 same-parent N=Box_vector+Rmix reconstruction','incoming_rule':'p+Q_before_insertion'},
 'checks':{'full_topology_13_sequences_19_requests':topo_ok,'exact_closed_triad':qclosure==(0,0,0,0),'shared_q_parent_all_requests':shared_ok,'nonzero_shifted_incoming_momenta':nonzero_shift,'validation':val},
 'physical_status':{'common_background_closed_triad_HN_routing':'FROZEN_IF_PASS','physical_cubic_determinant_trace_assembly':'ALLOWED_NEXT_IF_PASS','integrated_cut':'NOT_YET_ALLOWED','comparator_subtracted_residual':'ABSENT'},
 'guardrails':['ONE_SHARED_BACKGROUND_FOR_GRAVITON_AND_GHOST','NO_THRESHOLD_WEAKENING','UNSUPPORTED_IS_BLOCKED_NOT_ZERO_FILLED','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_HEAVY_FULL_C5'],
 'next_gate':('assemble the physical cubic determinant trace on this certified common closed background with Iteration-324 shifted propagators; retain 1 singleton + 3 bubble + 2 translation-only triangle families and classify pole/cut origin before any matched-observable subtraction' if ok else 'preserve scoped FAIL and diagnose common-background H/N reconstruction without changing parent dynamics or frozen thresholds')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not ok: raise SystemExit(2)
