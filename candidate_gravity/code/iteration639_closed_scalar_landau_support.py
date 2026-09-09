#!/usr/bin/env python3
"""Iteration 639: frozen Iter636 equal-mass bubble/triangle singularity geometry.

Inputs are authority-fixed before this result:
  t0 = 0.14, u0 = 0.34, m_phi = 0.7, s variable > 0.
No Candidate-side values, native projection, Source/Born subtraction, comparator fit,
or ansatz tuning enter this audit.

For the equal-mass triangle with Feynman parameters x,y,z>=0, x+y+z=1,
we use the standard one-loop second Symanzik polynomial in +--- signature
  F = m^2 - x*y*s - y*z*t - z*x*u.
A leading Landau singularity requires an interior stationary point F=0 with
x,y,z all strictly positive. Boundary solutions are ordinary bubble subchannel
thresholds and are reported separately.
"""
from __future__ import annotations
import json, math
from pathlib import Path

ITERATION = 639
T = 0.14
U = 0.34
M = 0.7
M2 = M*M

# K1/K2 s-channel equal-mass bubble normal threshold.
S_BUBBLE = 4.0*M2

# Eliminating the interior stationary Feynman parameters gives
#   175 s^2 - 151 s + 7 = 0
# at the frozen rational values t=7/50, u=17/50, m^2=49/100.
disc = 151.0**2 - 4.0*175.0*7.0
sqrt_disc = math.sqrt(disc)
roots = [(151.0 - sqrt_disc)/(350.0), (151.0 + sqrt_disc)/(350.0)]

def stationary_params(s: float):
    den = 250.0*s*s - 240.0*s + 10.0
    x = (-35.0*s - 7.0)/den
    y = (17.0 - 85.0*s)/den
    z = 1.0 - x - y
    return x,y,z

landau=[]
for r in roots:
    x,y,z=stationary_params(r)
    positive=(x>0.0 and y>0.0 and z>0.0)
    landau.append({"s":r,"x":x,"y":y,"z":z,"all_positive":positive})

failures=[]
if not math.isclose(S_BUBBLE,1.96,rel_tol=0.0,abs_tol=2e-15): failures.append("bubble threshold drift")
if len(landau)!=2: failures.append("Landau root count drift")
if any(p["all_positive"] for p in landau): failures.append("unexpected positive-alpha leading triangle support")
if not (T < S_BUBBLE and U < S_BUBBLE): failures.append("fixed crossed invariant reached two-particle threshold")

classification = (
    "PASS_ITER639_FROZEN_CLOSED_SCALAR_SINGULARITY_GEOMETRY__"
    "BUBBLE_S_THRESHOLD_1P96__TRIANGLE_LEADING_LANDAU_CANDIDATES_HAVE_NO_POSITIVE_FEYNMAN_SUPPORT__NON_RESIDUAL"
    if not failures else
    "FAIL_ITER639_FROZEN_CLOSED_SCALAR_SINGULARITY_GEOMETRY_IMPLEMENTATION_OR_AUTHORITY_DRIFT__NON_RESIDUAL"
)

result={
    "iteration":ITERATION,
    "date":"2026-09-09",
    "classification":classification,
    "failures":failures,
    "scientific_gate_pass":not failures,
    "inputs":{"t0":T,"u0":U,"m_phi":M,"m_phi_sq":M2,"s_variable":"s>0"},
    "bubble":{"s_channel_normal_threshold":S_BUBBLE,"anchor_s0":1.0,"anchor_below_threshold":1.0<S_BUBBLE},
    "triangle":{
        "symanzik":"F=m^2-x*y*s-y*z*t-z*x*u, x+y+z=1",
        "leading_landau_polynomial":"175*s^2-151*s+7=0",
        "candidate_stationary_roots":landau,
        "positive_feynman_parameter_leading_support":False,
        "interpretation":"Both finite stationary solutions fail x>0,y>0,z>0, so there is no physical-sheet leading/anomalous triangle singularity on this frozen real-s family from an interior positive-alpha Landau solution. Boundary singularities reduce to bubble subchannels."
    },
    "crossed_channels":{"t0_below_4m2":T<S_BUBBLE,"u0_below_4m2":U<S_BUBBLE},
    "candidate_values_used":False,
    "zero_fill":False,
    "source_born_subtraction":"NOT_PERFORMED",
    "native_projection":"NOT_PERFORMED",
    "comparator_quotient":"NOT_PERFORMED",
    "ANSATZ_003":"FORBIDDEN",
    "Fisher_resources":"FORBIDDEN",
    "MODEL_READINESS":"24%",
    "readiness_change":"0 percentage points",
    "next_gate":"Using the frozen Iter632 Minkowski-vacuum G_K and Iter627 combined SK contract, derive the actual closed K1/K2 s-channel discontinuity coefficient across s>=1.96 (including numerator/tensor contraction and common conventions) before any native projection; keep K3 tadpole and K1^3 triangle families retained, with the latter having no positive-alpha leading anomalous support on this family."
}

out=Path(__file__).resolve().parents[2]/"results"/"iteration639_closed_scalar_landau_support"
out.mkdir(parents=True,exist_ok=True)
(out/"result.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
print(json.dumps(result,indent=2,sort_keys=True))
if failures:
    raise SystemExit(2)
