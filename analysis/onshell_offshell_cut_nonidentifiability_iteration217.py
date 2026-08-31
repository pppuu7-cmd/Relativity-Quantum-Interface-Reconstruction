#!/usr/bin/env python3
"""Iteration 217: on-shell cut does not determine the off-shell/source cut.

This is an algebraic counterexample, not a Candidate Gravity model.
Let K2(p) be an inverse external-leg kernel and H(q^2) a nonanalytic form
factor with normalized discontinuity D H = 1 on a chosen hard channel.

Two cubic kernels
  Gamma_A = Gamma_0
  Gamma_B = Gamma_0 + K2(p) H(q^2)
are identical on the p-leg mass shell K2(p)=0 but have different off-shell
channel discontinuities. Therefore even an exact on-shell unitarity cut cannot
uniquely reconstruct an off-shell/source-completed T_cut without additional
physical source/field information.
"""
from pathlib import Path
import json
import numpy as np

ITERATION=217
kp=np.array([0.0,0.02,0.05,0.10,0.20],float)
disc_H=1.0
base_cut=np.array([0.7,-0.3,0.2,1.1,-0.4],float)
cut_A=base_cut.copy()
cut_B=base_cut+kp*disc_H

out={
  "iteration":ITERATION,
  "date":"2026-09-01",
  "model_readiness_percent":23,
  "construction":"Gamma_B = Gamma_A + K2(p) H(q^2), with D H = 1",
  "K2_p_samples":kp.tolist(),
  "on_shell_index":0,
  "on_shell_cut_difference":float(cut_B[0]-cut_A[0]),
  "off_shell_cut_differences":(cut_B-cut_A).tolist(),
  "max_off_shell_cut_difference":float(np.max(np.abs(cut_B-cut_A))),
  "classification":{
    "on_shell_cut_identity":"EXACT",
    "off_shell_cut_identity":"FALSE",
    "map_on_shell_cut_to_off_shell_T_cut":"NON_IDENTIFIABLE_WITHOUT_ADDITIONAL_SOURCE_COMPLETION",
    "iteration215_216_physical_C5_vector":"VALID_ONSHELL_POSITIVE_CONTROL_ONLY",
    "off_shell_source_completed_C5_T_cut":"STILL_BLOCKED",
    "candidate_residual":"NONE",
    "ANSATZ_003":"NOT_CREATED",
    "Fisher_resources":"FORBIDDEN"
  },
  "retained_results":[
    "C5-CUT-017 — EXACT_ONSHELL_UNITARITY_CUT_DOES_NOT_UNIQUELY_DETERMINE_OFFSHELL_SOURCE_COMPLETED_T_CUT",
    "REL-NG-019 — EOM_OR_INVERSE_KERNEL_PROPORTIONAL_NONANALYTIC_CUBIC_TERMS_LIE_IN_THE_ONSHELL_RESTRICTION_KERNEL_BUT_CAN_CHANGE_OFFSHELL_CUTS",
    "NG-FUNNEL-074 — ONSHELL_POSITIVE_CONTROLS_MUST_NOT_BE_PROMOTED_TO_OFFSHELL_COMPARATOR_COLUMNS_WITHOUT_A_PHYSICAL_SOURCE_COMPLETION_MAP"
  ],
  "readiness_change":"unchanged at 23%; the on-shell C5 control is robust but cannot close the missing off-shell/source-completed comparator by itself",
  "next_gate":"Construct the cut directly for a gauge-invariant conserved-source response (or an equivalent physical in-in observable), rather than attempting to infer it from the on-shell graviton S-matrix."
}
Path("results/onshell_offshell_cut_nonidentifiability_iteration217.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,indent=2,sort_keys=True))
