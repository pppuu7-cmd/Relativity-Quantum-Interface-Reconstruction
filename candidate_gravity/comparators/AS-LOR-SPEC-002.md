# AS-LOR-SPEC-002 — Lorentzian asymptotic-safety spectral comparator

**Frozen:** Iteration 166, 2026-08-31  
**Refined:** Iteration 167, 2026-08-31  
**Status:** FIXED_SCOPED_LINEAR_TIMELIKE_COMPARATOR  
**Not a Candidate Gravity ansatz.**

## Role

`AS-FRG-TT-001` remains the action/vertex comparator reconstructed mainly from Euclidean FRG data and still requires an explicit real-time prescription for its nonlinear off-shell RQIR map.

`AS-LOR-SPEC-002` is a separate comparator record for a genuinely Lorentzian two-point/spectral sector. It is based on:

- J. Fehre, D. F. Litim, J. M. Pawlowski, M. Reichert, *Lorentzian quantum gravity and the graviton spectral function*, arXiv:2111.13232 / Phys. Rev. Lett. 130, 081501 (2023);
- J. M. Pawlowski, M. Reichert, J. Wessely, *Self-consistent graviton spectral function in Lorentzian quantum gravity*, arXiv:2507.22169; **Physics Letters B 880 (2026) 140844**, DOI `10.1016/j.physletb.2026.140844`.

The self-consistent calculation is the primary authority for the frozen IR block because it feeds the full spectral function back into the flow and uses physical on-shell renormalisation.

## Published Lorentzian structure

For the scalar TT propagator `G_hh`, the source uses a Källén–Lehmann representation

`G_hh(p^2)=int_0^inf d(lambda) lambda/pi rho_h(lambda)/(lambda^2+p^2)`.

The spectral function is obtained from the retarded propagator via

`rho_h(omega)=2 Im G_hh(p^2 -> -(omega+i0)^2)`.

At `k=0` and vanishing physical cosmological constant, the spectral function contains

- a massless one-graviton pole;
- a positive multi-graviton / graviton-ghost scattering continuum.

The reported spectral sum normalisation is approximately

`z_spec ~= 1.486`, before the final physical-field rescaling.

The published finite-frequency continuum is not constant: it approaches the universal IR value near zero frequency and decreases at intermediate scales before entering its UV falloff.

## Controlled IR limit

The paper gives

`G_hh^ph = z_spec^-1 [1/p^2 - A_h log(p^2) + sub-leading]`,

with

`A_h = 61/(60*pi) = 0.32361505095352056`.

The unnormalised continuum onset is

`rho_tail(lambda -> 0) = 61/30 ~= 2.033333333333333`,

while after the reported physical-field normalisation it is approximately

`(61/30)/1.486 ~= 1.3683266038582322`.

The paper explicitly notes that the coefficient is scheme independent but gauge dependent in this TT fluctuation-field representation.

## RQIR Iteration-166 map

The Iteration-166 observable is a frequency-odd absorptive projection of the **linear** response `chi1R`, not the post-Gaussian `chi2R_odd` coordinate:

`A_odd(s)=[Im chi1R(+omega)-Im chi1R(-omega)]/(2*pi)`.

The leading IR AS logarithm gives a constant shape across positive `s`.

After allowing an overall source/field gain, this shape is exactly collinear with the leading perturbative-C5 massless-loop logarithmic direction:

`rank([v_C5_log, v_AS_IR])=1`.

On the eight Iteration-166 rows the numerical normalized projection residual is

`1.7153451629555285e-16`.

Classification:

**AS-NG-004 — `LORENTZIAN_AS_LEADING_IR_LOG_IS_COLLINEAR_WITH_C5_MASSLESS_LOOP_SHAPE`.**

This is a controlled leading-IR shape relation, not a finite-frequency theory identity.

## Iteration-167 conserved-source shape completion

Freeze the timelike source momentum

`k=(omega,0,0,0)`

and the conserved traceless external stress/source tensor

`T_0mu=0`,

`T_ij=diag(1,-1,0)/sqrt(2)`.

For the standard timelike spin-2 projector this satisfies on all eight rows

- conservation error `0`;
- trace error `0`;
- projector error `0`;
- `T:P2:T = 1` up to `2.22e-16`.

Thus in this scoped linear TT source-to-source channel the tensor/source overlap is frequency independent. The spectral **shape** of the source response is exactly the TT propagator shape up to a common coupling/field gain.

Iteration 167 therefore profiles the universal constant-log direction before evaluating any sub-leading shape. The resulting seven-dimensional orthonormal shape quotient gives

- C5 leading-log projected norm `3.80e-16`;
- AS leading-IR-log projected norm `1.44e-16`.

Retain:

**ABS-SHAPE-001 — `CONSERVED_TT_SOURCE_MAP_PRESERVES_TIMELIKE_SPECTRAL_SHAPE`.**

**NG-FUNNEL-026 — `PROFILE_UNIVERSAL_IR_LOG_BEFORE_SUBLEADING_SPECTRAL_SHAPE_SEARCH`.**

## Physical-normalisation boundary

The published `A_h` is a TT fluctuation-field coefficient. The conserved-TT shape map above eliminates frequency-independent source overlap and allows the universal constant shape to be profiled, but it does **not** turn the published finite-frequency spectral curve automatically into a complete operational RQIR comparator.

For a finite-frequency AS shape column RQIR still requires either

1. the numerical spectral data in a controlled normalisation, or
2. an independent reproduction of the spectral-flow result at the frozen frequencies.

Therefore:

- existence of the AS continuum: SUPPORTED;
- universal leading IR logarithmic shape: SUPPORTED and profiled;
- source-overlap preservation of TT spectral shape in the frozen linear channel: PASS_SCOPED;
- finite-frequency sub-leading AS shape column: `BLOCKED_NUMERICAL_SPECTRAL_DATA_OR_CONTROLLED_REPRODUCTION_REQUIRED`;
- AS nonlinear `chi2R_even/odd`, `N2`, and `C3sym`: outside this comparator record / BLOCKED.

Retain:

**NG-FUNNEL-025 — `BARE_TT_SPECTRAL_COEFFICIENT_IS_NOT_YET_A_SOURCE_COMPLETED_RQIR_OBSERVABLE`.**

**NG-FUNNEL-027 — `PUBLISHED_SPECTRAL_CURVE_IS_NOT_A_NUMERICAL_COMPARATOR_COLUMN_WITHOUT_DATA_OR_CONTROLLED_REPRODUCTION`.**

## Reproducibility

- `analysis/timelike_absorptive_protocol_iteration166.py`;
- `results/timelike_absorptive_protocol_iteration166.json`;
- `candidate_gravity/TIMELIKE_ABSORPTIVE_PROTOCOL_ITERATION166.md`;
- `analysis/absorptive_shape_quotient_iteration167.py`;
- `results/absorptive_shape_quotient_iteration167.json`.
