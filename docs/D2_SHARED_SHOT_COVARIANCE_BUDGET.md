# RQIR Iteration 038 — D2 Shared-Shot Covariance Budget and Coherence Break-Even

**Date:** 2026-08-29  
**Scope:** corrected centered D2 covariance resource layer after Iterations 034–037.  
**Status:** apparatus-neutral Fisher/resource bound; no new-physics claim.

## 1. Question

Iteration 037 showed that a single `m`-dimensional affine Gaussian covariance readout has an `m/2` Fisher ceiling for one full-range amplitude coordinate. It also suggested that a joint output could be cheaper than measuring the high-value covariance rows `(0,1,3,7)` in four independent campaigns.

The correct next question is stronger:

> If one shared detector cycle measures all four covariance coordinates at once, how much **multi-parameter** covariance Fisher can that one cycle contain while the Gaussian covariance remains physical for independent variations of all four coordinates?

This iteration derives the corresponding matrix-Fisher budget and combines it with the actual Toy009 coherence floor and the corrected source-preparation QFI.

## 2. Multi-parameter affine covariance model

Let one accepted phase-referenced detector cycle return

`y ~ N(mu, Sigma(u))`,

with `q` covariance calibration coordinates

`u=(u_1,...,u_q)`

and

`Sigma(u)=Sigma0 + sum_i u_i Sigma_i`.

Whiten around the nominal covariance:

`H_i = Sigma0^(-1/2) Sigma_i Sigma0^(-1/2)`.

Require the same affine model to remain positive for the full calibration hypercube

`u_i in [-1,1]`.

For every sign vector `s_i=+/-1`, positivity at both opposite vertices implies

`|| sum_i s_i H_i ||_op < 1`.

The per-shot covariance Fisher matrix is

`K_ij = 1/2 Tr(H_i H_j)`.

## 3. RQIR-NG-017 — multi-parameter covariance information budget

Average

`Tr[(sum_i s_i H_i)^2]`

over all sign vectors. Cross terms vanish, so

`E_s Tr[(sum_i s_i H_i)^2] = sum_i Tr(H_i^2)`.

But every signed sum has all eigenvalues in `(-1,1)`, hence

`Tr[(sum_i s_i H_i)^2] < m`.

Therefore

`boxed: Tr K < m/2`.

For `q` covariance coordinates,

`boxed: lambda_min(K) <= Tr K/q < m/(2q)`.

### Meaning

Shared acquisition does not create arbitrarily large covariance information. Positivity imposes a total per-shot information budget across all simultaneously encoded covariance directions.

For the four high-value RQIR covariance coordinates and the minimal `m=8` joint output,

`lambda_min(K) < 1`.

So even the best-balanced shared shot cannot contribute more than one Fisher unit per shot in its weakest one of the four covariance directions.

This is an apparatus-neutral necessary bound under the declared affine/full-hypercube assumptions.

## 4. Near-saturating joint architecture

The bound is not merely loose. Use four disjoint two-dimensional detector blocks and let each `H_i` be traceless on one block:

`H_i = a diag(+1,-1)`

on block `i`, zero elsewhere, with `a<1`.

Then the full hypercube remains positive and

`K = a^2 I_4`.

For `a=0.999`,

`K ~= 0.998001 I_4`,

`Tr K ~= 3.992004 < 4`.

Thus the limit `lambda_min(K) -> 1` can be approached.

## 5. Minimum shared-shot count at the centered D2 benchmark

Iteration 034's preferred centered D2 covariance weight is approximately

`gamma_cov = 0.590127e6`.

To reproduce a calibration block

`gamma_cov I_4`

with `N` accepted shared cycles requires

`N K >= gamma_cov I_4`.

Since `lambda_min(K)<1`,

`boxed: N_joint > 5.90127e5 accepted shared cycles`

at `lambda=1` in the ideal balanced limit.

The explicit `a=0.999` construction needs about

`5.91309e5`

accepted cycles.

For comparison, four separate near-optimal bivariate campaigns would need approximately four times as many cycles if their cycle durations and efficiencies were the same.

### RQIR-RESOURCE-014 — shared-shot speedup is dimension-limited

For `q=4,m=8`, simultaneous covariance acquisition can ideally recover a factor approaching four relative to four separate bivariate campaigns, but not an arbitrarily large factor. The gain comes from reusing the same cycle across four Fisher directions, not from violating the covariance positivity budget.

## 6. Nuisance profiling in covariance-matrix space

The covariance Fisher defines its own inner product,

`<A,B>_Sigma = 1/2 Tr(Sigma^-1 A Sigma^-1 B)`.

This makes detector nuisance orientation directly analogous to source-space Fisher geometry.

### Common variance/imprecision scale

For the near-saturating traceless block encoding at `Sigma0=I`, a common variance nuisance has derivative proportional to `I`.

Because

`Tr(H_i)=0`,

all four source covariance directions are Fisher-orthogonal to the common scale nuisance. Profiling the common scale leaves `K` unchanged at the nominal point.

### Aligned backaction/cross-noise nuisance

If an unknown detector nuisance has covariance derivative exactly aligned with `H_0`, profiling it removes the first calibration direction completely:

