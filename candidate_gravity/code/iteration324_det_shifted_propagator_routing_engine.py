#!/usr/bin/env python3
"""RQIR Iteration 324: explicit shifted-free-propagator routing engine.

This gate implements the denominator/routing skeleton required by the cubic
functional trace on the Iteration-322 closed triad.  It does NOT invent the
still-missing arbitrary-incoming-momentum H/N numerator factories.  Those remain
BLOCKED and are the next dependent gate.

For an ordered insertion sequence (a,b,...) the free inverses are evaluated at
successive loop momenta p, p+q(a), p+q(a)+q(b), ... .  Cyclic rotations of a
closed trace must define the same denominator family up to a common loop-momentum
translation; this is checked exactly on integerized Fourier shifts.
"""
from __future__ import annotations
import itertools, json, math
import numpy as np

D=4
ETA=np.diag([-1.,1.,1.,1.])
TARGET=(1,1,1)
# Iteration-322 closed triad, stored as exact integer multiples of 1/100.
QINT=[(27,-19,31,11),(-13,37,17,-29),(-14,-18,-48,18)]
P=np.array([.61,-.33,.24,.52],float)

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def qint(a): return tuple(sum(a[r]*QINT[r][mu] for r in range(3)) for mu in range(D))
def qvec(a): return np.array(qint(a),float)/100.0

def nonzero_subindices(target):
    out=[]
    for a in itertools.product(*(range(x+1) for x in target)):
        if any(a): out.append(a)
    return out
NZ=nonzero_subindices(TARGET)

def ordered_pairs():
    return [(a,b) for a in NZ for b in NZ if add(a,b)==TARGET]

def ordered_triples():
    out=[]
    for a in NZ:
      for b in NZ:
       for c in NZ:
        if add(add(a,b),c)==TARGET: out.append((a,b,c))
    return out

def cumulative_shifts(seq):
    # One free inverse before each insertion. The final closure shift is checked
    # separately and must return to the starting loop momentum.
    shifts=[(0,0,0,0)]
    cur=(0,0,0,0)
    for a in seq[:-1]:
        qa=qint(a); cur=tuple(cur[i]+qa[i] for i in range(D)); shifts.append(cur)
    total=(0,0,0,0)
    for a in seq:
        qa=qint(a); total=tuple(total[i]+qa[i] for i in range(D))
    return shifts,total

def translated_family_canonical(shifts):
    # Product denominators are unordered; quotient by a common loop shift.
    candidates=[]
    for origin in shifts:
        rel=sorted(tuple(s[i]-origin[i] for i in range(D)) for s in shifts)
        candidates.append(tuple(rel))
    return min(candidates)

def rotations(seq):
    return [seq[i:]+seq[:i] for i in range(len(seq))]

def denom(k): return float(k @ ETA @ k)

def route_record(seq):
    shifts,total=cumulative_shifts(seq)
    vals=[]
    for s in shifts:
        k=P+np.array(s,float)/100.0
        vals.append(denom(k))
    return {
      'sequence':[list(x) for x in seq],
      'propagator_shift_int100':[list(x) for x in shifts],
      'closure_shift_int100':list(total),
      'denominators_at_fixture_p':vals,
      'canonical_family_int100':[list(x) for x in translated_family_canonical(shifts)],
    }

pairs=ordered_pairs(); triples=ordered_triples()
pair_records=[route_record(x) for x in pairs]
triple_records=[route_record(x) for x in triples]

closure_ok=all(r['closure_shift_int100']==[0,0,0,0] for r in pair_records+triple_records)
finite_nonzero=all(math.isfinite(v) and abs(v)>1e-10 for r in pair_records+triple_records for v in r['denominators_at_fixture_p'])

def cyclic_ok(seq):
    fam=[]
    for r in rotations(seq):
        shifts,total=cumulative_shifts(r)
        if total!=(0,0,0,0): return False
        fam.append(translated_family_canonical(shifts))
    return len(set(fam))==1

pair_cyclic=all(cyclic_ok(x) for x in pairs)
triple_cyclic=all(cyclic_ok(x) for x in triples)
# Explicitly require nontrivial shifted inverses in every routed term.
shifted_present=all(any(any(c!=0 for c in s) for s in r['propagator_shift_int100'][1:]) for r in pair_records+triple_records)
qclosure=tuple(sum(QINT[r][mu] for r in range(3)) for mu in range(D))
qrank=int(np.linalg.matrix_rank(np.array(QINT,float),tol=1e-12))

ok=(qclosure==(0,0,0,0) and qrank==2 and closure_ok and finite_nonzero and pair_cyclic and triple_cyclic and shifted_present)
result={
 'iteration':324,
 'model_readiness_percent':24,
 'scientific_gate_pass':bool(ok),
 'classification':('PASS_SHIFTED_FREE_PROPAGATOR_ROUTING_ENGINE_CYCLIC_EQUIVALENCE' if ok else 'FAIL_SHIFTED_FREE_PROPAGATOR_ROUTING_ENGINE_CYCLIC_EQUIVALENCE'),
 'candidate_residual':False,
 'scope':{
   'target_multiindex':list(TARGET),
   'closed_triad_q_int100':[list(x) for x in QINT],
   'q_total_int100':list(qclosure),
   'q_rank':qrank,
   'ordered_pair_count':len(pairs),
   'ordered_triple_count':len(triples),
   'routing_rule':'G0(p+Q_before_each_insertion); Q accumulates ordered Fourier insertion momenta',
 },
 'checks':{
   'all_trace_sequences_close':closure_ok,
   'all_fixture_denominators_finite_nonzero':finite_nonzero,
   'all_pair_cyclic_families_equivalent_up_to_loop_shift':pair_cyclic,
   'all_triple_cyclic_families_equivalent_up_to_loop_shift':triple_cyclic,
   'explicit_nonzero_shifted_propagators_present':shifted_present,
 },
 'pair_routes':pair_records,
 'triple_routes':triple_records,
 'physical_status':{
   'shifted_denominator_routing_engine':'FROZEN_IF_PASS',
   'physical_HN_arbitrary_incoming_momentum_numerators':'BLOCKED_NEXT_DEPENDENT_GATE',
   'full_physical_determinant_loop_integrand_ready':False,
   'denominator_family_reduction_ready':False,
 },
 'guardrails':['NO_NUMERATOR_ZERO_FILL','NO_PHYSICAL_COEFFICIENT_PROMOTION_FROM_ROUTING_SKELETON','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_HEAVY_FULL_C5','UNSUPPORTED_IS_BLOCKED_NOT_ZERO_FILLED'],
 'next_gate':('refactor/evaluate frozen graviton H1/H2/H3 and ghost N1/N2/N3 insertion kernels as functions of their correct incoming loop momentum p+Q, then validate against exact geometry before assembling the shifted physical cubic trace' if ok else 'preserve FAIL and repair shifted-propagator routing engine without weakening closure/cyclic checks')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not ok: raise SystemExit(2)
