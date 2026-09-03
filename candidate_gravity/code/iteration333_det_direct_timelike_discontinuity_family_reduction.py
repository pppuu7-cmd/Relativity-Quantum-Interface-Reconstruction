#!/usr/bin/env python3
"""RQIR Iteration 333: direct-timelike determinant discontinuity family reduction.

Consumes only frozen authority from Iterations 312/324/329/331/332.  The exact
Iteration-332 closed timelike triad is used without changing parent dynamics,
logdet weights, shifted routing, signed-affine maps, or H/N conventions.

The gate first proves that the free H0/N0 factors can be stripped analytically
from the physical integrand under the canonical denominator convention.  It then
reduces each of the three canonical bubble families on its exact massless two-line
Cutkosky surface.  For the one signed-affine triangle family it analyzes all three
two-line channels, proves whether the uncut third propagator can hit zero on the
cut sphere, and, when bounded away from zero, evaluates the cut proxy with two
independent deterministic spherical cubatures.

The output is only a family-level zero/nonzero/BLOCKED discontinuity certificate.
It does not perform Source/Born subtraction, claim a full finite DR remainder,
construct ANSATZ-003, or run Fisher/resources.  Iteration-297 scheme/evanescent
warning remains binding for finite-remainder claims.
"""
from __future__ import annotations
import contextlib, io, itertools, json, math
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
ETA=np.diag([-1.,1.,1.,1.])
TIMELIKE_QINT=[(100,0,0,0),(-40,10,10,0),(-60,-10,-10,0)]

# Load only the frozen Iteration-330 definitions, specialized to the certified
# Iteration-332 exact timelike triad.  Stop before Iteration-330 executes its gate.
src=(ROOT/'iteration330_det_physical_numerator_family_canonicalization.py').read_text()
old="QINT=[(27,-19,31,11),(-13,37,17,-29),(-14,-18,-48,18)]"
new="QINT=[(100,0,0,0),(-40,10,10,0),(-60,-10,-10,0)]"
if src.count(old)!=1:
    raise RuntimeError('Iteration-330 QINT authority signature changed; refuse implicit rebase')
src=src.replace(old,new,1)
prefix=src.split('# Structural census and explicit maps.',1)
if len(prefix)!=2:
    raise RuntimeError('Iteration-330 structural-census boundary changed')
ns={'__name__':'iteration333_frozen_parent','__file__':str(ROOT/'iteration330_det_physical_numerator_family_canonicalization.py')}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(prefix[0],'iteration333_frozen_parent','exec'),ns,ns)

# Frozen definitions.
topology=ns['topology']; shifts_for=ns['shifts_for']; representative_for=ns['representative_for']
topology_weight=ns['topology_weight']; transformed_p=ns['transformed_p']; physical_integrand=ns['physical_integrand']
denom_product=ns['denom_product']; parent_at=ns['parent_at']; ZERO=ns['ZERO']; denom=ns['denom']


def mdot(a,b):
    return float(np.real_if_close(np.asarray(a,float)@ETA@np.asarray(b,float)))


def stripped_sector_numerator(seq,p,sector):
    """Numerator relative to prod[(p+s)^2], including K0 sign convention.

    Frozen flat identities are H0=+p^2 I_10 and N0=-p^2 I_4.  Therefore a
    ghost m-insertion trace carries (-1)^m when expressed over the positive
    scalar denominator product used by Iteration 330.
    """
    prod=None
    for a,s in zip(seq,shifts_for(seq)):
        kin=np.asarray(p,float)+np.asarray(s,float)/100.0
        g,N=parent_at(kin)
        K=g['H'] if sector=='H' else N
        block=K[a]
        prod=block if prod is None else prod@block
    return np.trace(prod)


def stripped_physical_numerator(seq,p):
    m=len(seq); w=topology_weight(seq)
    h=stripped_sector_numerator(seq,p,'H')
    n=stripped_sector_numerator(seq,p,'N')
    return w*(0.5*h-((-1)**m)*n)

# Build exact canonical records.
records=[]
for seq in topology():
    rep,sigma,C=representative_for(seq)
    records.append({'seq':seq,'rep':rep,'sigma':sigma,'C':C})

# Independent denominator-stripping validation against the original integrand.
strip_points=[np.array([.43,-.57,.36,.71]),np.array([.77,.28,-.41,.63])]
strip_err=0.0
for r in records:
    for k in strip_points:
        p=transformed_p(k,r['sigma'],r['C'])
        lhs=stripped_physical_numerator(r['seq'],p)
        rhs=physical_integrand(r['seq'],p)*denom_product(k,r['rep'])
        strip_err=max(strip_err,float(abs(lhs-rhs)/max(1.0,abs(lhs),abs(rhs))))

