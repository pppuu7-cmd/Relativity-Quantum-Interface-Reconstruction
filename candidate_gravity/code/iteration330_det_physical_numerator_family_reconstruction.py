#!/usr/bin/env python3
"""RQIR Iteration 330: physical cubic determinant numerator-family reconstruction.

Consumes only frozen prerequisites:
- Iteration 312 cubic logdet weights;
- Iteration 324 shifted free-propagator routing on the exact closed triad;
- Iteration 328 signed-affine denominator quotient;
- Iteration 329 one-common-background routed physical H/N kernels.

The gate first reconstructs every required H_a(p), N_a(p) insertion as a degree<=2
polynomial in the arbitrary incoming loop momentum p and validates those kernel
polynomials at held-out p.  It independently verifies that p^2 K0(p)^(-1) is a
constant free numerator matrix.  It then applies only proved signed-affine loop
changes p_old = sigma p_can - s0 to every routed term, combines the exact logdet
weights (1,-1/2,1/3) and the effective determinant weight 1/2 H - N, reconstructs
the resulting canonical family numerator polynomials, and validates them on
held-out loop momenta.

No integration, nonzero-cut claim, Source/Born subtraction, comparator residual,
ANSATZ promotion, Fisher/resources, zero-fill, or blind full-C5 work occurs.
"""
from __future__ import annotations
import contextlib, io, itertools, json, math
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
ETA=np.diag([-1.,1.,1.,1.])
TARGET=(1,1,1); ZERO=(0,0,0)
QINT=[(27,-19,31,11),(-13,37,17,-29),(-14,-18,-48,18)]
BASE=np.array([.61,-.33,.24,.52],float)

# Load Iteration-329 definitions only; do not re-run its top-level validation gate.
src=(ROOT/'iteration329_det_common_background_closed_triad_hn.py').read_text()
prefix=src.split('\nval=validate()',1)[0]
ns={}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(prefix,'iteration329_definitions','exec'),ns,ns)
load_graviton_parent=ns['load_graviton_parent']
build_ghost_same_parent=ns['build_ghost_same_parent']


def add(a,b): return tuple(x+y for x,y in zip(a,b))
def qint(a): return tuple(sum(a[r]*QINT[r][mu] for r in range(3)) for mu in range(4))
def nz_indices():
    return [a for a in itertools.product((0,1),repeat=3) if any(a)]
NZ=nz_indices()

def topology():
    one=[(TARGET,)]
    two=[(a,b) for a in NZ for b in NZ if add(a,b)==TARGET]
    three=[(a,b,c) for a in NZ for b in NZ for c in NZ if add(add(a,b),c)==TARGET]
    return one+two+three
SEQS=topology()

def route_shifts(seq):
    out=[]; cur=(0,0,0,0)
    for a in seq:
        out.append(cur)
        q=qint(a); cur=tuple(cur[i]+q[i] for i in range(4))
    if cur!=(0,0,0,0): raise AssertionError((seq,cur))
    return tuple(out)

def signed_canonical(shifts):
    """Return canonical denominator key and a map p_old=sigma*p_can-s0/100."""
    best=None
    for sigma in (1,-1):
        for s0 in shifts:
            mapped=tuple(sorted(tuple(sigma*(s[i]-s0[i]) for i in range(4)) for s in shifts))
            cand=(mapped,sigma,s0)
            if best is None or mapped<best[0]: best=cand
    return best

def denom(p): return float(np.real_if_close(p@ETA@p))

def exponents(maxdeg):
    out=[]
    for e in itertools.product(range(maxdeg+1),repeat=4):
        if sum(e)<=maxdeg: out.append(e)
    return out

def design(points,exps):
    return np.array([[np.prod([p[j]**e[j] for j in range(4)]) for e in exps] for p in points],complex)

def eval_poly(coeff,exps,p):
    x=np.array([np.prod([p[j]**e[j] for j in range(4)]) for e in exps],complex)
    return np.tensordot(x,coeff,axes=(0,0))

