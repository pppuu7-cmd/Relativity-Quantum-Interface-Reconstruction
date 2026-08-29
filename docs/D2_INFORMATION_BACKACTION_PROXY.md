# RQIR Iteration 043 — D2 Information–Backaction Proxy

**Date:** 2026-08-29  
**Scope:** current Toy009 D2 force-mean resource layer.  
**Status:** quantum-limited direct-monitoring proxy; not a complete D2 apparatus model and not a new-physics claim.

## 1. Why this gate is needed

Iteration 042 found that the backaction-safe seven-layer mean calibration becomes as fast as the best-four covariance floor when the per-accepted-layer standardized mean sensitivity reaches roughly

`xi_mu ~= 2.77`

in the transparent `100 Hz`, `p=0.5`, `1 ms` benchmark.

That result still treated `xi_mu` as a free detector number. If the same quantum source copy is continuously monitored to obtain this information, measurement information and source disturbance are linked.

Iteration 043 introduces the simplest standard diffusive-measurement proxy to determine whether the required mean Fisher is plausibly a weak perturbation.

## 2. Minimal diffusive measurement model

For a normalized Hermitian source observable `M`, use

`dy = 2 sqrt(eta kappa) <M> dt + dW`,

with unconditional backaction

`d rho/dt = kappa D[M] rho`,

`D[M]rho = M rho M - 1/2 {M^2,rho}`.

For a normalized local mean coordinate `u` with `d<M>/du=1`, a measurement window of duration `T` gives, to leading score order,

`I_u = 4 eta kappa T`.

Thus a required standardized sensitivity `xi_mu=sqrt(I_u)` implies

`zeta = kappa T = xi_mu^2/(4 eta)`.

Lower quantum efficiency therefore requires more dephasing strength for the same acquired mean information.

This is not yet the actual gravitational force-detector backaction law; it is a clean reference class against which any claimed shared-trajectory gain can be tested.

## 3. Toy009 source is sensitive to force-basis dephasing

Normalize the same-time force operators as

`M0=G0/||G0||_F`, `M1=G1/||G1||_F`.

They commute with each other at a fixed phase and can therefore be monitored in parallel in this proxy.

For the nominal hidden states, the first-order purity-loss coefficients are

`||[M0,rho_+]||_F^2 ~= 0.00433225`,

`||[M1,rho_+]||_F^2 ~= 0.00130355`,

with the same values for `rho_-`.

The coefficients are not enormous, but they are nonzero: the information-bearing force basis does disturb the coherent hidden states.

## 4. Backaction at the optimistic shared-cycle mean requirement

Iteration 041 found that if the `1.180254e6` covariance trajectories could also carry all mean Fisher, each trajectory would need only

`xi_mu ~= 1.245286`.

At ideal efficiency `eta=1`, this corresponds to

`zeta ~= 0.387685`.

Applying the exact dephasing semigroup for both commuting same-time force observables before evaluating the current normalized D2 ordered-response harmonic vector gives

- response-norm retention: `~0.856964`;
- response-direction alignment with the original signal: `~0.998751`.

So even this optimistic direct-monitoring proxy produces about a **14% response-amplitude loss**, although it barely rotates the response direction.

## 5. Backaction at the mean-vs-covariance wall-time crossover

For the Iteration-042 crossover

`xi_mu ~= 2.772804`,

the ideal-efficiency measurement strength is

`zeta ~= 1.922111`.

The same direct-monitoring proxy then gives

`boxed: response-norm retention ~= 0.49345`

and alignment

`~0.95693`.

Thus a measurement strong enough to make the independent seven-layer mean campaign as fast as the best-four covariance floor would, in this direct source-monitoring class, reduce the raw D2 ordered-response norm by roughly one half.

That makes it unsafe to treat the required mean Fisher as a free add-on to the response experiment.

## 6. Efficiency penalty

At fixed required `xi_mu=2.772804`, lower information efficiency increases the needed dephasing:

| `eta` | `zeta` | response-norm retention | alignment |
|---:|---:|---:|---:|
| 1.0 | `1.92211` | `0.49345` | `0.95693` |
| 0.8 | `2.40264` | `0.42596` | `0.92744` |
| 0.5 | `3.84422` | `0.29954` | `0.79325` |
| 0.2 | `9.61055` | `0.15771` | `0.33114` |

The effect is rapidly severe once the monitor is substantially inefficient.

### RQIR-NG-020 — direct-monitoring information/backaction obstruction

> In the standard diffusive measurement class, finite Fisher about a non-QND source observable necessarily carries dephasing backaction. For the current Toy009 force observables, the mean information required for resource-competitive calibration is not perturbatively free: at the `xi_mu~2.77` benchmark the ordered-response norm is reduced to about one half even at ideal efficiency in the simplest parallel-force dephasing proxy.

This is **protocol-specific**. A D2 detector that couples primarily to a separate probe, an ancilla-assisted protocol or another measurement architecture may have a different information/backaction relation and must be modeled explicitly.

## 7. RQIR-RESOURCE-018 — information efficiency is also a coherence resource

At fixed output Fisher,

`zeta proportional 1/eta`.

Therefore measurement efficiency cannot be treated only as a longer integration-time penalty. In a shared quantum-source trajectory it can directly increase state disturbance and reduce the very ordered-response signal being tested.

A wall-clock optimizer that ignores this coupling can select a formally fast but physically self-erasing measurement regime.

## 8. What this does not prove

This iteration does **not** show that D2 is impossible.

In particular, the physical D2 architecture considered earlier is a force detector acting on a probe. The true source backaction depends on the complete source–gravity–probe interaction, detector quantum noise and any reciprocal force. The direct source-monitoring SME above is only a conservative reference model.

The result does show that the next apparatus model must calculate, not assume, the relation between:

- force-mean Fisher;
- covariance Fisher;
- detector imprecision;
- reciprocal/backaction noise;
- loss/rotation of the ordered-response signal.

## 9. Reproducibility

Code:

`analysis/d2_information_backaction_proxy_iteration043.py`

The script reconstructs the accepted hidden pair and normalized D2 response, applies exact dephasing channels for `G0` and `G1`, and verifies the response-retention numbers above.

## 10. Next gate

Move one layer closer to the intended D2 experiment: introduce an explicit **source–probe linear-response detector model** rather than monitoring the source operator directly. Derive a measurement-noise/backaction matrix satisfying the relevant quantum noise inequality, then propagate it through the same `F_beta|theta` likelihood.

The key question is whether a probe-mediated readout can reach the required `xi_mu~2.8` and best-four covariance information while keeping source-response attenuation comfortably above the direct-monitoring proxy and without reopening detector/source nuisance degeneracies.