# Explicit flat free-operator sign checks at a held-out non-null momentum.
testp=np.array([.83,-.27,.31,.49])
g0,n0=parent_at(testp); p2=denom(testp)
flat_H0_err=float(np.max(np.abs(g0['H'][ZERO]-p2*np.eye(g0['H'][ZERO].shape[0]))))
flat_N0_err=float(np.max(np.abs(n0[ZERO]+p2*np.eye(n0[ZERO].shape[0]))))

# Group canonical families.  Each family numerator is the sum of its route-specific
# transported physical numerators; denominator equivalence never identifies them.
def keyrep(rep): return tuple(tuple(int(x) for x in s) for s in rep)
bubble_groups={}; triangle_groups={}
for r in records:
    if len(r['seq'])==2: bubble_groups.setdefault(keyrep(r['rep']),[]).append(r)
    elif len(r['seq'])==3: triangle_groups.setdefault(keyrep(r['rep']),[]).append(r)


def family_num(group,k):
    z=0j
    for r in group:
        p=transformed_p(k,r['sigma'],r['C'])
        z+=stripped_physical_numerator(r['seq'],p)
    return z

# Minkowski-orthonormal spacelike triad perpendicular to timelike Q.
def rest_basis(Q):
    Q=np.asarray(Q,float); M=math.sqrt(-mdot(Q,Q)); u=Q/M
    basis=[]
    candidates=[np.array([0.,1.,0.,0.]),np.array([0.,0.,1.,0.]),np.array([0.,0.,0.,1.]),np.array([1.,0.,0.,0.])]
    for v0 in candidates:
        v=v0+mdot(v0,u)*u
        for e in basis: v=v-mdot(v,e)*e
        n2=mdot(v,v)
        if n2>1e-12:
            basis.append(v/math.sqrt(n2))
        if len(basis)==3: break
    if len(basis)!=3: raise RuntimeError('failed timelike rest-basis construction')
    gram=np.array([[mdot(a,b) for b in basis] for a in basis])
    if np.max(np.abs(gram-np.eye(3)))>2e-12: raise RuntimeError(('bad rest basis',gram))
    return M,u,basis

# Normalized Lebedev-type cubatures.  14-point rule is degree-5; 26-point rule
# is degree-7.  Their normalized weights each sum to one.
def sphere14(basis):
    out=[]
    for i in range(3):
        for s in (-1.,1.): out.append((s*basis[i],1/15))
    for sg in itertools.product((-1.,1.),repeat=3):
        n=sum((sg[i]*basis[i] for i in range(3)),np.zeros(4))/math.sqrt(3)
        out.append((n,3/40))
    return out

def sphere26(basis):
    out=[]
    for i in range(3):
        for s in (-1.,1.): out.append((s*basis[i],1/21))
    for i,j in itertools.combinations(range(3),2):
        for si,sj in itertools.product((-1.,1.),repeat=2):
            out.append(((si*basis[i]+sj*basis[j])/math.sqrt(2),4/105))
    for sg in itertools.product((-1.,1.),repeat=3):
        n=sum((sg[i]*basis[i] for i in range(3)),np.zeros(4))/math.sqrt(3)
        out.append((n,9/280))
    return out

def rotated_basis(basis):
    # Fixed proper Euclidean rotation acting inside Q^perp; no data fitting.
    A=np.array([[1.,2.,3.],[-2.,1.,1.],[1.,-3.,2.]])
    q,_=np.linalg.qr(A)
    if np.linalg.det(q)<0: q[:,0]*=-1
    return [sum((q[j,i]*basis[j] for j in range(3)),np.zeros(4)) for i in range(3)]


def cut_k(rep,i,j,n):
    shifts=[np.asarray(s,float)/100.0 for s in rep]
    si,sj=shifts[i],shifts[j]; Q=sj-si
    M,_,_=rest_basis(Q)
    l=-0.5*Q+0.5*M*n
    return l-si

# Classification thresholds are frozen before looking at the outputs.
STRIP_TOL=2e-8
CUBATURE_AGREE=2e-5
NONZERO_RATIO=2e-6
ZERO_SAMPLE_RATIO=2e-10
THIRD_POLE_MARGIN=2e-9