def safe_points(n,seed,shifts=((0,0,0,0),)):
    rng=np.random.default_rng(seed); out=[]
    while len(out)<n:
        p=BASE+rng.normal(0,0.47,4)
        if all(abs(denom(p+np.array(s,float)/100.0))>0.07 for s in shifts): out.append(p)
    return out

# ---- degree-2 reconstruction of the physical insertion factories ----
KEX=exponents(2)  # 15 monomials in four variables
train=safe_points(22,33001)
hold=safe_points(10,33002)
needed=NZ
samplesH={a:[] for a in needed}; samplesN={a:[] for a in needed}
freeH=[]; freeN=[]
for p in train:
    g=load_graviton_parent(p); H=g['H']; N,_=build_ghost_same_parent(g)
    for a in needed:
        samplesH[a].append(np.asarray(H[a],complex)); samplesN[a].append(np.asarray(N[a],complex))
    freeH.append(np.asarray(H[ZERO],complex)); freeN.append(np.asarray(N[ZERO],complex))
X=design(train,KEX)
coeffH={}; coeffN={}
for a in needed:
    y=np.stack(samplesH[a]); c=np.linalg.lstsq(X,y.reshape(len(train),-1),rcond=None)[0]
    coeffH[a]=c.reshape((len(KEX),)+y.shape[1:])
    y=np.stack(samplesN[a]); c=np.linalg.lstsq(X,y.reshape(len(train),-1),rcond=None)[0]
    coeffN[a]=c.reshape((len(KEX),)+y.shape[1:])

kernel_max={'H':0.0,'N':0.0}
R_H=[]; R_N=[]
for p,H0,N0 in zip(train,freeH,freeN):
    d=denom(p); R_H.append(d*np.linalg.inv(H0)); R_N.append(d*np.linalg.inv(N0))
RH=np.mean(np.stack(R_H),axis=0); RN=np.mean(np.stack(R_N),axis=0)
free_const_err_H=max(float(np.max(np.abs(x-RH))) for x in R_H)/max(1.,float(np.max(np.abs(RH))))
free_const_err_N=max(float(np.max(np.abs(x-RN))) for x in R_N)/max(1.,float(np.max(np.abs(RN))))

for p in hold:
    g=load_graviton_parent(p); H=g['H']; N,_=build_ghost_same_parent(g)
    for a in needed:
        ph=eval_poly(coeffH[a],KEX,p); pn=eval_poly(coeffN[a],KEX,p)
        kernel_max['H']=max(kernel_max['H'],float(np.max(np.abs(ph-H[a])))/max(1.,float(np.max(np.abs(H[a])))))
        kernel_max['N']=max(kernel_max['N'],float(np.max(np.abs(pn-N[a])))/max(1.,float(np.max(np.abs(N[a])))))
    d=denom(p)
    free_const_err_H=max(free_const_err_H,float(np.max(np.abs(d*np.linalg.inv(H[ZERO])-RH)))/max(1.,float(np.max(np.abs(RH)))))
    free_const_err_N=max(free_const_err_N,float(np.max(np.abs(d*np.linalg.inv(N[ZERO])-RN)))/max(1.,float(np.max(np.abs(RN)))))

KERNEL_THR=2e-9; FREE_THR=2e-9
kernel_ok=kernel_max['H']<KERNEL_THR and kernel_max['N']<KERNEL_THR
free_ok=free_const_err_H<FREE_THR and free_const_err_N<FREE_THR

def KH(a,p): return eval_poly(coeffH[a],KEX,p)
def KN(a,p): return eval_poly(coeffN[a],KEX,p)

def sector_numerator(seq,p_old,sector):
    shifts=route_shifts(seq)
    R=RH if sector=='H' else RN
    K=KH if sector=='H' else KN
    prod=np.eye(R.shape[0],dtype=complex)
    for a,s in zip(seq,shifts):
        pin=p_old+np.array(s,float)/100.0
        prod=prod@R@K(a,pin)
    return np.trace(prod)

