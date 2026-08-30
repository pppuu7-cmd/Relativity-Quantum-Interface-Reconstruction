# RQIR Iteration 125 — Paper III Canonical Notation and Dependency Audit

**Date:** 2026-08-31  
**Status:** manuscript-facing notation/provenance closure. No apparatus forecast and no new-physics claim.

## 1. Purpose

Iteration 124 showed that the Paper-III scientific chain is structurally complete. The remaining editorial risk was that historical resource conventions could be mistaken for the final-significance convention used by the manuscript. The most important example is the old `C_prep=225` benchmark.

This iteration freezes the canonical notation and dependency rules for Paper III without rewriting historical research files.

## 2. Canonical significance notation

Use:

- `F_* = Z_final^2` — required **final nuisance-profiled** Fisher target;
- `A_raw` — raw detector/science Fisher before profiling an exactly aligned multiplicative source-amplitude nuisance;
- `C_src` — independent source-amplitude Fisher;
- `r = F_final/A_raw` — retained fraction when a fixed-retention slice is deliberately used.

For the aligned source-amplitude geometry,

`F_final = A_raw C_src/(A_raw+C_src)`.

If a final target `F_*=Z_final^2` and fixed retained fraction `r` are imposed, then

`boxed{A_raw = F_*/r}`

and

`boxed{C_src = F_*/(1-r)}`.

For `Z_final=5`, `r=0.90`:

- `A_raw=27.7777777778`;
- `C_src=250`;
- `F_final=25` exactly.

### RQIR-NUM-008 — historical `225` supersession rule

The pair

`A_raw=25`, `C_src=225`

is retained as a valid historical **raw-5-sigma / 90%-retention regression**. It gives

`F_final=22.5`, `Z_final=4.74341649`.

Therefore Paper III must never describe `C_src=225` as a final-5-sigma certificate. Historical files are not rewritten; the manuscript-facing convention supersedes only their interpretation.

The preferred final-design calculation is still the jointly optimized science/source schedule from Iteration 104 rather than an arbitrary fixed `r`.

## 3. Canonical rate symbols

The manuscript-facing symbols are frozen as follows.

| Symbol | Meaning | Units / semantics |
|---|---|---|
| `R_s` or `R_sci` | raw detector science Fisher rate before independent source-amplitude closure | Fisher / wall second |
| `R_c` | phase-profiled common-transfer-gain reference Fisher rate | Fisher / wall second |
| `R_cal,j` | physical Fisher rate for calibration block/layer `j` in its declared nuisance coordinates | Fisher / wall second or matrix Fisher rate |
| `R_A` | independent source-amplitude metrology Fisher rate | Fisher / wall second |
| `R_D` | effective detector-side rate after science, transfer, calibration and declared detector/control scheduling | final detector-side Fisher / wall second |
| `F_*` | final Fisher target | dimensionless Fisher |
| `Z_final` | final target significance | `sqrt(F_*)` in the local unit-displacement convention |
| `d` | information-free wall-clock duty fraction only | dimensionless |

A reference campaign that carries nuisance Fisher is **not** represented solely by `d`; it belongs in the campaign Fisher schedule (Iterations 103, 107, 116).

## 4. Canonical architecture variables

For Toy014 relative to Toy009:

`boxed{u = R_D14/R_D09}`,

`boxed{v = R_A14/R_A09}`,

`boxed{z = R_A09/R_D09}`,

`boxed{delta = (1-d14)/(1-d09)}`.

The final architecture ratio is

`boxed{Q14/Q09 = delta[(1+z^-1/2)/(u^-1/2+(v z)^-1/2)]^2}`.

Use `Q_i` only for the final duty-adjusted effective rate/throughput in this architecture comparison; do not reuse `Q` for source basis matrices inside the manuscript without an explicit local qualifier.

## 5. Canonical nuisance/profile notation

Primary detector inference object:

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

For campaign Fisher matrix

`J=[[a,b^T],[b,N]]`,

use

`Phi(J)=a-b^T N^-1 b`.

Exact hard constraints are eliminated before this profile. Singular supports must use exact support reduction / declared pseudoinverse geometry; arbitrary threshold deletion remains forbidden by NUM-001.

For common complex transfer:

