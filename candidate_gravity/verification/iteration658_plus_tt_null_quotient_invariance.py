#!/usr/bin/env python3
"""Iteration658 exact quotient-invariance audit for the frozen null-soft plus-TT measurement.

This gate uses no Candidate cut values and chooses no auxiliary null vector, off-null
regulator, or longitudinal complement.  It tests whether the already-frozen plus-TT
linear measurement M(h)=e_plus^{mu nu} h_{mu nu} annihilates the null pure-gauge
overlap Im(L_q) cap Ker(D_q).  If so M descends canonically to the quotient.
"""
from fractions import Fraction as F
import json
from pathlib import Path

pairs=[(i,j) for i in range(4) for j in range(i,4)]
qU=[F(1),F(0),F(0),F(1)]
qL=[F(1),F(0),F(0),F(-1)]

# Gauge map L_q(xi)_{mu nu}=q_mu xi_nu+q_nu xi_mu in symmetric-tensor coordinates.
L=[[F(0) for _ in range(4)] for _ in range(10)]
for a,(mu,nu) in enumerate(pairs):
    for k in range(4):
        L[a][k]=(qL[mu] if nu==k else 0)+(qL[nu] if mu==k else 0)

# Divergence D_q h = q^mu h_{mu nu}.
D=[[F(0) for _ in range(10)] for _ in range(4)]
for nu in range(4):
    for a,(mu,rho) in enumerate(pairs):
        if rho==nu:
            D[nu][a]+=qU[mu]
        if mu==nu and rho!=mu:
            D[nu][a]+=qU[rho]

# Frozen historical plus-TT polarization: e_11=+1, e_22=-1, all other entries zero.
M=[F(0) for _ in range(10)]
M[pairs.index((1,1))]=F(1)
M[pairs.index((2,2))]=F(-1)
hplus=M[:]

# M o L is the exact gauge variation of the measurement.  It vanishes identically,
# which is stronger than merely vanishing on Im(L_q) cap Ker(D_q).
ML=[sum(M[a]*L[a][k] for a in range(10)) for k in range(4)]
Dhplus=[sum(D[nu][a]*hplus[a] for a in range(10)) for nu in range(4)]
M_hplus=sum(M[a]*hplus[a] for a in range(10))

# Three explicit independent xi with q^upper xi_lower=0 generate the null overlap.
overlap_xi=[
    [F(0),F(1),F(0),F(0)],
    [F(0),F(0),F(1),F(0)],
    [F(1),F(0),F(0),F(-1)],
]
overlap_measurements=[]
overlap_divergences=[]
for xi in overlap_xi:
    g=[sum(L[a][k]*xi[k] for k in range(4)) for a in range(10)]
    overlap_measurements.append(sum(M[a]*g[a] for a in range(10)))
    overlap_divergences.append([sum(D[nu][a]*g[a] for a in range(10)) for nu in range(4)])

checks={
    "q_squared": qU[0]**2-qU[1]**2-qU[2]**2-qU[3]**2,
    "plus_TT_is_transverse": all(x==0 for x in Dhplus),
    "measurement_annihilates_full_gauge_image": all(x==0 for x in ML),
    "three_overlap_generators_are_transverse": all(all(x==0 for x in row) for row in overlap_divergences),
    "measurement_annihilates_three_overlap_generators": all(x==0 for x in overlap_measurements),
    "measurement_is_nontrivial_on_quotient_witness": M_hplus != 0,
    "plus_TT_self_measurement": M_hplus,
}
expected={
    "q_squared":0,
    "plus_TT_is_transverse":True,
    "measurement_annihilates_full_gauge_image":True,
    "three_overlap_generators_are_transverse":True,
    "measurement_annihilates_three_overlap_generators":True,
    "measurement_is_nontrivial_on_quotient_witness":True,
    "plus_TT_self_measurement":2,
}
failures=[]
for k,v in expected.items():
    if checks[k]!=v:
        failures.append(f"CHECK_FAILED:{k}:{checks[k]}!={v}")

classification=(
    "PASS_ITER658_PLUS_TT_MEASUREMENT_DESCENDS_TO_NULL_GAUGE_QUOTIENT"
    "__ANNIHILATES_IM_LQ__NO_COMPLEMENT_REQUIRED__NON_RESIDUAL"
)
result={
    "iteration":658,
    "scope":"MSSC001-CLOSED-SK-SOFT-TCUT-KIN-V1 plus-TT null quotient invariance",
    "checks":{k:(int(v) if isinstance(v,F) else v) for k,v in checks.items()},
    "quotient_statement":(
        "The frozen plus-TT functional M restricted to Ker(D_q) annihilates "
        "Im(L_q) intersect Ker(D_q), indeed M o L_q=0 on the full gauge image. "
        "Therefore M defines a unique nonzero linear functional on "
        "Ker(D_q)/(Im(L_q) intersect Ker(D_q)) without choosing a complement."
    ),
    "auxiliary_vector_or_off_null_regulator_selected":False,
    "candidate_cut_values_read":False,
    "source_born_subtraction":"NOT_PERFORMED",
    "native_soft_T_cut_value_computed":False,
    "zero_fill_allowed":False,
    "classification":classification,
    "scientific_gate_pass":len(failures)==0,
    "failures":failures,
    "MODEL_READINESS":"24%",
    "readiness_delta_percentage_points":0,
    "exact_next_gate":(
        "Use the quotient-safe plus-TT contraction directly on the same-parent normalized closed-SK "
        "soft Gamma3 integrand under the Iter655 cut-before-soft-limit protocol; classify K3 contact "
        "versus K1K2/K1^3 pole/cut origin before any Source/Born subtraction or numerical residual claim."
    ),
}
out=Path("candidate_gravity/results/iteration658_plus_tt_null_quotient_invariance.json")
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2,sort_keys=True))
if failures:
    raise SystemExit(1)
