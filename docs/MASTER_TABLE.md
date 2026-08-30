# RQIR Operational Master Table

**Version:** 3.0  
**Date:** 2026-08-31  
**Authoritative scientific front:** **Iteration 128**.  
**Authority rule:** repository source of truth. RQIR remains separate from RTK/DSIR. No toy, Fisher, resource or detector-model result is an empirical new-physics claim.

> This v3.0 table is a **current operational compression**. Detailed historical numbers remain in their iteration documents, analysis scripts, research logs and recovery deltas. When an old convention conflicts with a later correction, the later named correction/closure document supersedes interpretation without deleting historical provenance.

## 1. Programme objective

RQIR reconstructs the operational gravity–quantum interface from distinguishable observables rather than assuming a preferred quantum-gravity theory.

Primary inference object:

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Exact rank/nullspace is not statistical identifiability. Physical comparisons must include source preparation, calibration, detector transfer/noise, controls, backaction and wall-clock rates in one consistent parameter coordinate.

## 2. Publication / readiness table

| Branch | Scientific status | Current readiness | Authority |
|---|---|---:|---|
| Paper I — operational hierarchy / finite discriminants | **CLOSED** at Iteration 078 | **100% scientific** | `docs/PAPER_I_SCIENTIFIC_CLOSURE_ITERATION078.md` |
| Paper II — statistical identifiability / nuisance geometry | **CLOSED** at Iteration 079 | **100% scientific** | `docs/PAPER_II_REFERENCE_LIKELIHOOD_CERTIFICATE_ITERATION079.md` |
| Paper III — physical resources / experiment architecture | **CLOSED** at Iteration 128 | **100% scientific; 97% submission** | `docs/PAPER_III_SCIENTIFIC_CLOSURE_ITERATION128.md` |
| Repository ready to start Candidate Gravity | entry pipeline available | **90%** | `docs/CANDIDATE_GRAVITY_ENTRY_CRITERIA.md` |
| Concrete Candidate-Gravity model | **not yet constructed** | **~10%** | future separate branch |

Readiness history: `docs/READINESS_TRACKER.md`.

## 3. Mature Toy009 / Toy010 baseline

Toy009 radii:

`(1.00000,1.60090005,1.77911036,2.60900799,5.90723562)`.

Balanced Iteration-011 geometry:

- `y1=-3.7766873837`;
- phases `(0,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067)`;
- exact rank `24/25`;
- positive hidden states;
- selected equality residual `<1e-15`.

Toy009/Toy010 exact mean/noise equality and ordered-response split remain the mature constructive reference behind Papers I–III.

## 4. Mandatory numerical / notation corrections

### NUM-001 — exact hard constraints

Trace+energy constraints must be eliminated analytically through the exact reduced/nullspace basis. Huge penalties plus thresholded pseudoinverses can delete real weak nuisance directions and generate false Fisher gains.

### NUM-002 — source-amplitude coordinate

Use the fractional hidden-source coordinate `alpha_h` with

`a = 0.08 alpha_h`,

so

`F_Q^(alpha_h)=0.08^2 F_Q^(a)`.

Toy009 full source QFI:

`F_Q^(alpha_h)=0.0849323916`

per ideal accepted single-branch source copy.

### NUM-004 — source amplitude is not drive amplitude

Keep source amplitude `alpha_h` separate from pump/drive impulse `epsilon_drv`.

### CAL-013 — centered covariance

Use centered noise/covariance derivatives rather than raw second moments unless raw moments are explicitly the measured observable.

Toy009 centered D2 baseline:

- `gamma_mean=1.830264703e6`;
- `gamma_cov=5.901272925e5`.

### NUM-006 / NUM-008 — final significance

Canonical manuscript convention:

`F_*=Z_final^2`,

`F_final=A_raw C_src/(A_raw+C_src)`.

At fixed retained fraction `r`:

`A_raw=F_*/r`,

`C_src=F_*/(1-r)`.

For final `Z_final=5`, `r=.90`:

`A_raw=27.7777777778`, `C_src=250`, `F_final=25`.

Historical `A_raw=25`, `C_src=225` remains only a **raw-5-sigma / 90%-retention regression** and gives

