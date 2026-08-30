"""RQIR Iteration 123: manuscript claim/evidence classification regression.

The purpose is publication discipline: generic Fisher/OED ingredients are not
marked as RQIR novelty.  Candidate novelty is restricted to repository-specific
integrated constructions whose priority still requires final literature review.
"""
from __future__ import annotations

CLAIMS = {
    "profiled_fisher_schur": ("standard_method", False),
    "fisher_optimal_design": ("standard_method", False),
    "gravity_entanglement_resource_estimates": ("prior_gravity_literature", False),
    "classical_gravity_decoherence_diffusion_tests": ("prior_gravity_literature", False),
    "cross_spectral_force_sensing": ("experimental_precedent", False),
    "exact_f2f_mechanical_platform": ("experimental_precedent", False),
    "ordered_interface_reconstruction_hierarchy": ("rqir_candidate_novelty", True),
    "finite_nullspace_source_discriminant_pipeline": ("rqir_candidate_novelty", True),
    "source_calibration_plus_detector_profiled_wallclock_chain": ("rqir_candidate_novelty", True),
    "robust_architecture_certificate_u_v_z_delta": ("rqir_candidate_novelty", True),
    "likelihood_derived_transfer_recertification_chain": ("rqir_candidate_novelty", True),
}


def main() -> None:
    # No generic/prior ingredient may be presented as an RQIR novelty claim.
    for name, (kind, candidate_novelty) in CLAIMS.items():
        if kind in {"standard_method", "prior_gravity_literature", "experimental_precedent"}:
            assert not candidate_novelty, name

    candidates = [k for k, (_, c) in CLAIMS.items() if c]
    assert len(candidates) == 5
    print("candidate novelty claims", candidates)
    print("generic/prior claims", [k for k, (_, c) in CLAIMS.items() if not c])


if __name__ == "__main__":
    main()