- physical gain/phase coordinates may be `x=(g2,g4,phi2,phi4)`;
- common/differential basis may be `y=(c,d_g,phi2,phi4)`;
- write the **differential gain** as `d_g` in manuscript prose/equations to avoid collision with wall-clock duty `d`.

This is a manuscript-level disambiguation; historical Iteration-114/115 code using local `d` remains valid.

## 6. Source-amplitude coordinate rule

The physical hidden source coordinate remains the fractional amplitude `alpha_h` where the older physical amplitude obeys

`a = 0.08 alpha_h`.

Thus

`F_Q^(alpha_h)=0.08^2 F_Q^(a)`.

Keep `epsilon_drv` for pump/drive impulse amplitude. Do not use `alpha` for both source preparation and drive strength. This preserves NUM-004 and NUM-002.

## 7. Claim-to-authority dependency map

The minimum manuscript authority chain is frozen as:

| Paper-III claim | Canonical authority |
|---|---|
| nuisance-profiled detector information | `docs/PAPER_II_REFERENCE_LIKELIHOOD_CERTIFICATE_ITERATION079.md` plus Paper-III detector likelihoods |
| physical source-preparation Fisher / shots | Iterations 047–058, 068, 098, 104 |
| science two-band/cross-PSD rate | Iterations 084–087, 101–103 |
| transfer common-gain profile/rate | Iterations 112–115 |
| seven-layer calibration physical rate/uncertainty | Iterations 068–070, 088, 118–121 |
| no-double-counted joint references | Iteration 116 |
| span/rank feasibility | Iterations 117–119 |
| robust detector ratio `u` | Iterations 106, 111, 120–121 |
| final `(u,v,z,delta)` certificate | Iterations 104–105 |
| external apparatus boundary | Iteration 122 |
| novelty/claim boundary | Iteration 123 |
| manuscript claim structure | Iteration 124 |

Older documents remain provenance/regression evidence but cannot silently override later correction/closure documents.

## 8. Historical numbering and alias policy

The repository contains historical duplicated/reindexed iteration labels from the early development period (for example the old Iteration-011/012 naming and the canonical reindexing around Toy012/Iteration 055–056). These are already documented in recovery files.

### RQIR-CAL-025 — do not renumber historical provenance

Do not rewrite old filenames/commits merely to obtain a visually consecutive historical numbering scheme. Manuscript citations should use the canonical named result/gate and the current authority chain. Recovery documents preserve aliases.

For the manuscript-facing late front (Iterations 078–125), use the current unique named documents and gate labels as authority.

## 9. Dependency rule for apparatus claims

The following are different claim classes and must remain separate:

1. exact theorem/derivation;
2. deterministic toy regression;
3. externally demonstrated component capability;
4. parameterized apparatus specification;
5. same-apparatus numerical forecast.

Iteration 122 shows that item 3 exists for many needed components but the compatible input vector for item 5 is not publicly complete. Therefore no numerical Toy009/Toy014 apparatus winner is part of scientific closure.

## 10. Reproducibility regression

`analysis/paper3_notation_dependency_audit_iteration125.py` verifies:

- historical `(25,225) -> F=22.5 -> Z=4.74341649`;
- final-5-sigma fixed-90% pair `(27.7777778,250) -> F=25`;
- rate-dependent optimal retention;
- 90% optimum only at `R_A/R_s=81`;
- canonical definitions of `(u,v,z,delta)`.

## 11. Readiness snapshot — Iteration 125

Project-management estimates, not statistical confidence measures:

- **Paper III scientific-content readiness:** **97%**.
- **Paper III submission readiness:** **89%**.
- **Repository readiness to begin a concrete Candidate-Gravity model:** **86%**.
- **Concrete Candidate-Gravity model itself:** **~10%**.

The increase comes from freezing the manuscript semantics and removing the main final-significance ambiguity. No apparatus-specific evidence was added.

## 12. Next gate

Build the minimum Paper-III reproducibility manifest:

- one command per manuscript-bearing numerical/regression result;
- expected invariant/output for each command;
- distinction between deterministic code regressions and external-evidence tables;
- dependency order and environment assumptions;
- explicit statement of which figures/tables are generated from parameterized rather than measured inputs.

After that, perform one final literature/priority audit before scientific closure.