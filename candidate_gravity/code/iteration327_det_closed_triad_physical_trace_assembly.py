#!/usr/bin/env python3
"""RQIR Iteration 327: closed-triad physical cubic determinant trace assembly.

Scientific contract
-------------------
The determinant trace must use one and the same closed Fourier triad in both
(i) successive free-propagator shifts and (ii) the physical H/N insertion
kernels.  Iteration 326 certified arbitrary incoming p+Q evaluation of the
frozen kernels, but its independent source fixtures retain their original
non-collinear q modes.  This gate therefore specializes the *same frozen parent
kernels* to the exact Iteration-324 closed triad, re-validates the instantiated
H/N coefficients against their exact-geometry direct oracles with the unchanged
Iteration-326 h/thresholds, and only then assembles

  Tr(G0 K3)
  - 1/2 sum_{a+b=111} Tr(G0 K_a G0 K_b)
  + 1/3 sum_{a+b+c=111} Tr(G0 K_a G0 K_b G0 K_c)

with G0 evaluated at each successive p+Q shift.  Graviton/ghost combination is
1/2 Gamma_H - Gamma_N.  No integration, Source/Born subtraction, comparator
subtraction, zero filling, Fisher/resource inference, or ANSATZ promotion is
performed here.
"""
from __future__ import annotations
import contextlib, io, itertools, json, math, re
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
D=4; TARGET=(1,1,1); ZERO=(0,0,0)
ETA=np.diag([-1.,1.,1.,1.])
QINT=[(27,-19,31,11),(-13,37,17,-29),(-14,-18,-48,18)]
QMODES=[np.array(q,float)/100.0 for q in QINT]
P=np.array([.61,-.33,.24,.52],float)


def add(a,b): return tuple(x+y for x,y in zip(a,b))
def qint(a): return tuple(sum(a[r]*QINT[r][mu] for r in range(3)) for mu in range(D))
def qvec(a): return np.array(qint(a),float)/100.0
def deg(a): return sum(a)

def nonzero_subindices(target):
    return [a for a in itertools.product(*(range(x+1) for x in target)) if any(a)]
NZ=nonzero_subindices(TARGET)

def singleton(): return [(TARGET,)]
def ordered_pairs(): return [(a,b) for a in NZ for b in NZ if add(a,b)==TARGET]
def ordered_triples():
    return [(a,b,c) for a in NZ for b in NZ for c in NZ if add(add(a,b),c)==TARGET]
def topology_sequences(): return singleton()+ordered_pairs()+ordered_triples()

def route(seq):
    shift=(0,0,0,0); rows=[]
    for a in seq:
        rows.append((shift,a))
        qa=qint(a); shift=tuple(shift[i]+qa[i] for i in range(D))
    return rows,shift


def load_closed_triad_prefix(filename:str, marker:str, p_in:np.ndarray):
    """Execute frozen kernel construction after changing fixture q and incoming p only."""
    src=(ROOT/filename).read_text().split(marker,1)[0]
    pattern=r'qs=\[.*?\]\np=np\.array\([^\n]+\)'
    replacement='qs=[np.array(x,float) for x in QMODES]\np=P_IN.copy()'
    src,n=re.subn(pattern,replacement,src,count=1,flags=re.S)
    if n!=1: raise RuntimeError(f'failed q/p fixture specialization in {filename}: {n}')
    ns={'QMODES':[x.copy() for x in QMODES],'P_IN':np.array(p_in,float)}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(src,filename,'exec'),ns,ns)
    return ns


def mixed_coeff_from_direct(direct,a,h):
    active=[r for r,x in enumerate(a) if x]
    if any(x not in (0,1) for x in a) or not active: raise ValueError(a)
    acc=None
    for signs in itertools.product((-1.0,1.0),repeat=len(active)):
        t=np.zeros(3,float); w=1.0
        for r,s in zip(active,signs): t[r]=s*h; w*=s
        v=np.asarray(direct(t))
        acc=w*v if acc is None else acc+w*v
    return acc/((2*h)**len(active))


def request_inventory():
    req=set(); routes=[]
    for seq in topology_sequences():
        rr,total=route(seq)
        if total!=(0,0,0,0): raise AssertionError((seq,total))
        routes.append((seq,rr)); req.update(rr)
    return sorted(req),routes
REQUESTS,ROUTES=request_inventory()