`F_final=22.5`, `Z_final=4.74341649`.

Do not describe `225` as a final-5-sigma certificate.

## 5. Retained structural no-go backbone

The following remain active as logical guards even after Paper-III closure:

- **NG-005:** an exact gravitational null cannot self-calibrate a multiplicative hidden source amplitude; independent source metrology or complementary calibration is required.
- **NG-006:** timing/geometry/additive nuisance directions can remain detector-degenerate at arbitrarily high science exposure.
- **NG-007:** a low-frequency stability floor above target cannot be repaired by white-noise averaging.
- **NG-019:** the retained 14 force means are not one disturbance-free multitime bundle; only seven same-time dual-probe pairs commute.
- **NG-021/022:** reciprocal probe information/backaction and full nuisance profiling limit same-copy shared-information gains.
- **NG-023:** QND with respect to isolated source `H` is not ordered-response nondemolition.
- **NG-025:** locality belongs inside source co-design; post-hoc truncation is not a valid locality proof.
- **NG-026:** full hard rank does not imply finite-noise/resource closure.
- **NG-030:** overlapping certified architecture intervals mean unresolved; a nominal central-value crossing is not a robust winner.
- **NG-054/055:** separate Fourier bins and high-SNR two-tone injection do not by themselves certify zero covariance or linear calibration.
- **NG-056/071:** free multiplicative transfer gain can absorb the science amplitude; in the two-band quotient common gain is beta-aligned and differential gain is spectral-tilt aligned.
- **NG-069/070:** transfer uncertainty is a likelihood-derived Fisher/covariance set; deterministic hard bounds and Gaussian prior budgets are different objects.
- **NG-072:** same hardware does not imply identical common-gain Fisher rates for Toy009/Toy014.
- **NG-073/074:** do not double-count shared records; more SNR in an unchanged setting cannot create missing Fisher directions.
- **NG-080:** do not splice incompatible experimental platforms into one apparatus forecast.
- **NG-082/083/084:** manuscript/reproducible/scientific closure is not apparatus-specific numerical closure.

Detailed historical no-go numbering remains in `docs/RECOVERY_GUIDE.md` and iteration documents.

## 6. Source metrology — mature physical bridge

Independent source metrology is a first-class resource.

Toy009 anchors:

- projective energy-population Fisher `F_E^(alpha_h)=0.0093918844`;
- full QFI ceiling `0.0849323916`;
- Ramsey zero-reset rate optimum `phi~1.09231`;
- `R/(p Omega_E)=0.0025234392`.

Strong source metrology remains on independent/sacrificial copies unless a same-copy nondemolition likelihood is explicitly proved.

For a copy Fisher `I_alpha,copy`, acceptance `p` and full copy cycle `tau_copy`:

`N_acc=C_src/I_alpha,copy`,

`R_A=p I_alpha,copy/tau_copy`.

For final design, source metrology belongs in the joint final-significance optimization rather than being fixed a priori at 90% retention.

## 7. Locality branch — retained conclusions

### Toy011

Exact nearest-neighbour dynamics can coexist with rank `24/25`, positive hidden states and nonzero ordered response, but the first Toy011 points were resource-poor.

### Toy012

Toy012 demonstrated that exact nearest-neighbour dynamics can recover near-Toy009 calibration efficiency while retaining a substantial detector-signal penalty. It remains an important locality-constrained historical design result.

### Toy014

Later source co-design produced the leading balanced exact-local comparator used in the mature Paper-III Toy009/Toy014 architecture certificates.

**Scope rule:** Paper III is now frozen; do not launch Toy015 merely to continue optimization. New source design belongs to a later branch unless a real contradiction or manuscript-required source gap appears.

## 8. Paper III — complete physical-resource backbone

### 8.1 Same-state science

For the retained two-band reduction,

`R_beta = 4 r2 r4/(r2+r4+2 rho sqrt(r2 r4))`.

Temporal `f,2f` covariance depends on the finite acquisition filters and full spectral density, not only on two scalar ASD values.

At the transparent balanced 90%-retention correlation benchmark:

