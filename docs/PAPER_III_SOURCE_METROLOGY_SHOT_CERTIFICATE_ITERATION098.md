# RQIR Iteration 098 — Source-Metrology Physical Shot Certificate

**Date:** 2026-08-30  
**Status:** Paper-III physical source-preparation/resource closure; parameterized apparatus result, not a hardware forecast and not a new-physics claim.

## 1. Purpose

The current Paper-III front already converted the abstract source-amplitude prior of RQIR-NG-005 into the independent Fisher requirement `C_src=225` for the standard `Z=5`, 90% multiplicative-retention benchmark. The remaining useful step is to express that Fisher requirement directly as physical repetitions, preparation attempts, coherent evolution and wall clock for the mature Toy009 and Toy014 Ramsey source-metrology channels.

For a Ramsey setting with accepted-copy Fisher `F_alpha(phi,V)`, preparation acceptance `p_E`, energy-gap angular frequency `Omega_E`, and reset/readout overhead `t_reset`,

`N_acc = C_src/F_alpha`,

`N_try = C_src/(p_E F_alpha)`,

and

`T_src = N_try [t_reset + phi/Omega_E]`.

Writing `tau_reset=Omega_E t_reset` and

`q(phi,V,tau)=F_alpha(phi,V)/(tau+phi)`,

this is exactly

`boxed{T_src = C_src/[p_E Omega_E q]}`,

so the shot-count and Fisher-rate descriptions are identical.

## 2. RQIR-RESOURCE-051 — independent source Fisher becomes a finite shot budget

For any declared source-metrology operating point,

`boxed{N_acc >= C_src/F_copy}`,

`boxed{N_try >= C_src/(p_E F_copy)}`.

Thus the source-preparation information required by NG-005 is not an abstract prior: it corresponds to a finite number of independently prepared/sacrificial source copies. The copies are distinct from science copies whenever NG-023/backaction prohibits same-copy source metrology.

## 3. Toy009 and Toy014 zero-reset benchmark

Repository-retained zero-reset, `V=1` Ramsey Fisher-per-time optima are:

Toy009:

- `phi_009 ~= 1.09231`;
- `q_009 = max F_alpha/phi = 0.0025234392`.

Toy014:

- `phi_014 = 0.9264295097660072`;
- `q_014 = 0.0037632915041337926`.

Therefore the accepted-copy Fisher at the rate-optimal points is

- Toy009: `F_copy ~= 0.002756377872552`;
- Toy014: `F_copy ~= 0.00348642430328125`.

For `C_src=225`, the exact continuous shot budgets are

- Toy009: `N_acc ~= 81,628.866`;
- Toy014: `N_acc ~= 64,536.035`.

The actual integer campaign must round these upward.

Toy014 therefore needs about `0.7906` times as many accepted Ramsey source copies at its own zero-reset rate-optimal phase.

## 4. Preparation success / attempted copies

At preparation acceptance `p_E`,

- Toy009: `N_try ~= 81,628.866/p_E`;
- Toy014: `N_try ~= 64,536.035/p_E`.

For the transparent `p_E=0.5` benchmark:

- Toy009: `N_try ~= 163,257.732`;
- Toy014: `N_try ~= 129,072.070`.

This is the direct preparation-throughput cost of the independent source-amplitude calibration required by NG-005.

## 5. Coherent-evolution benchmark at a 100-Hz gap

Use only as a declared timing slice:

`Omega_E = 2 pi * 100 s^-1`.

The Ramsey coherent evolution per attempted copy at the rate optimum is then

- Toy009: `t_evol ~= 1.738465 ms`;
- Toy014: `t_evol ~= 1.474458 ms`.

Both are below the retained maximum source-evolution benchmarks of roughly `7.943 ms` (Toy009) and `6.813 ms` (Toy014) at the same 100-Hz scaling. This comparison is only a timing consistency check; an ancilla/source implementation must still certify its actual coherence and reset model.

With `p_E=0.5`, zero reset and `V=1`, the corresponding source-metrology wall clocks are

- Toy009: `T_src ~= 283.818 s` (`4.73 min`);
- Toy014: `T_src ~= 190.311 s` (`3.17 min`).

These values are not full experimental campaign forecasts; they exclude detector science, the seven calibration layers, controls, drift recertification and nonzero reset/visibility losses.

## 6. RQIR-RESOURCE-052 — source-attempt throughput floor for a wall-clock cap

Iteration 091 gave the source-only feasibility condition

`R_src > m C_src/T_cap`, with `m=1/(1-d)`.

Since

`R_src = p_E Omega_E q`,

the same condition becomes

`boxed{p_E Omega_E > [m C_src/T_cap]/q}`.

This is an explicit preparation-success × source-coupling/evolution-rate requirement.

For the transparent `T_cap=7 days`, `d=0.05`, zero-reset `V=1` slice,

`R_src,floor = 3.91604010025e-4 s^-1`.

Hence the best-case source-attempt throughput requirements are

- Toy009: `p_E Omega_E > 0.155186624 s^-1`;
- Toy014: `p_E Omega_E > 0.104058909 s^-1`.

Finite reset or reduced visibility lowers `q` and therefore increases these minimum products. The exact reset/visibility dependence must use the Iteration-092 robust Ramsey optimization rather than the zero-reset constants above.

## 7. RQIR-NG-051 — detector exposure cannot substitute for missing source copies

The finite-shot form sharpens NG-005/NG-041:

If the independent source campaign supplies fewer than `C_src/F_copy` accepted source copies (or an equivalent independent Fisher channel), increasing detector science exposure cannot recover the missing source-amplitude information. The detector derivatives in `(beta,a)` remain collinear, so the deficiency is structural rather than ordinary detector shot noise.

This is not a new no-go mechanism; it is the physical shot-budget form of the existing source-amplitude identifiability obstruction.

## 8. Relation to the primitive characterization table

Iteration 098 fills the **source-model part** of the upcoming primitive table:

Known from the repository for the zero-reset reference branch:

- rate-optimal `phi`;
- normalized Ramsey rate coefficient `q`;
- accepted-copy Fisher at that optimum;
- accepted-copy count required by `C_src`;
- exact scaling with preparation success, reset and `Omega_E`.

Still apparatus-dependent and therefore not to be invented:

- measured `p_E` and its uncertainty/floor;
- physical `Omega_E` and drift;
- `t_reset`/readout distribution;
- visibility and coherence over the actual campaign;
- their characterization Fisher rates/correlations/duty.

The detector/calibration side still requires the common-normalization `a2,a4,rho` and seven physical `2x2` calibration Fisher blocks identified by Iterations 087–097.

## 9. Reproducibility

Run

`python analysis/source_metrology_shot_certificate_iteration098.py`.

The script verifies the equality between shot-count and Fisher-rate wall-clock formulas and reproduces all numerical values above from the repository-retained Toy009/Toy014 Ramsey coefficients.