def validate_and_cache(kind,filename,marker,dict_name,h,thresholds):
    by_shift={}
    for shift,a in REQUESTS: by_shift.setdefault(shift,[]).append(a)
    cache={}; rows=[]; max_by_order={1:0.,2:0.,3:0.}; counts={1:0,2:0,3:0}
    for shift,targets in sorted(by_shift.items()):
        p_in=P+np.array(shift,float)/100.0
        ns=load_closed_triad_prefix(filename,marker,p_in)
        coeffs=ns[dict_name]; direct=ns['direct']; cache[shift]=coeffs
        for a in sorted(set(targets)):
            order=deg(a); counts[order]+=1
            fd=mixed_coeff_from_direct(direct,a,h)
            err=float(np.max(np.abs(fd-coeffs[a])))
            scale=max(1.0,float(np.max(np.abs(coeffs[a]))))
            rel=err/scale; max_by_order[order]=max(max_by_order[order],rel)
            rows.append({'shift_int100':list(shift),'multiindex':list(a),'order':order,
                         'scaled_error':rel,'max_abs_error':err,'scale':scale})
    ok=all(counts[k]>0 and max_by_order[k]<thresholds[k] for k in (1,2,3))
    return cache,{
        'kind':kind,'request_count':len(rows),'request_count_by_order':{str(k):counts[k] for k in counts},
        'finite_difference_h':h,'max_scaled_error_by_order':{str(k):v for k,v in max_by_order.items()},
        'threshold_by_order':{str(k):thresholds[k] for k in thresholds},'requests':rows,'pass':bool(ok)}

# Same h and thresholds as Iteration 326; no post-hoc weakening.
ghost_cache,ghost_val=validate_and_cache(
    'ghost','iteration317_det_ghost_three_mode_routing.py','# Multivariate direct fit.','N',
    2.0e-4,{1:2e-6,2:3e-4,3:8e-2})
grav_cache,grav_val=validate_and_cache(
    'graviton','iteration319_det_graviton_three_mode_routing.py','FIT=indices(4)','H',
    2.0e-4,{1:3e-6,2:5e-4,3:1.2e-1})


def translated_family_canonical(shifts):
    candidates=[]
    for origin in shifts:
        rel=sorted(tuple(s[i]-origin[i] for i in range(D)) for s in shifts)
        candidates.append(tuple(rel))
    return min(candidates)


def sector_trace(cache,seq):
    rr,total=route(seq)
    if total!=(0,0,0,0): raise AssertionError(total)
    prod=None; shifts=[]
    for shift,a in rr:
        coeffs=cache[shift]
        G0=np.linalg.inv(np.asarray(coeffs[ZERO],complex))
        K=np.asarray(coeffs[a],complex)
        A=G0@K
        prod=A if prod is None else prod@A
        shifts.append(shift)
    return complex(np.trace(prod)),tuple(shifts)


def cjson(z): return {'re':float(np.real(z)),'im':float(np.imag(z)),'abs':float(abs(z))}

def weight(seq): return 1.0 if len(seq)==1 else (-0.5 if len(seq)==2 else 1.0/3.0)

rows=[]; GH=0j; GN=0j
for seq in topology_sequences():
    th,sh=sector_trace(grav_cache,seq); tn,shn=sector_trace(ghost_cache,seq)
    assert sh==shn
    w=weight(seq); GH+=w*th; GN+=w*tn
    fam=translated_family_canonical(sh)
    rows.append({'sequence':[list(a) for a in seq],'topology_order':len(seq),'weight':w,
                 'propagator_shift_int100':[list(s) for s in sh],
                 'canonical_denominator_family_int100':[list(s) for s in fam],
                 'graviton_trace':cjson(th),'ghost_trace':cjson(tn),
                 'effective_weighted_contribution':cjson(w*(0.5*th-tn))})
GEFF=0.5*GH-GN

# Family census and cut-origin classification.  This is structural classification,
# not an integrated discontinuity claim.
families={}
for r in rows:
    key=tuple(tuple(x) for x in r['canonical_denominator_family_int100'])
    families.setdefault(key,[]).append(r)
family_rows=[]
for fam,fr in sorted(families.items(),key=lambda kv:(len(kv[0]),kv[0])):
    n=len(fam)
    if n==1:
        origin='MASSLESS_ONE_PROPAGATOR_TADPOLE_SCALELESS_IN_DR'
        cut_capable=False; fixture_timelike=False; invariants=[]
    elif n==2:
        delta=np.array(fam[1],float)/100.0-np.array(fam[0],float)/100.0
        q2=float(delta@ETA@delta); s=-q2
        origin='NONLOCAL_BUBBLE_CUT_CAPABLE_UNDER_TIMELIKE_CONTINUATION'
        cut_capable=True; fixture_timelike=(s>0); invariants=[{'q2':q2,'s_minus_q2':s}]
    elif n==3:
        origin='NONLOCAL_TRIANGLE_CUT_CAPABLE_UNDER_TIMELIKE_CONTINUATION'
        cut_capable=True; invariants=[]; fixture_timelike=False
        for i,j in itertools.combinations(range(3),2):
            d=np.array(fam[j],float)/100.0-np.array(fam[i],float)/100.0
            q2=float(d@ETA@d); s=-q2; fixture_timelike=fixture_timelike or s>0
            invariants.append({'pair':[i,j],'q2':q2,'s_minus_q2':s})
    else:
        origin='BLOCKED_UNSUPPORTED_DENOMINATOR_CARDINALITY'; cut_capable=False; fixture_timelike=False; invariants=[]
    family_rows.append({'propagator_count':n,'canonical_shifts_int100':[list(x) for x in fam],
                        'term_count':len(fr),'origin_classification':origin,
                        'cut_capable_under_analytic_continuation':cut_capable,
                        'timelike_at_current_fixture':fixture_timelike,'invariants':invariants})

