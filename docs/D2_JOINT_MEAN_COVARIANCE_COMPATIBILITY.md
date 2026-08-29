# RQIR Iteration 041 — D2 Joint Mean/Covariance Compatibility Gate

**Date:** 2026-08-29  
**Scope:** Toy009 / balanced Iteration-011 D2 force calibration after the centered-noise correction.  
**Status:** measurement-compatibility/resource gate; no new-physics claim.

## 1. Question

Iteration 040 showed that covariance-only completion is expensive and suggested a more favorable architecture: use the **same coherent D2 trajectory** to earn force-mean, covariance and control Fisher.

Before crediting one trajectory with all of those resources, RQIR must check whether the corresponding quantum source observables can actually be monitored on one undisturbed source copy.

The current D2 mean calibration consists of 14 force operators

`G_k(t_j)`, `k in {0,1}`, `j=0..6`,

with two probe locations and seven phase/time settings.

## 2. Pairwise commutator audit

There are `C(14,2)=91` operator pairs.

The deterministic Toy009 reconstruction gives:

- commuting pairs: `7`;
- noncommuting pairs: `84`;
- median Frobenius commutator norm over all pairs: `~1.11458e-2`;
- maximum: `~0.521190`.

The **only** commuting pairs are

`G0(t_j)` with `G1(t_j)`

at the same time setting `t_j`.

Every pair belonging to different time settings is noncommuting to numerical precision.

This has a simple structural origin: at a fixed time the two probe-force operators are functions of the same source-position operator and share an eigenbasis; Hamiltonian evolution rotates that basis between different times.

Therefore the 14 force means naturally decompose into **seven commuting two-probe time layers**, not one commuting 14-observable bundle.

## 3. The force observables are not QND under the source Hamiltonian

For the unevolved probe operators,

`||[G0,H]||_F / ||G0||_F ~= 1.9056406`,

`||[G1,H]||_F / ||G1||_F ~= 1.0586202`.

Both are strongly nonzero in the current dimensionless model.

Thus repeated force monitoring is not a quantum-nondemolition measurement of the closed Toy009 dynamics.

### RQIR-NG-019 — non-QND shared-trajectory obstruction

> A multi-time D2 calibration cannot be credited as a disturbance-free simultaneous measurement of all 14 force means merely because one classical detector trajectory contains seven timestamps. The corresponding source observables are mutually noncommuting across time and are not QND with respect to the source Hamiltonian. A shared-trajectory likelihood must therefore include measurement backaction, or else use independent preparations/time layers.

This does not say continuous weak monitoring is impossible. It says its information cannot be counted without the measurement dynamics that generates the output record.

## 4. Best-four covariance endpoints have the same issue

The best centered covariance rows `(0,1,3,7)` use six unique endpoints:

- `G0@0`, `G1@0`;
- `G0@TR`, `G1@TR`;
- `G0@T1`;
- `G0@T6`.

They span four distinct time layers.

Among the 15 endpoint pairs:

- two same-time pairs commute;
- thirteen cross-time pairs do not commute.

Therefore the covariance graph from Iterations 039–040 is not only a classical Gaussian positivity problem; its realization on the quantum source also needs an explicit sequential/weak/ancilla measurement model.

## 5. Optimistic shared-output information requirements

Iteration 040 gives the best-four covariance lower bound

`N_cov > 1.180254e6`

accepted joint trajectories.

Suppose, optimistically, that those very same accepted trajectories also supplied the **entire** current centered mean and control Fisher without backaction penalty or extra covariance between estimators.

The centered D2 targets are

`gamma_mean ~= 1.830265e6`,

`sigma(delta tau) ~= 5.77425e-3`,

`sigma(b_mean) ~= 7.39168e-5`,

`sigma(b_cov) ~= 1.30175e-4`.

Dividing their required information by `N_cov` gives the necessary average information per accepted shared trajectory:

| resource | per-cycle Fisher | standardized sensitivity `sqrt(I)` |
|---|---:|---:|
| one normalized mean row | `1.550738` | `1.245286` |
| timing coordinate `delta tau` | `0.0254117` | `0.159410` |
| common mean-offset reference | `155.07372` | `12.45286` |
| common covariance-offset reference | `49.99992` | `7.07106` |

The mean requirement itself is not enormous: if an actual trajectory could provide per-row standardized mean sensitivity of order `1.25` while also saturating the covariance graph bound, covariance-determined cycle count would already be sufficient for the nominal mean Fisher.

The additive-reference requirements are much stronger. This reinforces RQIR-CAL-007: independent control/reference information must not be silently treated as free merely because a science trajectory exists.

## 6. RQIR-RESOURCE-016 — shared-Fisher credit rule

> One accepted trajectory may be credited simultaneously to mean, covariance and control budgets only when a single declared physical likelihood generates all of those score vectors and their cross-information, including measurement backaction and detector correlations. Otherwise, adding row Fisher or reusing the same cycle count is not a valid wall-clock conversion.

The current numbers in Section 5 are therefore **optimistic lower-bound requirements**, not a hardware forecast.

## 7. Design implication

A useful structure nevertheless emerges:

1. same-time dual-probe force means are mutually compatible and should be co-acquired where possible;
2. the seven distinct phase settings are the natural scheduling layers;
3. cross-time information requires either independent source copies or an explicit weak/continuous/ancilla measurement model;
4. the high-value covariance core spans four such time layers and therefore necessarily probes noncommuting temporal information;
5. a successful joint D2 architecture must demonstrate an information/backaction tradeoff, not only a Gaussian output covariance matrix.

## 8. Reproducibility

Code:

`analysis/d2_joint_mean_covariance_compatibility_iteration041.py`

The script reconstructs the force operators, verifies the `7/84` commuting/noncommuting split, checks non-QND Hamiltonian commutators, audits the best-four endpoint set and derives the optimistic shared-cycle Fisher requirements.

## 9. Next gate

Build the first explicit resource schedule consistent with this operator structure:

- **independent-preparation time-layer branch:** use seven separate same-time dual-probe layers and convert the centered `gamma_mean` into repetitions and wall time using coherence/evolution time, acceptance, dead time and per-cycle standardized force sensitivity;
- in parallel, formulate a continuous weak-measurement branch whose stochastic master equation/output record includes backaction, so the possible shared mean+covariance advantage can be tested rather than assumed.