`lambda_min(K_profiled)=0`.

The other three directions remain finite in the explicit block example.

### RQIR-CAL-014 — covariance Fisher-orthogonality design rule

> A shared covariance detector should encode source covariance derivatives in covariance-matrix directions that are Fisher-orthogonal to the dominant imprecision, backaction and cross-noise nuisance derivatives. Shared acquisition by itself does not protect identifiability.

An aligned unknown backaction direction can reopen an exact calibration degeneracy even when the raw covariance signal is large.

## 7. Comparison with independent source metrology

At `y_ref=-4`, adding the best four centered force-covariance rows reduces the required source prior from approximately

`C_alpha=4.55511`

to

`C_alpha=0.0500614`.

Thus the saved preparation information is

`Delta C_alpha ~= 4.5050486`.

With the coordinate-correct QFI

`F_Q^(alpha) ~= 0.0849323916`

per accepted single-branch copy, this corresponds to only

`boxed: ~53.04 accepted single-branch source-metrology copy equivalents`.

The covariance side, even under the ideal shared `m=8` architecture, needs more than

`5.90e5`

accepted detector cycles.

Therefore at equal acceptance/efficiency the necessary cycle-time ratio is

`boxed: t_P/t_C > ~1.11255e4`.

More generally,

`(p_C eta_C)/(p_P eta_P) * t_P/t_C > ~1.11255e4`.

This is the factor-four improvement over the separate-bivariate Iteration-037 bound `~4.4502e4`.

## 8. Coherence-time closure

The shared high-value set includes the latest stored source phase

`tau_max=4.99085067`.

A single joint cycle that samples all four phase-referenced covariance observables cannot finish before the source has coherently evolved through this phase. Therefore

`T_C >= T_coh,min = tau_max/(2 pi f_gap)`

before any readout/reset overhead.

At `f_gap=100 Hz`,

`T_coh,min ~= 7.94319 ms`.

Combining this hard lower bound with the ideal shared-shot break-even gives, at equal acceptance/efficiency,

`boxed: t_P > ~88.37 s`

as a **necessary** source-metrology cycle time for the best-four covariance bundle even to have a chance to beat independent source metrology in wall clock.

If a transparent `1 ms` detector dead/readout time is added,

`boxed: t_P > ~99.50 s`.

Representative no-dead-time values:

| gap | `T_coh,min` | necessary `t_P` |
|---:|---:|---:|
| 10 Hz | ~79.43 ms | ~883.7 s |
| 100 Hz | ~7.943 ms | ~88.37 s |
| 1 kHz | ~0.7943 ms | ~8.84 s |

These are lower-bound comparisons, not apparatus forecasts.

## 9. Strong negative resource conclusion

Under the current assumptions — full-range affine Gaussian covariance model, four high-value covariance coordinates, minimal eight-output shared detector, phase-referenced joint acquisition and coordinate-correct source QFI — the covariance-complementarity route cannot be wall-clock cheaper than source metrology if source-state verification cycles are substantially faster than the coherence-coupled threshold above.

At 100 Hz, if independent source metrology can be performed in much less than roughly one to two minutes per accepted effective copy while the joint covariance detector must remain coherent to the latest phase, even an ideal near-saturating shared Gaussian covariance readout cannot win purely by replacing `C_alpha`.

This does **not** rule out the complementary branch. It can still win if:

- source metrology is physically much slower than the toy QFI suggests;
- one detector cycle carries useful mean/response information in addition to covariance Fisher;
- a higher-dimensional output is available without proportional cycle-time cost;
- the physical calibration coordinate domain is narrower than the full `[-1,1]` hypercube;
- a non-affine or non-Gaussian measurement outperforms the present Gaussian bound;
- covariance measurements are required anyway for independent systematics/consistency purposes.

## 10. What is retained

Retained without change:

- RQIR-NG-005 source-amplitude obstruction;
- RQIR-NUM-002 coordinate-correct source QFI;
- centered covariance correction RQIR-CAL-013;
- RQIR-NG-014/015 nonstationarity and ordering gates;
- RQIR-NG-016 single-coordinate Gaussian positivity bound;
- centered D2 row-selection result `(0,1,3,7)`.

This iteration strengthens the resource interpretation only.

## 11. Reproducibility

Code:

`analysis/d2_shared_shot_covariance_budget_iteration038.py`

Regression checks verify the hypercube positivity construction, the `Tr K<m/2` budget, near-saturating `K`, common-scale nuisance orthogonality, aligned-nuisance collapse, accepted-cycle lower bound and 100-Hz coherence-coupled break-even.

## 12. Next gate

The most useful next step is no longer a generic covariance-only Gaussian model. Build a **joint mean + covariance D2 output likelihood** in which the same accepted cycle contributes:

1. direct force-mean information;
2. the four high-value centered covariance directions;
3. timing/additive references;
4. explicit imprecision/backaction nuisance derivatives.

Then evaluate the full profiled information gained per physical cycle. A joint detector can only beat the covariance-only bound by extracting useful information from additional mean/response channels or by changing the measurement class; this must be demonstrated rather than assumed.