bubble_results=[]
for rep,group in sorted(bubble_groups.items()):
    if len(rep)!=2: raise AssertionError(rep)
    s0=np.asarray(rep[0],float)/100.; s1=np.asarray(rep[1],float)/100.; Q=s1-s0
    q2=mdot(Q,Q)
    if not q2 < -1e-12:
        bubble_results.append({'rep_int100':[list(x) for x in rep],'status':'BLOCKED_NON_TIMELIKE_CHANNEL','q2':q2})
        continue
    M,u,basis=rest_basis(Q)
    designs=[sphere14(basis),sphere14(rotated_basis(basis)),sphere26(basis)]
    av=[]; samplemax=0.0
    for design in designs:
        z=0j
        for n,w in design:
            k=cut_k(rep,0,1,n); val=family_num(group,k); z+=w*val; samplemax=max(samplemax,float(abs(val)))
        av.append(z)
    central=av[2]
    agree=max(abs(av[0]-central),abs(av[1]-central))/max(samplemax,1e-30)
    ratio=abs(central)/max(samplemax,1e-30)
    if samplemax < 1e-20 or (ratio<ZERO_SAMPLE_RATIO and agree<CUBATURE_AGREE): status='ZERO_NUMERATOR_ON_CUT_CERTIFICATE'
    elif ratio>NONZERO_RATIO and agree<CUBATURE_AGREE: status='NONZERO_TWO_PARTICLE_DISCONTINUITY_CERTIFICATE'
    else: status='BLOCKED_NEAR_CANCELLATION_OR_CUBATURE_CONVERGENCE'
    bubble_results.append({'rep_int100':[list(x) for x in rep],'route_count':len(group),'q2':q2,'mass':M,
        'cut_proxy_degree5_base':[float(np.real(av[0])),float(np.imag(av[0]))],
        'cut_proxy_degree5_rotated':[float(np.real(av[1])),float(np.imag(av[1]))],
        'cut_proxy_degree7':[float(np.real(central)),float(np.imag(central))],
        'max_abs_sample':samplemax,'central_to_sample_ratio':float(ratio),'cubature_disagreement_to_sample':float(agree),'status':status})

triangle_results=[]
if len(triangle_groups)!=1:
    raise RuntimeError(f'expected one signed-affine triangle family, got {len(triangle_groups)}')
for rep,group in triangle_groups.items():
    shifts=[np.asarray(s,float)/100.0 for s in rep]
    channels=[]
    for i,j in itertools.combinations(range(3),2):
        kidx=({0,1,2}-{i,j}).pop(); si,sj,sk=shifts[i],shifts[j],shifts[kidx]
        Q=sj-si; q2=mdot(Q,Q)
        if q2>=-1e-12:
            channels.append({'cut_pair':[i,j],'status':'BLOCKED_NON_TIMELIKE_CHANNEL','q2':q2}); continue
        M,u,basis=rest_basis(Q)
        R=sk-si; A=R-0.5*Q; Aperp=A+mdot(A,u)*u
        const=mdot(A,A)+M*M/4; amp=M*math.sqrt(max(0.0,mdot(Aperp,Aperp)))
        dmin=const-amp; dmax=const+amp
        third_hits=(dmin<=THIRD_POLE_MARGIN and dmax>=-THIRD_POLE_MARGIN)
        rec={'cut_pair':[i,j],'uncut_index':kidx,'q2':q2,'third_denominator_range':[float(dmin),float(dmax)],'third_propagator_hits_zero_on_cut':bool(third_hits)}
        if third_hits:
            rec['status']='BLOCKED_DR_OVERLAPPING_CUT_THIRD_PROPAGATOR_ON_SHELL'; channels.append(rec); continue
        vals=[]; samplemax=0.0
        for bset in (basis,rotated_basis(basis)):
            z=0j
            for n,w in sphere26(bset):
                kk=cut_k(rep,i,j,n); third=denom(kk+sk)
                val=family_num(group,kk)/third
                z+=w*val; samplemax=max(samplemax,float(abs(val)))
            vals.append(z)
        central=0.5*(vals[0]+vals[1]); agree=abs(vals[0]-vals[1])/max(samplemax,1e-30); ratio=abs(central)/max(samplemax,1e-30)
        rec.update({'cut_proxy_degree7_base':[float(np.real(vals[0])),float(np.imag(vals[0]))],
                    'cut_proxy_degree7_rotated':[float(np.real(vals[1])),float(np.imag(vals[1]))],
                    'max_abs_sample':samplemax,'central_to_sample_ratio':float(ratio),'cubature_disagreement_to_sample':float(agree)})
        if samplemax<1e-20 or (ratio<ZERO_SAMPLE_RATIO and agree<CUBATURE_AGREE): rec['status']='ZERO_TWO_PARTICLE_CHANNEL_DISCONTINUITY_CERTIFICATE'
        elif ratio>NONZERO_RATIO and agree<CUBATURE_AGREE: rec['status']='NONZERO_TWO_PARTICLE_CHANNEL_DISCONTINUITY_CERTIFICATE'
        else: rec['status']='BLOCKED_NEAR_CANCELLATION_OR_CUBATURE_CONVERGENCE'
        channels.append(rec)
    statuses=[c['status'] for c in channels]
    if any(s.startswith('NONZERO_') for s in statuses): family_status='NONZERO_DISCONTINUITY_CERTIFICATE'
    elif all(s.startswith('ZERO_') for s in statuses): family_status='ZERO_DISCONTINUITY_CERTIFICATE'
    else: family_status='BLOCKED_CHANNEL_REDUCTION_INCOMPLETE'
    triangle_results.append({'rep_int100':[list(x) for x in rep],'route_count':len(group),'channels':channels,'status':family_status})

