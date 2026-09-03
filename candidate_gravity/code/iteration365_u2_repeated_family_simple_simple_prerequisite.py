#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 365.

Independent prerequisite for the 18 timelike simple-simple cuts inside repeated
(2,1,1) U2 families.  These cuts do NOT pass through the unique double-pole
group; the double pole remains uncut.

This gate:
1) identifies exactly the ordinary-simple distinct-group channels inside the
   Iteration-359 repeated-family census;
2) analytically certifies the uncut double-pole squared momentum stays away from
   zero over the complete massless two-particle cut sphere;
3) validates the direct uncut repeated factor against the auxiliary-mass identity
       (s1*s2)/D^2 = -(s1*s2) d/d(mu2)[1/(D+mu2)]|0
   on deterministic on-shell angular fixtures.

No physical cut integral is evaluated here.  It is independent of the active
Iteration-364 cut-through-double-pole integration.
"""
from __future__ import annotations
import contextlib, io, json, math, runpy
from pathlib import Path
import numpy as np

ITERATION=365
ROOT=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    P359=runpy.run_path(str(ROOT/'iteration359_u2_repeated_pole_derivative_contract.py'),run_name='iteration365_parent359')

if not P359['result']['scientific_gate_pass']:
    raise RuntimeError('iteration359_parent_not_authoritative')
mdot=P359['mdot']
SEP_TOL=1e-10
FACTOR_TOL=1e-8
FD_H=1e-5


def mbilin(a,b):
    a=np.asarray(a,float); b=np.asarray(b,float)
    return float(-a[0]*b[0]+np.dot(a[1:],b[1:]))


def sq(a):
    return mbilin(a,a)


def species_sign(sp):
    if sp=='ghost': return -1.0
    if sp=='graviton': return 1.0
    raise ValueError(sp)


def full_sphere_massless_uncut_range(a,b,c):
    # Cut momenta p1=k+a, p2=k+b=p1+q satisfy p1^2=p2^2=0.
    q=np.asarray(b,float)-np.asarray(a,float); q2=sq(q)
    if q2>=-2e-12:
        return None
    alpha=-0.5
    rho2=-alpha*alpha*q2
    rho=math.sqrt(max(0.0,rho2))
    r=alpha*q+(np.asarray(c,float)-np.asarray(a,float))
    rperp=r-q*(mbilin(r,q)/q2)
    rp2=sq(rperp)
    if rp2 < -2e-12:
        return None
    amp=2.0*rho*math.sqrt(max(0.0,rp2))
    center=sq(r)+rho2
    lo=center-amp; hi=center+amp
    if lo>hi: lo,hi=hi,lo
    minabs=0.0 if lo<=0.0<=hi else min(abs(lo),abs(hi))
    return {'q2':q2,'range':[lo,hi],'min_abs':minabs,'rho2':rho2}


def transverse_basis(q):
    q=np.asarray(q,float); q2=sq(q)
    seeds=[np.array([0.,1.,0.,0.]),np.array([0.,0.,1.,0.]),np.array([0.,0.,0.,1.]),np.array([1.,0.,0.,0.]),np.array([1.,1.,0.,0.])]
    out=[]
    for seed in seeds:
        v=seed-q*(mbilin(seed,q)/q2)
        for e in out: v=v-mbilin(v,e)*e
        n2=sq(v)
        if n2>1e-12: out.append(v/math.sqrt(n2))
        if len(out)==3: break
    if len(out)!=3: raise RuntimeError('transverse_basis_failure')
    return out


def central4_derivative(fun,h):
    return (fun(-2*h)-8.0*fun(-h)+8.0*fun(h)-fun(2*h))/(12.0*h)


records=[]; max_factor_err=0.0; min_sep=float('inf'); blocked=0
for fam in P359['result']['families']:
    groups=fam['groups']
    if sorted(int(g['multiplicity']) for g in groups)!=[1,1,2]:
        continue
    repeated=[i for i,g in enumerate(groups) if int(g['multiplicity'])==2]
    if len(repeated)!=1: raise RuntimeError(('bad_repeated_group_count',fam['route'],fam['subterm']))
    rg=repeated[0]
    for ch in fam['timelike_distinct_group_channels']:
        if not ch['ordinary_simple_pair']:
            continue
        ia,ib=map(int,ch['group_pair'])
        if rg in (ia,ib):
            raise RuntimeError(('ordinary_simple_channel_contains_repeated_group',fam['route'],fam['subterm'],ia,ib,rg))
        a=np.asarray(groups[ia]['offset'],float); b=np.asarray(groups[ib]['offset'],float); c=np.asarray(groups[rg]['offset'],float)
        rr=full_sphere_massless_uncut_range(a,b,c)
        if rr is None:
            records.append({'route':fam['route'],'subterm':fam['subterm'],'group_pair':[ia,ib],'status':'BLOCKED_RANGE'})
            blocked+=1; continue
        min_sep=min(min_sep,rr['min_abs'])
        q=b-a; rho=math.sqrt(rr['rho2']); basis=transverse_basis(q)
        dirs=[basis[0],-basis[0],basis[1],-basis[1],basis[2],-basis[2],
              (basis[0]+basis[1]+basis[2])/math.sqrt(3.0)]
        sprod=1.0
        for sp in groups[rg]['species']: sprod*=species_sign(sp)
        errs=[]; samples=[]
        for unit in dirs:
            k=-a-0.5*q+rho*unit
            D=sq(k+c)
            direct=sprod/(D*D)
            aux=-sprod*central4_derivative(lambda mu: 1.0/(D+mu),FD_H)
            err=abs(direct-aux)/max(1.0,abs(direct),abs(aux))
            errs.append(err); max_factor_err=max(max_factor_err,float(err))
            samples.append({'D':D,'direct_factor':direct,'aux_factor':aux,'scaled_error':err})
        status='REGULAR' if rr['min_abs']>SEP_TOL and max(errs)<=FACTOR_TOL else 'BLOCKED_PREREQUISITE'
        if status!='REGULAR': blocked+=1
        records.append({'route':int(fam['route']),'subterm':int(fam['subterm']),'group_pair':[ia,ib],
                        'repeated_group':int(rg),'q2':float(rr['q2']),'status':status,
                        'uncut_double_pole_squared_momentum_range':rr['range'],
                        'analytic_min_abs_squared_momentum':rr['min_abs'],
                        'repeated_group_species':groups[rg]['species'],'repeated_group_algebraic_sign':sprod,
                        'max_aux_factor_scaled_error':max(errs),'factor_samples':samples})

resolved=bool(len(records)==18 and blocked==0 and min_sep>SEP_TOL and max_factor_err<=FACTOR_TOL)
classification=('PASS_U2_REPEATED_FAMILY_SIMPLE_SIMPLE_18_CHANNEL_PREREQUISITE__ALL_REGULAR'
                if resolved else 'FAIL_U2_REPEATED_FAMILY_SIMPLE_SIMPLE_PREREQUISITE')
result={'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':resolved,'candidate_residual':False,
        'classification':classification,
        'census':{'typed_simple_simple_channels_in_repeated_families':len(records),'REGULAR':len(records)-blocked,'BLOCKED':blocked,
                  'minimum_analytic_uncut_double_pole_abs_squared_momentum':min_sep,
                  'max_direct_vs_aux_repeated_factor_scaled_error':max_factor_err},
        'thresholds':{'uncut_double_pole_separation':SEP_TOL,'direct_vs_aux_factor_scaled_error':FACTOR_TOL},
        'records':records,
        'scope':'18_SIMPLE_SIMPLE_TIMELIKE_CUTS_IN_REPEATED_211_FAMILIES__PREREQUISITE_ONLY__NO_CUT_INTEGRAL',
        'guardrails':['DOUBLE_POLE_REMAINS_UNCUT','FULL_SPHERE_ANALYTIC_RANGE','DIRECT_D_MINUS2_AND_AUX_DERIVATIVE_CROSSCHECK',
                      'NO_PHYSICAL_INTEGRATION_IN_THIS_GATE','DISTINCT_Q2_NOT_SUMMED','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
        'next_gate':'if PASS, integrate these 18 massless simple-simple cuts with the direct squared uncut denominator, repeat the high-grid result using the auxiliary derivative representation, require angular and representation agreement, then combine q2-by-q2 with Iteration361 and the cut-through-double-pole sector once Iteration364 is authoritative'}
print(json.dumps(result,indent=2,sort_keys=True))
if not resolved: raise SystemExit(2)
