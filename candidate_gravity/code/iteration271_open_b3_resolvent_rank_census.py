#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 271.

Exact bookkeeping audit for the Iteration-270 routed null-soft B3 kernel.
The goal is to determine what denominator information is actually available
before a closure/source insertion is specified.

No tensor reduction or loop integration is attempted here.
"""
import itertools, json
from collections import Counter

LEGS = ('s','a','b')
K = {
    's': (1.0,0.0,0.0,1.0),
    'a': (0.25,0.6,0.3,0.15),
    'b': (-0.15,0.2,0.55,-0.35),
}


def u(xs):
    out=set()
    for x in xs: out.add(x)
    return frozenset(out)


def qbranches(legs, base=frozenset()):
    """Return primitive inverse-recursion branches and routed Q0 shifts.

    A shift frozenset S denotes Q0(p + sum_{x in S} k_x).
    """
    legs=tuple(legs); base=frozenset(base)
    if len(legs)==0:
        return [('Q0',[base])]
    if len(legs)==1:
        x=legs[0]
        return [(f'Q1[{x}]',[base|{x},base])]
    if len(legs)==2:
        x,y=legs
        return [
            (f'Q2_seq_{x}{y}',[base|{x,y},base|{y},base]),
            (f'Q2_seq_{y}{x}',[base|{x,y},base|{x},base]),
            (f'Q2_contact_{x}{y}',[base|{x,y},base]),
        ]
    raise ValueError('Q3 is forbidden here because A0=0')

surviving=[]
for assign in itertools.product('LMR', repeat=3):
    L=tuple(LEGS[i] for i,a in enumerate(assign) if a=='L')
    A=tuple(LEGS[i] for i,a in enumerate(assign) if a=='M')
    R=tuple(LEGS[i] for i,a in enumerate(assign) if a=='R')
    if not A: continue
    if A==('s',): continue  # exact null-soft A1[s]=0
    surviving.append((L,A,R))

primitive=[]
for L,A,R in surviving:
    # term = Q_L(p+k_R+k_A) A_A(p+k_R) Q_R(p)
    baseL=u(R)|u(A)
    for lname,lshifts in qbranches(L,baseL):
        for rname,rshifts in qbranches(R,frozenset()):
            shifts=lshifts+rshifts
            primitive.append({
                'L':L,'A':A,'R':R,
                'left_branch':lname,'right_branch':rname,
                'q0_factor_count':len(shifts),
                'distinct_q0_shift_count':len(set(shifts)),
                'q0_shifts':['+'.join(sorted(s)) if s else '0' for s in shifts],
            })

Ktot=tuple(sum(K[x][i] for x in LEGS) for i in range(4))
etaK2=-Ktot[0]**2+sum(z*z for z in Ktot[1:])
qcount=Counter(r['q0_factor_count'] for r in primitive)
dcount=Counter(r['distinct_q0_shift_count'] for r in primitive)
maxq=max(qcount)
all_distinct=all(r['q0_factor_count']==r['distinct_q0_shift_count'] for r in primitive)

result={
    'iteration':271,
    'input_authority':'Iteration 270 physical routed null-soft B3',
    'surviving_unexpanded_B3_terms':len(surviving),
    'primitive_inverse_recursion_branches':len(primitive),
    'q0_factor_count_histogram':dict(sorted(qcount.items())),
    'distinct_q0_shift_count_histogram':dict(sorted(dcount.items())),
    'maximum_q0_factors_in_one_open_branch':maxq,
    'all_open_branch_q0_shifts_distinct_at_generic_leg_labels':all_distinct,
    'frozen_total_background_shift_K':Ktot,
    'frozen_K_minkowski_square':etaK2,
    'K_is_nonzero':any(abs(z)>0 for z in Ktot),
    'classification':'PASS_EXACT_OPEN_B3_RESOLVENT_RANK_CENSUS',
    'operational_status':'BLOCKED_MASTER_REDUCTION_UNTIL_KINEMATIC_CLOSURE_AND_P_DEPENDENT_INTEGRAND',
    'guardrails':[
        'DO_NOT_FORCE_OPEN_B3_BRANCHES_INTO_CLOSED_BUBBLE_TRIANGLE_MASTERS_BEFORE_CLOSURE',
        'ITER245_250_TOPOLOGY_BOUND_APPLIES_TO_CLOSED_COMPOSITE_TRACE_FAMILIES_NOT_TO_AN_UNCLOSED_FIXED_P_KERNEL',
        'NONZERO_AT_ONE_P_IS_NOT_A_LOOP_INTEGRAND_RECONSTRUCTION',
    ],
    'primitive_rows':primitive,
}
print(json.dumps(result,indent=2))
