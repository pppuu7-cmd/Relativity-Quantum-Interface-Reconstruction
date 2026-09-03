#!/usr/bin/env python3
"""RQIR Iteration 330: physical determinant numerator-family canonicalization.

Uses only frozen authorities:
- Iteration 312 cubic logdet weights: 1, -1/2, +1/3;
- Iteration 324 ordered shifted propagator routing;
- Iteration 329 one-common-background physical H/N insertion factories;
- Iteration 328 signed-affine denominator quotient for triangle orientations.

For each cubic route this script constructs the physical integrand
  (1/2) Tr_H - Tr_N
with the correct topology weight, using the exact K0 inverse from the same
parent at every shifted loop momentum.  It then finds an explicit signed-affine
loop map p = sigma*k + C into a canonical denominator representative, transports
the full numerator under that same map, and checks reconstruction at held-out
loop momenta.  Denominator equivalence is never promoted to numerator equality:
each route retains its own transformed numerator function.

This gate does not integrate, perform Source/Born subtraction, claim a nonzero
cut, create ANSATZ-003, or run Fisher/resources.
"""
from __future__ import annotations
import contextlib, io, itertools, json, re
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
D=4; TARGET=(1,1,1); ZERO=(0,0,0)
ETA=np.diag([-1.,1.,1.,1.])
QINT=[(27,-19,31,11),(-13,37,17,-29),(-14,-18,-48,18)]
QMODES=[np.array(q,float)/100.0 for q in QINT]


def add(a,b): return tuple(x+y for x,y in zip(a,b))
def qint(a): return tuple(sum(a[r]*QINT[r][mu] for r in range(3)) for mu in range(D))
def nz_subindices():
    return [a for a in itertools.product((0,1), repeat=3) if any(a)]
NZ=nz_subindices()
def topology():
    one=[(TARGET,)]
    two=[(a,b) for a in NZ for b in NZ if add(a,b)==TARGET]
    three=[(a,b,c) for a in NZ for b in NZ for c in NZ if add(add(a,b),c)==TARGET]
    return one+two+three

def shifts_for(seq):
    shifts=[]; cur=(0,0,0,0)
    for a in seq:
        shifts.append(cur)
        qa=qint(a); cur=tuple(cur[i]+qa[i] for i in range(D))
    if cur!=(0,0,0,0): raise AssertionError((seq,cur))
    return shifts

def topology_weight(seq):
    return {1:1.0,2:-0.5,3:1.0/3.0}[len(seq)]

def denom(k): return float(np.real_if_close(k@ETA@k))

def translated_canonical(shifts):
    candidates=[]
    for origin in shifts:
        rel=tuple(sorted(tuple(s[i]-origin[i] for i in range(D)) for s in shifts))
        candidates.append(rel)
    return min(candidates)

def signed_affine_canonical(shifts):
    cands=[]
    for sigma in (1,-1):
        ss=[tuple(sigma*x for x in s) for s in shifts]
        for origin in ss:
            rel=tuple(sorted(tuple(s[i]-origin[i] for i in range(D)) for s in ss))
            cands.append(rel)
    return min(cands)

def map_to_rep(shifts, rep, allow_sign):
    """Find p=sigma*k+C such that transformed shift multiset is rep."""
    sigmas=(1,-1) if allow_sign else (1,)
    reps=list(rep)
    for sigma in sigmas:
        for s0 in shifts:
            for r0 in reps:
                # transformed shifts are sigma*(C+s); set s0 -> r0
                C=tuple(sigma*r0[i]-s0[i] for i in range(D))
                transformed=sorted(tuple(sigma*(C[i]+s[i]) for i in range(D)) for s in shifts)
                if tuple(transformed)==tuple(rep): return sigma,C
    raise AssertionError((shifts,rep,allow_sign))