def logdet_weight(n): return {1:1.0,2:-0.5,3:1.0/3.0}[n]
def effective_route_numerator(seq,p_old):
    w=logdet_weight(len(seq))
    return w*(0.5*sector_numerator(seq,p_old,'H')-sector_numerator(seq,p_old,'N'))

# Group routes by the proved signed-affine denominator quotient and retain each map.
groups={}
route_maps=[]
for seq in SEQS:
    shifts=route_shifts(seq); key,sigma,s0=signed_canonical(shifts)
    rec={'seq':seq,'shifts':shifts,'sigma':sigma,'s0':s0,'key':key}
    groups.setdefault(key,[]).append(rec); route_maps.append(rec)

family_counts=sorted(len(v) for v in groups.values())
family_structure_ok=(len(SEQS)==13 and len(groups)==5 and family_counts==[1,2,2,2,6])

def family_num(routes,p_can):
    z=0j
    for r in routes:
        p_old=r['sigma']*p_can-np.array(r['s0'],float)/100.0
        z+=effective_route_numerator(r['seq'],p_old)
    return z

# Reconstruct each transformed family numerator at its mathematically maximal degree 2*n.
family_results=[]; family_ok=True
for fi,(key,routes) in enumerate(sorted(groups.items(),key=lambda kv:kv[0])):
    nprop=len(key); deg=2*nprop; exps=exponents(deg)
    pts=safe_points(len(exps)+35,33100+fi,key)
    vals=np.array([family_num(routes,p) for p in pts],complex)
    A=design(pts,exps); coef=np.linalg.lstsq(A,vals,rcond=None)[0]
    pred=A@coef
    train_rel=float(np.max(np.abs(pred-vals)))/max(1.,float(np.max(np.abs(vals))))
    hpts=safe_points(30,33200+fi,key)
    hv=np.array([family_num(routes,p) for p in hpts],complex)
    hp=design(hpts,exps)@coef
    held_rel=float(np.max(np.abs(hp-hv)))/max(1.,float(np.max(np.abs(hv))))
    passfit=(train_rel<2e-8 and held_rel<2e-8)
    family_ok=family_ok and passfit
    # Topological origin classification only; no nonzero-discontinuity claim.
    if nprop==1:
        origin='SINGLETON_SCALELESS_LOCAL_DR_ZERO_CUT_TOPOLOGY'
    elif nprop==2:
        dq=np.array(key[1],float)/100.0; q2=denom(dq)
        origin='BUBBLE_CUT_CAPABLE_TOPOLOGY' if abs(q2)>1e-12 else 'BUBBLE_DEGENERATE_BLOCKED'
    else:
        inv=[]
        for s in key[1:]: inv.append(denom(np.array(s,float)/100.0))
        origin='TRIANGLE_CUT_CAPABLE_TOPOLOGY' if any(abs(x)>1e-12 for x in inv) else 'TRIANGLE_DEGENERATE_BLOCKED'
    sparse=[]
    for e,c in zip(exps,coef):
        if abs(c)>1e-11:
            sparse.append({'exp':list(e),'re':float(c.real),'im':float(c.imag)})
    family_results.append({
        'family_index':fi,'propagator_count':nprop,'canonical_shifts_int100':[list(s) for s in key],
        'route_count':len(routes),'degree_bound':deg,'coefficient_count':len(exps),
        'nonnegligible_coefficient_count':len(sparse),'train_relative_error':train_rel,
        'heldout_relative_error':held_rel,'pass':passfit,'origin_classification':origin,
        'coefficients_sparse_threshold_1e-11':sparse,
        'route_maps':[{'sequence':[list(a) for a in r['seq']],'sigma':r['sigma'],'s0_int100':list(r['s0'])} for r in routes]
    })

all_origins_ok=(sum(x['propagator_count']==1 for x in family_results)==1 and
                sum(x['propagator_count']==2 for x in family_results)==3 and
                sum(x['propagator_count']==3 for x in family_results)==1 and
                all('BLOCKED' not in x['origin_classification'] for x in family_results))
