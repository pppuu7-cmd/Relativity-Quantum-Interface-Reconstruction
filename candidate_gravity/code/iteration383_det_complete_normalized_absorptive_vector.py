#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / "candidate_gravity" / "results"
REC = ROOT / "candidate_gravity" / "recovery"

def load(name):
    return json.loads((R / name).read_text())

i333 = load("iteration333_det_direct_timelike_discontinuity_family_reduction.json")
i380 = load("iteration380_det_triangle_q2minus1_analytic_azimuth_reduction.json")
r337 = (REC / "RECOVERY_DELTA_ITERATION_337.md").read_text()
r338 = (REC / "RECOVERY_DELTA_ITERATION_338.md").read_text()

assert i333["scientific_gate_pass"] is True and i333["iteration"] == 333
assert i380["scientific_gate_pass"] is True and i380["iteration"] == 380
assert len(i333["bubble_families"]) == 3
assert len(i333["triangle_family"]["channels"]) == 3
# Provenance-only text checks.  Iteration 337 records the full bridge
# D_s I[F] = -8*pi*int dPhi2 F = -sphere_mean(F), not the shortened form.
assert "D_s I[F] = -8*pi" in r337 and "= - sphere_mean(F)" in r337
assert "D_s Gamma_det = -i*m" in r338

# Canonical three coordinates.  They remain distinct and are never summed.
Q2 = (-1.0, -0.34, -0.14)

def key(q):
    return min(Q2, key=lambda x: abs(x-float(q)))

bubbles = {}
for row in i333["bubble_families"]:
    q = key(row["q2"])
    assert row["status"] == "NONZERO_TWO_PARTICLE_DISCONTINUITY_CERTIFICATE"
    assert abs(q-float(row["q2"])) < 1e-12
    assert q not in bubbles
    bubbles[q] = float(row["cut_proxy_degree7"])
assert set(bubbles) == set(Q2)

triangles = {}
for row in i333["triangle_family"]["channels"]:
    q = key(row["q2"])
    if q == -1.0:
        # Iteration 333 was numerically BLOCKED here; it may not be used.
        assert row["status"] == "BLOCKED_NEAR_CANCELLATION_OR_CUBATURE_CONVERGENCE"
        continue
    assert row["status"] == "NONZERO_TWO_PARTICLE_CHANNEL_DISCONTINUITY_CERTIFICATE"
    assert abs(q-float(row["q2"])) < 1e-12
    assert q not in triangles
    triangles[q] = float(row["cut_proxy"])

assert i380["classification"] == "PASS_DET_TRIANGLE_Q2_MINUS1_ANALYTIC_AZIMUTH_REDUCTION_NONZERO_DISCONTINUITY"
assert abs(float(i380["q2"])+1.0) < 1e-15
assert float(i380["direct_sparse_crosscheck"]["scaled_disagreement"]) < float(i380["thresholds"]["unchanged_discontinuity_scaled_convergence_max"])
triangles[-1.0] = float(i380["analytic_sphere_mean"][0])
assert set(triangles) == set(Q2)

coordinates = []
for q in Q2:
    b = bubbles[q]
    t = triangles[q]
    m = b + t
    # Frozen bridge: D_s C_det=-m; Gamma_det=+i C_det; therefore D_s Gamma_det=-i m.
    ds_cdet = -m
    ds_gamma = [0.0, -m]
    coordinates.append({
        "q2": q,
        "bubble_normalized_angular_mean": b,
        "triangle_normalized_angular_mean": t,
        "total_normalized_angular_mean": m,
        "D_s_C_det": ds_cdet,
        "D_s_Gamma_det_complex": ds_gamma,
        "status": "NONZERO" if abs(m) > 0.0 else "ZERO"
    })

assert all(c["status"] == "NONZERO" for c in coordinates)
assert len({c["q2"] for c in coordinates}) == 3

out = {
    "iteration": 383,
    "classification": "PASS_COMPLETE_CHANNEL_RESOLVED_NORMALIZED_DETERMINANT_ORDINARY_SIMPLE_CUT_ABSORPTIVE_VECTOR",
    "scientific_gate_pass": True,
    "candidate_residual": False,
    "model_readiness_percent": 24,
    "input_authorities": {
        "family_and_two_converged_triangle_channels": 333,
        "q2_minus1_triangle_replacement": 380,
        "simple_cut_normalization_bridge": 337,
        "determinant_outer_effective_action_prefactor": 338
    },
    "family_counts": {"bubble": 3, "triangle": 3, "q2_coordinates": 3},
    "coordinates": coordinates,
    "normalization": {
        "D_s_C_det": "-sphere_mean",
        "Gamma_det": "+i*C_det",
        "D_s_Gamma_det": "-i*sphere_mean",
        "internal_graviton_ghost_weights_reapplied": False
    },
    "guardrails": [
        "DISTINCT_Q2_COORDINATES_NOT_SUMMED",
        "ITERATION333_BLOCKED_Q2_MINUS1_TRIANGLE_VALUE_NOT_USED",
        "ITERATION380_VALUE_USED_ONLY_FOR_Q2_MINUS1_TRIANGLE",
        "NO_DOUBLE_APPLICATION_OF_DETERMINANT_WEIGHTS",
        "ITERATION297_FINITE_DR_WARNING_REMAINS_BINDING",
        "NO_SOURCE_BORN_SUBTRACTION",
        "NO_ANSATZ003",
        "NO_FISHER_RESOURCES"
    ],
    "scope": "ordinary two-simple-particle determinant cut vector only; not the full finite-DR determinant, not source-completed, not comparator-subtracted",
    "next_gate": "retain this vector as determinant ordinary-simple origin accounting; continue active TrU1sq/TrU2 repeated-cut closures, then perform Source/Ward/contact completion and matched K2 subtraction only after operator coordinates are complete"
}
print(json.dumps(out, indent=2, sort_keys=True))
