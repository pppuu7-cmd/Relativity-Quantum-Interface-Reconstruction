"""RQIR Candidate Gravity Iteration 147

Structural audit for the first C5 retarded nonlinear-response embedding.

This script deliberately does NOT invent a numerical gravitational chi2R.  It
freezes the CTP/source convention, records the exact tree-level retarded kernel
factorization, and checks whether the Iteration-146 frozen data are sufficient
to evaluate that kernel in the Iteration-145 finite coordinates.
"""

import json
from pathlib import Path

ITERATION = 147

ct_preset = {
    "background": "D=4 Minkowski",
    "state": "interacting in-vacuum adiabatically connected to free graviton vacuum",
    "gauge": "de Donder gauge for perturbative evaluation; final source projections must be conserved",
    "source_coupling": "S_J = integral d4x J_A h^A, with J conserved in physical projections",
    "retarded_prescription": "all response legs use G_R; no Feynman-to-retarded identification by fiat",
    "eft_baseline": "Einstein-Hilbert + same parity-even local EFT operator set frozen in Iteration 146",
}

# Condensed DeWitt-index formula.  With EOM K h + 1/2 V[h,h] + J = 0,
# h^(1)=-G_R J and d^2 h / dJ dJ = -G_R V G_R G_R.
retarded_kernel = {
    "position_space": "chi2R_A;BC(x;y,z) = - integral d4w GR_AA'(x,w) V^A'_{B'C'}(w) GR^B'_B(w,y) GR^C'_C(w,z) + contact/source terms if the declared coupling contains them",
    "momentum_space": "chi2R_A;BC(p;q,r) = -(2pi)^4 delta4(p-q-r) GR_AA'(p) Gamma3^A'_{B'C'}(p,-q,-r) GR^B'_B(q) GR^C'_C(r)",
    "input_symmetry": "chi2R_A;BC(p;q,r)=chi2R_A;CB(p;r,q) when Gamma3 is Bose symmetric",
    "causality": "retarded support follows from the three GR factors and the in-in/CTP prescription",
}

# Exact information required to turn the off-shell retarded tensor kernel into
# finite RQIR coordinates.  The Iteration-146 data are 2->2 on-shell Mandelstam
# fingerprints and therefore do not supply these objects.
required_retarded_protocol = {
    "off_shell_momenta": ["p", "q", "r", "p=q+r", "p2", "q2", "r2", "energy_signs"],
    "tensor_projection": ["output_projector_A", "input_projector_B", "input_projector_C"],
    "smearing": ["time_window", "spatial_smearing", "normalization"],
    "ward_lock": ["conserved_source_projection", "gauge_artifact_null_test"],
    "chi2R_coordinate_map": ["definition_of_even_coordinate", "definition_of_odd_coordinate"],
}

iteration146_fields = {
    "on_shell_2to2": ["s", "t", "u", "s+t+u=0", "polarization_phase_phi"],
    "amplitude_type": "four-graviton on-shell crossing-symmetric amplitude",
    "does_not_fix": [
        "off-shell p2,q2,r2",
        "retarded energy routing",
        "three external tensor/source projectors",
        "finite smearing/window normalization",
        "chi2R_even/odd coordinate definitions",
    ],
}

certificate = {
    "iteration": ITERATION,
    "status": "PARTIAL_CLOSURE_WITH_EXACT_BLOCKER",
    "ct_prescription_frozen": True,
    "tree_retarded_factorization_derived": True,
    "ward_status": "SCOPED_FORMAL: conserved-source projection required; numerical Ward test awaits explicit projector/vertex evaluation",
    "iteration146_on_shell_data_sufficient_for_chi2R": False,
    "chi2R_even_odd_numeric_embedding": "BLOCKED_PROTOCOL_UNDERSPECIFIED",
    "local_eft_chi2R_rank": "NOT_COMPUTABLE_WITHOUT_CUBIC_VERTEX_AND_PROJECTOR_MAP",
    "loop_nonanalytic_columns": "BLOCKED_NOT_DERIVED_IN_SAME_CTP_CONVENTION",
    "N2": "BLOCKED_REQUIRES_CTP_LOOP_OR_INFLUENCE_FUNCTIONAL",
    "C3sym": "BLOCKED_REQUIRES_CTP_LOOP_OR_STATE_NON_GAUSSIAN_DERIVATION",
    "new_negative_result": "NG-FUNNEL-007: ON_SHELL_4PT_KINEMATICS_DO_NOT_FIX_OFF_SHELL_RETARDED_3PT",
    "fisher_resources_allowed": False,
    "ansatz003_allowed": False,
    "ct_preset": ct_preset,
    "retarded_kernel": retarded_kernel,
    "required_retarded_protocol": required_retarded_protocol,
    "iteration146_fields": iteration146_fields,
    "next_gate": "Freeze an explicit finite off-shell source/projector/smearing protocol and evaluate the de-Donder EH+cubic-EFT Gamma3 contractions at those points before any chi2R rank claim.",
}

out = Path("results/c5_retarded_embedding_iteration147.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
print(json.dumps(certificate, indent=2))
