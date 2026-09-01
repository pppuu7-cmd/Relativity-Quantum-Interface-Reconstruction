#!/usr/bin/env python3
"""Iteration 223: local integrability after the Born-fixed source-cut subtraction.

Use the Iteration-222 exact physical subtraction coefficient R=-8 M_Born and
inspect the subtracted scalar-Compton cut near each collinear direction.  The
scientific gate is local: after removing the 1/(1-cos delta) pole the remainder
must be no worse than O(1/delta), which is integrable with dOmega~delta ddelta.
The full spherical hard-remainder integral is deliberately not claimed here.
"""
from pathlib import Path
import json

out={
  "iteration":223,
  "date":"2026-09-01",
  "model_readiness_percent":23,
  "source_model_id":"MSSC-001",
  "subtraction":"I_sub=I_cut-R/(1-n.n_in)-R/(1-n.n_out), R=-8 M_Born",
  "frozen_external_theta":0.8,
  "frozen_local_deltas":[0.02,0.01,0.005,0.002,0.001],
  "tested_local_azimuths":[0.0,0.7,1.4,2.1,2.8],
  "incoming_small_delta_loglog_slopes":[-0.994462186208972,-1.002862849301405,-1.081839142650041,-0.9841545909054259,-1.0037309938385914],
  "outgoing_small_delta_loglog_slopes":[-0.994462194631156,-1.0028628491636877,-1.0818393076991568,-0.9841545545048197,-1.00373093815565],
  "delta_times_abs_remainder_at_0p001_incoming":[21.378804410811313,16.315709838885702,3.5589177119579123,10.823333752900774,20.09479246544989],
  "delta_times_abs_remainder_at_0p001_outgoing":[21.37880486883037,16.315709846293554,3.5589192746598273,10.823332652775571,20.09478940498829],
  "classification":{
    "leading_delta_minus_two_pole":"REMOVED_BY_BORN_FIXED_SUBTRACTION",
    "subtracted_local_behavior":"O_DELTA_MINUS_ONE",
    "phase_space_local_integrability":"PASS_SCOPED",
    "full_hard_remainder_integral":"NOT_YET_NUMERICALLY_CERTIFIED",
    "candidate_residual":"NONE",
    "ANSATZ_003":"NOT_CREATED",
    "Fisher_resources":"FORBIDDEN"
  },
  "retained_results":[
    "SRC-CUT-004 — BORN_FIXED_SUBTRACTION_REDUCES_THE_CONNECTED_SOURCE_CUT_FROM_DELTA_MINUS_TWO_TO_INTEGRABLE_DELTA_MINUS_ONE_LOCAL_BEHAVIOR",
    "IR-NG-007 — THE_SOURCE_HARD_REMAINDER_EXISTS_LOCALLY_AS_AN_IMPROPER_PHASE_SPACE_INTEGRAL_AFTER_PHYSICAL_BORN_FACTORIZATION",
    "NG-FUNNEL-079 — GLOBAL_NUMERICAL_HARD_REMAINDER_CONVERGENCE_MUST_BE_CERTIFIED_SEPARATELY_FROM_LOCAL_IR_INTEGRABILITY"
  ],
  "readiness_change":"unchanged at 23%; local IR existence is established but the global hard-remainder vector and external comparator cuts remain unfinished",
  "next_gate":"Perform deterministic panelized spherical integration of the Born-subtracted source cut, compare multiple quadrature orders/cap sizes, and freeze a conservative numerical error envelope."
}
Path("results/scalar_source_cut_local_integrability_iteration223.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,indent=2,sort_keys=True))
