# Candidate Gravity — Iteration 167

## Conserved-TT source map and constant-log-null spectral shape quotient

**Date:** 2026-08-31  
**MODEL_READINESS:** **24%** (unchanged)

## Objective

Iteration 166 found an observable type that cannot be saturated by an arbitrary local Hermitian tree derivative tower: the off-pole timelike odd absorptive part of a retarded response. However, the leading nonzero constant logarithmic onset is already shared by perturbative C5 and Lorentzian asymptotic safety.

Iteration 167 asks whether we can remove this universal leading direction **before** any Candidate Gravity target is evaluated, while keeping an operational conserved-source map.

## Observable clarification

The Iteration-166/167 quantity is

`A_odd(s)=[Im chi1R(+omega)-Im chi1R(-omega)]/(2*pi)`.

It is the frequency-odd absorptive part of the **linear** retarded susceptibility `chi1R`.

It is **not** the post-Gaussian second-order causal coordinate `chi2R_odd` from the higher-response contract. These two notions of `odd` must not be conflated in the model paper.

## Conserved source completion of the linear TT shape

Use timelike momentum

`k=(omega,0,0,0)`

on the same eight rows

`s=omega^2=0.004,0.008,...,0.032`.

Freeze the external source and detector stress tensor

`T_0mu=0`,

`T_ij=diag(1,-1,0)/sqrt(2)`.

It is spatial, traceless and conserved for every row. With the standard D=4 spin-2 projector,

`T:P2:T=1`.

Regression over all eight rows gives

- maximum conservation error: `0`;
- maximum trace error: `0`;
- maximum projector error: `0`;
- maximum overlap deviation from one: `2.22e-16`.

Therefore the scoped linear source-to-source response has the form

`A_R(s) = common_gain * G_R^TT(s)`

with a frequency-independent tensor/source overlap. The common coupling/field normalization may be calibrated at the GR pole and/or profiled; it does not create spectral shape.

Retain:

**ABS-SHAPE-001 — `CONSERVED_TT_SOURCE_MAP_PRESERVES_TIMELIKE_SPECTRAL_SHAPE`.**

This is a linear source-map statement only. It does not close the nonlinear detector or `chi2R` problem.

## Target-independent constant-log quotient

Define

`x_i=s_i/s_max=i/8`.

Construct the full Vandermonde matrix

`V=[1,x,x^2,...,x^7]`.

A deterministic QR factorization gives an orthonormal constant direction `q0` and seven orthonormal columns `Q_shape` spanning its orthogonal complement.

The quotient is

`y_shape = Q_shape^T A_odd`.

Properties:

- row dimension: `8`;
- profiled universal direction: `1`;
- remaining shape dimension: `7`;
- maximum `|Q_shape^T 1| = 2.22e-16`;
- orthonormality error: `4.44e-16`.

The leading perturbative-C5 massless logarithm is a constant absorptive vector, hence

`||Q_shape^T v_C5_log|| = 3.80e-16`.

The leading IR Lorentzian-AS logarithm is proportional to the same constant, hence

`||Q_shape^T v_AS_IR|| = 1.44e-16`.

Thus both are removed to machine precision **without using a Candidate Gravity target**.

Retain:

**ABS-SHAPE-002 — `CONSTANT_LOG_NULL_QUOTIENT_LEAVES_SEVEN_SUBLEADING_SHAPE_DIMENSIONS`.**

**NG-FUNNEL-026 — `PROFILE_UNIVERSAL_IR_LOG_BEFORE_SUBLEADING_SPECTRAL_SHAPE_SEARCH`.**

## Does the quotient retain useful information?

Yes. As a target-independent capacity audit, project the three simple shapes

`x`, `x^2`, `x^3`.

Their quotient matrix has rank `3/3` with singular values

`[1.5426185527, 0.2275834312, 0.02224505048]`.

So removing the universal constant does not collapse the protocol; it retains genuine finite-frequency shape information.

This is **not** a claim that these three shapes are Candidate Gravity directions or three independent C5 loop parameters.

## Optional high-pass diagnostic

A fourth finite difference with coefficients

`[1,-4,6,-4,1]`

annihilates every polynomial absorptive envelope through cubic order exactly on equally spaced rows. However its single-window white-noise amplification is

`sqrt(70)=8.3666002653`.

Therefore it is retained only as a diagnostic and is **not** adopted as the primary protocol. The orthonormal quotient is better conditioned and lets actual comparator columns determine what must be removed.

## Lorentzian AS finite-frequency boundary

The self-consistent Lorentzian AS result is now published as

J. M. Pawlowski, M. Reichert, J. Wessely, *Self-consistent graviton spectral function in Lorentzian quantum gravity*, **Physics Letters B 880 (2026) 140844**, DOI `10.1016/j.physletb.2026.140844`, arXiv:2507.22169.

The paper supports:

- a positive massless peak;
- a positive scattering continuum;
- the universal constant IR onset;
- a decrease of the continuum at intermediate frequencies;
- UV decay proportional to `1/[lambda^2 log^3(lambda^2)]`.

Hence the AS vector in the seven-dimensional quotient is **not generally zero** outside the strict IR leading term.

The paper publishes the curve and analytic limits, but the repository does not have a numerical dataset for the finite-frequency curve and we have not reproduced the full spectral-flow computation. A visual plot may not be converted into a precision comparator tangent by wishful digitization.

Therefore:

`AS finite-frequency shape = BLOCKED_NUMERICAL_SPECTRAL_DATA_OR_CONTROLLED_REPRODUCTION_REQUIRED`.

Retain:

**NG-FUNNEL-027 — `PUBLISHED_SPECTRAL_CURVE_IS_NOT_A_NUMERICAL_COMPARATOR_COLUMN_WITHOUT_DATA_OR_CONTROLLED_REPRODUCTION`.**

## C5 boundary

The universal leading massless-log direction is removed, but sub-leading loop orders, higher-derivative insertions and physical thresholds have not yet been frozen in the same source convention.

Therefore:

`C5 sub-leading absorptive shape = BLOCKED_SOURCE_COMPLETED_LOOP_ORDER_SPECIFICATION`.

No sub-leading residual may be called Candidate Gravity until this C5 block and the supported AS finite-frequency block are instantiated or bounded.

## Candidate state

No robust Candidate Gravity residual exists yet.

`ANSATZ-003`: **NOT CREATED**.  
Fisher/resources: **FORBIDDEN**.

`MODEL_READINESS = 24%` remains unchanged. The source/shape ambiguity is substantially reduced, but no comparator-subtracted sub-leading direction is yet established.

## Exact next gate — Iteration 168

1. Freeze C5 loop order/power counting in the conserved-TT absorptive source channel.
2. Determine analytically which massless one-loop source-response shapes survive the constant-log quotient.
3. Separate genuinely new shape directions from two-loop/higher-derivative C5 truncation uncertainty.
4. Treat the published finite-frequency AS continuum as BLOCKED until numerical data are obtained or its spectral flow is reproduced; do not infer values from a plot alone.
5. Only after the authorized C5 sub-leading span is frozen should the next observable null/filter be designed.