all_bubble_resolved=all(x['status'] in ('NONZERO_TWO_PARTICLE_DISCONTINUITY_CERTIFICATE','ZERO_NUMERATOR_ON_CUT_CERTIFICATE') for x in bubble_results)
triangle_resolved=all(x['status'] in ('NONZERO_DISCONTINUITY_CERTIFICATE','ZERO_DISCONTINUITY_CERTIFICATE') for x in triangle_results)
structural_ok=(len(records)==13 and len(bubble_groups)==3 and len(triangle_groups)==1 and flat_H0_err<1e-10 and flat_N0_err<1e-10 and strip_err<STRIP_TOL)
scientific_ok=bool(structural_ok and all_bubble_resolved and triangle_resolved)

result={
 'iteration':333,'model_readiness_percent':24,'scientific_gate_pass':scientific_ok,
 'classification':('PASS_DIRECT_TIMELIKE_DETERMINANT_DISCONTINUITY_FAMILY_REDUCTION' if scientific_ok else 'BLOCKED_DIRECT_TIMELIKE_DETERMINANT_DISCONTINUITY_FAMILY_REDUCTION'),
 'candidate_residual':False,
 'scope':{'fixture':'Iteration-332 exact rank-2 closed triad','signature':'(-,+,+,+)','QINT_int100':[list(x) for x in TIMELIKE_QINT],
          'physical_combination':'logdet weight * (1/2 Tr_H - Tr_N)','canonical_families':'3 bubbles + 1 signed-affine triangle',
          'discontinuity_method':'massless two-line Cutkosky surface; normalized angular proxy; universal nonzero phase-space prefactor omitted because only zero/nonzero/BLOCKED is classified'},
 'denominator_stripping_validation':{'max_scaled_error':strip_err,'threshold':STRIP_TOL,'flat_H0_identity_error':flat_H0_err,'flat_N0_minus_identity_error':flat_N0_err},
 'thresholds':{'cubature_disagreement_to_sample':CUBATURE_AGREE,'nonzero_central_to_sample_ratio':NONZERO_RATIO,'zero_ratio':ZERO_SAMPLE_RATIO,'third_pole_margin':THIRD_POLE_MARGIN},
 'bubble_families':bubble_results,'triangle_family':triangle_results,
 'physical_status':{'determinant_family_discontinuities':('FROZEN_IF_PASS' if scientific_ok else 'BLOCKED_WITH_TYPED_FAMILY_DIAGNOSTICS'),
                    'integrated_normalized_determinant_cut':'NEXT_ONLY_IF_THIS_GATE_PASSES','full_finite_DR_remainder':'BLOCKED_BY_ITERATION297_EVANESCENT_SCHEME_AUTHORITY',
                    'source_born_subtraction':'FORBIDDEN_UNTIL_MATCHED_ORIGIN_CLASSIFICATION_COMPLETES','comparator_subtracted_residual':'ABSENT'},
 'guardrails':['DENOMINATOR_EQUIVALENCE_NOT_NUMERATOR_EQUIVALENCE','CUT_CAPABLE_TOPOLOGY_NOT_ASSUMED_NONZERO','ZERO_NONZERO_BLOCKED_TYPED_SEPARATELY','ITERATION297_EVANESCENT_SCHEME_BLOCKER_REMAINS','NO_SOURCE_BORN_SUBTRACTION_YET','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_HEAVY_FULL_C5'],
 'next_gate':('assemble the frozen family discontinuities into the normalized determinant e=0,c<=3 cut, preserving family provenance and regulator scope; then perform pole/cut-origin classification before any matched Source/Born subtraction' if scientific_ok else 'preserve typed BLOCKED result and resolve only the explicitly blocked family/channel without weakening frozen parent dynamics or thresholds')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not scientific_ok: raise SystemExit(2)