`rho_hi=1/9`.

The ideal independent-Gaussian block certificate at `z=1.96` requires

`N_rho>=312`.

These are design/regression targets, not apparatus measurements.

### 8.2 Physical calibration rates

For scalar/template calibration:

`I_j = 4 int |d htilde_j/du_j|^2 / S_out,j(f) df`,

`R_cal,j = p_j I_j/tau_j`.

For a correlated simultaneous two-row layer use the full matrix Fisher block; a conservative scalar throughput is its weakest relevant eigenvalue after the declared coordinate mapping.

Seven-layer independent scheduling uses the appropriate harmonic-rate/time sum; shared records must instead enter the joint Fisher scheduler once.

### 8.3 Complex transfer calibration

Full complex transfer coordinates may be represented by

`x=(g2,g4,phi2,phi4)`.

After transforming to common/differential gain and profiling differential gain and phases, the common-gain reference rate is

`R_c = k_cc - k_cnu K_nunu^-1 k_nuc`.

Science plus a separate common-gain reference has the harmonic optimized rate

`R_DT = 1/[1/sqrt(R_s)+1/sqrt(R_c)]^2`.

### 8.4 Control recertification

Scalar control with usable variance budget `S=sigma_*^2-sigma_f^2`, Brownian convention `Var=D t/2`, and reference Fisher rate `R_ref` has

`sigma_ref^2=S/2`,

`t_ref*=2/(R_ref S)`,

`tau_live*=S/D`,

`r_min=2D/(R_ref S^2)`.

Complex gain/phase recertification is the matrix generalization

`(t_ref F_ref)^-1 + tau Q/2 <= S_matrix`.

### 8.5 Joint campaign / no-double-counting

For campaign Fisher matrices `J_k` and times `t_k`:

`J=sum_k t_k J_k=[[a,b^T],[b,N]]`,

`Phi(J)=a-b^T N^-1 b`.

The optimized rate is

`R_*=max_x Phi(sum_k x_k J_k)`

with a max-min robust extension under declared uncertainty.

For one mandatory nuisance quota `H_*` and one joint reference rate matrix `K_ref`:

`T_ref,*=lambda_max(K_ref^-1/2 H_* K_ref^-1/2)`.

One physical record receives one wall-clock charge.

### 8.6 Rank/span feasibility

Finite quota feasibility requires

`range(H_*) subseteq range(K_tot)`.

Repeating an unchanged four-real dual-tone setting cannot create missing score directions.

For the retained Toy009/Toy014 source nuisance basis:

- exact nuisance dimension: `22`;
- seven mean dual-probe layers: rank `14`;
- centered covariance complement: rank `8`;
- combined: full rank `22`.

### 8.7 Covariance endpoint / backaction structure

The full eight-row covariance endpoint graph has a four-matching optimum within the declared cross-covariance-only detector-output class. This output-level sharing result does **not** waive NG-019: quantum-source sharing across noncommuting times requires an explicit measurement/backaction likelihood.

### 8.8 Detector-side architecture interval

Science, common-gain transfer, mean calibration and covariance calibration rates propagate into a certified interval for

`u=R_D14/R_D09`.

This is the correct Paper-III detector-side result when same-apparatus absolute rates are unavailable.

### 8.9 Final detector+source architecture certificate

Define

`u=R_D14/R_D09`,

`v=R_A14/R_A09`,

`z=R_A09/R_D09`,

`delta=(1-d14)/(1-d09)`.

Then

`Q14/Q09 = delta[(1+z^-1/2)/(u^-1/2+(v z)^-1/2)]^2`.

A robust architecture winner requires NG-030 interval separation.

## 9. Paper III external-evidence / novelty boundary

External literature audits establish prior/component feasibility for:

- nuisance-aware Fisher/OED;
- system identification and transfer calibration;
- gravity-test resource/feasibility studies including QGEM;
- classical/stochastic/postquantum gravity observables;
- measurement-disturbance/interferometric tests;
- calibrated force sensing, cross-spectral/multimode sensing and exact fundamental/second-harmonic operation.

No inspected source supplied the complete compatible same-apparatus RQIR closure vector.

