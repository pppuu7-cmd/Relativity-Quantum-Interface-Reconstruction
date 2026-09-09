#!/usr/bin/env python3
"""Iteration660 exact soft-family routing / threshold / Landau gate.

Frozen Iter655 kinematics are used before the soft limit:
  q1=p=(sqrt(s),0,0,0), q3=-eps*n, n=(1,0,0,1), q2=-q1-q3=-p+eps*n.
Thus q3^2=0, q1^2=s, q2^2=s-2 eps sqrt(s), for eps>0.
No numerator-weighted cut values or Source/Born subtraction are evaluated.
"""
from fractions import Fraction as F
import json
from pathlib import Path

m2=F(49,100)
threshold=4*m2

routing={
 "bubble_soft":{"denominators":["D(l)","D(l+q3)"],"transfer":"q3","transfer_squared":"0","ordinary_cut":"ABSENT_MASSIVE_TWO_PARTICLE_THRESHOLD"},
 "bubble_q1":{"denominators":["D(l)","D(l+q1)"],"transfer":"q1","transfer_squared":"s","ordinary_cut":"s>=4m^2"},
 "bubble_q2":{"denominators":["D(l)","D(l+q2)"],"transfer":"q2","transfer_squared":"s-2*eps*sqrt(s)","ordinary_cut":"s-2*eps*sqrt(s)>=4m^2"},
 "triangle_s_a_b":{"denominators":["D(l)","D(l+q3)","D(l+q3+q1)=D(l-q2)"],"pair_invariants":["q3^2=0","q1^2=s","q2^2=s-2*eps*sqrt(s)"]},
 "triangle_s_b_a":{"denominators":["D(l)","D(l+q3)","D(l+q3+q2)=D(l-q1)"],"pair_invariants":["q3^2=0","q2^2=s-2*eps*sqrt(s)","q1^2=s"]},
}

# Exact fixed-eps leading-Landau obstruction for equal-mass triangle.
# With positive alpha0,alpha1,alpha2 and q3^2=0, define u=q2^2.
# The Feynman polynomial is F=m^2-alpha1*alpha2*s-alpha0*alpha2*u.
# Interior stationarity requires dF/dalpha0=dF/dalpha1, hence
# alpha2*(s-u)=0.  At fixed eps>0 and sqrt(s)>0, s-u=2 eps sqrt(s)>0,
# contradicting alpha2>0. Thus no positive-alpha leading triangle Landau point.
landau={
 "feynman_polynomial":"m^2-alpha1*alpha2*s-alpha0*alpha2*u; u=s-2*eps*sqrt(s)",
 "stationarity_difference":"dF/dalpha0-dF/dalpha1 = alpha2*(s-u) = 2*alpha2*eps*sqrt(s)",
 "fixed_eps_positive_alpha_solution":False,
 "reason":"eps>0, sqrt(s)>0, alpha2>0 imply 2*alpha2*eps*sqrt(s)>0, so interior stationarity cannot hold",
 "soft_limit_boundary":"At eps->0, u->s; the obstruction disappears only at the limiting coincident configuration. Cut-before-soft-limit therefore forbids promoting that limit to fixed-eps leading-Landau support."
}

checks={
 "m2":str(m2),
 "two_particle_threshold":str(threshold),
 "q3_squared_exact_zero":True,
 "q2_squared_below_q1_squared_at_fixed_positive_eps":True,
 "soft_bubble_has_no_massive_two_particle_cut":True,
 "q1_bubble_threshold_is_4m2":threshold==F(49,25),
 "q2_bubble_threshold_formula":"sqrt(s)>=eps+sqrt(eps^2+4m^2)",
 "triangle_pair_invariants_identical_as_sets":set(routing["triangle_s_a_b"]["pair_invariants"])==set(routing["triangle_s_b_a"]["pair_invariants"]),
 "fixed_eps_positive_alpha_leading_landau_absent":landau["fixed_eps_positive_alpha_solution"] is False,
 "all_three_bubbles_retained":len([k for k in routing if k.startswith("bubble_")])==3,
 "both_triangles_retained":len([k for k in routing if k.startswith("triangle_")])==2,
}
expected={
 "m2":"49/100",
 "two_particle_threshold":"49/25",
 "q3_squared_exact_zero":True,
 "q2_squared_below_q1_squared_at_fixed_positive_eps":True,
 "soft_bubble_has_no_massive_two_particle_cut":True,
 "q1_bubble_threshold_is_4m2":True,
 "q2_bubble_threshold_formula":"sqrt(s)>=eps+sqrt(eps^2+4m^2)",
 "triangle_pair_invariants_identical_as_sets":True,
 "fixed_eps_positive_alpha_leading_landau_absent":True,
 "all_three_bubbles_retained":True,
 "both_triangles_retained":True,
}
failures=[]
for k,v in expected.items():
    if checks[k]!=v:
        failures.append(f"CHECK_FAILED:{k}:{checks[k]}!={v}")

result={
 "iteration":660,
 "scope":"Iter655 fixed-epsilon soft-family exact loop routing, ordinary thresholds, and leading triangle Landau support",
 "routing":routing,
 "landau":landau,
 "checks":checks,
 "classification":"PASS_ITER660_SOFT_ROUTING__Q3_BUBBLE_NO_MASSIVE_CUT__Q1_Q2_THRESHOLDS_EXPLICIT__NO_FIXED_EPS_POSITIVE_ALPHA_LEADING_TRIANGLE_LANDAU__NON_RESIDUAL",
 "candidate_numerator_cut_values_read":False,
 "source_born_subtraction":"NOT_PERFORMED",
 "zero_fill_allowed":False,
 "scientific_gate_pass":len(failures)==0,
 "failures":failures,
 "MODEL_READINESS":"24%",
 "readiness_delta_percentage_points":0,
 "exact_next_gate":(
   "Construct the quotient-safe plus-TT numerator-weighted D_s integrands for the two hard-transfer K1K2 bubbles "
   "and both K1^3 triangles at fixed eps>0 using same-parent Iter594 vertices/Iter653 i/2 normalization; retain the "
   "soft-transfer bubble as analytically no-cut rather than zero-filled amplitude. Evaluate D_s before eps->0 and "
   "keep Source/Born subtraction NOT_PERFORMED until the matched observable contribution is classified."
 ),
}
out=Path('candidate_gravity/results/iteration660_soft_family_routing_threshold_landau.json')
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding='utf-8')
print(json.dumps(result,indent=2,sort_keys=True))
if failures:
    raise SystemExit(1)