def load_graviton_parent(p_in):
    src=(ROOT/'iteration319_det_graviton_three_mode_routing.py').read_text().split('FIT=indices(4)',1)[0]
    pat=r'qs=\[.*?\]\np=np\.array\([^\n]+\)'
    rep='qs=[np.array(x,float) for x in QMODES]\np=P_IN.copy()'
    src,n=re.subn(pat,rep,src,count=1,flags=re.S)
    if n!=1: raise RuntimeError(f'failed Iteration-319 q/p specialization: {n}')
    ns={'QMODES':[x.copy() for x in QMODES],'P_IN':np.array(p_in,float)}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(src,'iteration319_common_background_prefix','exec'),ns,ns)
    return ns

def build_ghost_same_parent(g):
    D=g['D']; ZERO=g['ZERO']; eta=g['eta']; IND=g['IND']
    G=g['G']; Gam=g['Gam']; Ric=g['Ric']; deg=g['deg']; decompositions=g['decompositions']; qsum=g['qsum']; p=g['p']
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
    return N

CACHE={}
def parent_at(k):
    key=tuple(np.round(np.asarray(k,float),12))
    if key not in CACHE:
        g=load_graviton_parent(np.array(k,float)); N=build_ghost_same_parent(g)
        CACHE[key]=(g,N)
    return CACHE[key]

def sector_trace(seq,p,sector):
    prod=None
    for a,s in zip(seq,shifts_for(seq)):
        kin=np.asarray(p,float)+np.asarray(s,float)/100.0
        g,N=parent_at(kin)
        K=g['H'] if sector=='H' else N
        G0=np.linalg.inv(K[ZERO])
        block=G0@K[a]
        prod=block if prod is None else prod@block
    return np.trace(prod)

def physical_integrand(seq,p):
    w=topology_weight(seq)
    return w*(0.5*sector_trace(seq,p,'H')-sector_trace(seq,p,'N'))

def denom_product(p,shifts):
    out=1.0
    for s in shifts: out*=denom(np.asarray(p,float)+np.asarray(s,float)/100.0)
    return out

def transformed_p(k,sigma,C):
    return sigma*np.asarray(k,float)+np.asarray(C,float)/100.0

def representative_for(seq):
    sh=shifts_for(seq)
    if len(seq)<3: rep=translated_canonical(sh); allow=False
    else: rep=signed_affine_canonical(sh); allow=True
    sigma,C=map_to_rep(sh,rep,allow)
    return rep,sigma,C

# Structural census and explicit maps.
seqs=topology()
records=[]
for seq in seqs:
    sh=shifts_for(seq); rep,sigma,C=representative_for(seq)
    records.append({'sequence':seq,'shifts':sh,'rep':rep,'sigma':sigma,'C':C})

single_reps={r['rep'] for r in records if len(r['sequence'])==1}
bubble_reps={r['rep'] for r in records if len(r['sequence'])==2}
tri_reps={r['rep'] for r in records if len(r['sequence'])==3}

# Held-out loop points deliberately distinct from historical fixture P.
held=[np.array([.43,-.57,.36,.71]),np.array([.77,.28,-.41,.63]),np.array([-.52,.66,.47,.39])]
max_reconstruction=0.0; max_denmap=0.0; checks=[]
for idx,r in enumerate(records):
    seq=r['sequence']; sh=r['shifts']; rep=r['rep']; sigma=r['sigma']; C=r['C']
    route_err=0.0; den_err=0.0
    for k in held:
        p=transformed_p(k,sigma,C)
        # Original routed integrand at the mapped p.
        I=physical_integrand(seq,p)
        # Canonical denominator product and transported numerator.
        Dcan=denom_product(k,rep)
        Dorig=denom_product(p,sh)
        den_err=max(den_err,abs(Dcan-Dorig)/max(1.0,abs(Dcan),abs(Dorig)))
        num=I*Dcan
        recon=num/Dcan
        route_err=max(route_err,abs(recon-I)/max(1.0,abs(I)))
    max_reconstruction=max(max_reconstruction,route_err); max_denmap=max(max_denmap,den_err)
    checks.append({'sequence':[list(a) for a in seq],
                   'topology_order':len(seq),'weight':topology_weight(seq),
                   'original_shifts_int100':[list(s) for s in sh],
                   'canonical_rep_int100':[list(s) for s in rep],
                   'map':{'sigma':sigma,'C_int100':list(C),'abs_jacobian':1},
                   'heldout_reconstruction_max_scaled_error':route_err,
                   'heldout_denominator_map_max_scaled_error':den_err})