**PRIORITY-001:** the defendable candidate Paper-III contribution is the **RQIR-specific end-to-end integration/closure discipline**, not invention of any constituent Fisher/OED, force sensing, cross-spectrum, QGEM or gravity-test method. This is a finite-search statement, not proof of global priority; refresh literature before submission.

## 10. Paper III scientific closure — Iteration 128

**Decision:** **CLOSED — 100% scientific-content readiness for the frozen resource/design/certificate scope.**

Authority:

`docs/PAPER_III_SCIENTIFIC_CLOSURE_ITERATION128.md`.

The closed chain is

`interface discriminant -> exact constraints/source calibration -> detector nuisance profile -> source metrology -> transfer/cross-PSD calibration -> calibration span/backaction/no-double-counting -> physical Fisher rates -> robust wall clock -> final architecture certificate`.

### NG-084

Scientific closure is **not** apparatus closure. Paper III does not claim:

- a measured RQIR signal;
- a same-apparatus numerical runtime;
- an experimentally established Toy009/Toy014 winner.

### Conditional apparatus extension

If a numerical apparatus verdict is desired, obtain within one compatible likelihood/accounting:

1. same-state two-band science transduction and PSD/cross-PSD;
2. full complex transfer-reference Fisher-rate matrix;
3. seven physical calibration Fisher-rate matrices and uncertainty correlations;
4. geometry/additive reference Fisher and drift/floor models;
5. a physical measurement/backaction likelihood if covariance-sharing credit is used;
6. measured source-metrology rate and duty;
7. a robust `u` interval narrow enough for NG-030.

These instantiate the completed theory; they are not hidden Paper-III prerequisites.

## 11. Reproducibility / manuscript authorities

- manuscript skeleton: `docs/PAPER_III_MANUSCRIPT_SKELETON_ITERATION124.md`;
- canonical notation/dependencies: `docs/PAPER_III_NOTATION_DEPENDENCY_AUDIT_ITERATION125.md`;
- reviewer-scale reproducibility manifest: `docs/PAPER_III_REPRODUCIBILITY_MANIFEST_ITERATION126.md`;
- final priority audit: `docs/PAPER_III_FINAL_PRIORITY_AUDIT_ITERATION127.md`;
- scientific closure: `docs/PAPER_III_SCIENTIFIC_CLOSURE_ITERATION128.md`;
- readiness history: `docs/READINESS_TRACKER.md`.

Figure/table provenance classes are:

`DERIVATION`, `DETERMINISTIC_REGRESSION`, `PARAMETRIC_SPECIFICATION`, `EXTERNAL_EVIDENCE`, `MEASURED_APPARATUS`.

Current Paper III has no complete `MEASURED_APPARATUS` RQIR closure dataset.

## 12. Current priority after v3.0

### Paper III

Scientific research scope is frozen. Remaining work is submission production:

1. generate/canonicalize figures and tables from the Iteration-126 manifest;
2. draft/polish prose from the Iteration-124 skeleton;
3. refresh the literature/priority audit immediately before submission;
4. run one independent clean/reviewer-style reproduction pass;
5. apply journal-specific references/style/formatting.

### Candidate Gravity — separate next research branch

The repository is approximately **90% ready to start** a concrete Candidate-Gravity model because Papers I–III now supply the discriminant -> identifiability -> resource/measurability test pipeline.

The **concrete model itself remains ~10%**. Begin from `docs/CANDIDATE_GRAVITY_ENTRY_CRITERIA.md`; QG-001…QG-010 have not yet been passed.

A future candidate must supply its own state space, dynamics, constraints/gauge structure, controlled GR/Newtonian and flat-QFT limits, conservation/Bianchi/Ward consistency, causal structure, positivity/unitarity/CP as appropriate, EFT/renormalization consistency, model-degeneracy comparison and detector/resource propagation through RQIR I–III.

## 13. Scope-freeze rule

**P3-CLOSE-001:** absent a documented contradiction, failed regression or materially relevant new requirement, do not reopen Paper III merely to continue the iteration count. Toy015/new source searches belong to later work unless a manuscript review shows they are required by the frozen claim.
