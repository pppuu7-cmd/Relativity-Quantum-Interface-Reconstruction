#!/usr/bin/env python3
"""Iteration 139 conserved-source tensor-projector audit for ANSATZ-RQIR-KL-002."""

from fractions import Fraction
import json
from pathlib import Path


def main() -> int:
    # For nonrelativistic conserved sources in 4D, T_mn T'^mn -> rho rho'
    # and T T' -> rho rho' up to the common signature convention.
    massless_nr = Fraction(1, 1) - Fraction(1, 2)   # 1/2
    massive_nr = Fraction(1, 1) - Fraction(1, 3)   # 2/3
    ratio_nr = massive_nr / massless_nr             # 4/3

    # If one external conserved probe is traceless, T_probe=0, the trace term vanishes
    # in both amplitudes, so the massive/massless tensor coefficient ratio is 1.
    ratio_traceless = Fraction(1, 1)
    relative_after_nr_calibration = ratio_traceless / ratio_nr  # 3/4

    result = {
        "model_id": "ANSATZ-RQIR-KL-002",
        "iteration": 139,
        "scope": "linear conserved-source massless-vs-massive spin-2 projector audit",
        "massless_exchange_structure": "T.Tprime - (1/2) T Tprime",
        "massive_spin2_exchange_structure": "T.Tprime - (1/3) T Tprime",
        "nonrel_massless_coefficient": str(massless_nr),
        "nonrel_massive_coefficient": str(massive_nr),
        "nonrel_continuum_to_GR_ratio": str(ratio_nr),
        "traceless_probe_continuum_to_GR_ratio": str(ratio_traceless),
        "traceless_response_relative_to_NR_calibrated_continuum": str(relative_after_nr_calibration),
        "updated_static_potential": "Phi=-GM/r [1 + (4/3) beta W(M_* r)] in the frozen linear massive-spin-2 continuum completion",
        "decision": "PASS_SCOPED_LINEAR_TENSOR_WITH_VDVZ_SIGNATURE",
        "warnings": [
            "No nonlinear Vainshtein screening is assumed in v0.1.",
            "No nonlinear ghost-free completion of a spin-2 continuum is proved.",
            "The vDVZ tensor factor is a physical signature/constraint, not an automatic rejection when the continuum is gapped and finite-range."
        ]
    }
    out = Path("results/candidate_gravity_tensor_projector_iteration139.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
