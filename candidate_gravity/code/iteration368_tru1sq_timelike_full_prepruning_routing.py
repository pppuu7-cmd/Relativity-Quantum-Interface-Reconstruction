#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 368.

Full pre-pruning physical routing/contraction gate for cubic Tr(U1^2) on the
current timelike common-background fixture, following Iteration 367.

The historical Iteration-308/310 42 ordered placements are reconstructed before
any pruning.  Each first-order block and each of the seven second-order
Leibniz primitives is evaluated from the same-parent U1 infrastructure

    U1 = Q_L A Q_R Y_down

with exact routed loop momenta.  The two block orientations are retained as
separate ordered rows; cyclic trace equivalence is tested only through the
required loop-momentum translation.  No cut integral is performed here.
"""
from __future__ import annotations
import contextlib, io, itertools, json
from pathlib import Path
import numpy as np

ITERATION=368
ROOT=Path(__file__).resolve().parent
PARENT=ROOT/'iteration270_vd_physical_b3_nonzero.py'
src=PARENT.read_text().split('# A-layer certificates.',1)[0]
ns={'__name__':'iteration368_parent','__file__':str(PARENT)}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src,str(PARENT),'exec'),ns,ns)

ETA=ns['ETA']; Q0=ns['Q0']; Q1=ns['Q1']; Asub=ns['Asub']; y_down=ns['y_down']

LEGS=('s','a','b')
TIMELIKE_Q=[np.array([1.,0.,0.,0.]),np.array([-.4,.1,.1,0.]),np.array([-.6,-.1,-.1,0.])]
rng=np.random.default_rng(319)
TIMELIKE_H=[]
for _ in range(3):
    x=rng.normal(size=(4,4)); TIMELIKE_H.append(0.12*(x+x.T)/2.0)
M={x:(TIMELIKE_Q[i],TIMELIKE_H[i]) for i,x in enumerate(LEGS)}
Y0=y_down([],[])

PROBES=[np.array([.43,-.27,.39,.21]),np.array([.61,.19,-.31,.47])]
ZERO_TOL=1e-11
CYCLIC_REL_TOL=3e-5
CLOSURE_TOL=1e-14


def ksum(legs):
    return sum((M[x][0] for x in legs),np.zeros(4))


def mdot(a,b):
    return float(np.real(np.asarray(a,float)@ETA@np.asarray(b,float)))


def y1(x,h=4e-5):
    mode=[M[x]]
    return (y_down([h],mode)-y_down([-h],mode))/(2*h)


def first_u1(x,p):
    q=M[x][0]
    A1=Asub(M,(x,),p,h1=1e-4)
    return Q0(p+q)@A1@Q0(p)@Y0


def second_primitive(pair,spec,p):
    """One of the seven order-2 U1 Leibniz primitives for an unordered pair."""
    pair=tuple(pair); site=spec['extra_site']
    if site=='V2':
        q=ksum(pair)
        A2=Asub(M,pair,p,h2=5e-4)
        return Q0(p+q)@A2@Q0(p)@Y0
    vleg=spec['V2_legs'][0]; dleg=spec['extra_local_legs'][0]
    qv=M[vleg][0]; qd=M[dleg][0]
    if site=='N_L':
        A1=Asub(M,(vleg,),p,h1=1e-4)
        return Q1(M,dleg,p+qv)@A1@Q0(p)@Y0
    if site=='N_R':
        A1=Asub(M,(vleg,),p+qd,h1=1e-4)
        return Q0(p+qd+qv)@A1@Q1(M,dleg,p)@Y0
    if site=='Y':
        A1=Asub(M,(vleg,),p+qd,h1=1e-4)
        return Q0(p+qd+qv)@A1@Q0(p+qd)@y1(dleg)
    raise ValueError(site)


def second_specs(pair):
    pair=tuple(pair); out=[{'extra_site':'V2','V2_legs':pair,'extra_local_legs':()}]
    for site in ('N_L','N_R','Y'):
        for vleg in pair:
            dleg=pair[1] if pair[0]==vleg else pair[0]
            out.append({'extra_site':site,'V2_legs':(vleg,), 'extra_local_legs':(dleg,)})
    assert len(out)==7
    return out

# Cache expensive same-parent blocks by routed loop momentum.
F_CACHE={}; S_CACHE={}
def pkey(p): return tuple(np.round(np.asarray(p,float),14))
def F(x,p):
    key=(x,pkey(p))
    if key not in F_CACHE: F_CACHE[key]=first_u1(x,np.asarray(p,float))
    return F_CACHE[key]
def S(pair,spec,p):
    sk=(spec['extra_site'],tuple(spec['V2_legs']),tuple(spec['extra_local_legs']))
    key=(tuple(pair),sk,pkey(p))
    if key not in S_CACHE: S_CACHE[key]=second_primitive(pair,spec,np.asarray(p,float))
    return S_CACHE[key]

rows=[]; max_closure=0.0; max_cyclic_rel=0.0
nonzero_rows=0; zero_rows=0
for singleton in LEGS:
    pair=tuple(x for x in LEGS if x!=singleton)
    qs=M[singleton][0]; qp=ksum(pair)
    closure=float(np.max(np.abs(qs+qp))); max_closure=max(max_closure,closure)
    for spec_index,spec in enumerate(second_specs(pair)):
        probe_rows=[]; row_nonzero=False
        for p in PROBES:
            # Orientation A = Tr(U_singleton U_second): second block acts first.
            amp_A=np.trace(F(singleton,p+qp)@S(pair,spec,p))
            # Orientation B = Tr(U_second U_singleton): singleton acts first.
            amp_B=np.trace(S(pair,spec,p+qs)@F(singleton,p))
            # Cyclic equivalence requires loop translation p -> p+qs:
            # A(p+qs) = Tr[F(p) S(p+qs)] = B(p) by finite-dimensional trace cyclicity.
            amp_A_shift=np.trace(F(singleton,p)@S(pair,spec,p+qs))
            scale=max(abs(amp_B),abs(amp_A_shift),1e-30)
            cyc=float(abs(amp_B-amp_A_shift)/scale)
            max_cyclic_rel=max(max_cyclic_rel,cyc)
            mag=max(abs(amp_A),abs(amp_B))
            row_nonzero=row_nonzero or bool(mag>ZERO_TOL)
            probe_rows.append({'p':p.tolist(),'orientation_A_re':float(np.real(amp_A)),'orientation_A_im':float(np.imag(amp_A)),
                               'orientation_B_re':float(np.real(amp_B)),'orientation_B_im':float(np.imag(amp_B)),
                               'cyclic_shift_relative_error':cyc,'max_abs_amplitude':float(mag)})
        if row_nonzero: nonzero_rows+=2
        else: zero_rows+=2
        base={'singleton_leg':singleton,'pair_legs':pair,'second_order_spec':spec,'spec_index':spec_index,
              'routed_momentum_closure_max_abs':closure,'physical_support':'NONZERO' if row_nonzero else 'ZERO',
              'probe_results':probe_rows}
        rows.append(dict(base,block_orientation='U1_FIRST_SINGLETON'))
        rows.append(dict(base,block_orientation='U1_SECOND_SINGLETON'))

assert len(rows)==42
assert nonzero_rows+zero_rows==42
q2=[mdot(q,q) for q in TIMELIKE_Q]
q2err=max(abs(a-b) for a,b in zip(q2,[-1.,-.14,-.34]))
all_finite=all(np.isfinite(v) for r in rows for pr in r['probe_results'] for k,v in pr.items() if k!='p')
passed=bool(max_closure<=CLOSURE_TOL and q2err<=CLOSURE_TOL and all_finite and max_cyclic_rel<=CYCLIC_REL_TOL)
classification=('PASS_TRU1SQ_TIMELIKE_FULL_42_PREPRUNING_PHYSICAL_ROUTING_AND_CYCLIC_TRANSLATION_GATE'
                if passed else 'FAIL_TRU1SQ_TIMELIKE_FULL_PREPRUNING_ROUTING_GATE')

# Cyclic quotient is permitted only after the routed equality check above.  The
# two orientations of each (singleton, second-order primitive) then form one
# cyclic class, irrespective of whether the physical amplitude happens to be zero.
cyclic_class_count=21 if passed else None
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':passed,'candidate_residual':False,
 'classification':classification,
 'scope':'FULL_42_ORDERED_TRU1SQ_CUBIC_PREPRUNING_ROUTING__NO_CUT_INTEGRAL',
 'authoritative_inputs':['Iteration 367 timelike singleton-pruning reaudit','Iteration 308 raw 42-placement combinatorics',
                         'Iteration 270 same-parent U1/Q-A-Q-Y infrastructure'],
 'fixture':{'q_squared':q2,'q_squared_target':[-1.,-.14,-.34],'q2_max_error':q2err,
            'momentum_closure_max_abs':max_closure,'metric_tensor_seed':319,'metric_tensor_scale':0.12,
            'loop_probes':[p.tolist() for p in PROBES]},
 'thresholds':{'zero_support_abs':ZERO_TOL,'cyclic_translation_relative_max':CYCLIC_REL_TOL,'closure_max':CLOSURE_TOL},
 'counts':{'raw_ordered_placements':42,'physical_nonzero_ordered_rows':nonzero_rows,'physical_zero_ordered_rows':zero_rows,
           'cyclic_classes_after_routed_translation_validation':cyclic_class_count},
 'max_cyclic_translation_relative_error':max_cyclic_rel,
 'rows':rows,
 'guardrails':['NO_HISTORICAL_SINGLETON_SOFT_PRUNING','NO_ZERO_FILL_FOR_UNSUPPORTED','CYCLIC_QUOTIENT_ONLY_AFTER_ROUTED_TRANSLATION_CHECK',
               'NO_REVERSAL_QUOTIENT','NO_CUT_INTEGRATION_IN_THIS_GATE','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_HEAVY_FULL_C5'],
 'next_gate':('classify the 21 routed cyclic TrU1sq classes by exact denominator topology and physical numerator transport; only after that classify cut support and singularity type before any normalized discontinuity integration'
              if passed else 'preserve FAIL and diagnose only the failing routing/cyclic-translation prerequisite without weakening thresholds')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
