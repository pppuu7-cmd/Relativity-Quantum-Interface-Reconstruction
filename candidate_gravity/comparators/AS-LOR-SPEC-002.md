# AS-LOR-SPEC-002 — Lorentzian asymptotic-safety spectral comparator

**Frozen:** Iteration 166, 2026-08-31  
**Status:** FIXED_SCOPED_LINEAR_TIMELIKE_COMPARATOR  
**Not a Candidate Gravity ansatz.**

## Role

`AS-FRG-TT-001` remains the action/vertex comparator reconstructed mainly from Euclidean FRG data and still requires an explicit real-time prescription for its nonlinear off-shell RQIR map.

`AS-LOR-SPEC-002` is a separate comparator record for a genuinely Lorentzian two-point/spectral sector. It is based on:

- J. Fehre, D. F. Litim, J. M. Pawlowski, M. Reichert, *Lorentzian quantum gravity and the graviton spectral function*, arXiv:2111.13232 / PRL 130, 081501 (2023);
- J. M. Pawlowski, M. Reichert, J. Wessely, *Self-consistent graviton spectral function in Lorentzian quantum gravity*, arXiv:2507.22169 (2025).

The 2025 calculation is the primary authority for the frozen IR block because it feeds the full spectral function back self-consistently and uses physical on-shell renormalisation.

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

Use the frozen odd absorptive pre-protocol

`A_odd(s)=[Im chi_R(+omega)-Im chi_R(-omega)]/(2*pi)`.

The leading IR AS logarithm gives a constant shape across positive `s`.

After allowing an overall source/field gain, this shape is exactly collinear with the leading perturbative-C5 massless-loop logarithmic direction:

`rank([v_C5_log, v_AS_IR])=1`.

On the eight Iteration-166 rows the numerical normalized projection residual is

`1.7153451629555285e-16`.

Classification:

**AS-NG-004 — `LORENTZIAN_AS_LEADING_IR_LOG_IS_COLLINEAR_WITH_C5_MASSLESS_LOOP_SHAPE`.**

This is a controlled leading-IR shape relation, not a finite-frequency theory identity.

## Physical-normalisation boundary

The published `A_h` is a TT fluctuation-field coefficient. RQIR ultimately requires a conserved-source / detector transfer built from the same physical metric convention used by the rest of the funnel, including all source/vertex pieces needed for a gauge-invariant operational quantity.

Therefore:

- the **existence and leading logarithmic shape** of the AS continuum is SUPPORTED;
- the **source-completed RQIR amplitude** is BLOCKED;
- sub-leading finite-frequency shape on the Iteration-166 rows is BLOCKED unless extracted from the published numerical spectral function in a compatible normalization;
- AS nonlinear `chi2R_even/odd`, `N2`, and `C3sym` remain outside this comparator record.

Retain:

**NG-FUNNEL-025 — `BARE_TT_SPECTRAL_COEFFICIENT_IS_NOT_YET_A_SOURCE_COMPLETED_RQIR_OBSERVABLE`.**

## Reproducibility

- `analysis/timelike_absorptive_protocol_iteration166.py`;
- `results/timelike_absorptive_protocol_iteration166.json`;
- `candidate_gravity/TIMELIKE_ABSORPTIVE_PROTOCOL_ITERATION166.md`.