qclosure=tuple(sum(QINT[r][mu] for r in range(3)) for mu in range(D))
qrank=int(np.linalg.matrix_rank(np.array(QINT,float),tol=1e-12))
finite_trace=all(math.isfinite(x) for z in (GH,GN,GEFF) for x in (z.real,z.imag))
# Closed triad gives exactly one tadpole family, three bubble families and one triangle family.
family_cardinality=(sum(f['propagator_count']==1 for f in family_rows)==1 and
                    sum(f['propagator_count']==2 for f in family_rows)==3 and
                    sum(f['propagator_count']==3 for f in family_rows)==1)
all_supported=all('BLOCKED_' not in f['origin_classification'] for f in family_rows)
ok=bool(qclosure==(0,0,0,0) and qrank==2 and ghost_val['pass'] and grav_val['pass'] and
        len(singleton())==1 and len(ordered_pairs())==6 and len(ordered_triples())==6 and
        len(REQUESTS)==19 and finite_trace and family_cardinality and all_supported)

result={
 'iteration':327,'model_readiness_percent':24,'scientific_gate_pass':ok,
 'classification':('PASS_CLOSED_TRIAD_PHYSICAL_CUBIC_DETERMINANT_TRACE_ASSEMBLY_AND_ORIGIN_CLASSIFICATION' if ok else
                   'FAIL_CLOSED_TRIAD_PHYSICAL_CUBIC_DETERMINANT_TRACE_ASSEMBLY_AND_ORIGIN_CLASSIFICATION'),
 'candidate_residual':False,
 'scope':{'target_multiindex':list(TARGET),'closed_triad_q_int100':[list(x) for x in QINT],
          'q_total_int100':list(qclosure),'q_rank':qrank,'topology_counts':{'singleton':1,'pairs':6,'triples':6},
          'unique_routed_insertion_requests':len(REQUESTS),
          'kernel_specialization':'same frozen Iteration-317/319 parent kernels; q fixture specialized to exact Iteration-324 closed triad; incoming p routed successively'},
 'closed_triad_exact_geometry_revalidation':{'ghost':ghost_val,'graviton':grav_val},
 'assembled_trace':{'graviton_logdet_cubic':cjson(GH),'ghost_logdet_cubic':cjson(GN),
                    'effective_half_graviton_minus_ghost':cjson(GEFF)},
 'denominator_family_census':family_rows,'routed_terms':rows,
 'checks':{'trace_closure':qclosure==(0,0,0,0),'closed_triad_rank_two':qrank==2,
           'full_cubic_topology_13_sequences':len(topology_sequences())==13,
           'unique_request_count_19':len(REQUESTS)==19,'finite_assembled_trace':finite_trace,
           'expected_family_cardinality_1_tadpole_3_bubble_1_triangle':family_cardinality,
           'all_family_origins_supported':all_supported},
 'physical_status':{'physical_cubic_determinant_loop_integrand':'FROZEN_IF_PASS',
                    'denominator_family_origin_classification':'FROZEN_IF_PASS',
                    'integrated_normalized_timelike_cut':'OPEN_NEXT_GATE',
                    'comparator_subtracted_residual':'ABSENT',
                    'source_born_subtraction':'FORBIDDEN_UNTIL_MATCHED_OBSERVABLE_AFTER_ORIGIN_CLASSIFICATION'},
 'guardrails':['UNSUPPORTED_IS_BLOCKED_NOT_ZERO_FILLED','NO_THRESHOLD_WEAKENING','NO_SOURCE_BORN_SUBTRACTION_IN_THIS_GATE',
               'NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_HEAVY_FULL_C5','NO_INTEGRATED_CUT_CLAIM_FROM_FIXTURE_TRACE'],
 'next_gate':('reduce the three bubble plus one triangle cut-capable determinant families in DR with explicit retarded/advanced continuation and compute the normalized determinant timelike discontinuity; preserve the tadpole as scaleless and do not Source/Born subtract before matched-observable assembly' if ok else
              'preserve scoped FAIL; diagnose closed-triad H/N specialization or trace/family assembly without changing frozen parent kernels or thresholds')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not ok: raise SystemExit(2)

# Trigger-only marker: scientific contract above is unchanged.