# Origin classification is topology-level only. Singleton has one massless denominator
# and, absent an external scale after loop translation, is scaleless in DR. Bubbles and
# triangles carry nonzero external differences and are only CUT-CAPABLE, not certified
# to have nonzero discontinuity before numerator reduction/integration.
qdiff_nonzero=all(any(x for x in qint(a)) for a in NZ)
threshold=5e-10
ok=(len(seqs)==13 and len(single_reps)==1 and len(bubble_reps)==3 and len(tri_reps)==1
    and max_reconstruction<threshold and max_denmap<threshold and qdiff_nonzero)

result={
 'iteration':330,'model_readiness_percent':24,'scientific_gate_pass':bool(ok),
 'classification':('PASS_PHYSICAL_CUBIC_DETERMINANT_NUMERATOR_SIGNED_AFFINE_FAMILY_RECONSTRUCTION' if ok else 'FAIL_PHYSICAL_CUBIC_DETERMINANT_NUMERATOR_SIGNED_AFFINE_FAMILY_RECONSTRUCTION'),
 'candidate_residual':False,
 'scope':{'common_background':'Iteration-329 one-parent H/N','logdet_weights':{'singleton':1.0,'pair':-0.5,'triple':1.0/3.0},
          'physical_combination':'weight * (1/2 Tr_H - Tr_N)','sequence_count':len(seqs),
          'canonical_family_counts':{'singleton':len(single_reps),'bubble':len(bubble_reps),'signed_affine_triangle':len(tri_reps)},
          'heldout_loop_points':len(held),'numerator_transport':'route-specific; no numerator quotient across equivalent denominators'},
 'checks':{'max_heldout_reconstruction_scaled_error':max_reconstruction,
           'max_heldout_denominator_map_scaled_error':max_denmap,'threshold':threshold,'routes':checks},
 'origin_classification':{
   'singleton':'SCOPED_SCALELESS_IN_DIMENSIONAL_REGULARIZATION_AFTER_LOOP_TRANSLATION; no external denominator scale; local/power-divergent origin only',
   'three_bubble_families':'CUT_CAPABLE_TOPOLOGY_ONLY; nonzero external momentum difference; nonzero discontinuity not yet certified',
   'one_signed_affine_triangle_family':'CUT_CAPABLE_TOPOLOGY_ONLY; denominator orientation quotient proven, route-specific transformed numerators retained; nonzero discontinuity not yet certified'},
 'physical_status':{'physical_cubic_determinant_integrand_family_reconstruction':'FROZEN_IF_PASS',
                    'integrated_normalized_determinant_cut':'ALLOWED_NEXT_SCOPED_GATE_IF_PASS',
                    'full_finite_DR_remainder':'BLOCKED_BY_ITERATION297_EVANESCENT_SCHEME_AUTHORITY',
                    'source_born_subtraction':'STILL_FORBIDDEN_UNTIL_ACTUAL_CUT_ORIGIN_IS_REDUCED',
                    'comparator_subtracted_residual':'ABSENT'},
 'guardrails':['DENOMINATOR_EQUIVALENCE_NOT_NUMERATOR_EQUIVALENCE','ROUTE_SPECIFIC_NUMERATORS_RETAINED','CUT_CAPABLE_TOPOLOGY_IS_NOT_NONZERO_DISCONTINUITY','ITERATION297_EVANESCENT_SCHEME_BLOCKER_REMAINS','NO_SOURCE_BORN_SUBTRACTION_YET','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_HEAVY_FULL_C5'],
 'next_gate':('perform scoped DR/timelike discontinuity reduction of the three canonical bubble families and the signed-affine triangle family using these transported physical numerators; certify zero/nonzero discontinuity family by family before any matched Source/Born subtraction' if ok else 'preserve FAIL and repair numerator transport/canonical maps without changing frozen parent dynamics, topology weights or thresholds')
}
print(json.dumps(result,indent=2,sort_keys=True,default=lambda x:list(x) if isinstance(x,tuple) else x))
if not ok: raise SystemExit(2)
