# ASSUMPTIONS LEDGER — ANSATZ-RQIR-CTP-001 v0.1

Every unresolved item below is an explicit model assumption or open derivation. None may be silently upgraded to a theorem.

| ID | Assumption / open point | Type | Current status | Failure consequence |
|---|---|---|---|---|
| A-001 | Weak-field expansion around asymptotically Minkowski spacetime is sufficient for the first RQIR discriminator. | domain | OPEN | v0.1 cannot address strong-field/cosmological regimes. |
| A-002 | The resolved metric sector can be represented by a Gaussian CTP effective action through the first discriminator order. | truncation | OPEN | Higher connected metric cumulants must be added and may change the fingerprint. |
| A-003 | The v0.1 spectral shape `rho_hat(s)=exp(1-s)Theta(s-1)` is a legitimate positive test shape rather than a physically derived microscopic spectrum. | phenomenological shape | DECLARED | No microscopic interpretation or novelty may be claimed from the shape alone. |
| A-004 | `beta>=0` and `M_*>0`; the first audit is restricted to the region in which the Euclidean kernel is manifestly nonzero. | parameter domain | FROZEN_V0.1 | Changing sign/domain defines a materially different stability problem. |
| A-005 | Vacuum zero-temperature spectral/KMS relation is used to tie the absorptive retarded kernel to the Gaussian noise kernel. | state | OPEN_NORMALIZATION | Finite-temperature/nonstationary gravity states require a new version or explicit extension. |
| A-006 | The deformation is placed in the transverse spin-2 self-energy while the remaining linearized GR constraint sectors retain their reference structure at v0.1. | tensor structure | OPEN | Full Ward/Bianchi restoration may force extra spin-0/constraint terms or reject the ansatz. |
| A-007 | A causal positive microscopic/unitary dilation exists for the chosen effective kernel. | consistency | NOT_PROVEN | QG-004 fails and the ansatz is rejected if no such completion exists in the claimed domain. |
| A-008 | The low-momentum vanishing of the form factor is sufficient to preserve the correct Newtonian pole/residue after the full tensor/source normalization is restored. | limit | NOT_PROVEN | QG-003 fails or the kernel definition must be revised. |
| A-009 | RQIR `N` normalization and the model CTP Hadamard/noise normalization can be made identical without an extra free parameter. | convention | NOT_PROVEN | The Model->RQIR contract is blocked until corrected. |
| A-010 | The beta-direction is not exactly removable by source, calibration, transfer, spectral or comparator nuisance freedom in the eventual finite detector map. | identifiability | NOT_TESTED | QG-008/QG-009 fail if profiled Fisher is zero. |
| A-011 | The full spectral shape near `p^2~M_*^2` is not exactly degenerate with an already known nonlocal/form-factor/hidden-sector gravity model. | novelty/comparator | NOT_TESTED | Retain as comparator/control rather than promote as a new Candidate Gravity model. |
| A-012 | Renormalized/smeared stress-energy observables can be coupled to the same kernel without violating the frozen RQIR conservation and hard-constraint rules. | renormalization/interface | NOT_TESTED | Source hierarchy mapping is blocked. |

## Frozen v0.1 choices

- Model ID: `ANSATZ-RQIR-CTP-001`.
- Spectral support threshold: `s>=1`, corresponding to timelike scale `M_*`.
- Spectral shape: `exp(1-s)` on the support.
- Parameter direction: `beta=0` is the C5 reference boundary; `beta>0` is the deformation direction.
- No independent tuning of response and noise.

## Explicit non-assumptions

The model does **not** assume:

- that the ansatz is a UV completion;
- that the ansatz is new in the literature;
- that a Euclidean no-zero result proves Lorentzian unitarity;
- that a nonzero raw beta response remains identifiable after nuisance profiling;
- that any future experimental anomaly would by itself prove quantum gravity.