qclosure=tuple(sum(QINT[r][mu] for r in range(3)) for mu in range(4))
ok=bool(qclosure==(0,0,0,0) and kernel_ok and free_ok and family_structure_ok and family_ok and all_origins_ok)

result={
 'iteration':330,'model_readiness_percent':24,'scientific_gate_pass':ok,
 'classification':('PASS_PHYSICAL_CUBIC_DETERMINANT_CANONICAL_NUMERATOR_FAMILIES_AND_ORIGIN_CLASSIFICATION' if ok else 'FAIL_PHYSICAL_CUBIC_DETERMINANT_CANONICAL_NUMERATOR_FAMILIES_AND_ORIGIN_CLASSIFICATION'),
 'candidate_residual':False,
 'scope':{
   'closed_triad_q_int100':[list(q) for q in QINT],'q_total_int100':list(qclosure),
   'logdet_weights':{'singleton':1.0,'pair':-0.5,'triple':1.0/3.0},
   'effective_sector_weight':'1/2 graviton - ghost',
   'free_routing':'G0(p+Q_before_insertion)',
   'allowed_loop_maps':'p_old = sigma*p_canonical - s0, sigma in {+1,-1}, with s0 a routed denominator shift',
   'family_skeleton':'1 singleton + 3 bubbles + 1 signed-affine triangle'
 },
 'checks':{
   'kernel_polynomial_degree_bound':2,'kernel_holdout_max_relative_error':kernel_max,
   'kernel_threshold':KERNEL_THR,'kernel_reconstruction_pass':kernel_ok,
   'free_numerator_const_relative_error_H':free_const_err_H,'free_numerator_const_relative_error_N':free_const_err_N,
   'free_numerator_const_threshold':FREE_THR,'free_numerator_const_pass':free_ok,
   'sequence_count':len(SEQS),'canonical_family_count':len(groups),'family_route_counts_sorted':family_counts,
   'family_structure_pass':family_structure_ok,'all_family_polynomial_heldout_pass':family_ok,
   'origin_classification_pass':all_origins_ok
 },
 'families':family_results,
 'physical_status':{
   'physical_common_background_cubic_determinant_integrand':'CANONICAL_FAMILY_NUMERATORS_FROZEN_IF_PASS',
   'singleton_origin':'SCALELESS_LOCAL_DR_ZERO_CUT_TOPOLOGY_IF_PASS',
   'bubble_triangle_origins':'CUT_CAPABLE_TOPOLOGY_ONLY_NOT_NONZERO_CUT',
   'scoped_DR_timelike_cut_reduction':'ALLOWED_NEXT_IF_PASS_SUBJECT_TO_ITERATION297_REGULATOR_WARNING',
   'source_born_subtraction':'FORBIDDEN_UNTIL_MATCHED_OBSERVABLE_ORIGIN_CLASSIFICATION_COMPLETE',
   'comparator_subtracted_residual':'ABSENT'
 },
 'guardrails':['UNSUPPORTED_IS_BLOCKED_NOT_ZERO_FILLED','DENOMINATOR_EQUIVALENCE_NOT_NUMERATOR_EQUIVALENCE_HENCE_EXPLICIT_TRANSFORMED_NUMERATOR_FIT','CUT_CAPABLE_TOPOLOGY_IS_NOT_NONZERO_DISCONTINUITY','ITERATION297_EVANESCENT_REGULATOR_WARNING_BINDING','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_HEAVY_FULL_C5'],
 'next_gate':('perform scoped DR/direct-timelike discontinuity reduction of the three canonical bubbles and one canonical triangle using these frozen numerator polynomials, preserving Iteration-297 evanescent/regulator caveat and classifying pole/cut origin before any matched-observable subtraction' if ok else 'preserve FAIL diagnostics and repair only the failed numerator transformation/reconstruction prerequisite without threshold weakening or zero-fill')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not ok: raise SystemExit(2)
