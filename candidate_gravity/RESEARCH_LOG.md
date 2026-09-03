# Candidate Gravity Research Log

## 2026-09-03 — Iterations 319-324

### Iteration 319 — physical graviton routed components
Validated the Iteration-318 frozen minimal tensor Laplace operator `H=-(I Box+Pi)` through cubic background order in a fixed 10-component symmetric contravariant tensor basis. Raw Actions artifact passed sentinel/schema and frozen numerical thresholds. Full routed graviton `H1/H2/H3` authority is frozen in this scope.

### Iterations 320-324 — common fixture, closure and shifted propagators
Iteration 320 assembled common H/N local routing; Iteration 321 correctly blocked physical promotion because the original triad was not trace-closed. Iteration 322 rebuilt on `q3=-(q1+q2)`. Iteration 323 found the higher-level missing successive shifted propagators. Iteration 324 then froze explicit ordered `G0(p+Q)` routing and cyclic denominator-family equivalence. Missing numerator evaluations remained fail-closed rather than zero-filled.

## 2026-09-03 — Iterations 325-336

### Iterations 325-331 — common-background physical determinant family reconstruction
Scoped gate-design failures in Iterations 325, 327 and 330 were preserved rather than relabelled. Iteration 329 closed the one-common-background H/N requirement and validated the routed physical insertions. Iteration 328 supplied only denominator signed-affine equivalence, never numerator equivalence. Iteration 331 then froze the physical cubic determinant integrand into `1 singleton + 3 bubbles + 1 signed-affine triangle` with route-specific transformed numerators. Raw run `33742866100`, job `100608562495`, artifact `9888424625`; maximum held-out numerator reconstruction error `1.3877787807814457e-17`, denominator-map error `1.1102230246251565e-16`.

### Iteration 332 — direct-timelike closed fixture
A prerequisite audit showed the Iteration-331 closed fixture was spacelike, so no direct timelike-cut authority was claimed from it. Iteration 332 changed only the external closed triad to `q1=(1,0,0,0)`, `q2=(-0.4,0.1,0.1,0)`, `q3=(-0.6,-0.1,-0.1,0)`, all timelike in signature `(-,+,+,+)`. The first run failed operationally during NumPy JSON serialization before artifact creation; a serialization-only repair was made with no scientific change.

Validated rerun `33743302046`, job `100609965778`, artifact `9888598043`, artifact digest `sha256:8d8210b882bd4d5cba45be1e5c2efd89f9fee025d14e6d8c5f942e12c9f2c70c`, scientific JSON SHA-256 `29a3e65146a03c8a0487c4a39d9b809ed985697fa0d5244ceca77e452aba7795`. Authority: `PASS_TIMELIKE_CLOSED_TRIAD_PHYSICAL_CUBIC_DETERMINANT_NUMERATOR_FAMILY_FIXTURE`. Maximum held-out numerator reconstruction scaled error `2.7755575615628914e-17`; denominator-map error `1.1102230246251565e-16`.

### Iteration 333 — direct-timelike cut-origin reduction
Two earlier/parallel implementations are preserved as operational/gate-design failures, not scientific failures. The first had a namespace-loading error. The next repaired namespace but evaluated `K0^{-1}` on the exact massless Cutkosky shell and therefore hit the expected singular free operator (`LinAlgError: Singular matrix`) before any schema-valid artifact. No physical zero/nonzero conclusion is taken from those runs.

The validated implementation strips the free graviton/ghost denominators analytically before shell evaluation, using the frozen flat identities `H0=+p^2 I_10`, `N0=-p^2 I_4`, and independently checks the stripping reconstruction off shell. Validated run `33748344954`, job `100625932251`, artifact `9890612109`, artifact digest `sha256:41f2e2e91e8b425c0f2704e5feec5982dac96e64cbd8ca2c3f8eb6a7e51ae545`, scientific JSON SHA-256 `0620bce57a69d8e2f51a63989301cc281c53a8b7d5144f4d2d4636bfc64e4567`. Maximum denominator-stripping reconstruction error `1.5265566588595902e-16`.

All three bubble families have stable NONZERO direct two-particle discontinuity certificates:
- `q^2=-1`: normalized angular cut proxy `-0.004517862848697545`;
- `q^2=-0.34`: `9.802036921027348e-05`;
- `q^2=-0.14`: `0.00013296877895753044`.

The signed-affine triangle family is NONZERO at family level: its `q^2=-0.14` and `q^2=-0.34` channels independently pass. The remaining `q^2=-1` channel has its uncut third denominator bounded strictly away from zero, approximately `[0.1185786438,0.4014213562]`, so it has no third-propagator/PV ambiguity, but its two low-order cubatures disagree at `1.405487804189524e-4`, above the frozen `2e-5` threshold. It remains typed `BLOCKED_NEAR_CANCELLATION_OR_CUBATURE_CONVERGENCE`; no post-hoc threshold weakening.

Authority: `PASS_DIRECT_TIMELIKE_DETERMINANT_DISCONTINUITY_FAMILY_REDUCTION__THREE_BUBBLES_NONZERO__TRIANGLE_FAMILY_NONZERO__Q2_MINUS1_TRIANGLE_CHANNEL_NUMERICALLY_BLOCKED`.

### Iteration 334 — high-resolution resolution remains BLOCKED
Raw artifact from run `33748965082`, job `100627871946`, artifact `9891879802`, digest `sha256:6cf1702b0a3733d9110d9316133037b327bf27de8cf9b9d7ba846d40d66718b8`, scientific JSON SHA-256 `a01ec6eae6395edfd339b74ae0e43faed48aceff49cd3e06d4dac470595c5fe6` is schema-valid and scientifically BLOCKED, not an infrastructure failure. The deterministic Fibonacci-sphere means converge near `0.006876`, but the frozen normalized convergence ratio is `2.2111065687680303e-4`, still above `2e-5`. The third propagator remains analytically bounded away from zero on the cut sphere, `[0.11857864376269048,0.40142135623730957]`, and cut-shell errors are below `8.1e-17`. Thus the remaining blocker is numerical angular-integration authority only; no threshold weakening is permitted.

### Iteration 335 — independent product quadrature active
Only the unresolved `q^2=-1` triangle channel is being evaluated with a genuinely independent tensor-product rule: Gauss-Legendre in `z=cos(theta)` times periodic azimuth quadrature, plus a phase-shifted azimuth cross-check. Parent dynamics, exact fixture, numerator, cut surface and frozen convergence threshold `2e-5` are unchanged. Original run `33753368856` was cancelled during the scientific step at the workflow time limit before schema-valid output or artifact upload. Timeout only was raised to 180 minutes; replacement run `33759144658` is in progress and is not duplicated.

### Iteration 336 — exact massless two-particle phase-space normalization PASS
Independent of the active Iteration 335 angular calculation, the exact geometric 4D massless two-particle cut normalization is frozen in signature `(-,+,+,+)`:

`dPhi2 = dOmega/(32*pi^2)`, hence `int dPhi2 = 1/(8*pi)`.

Because Iteration-333/335 cut proxies are normalized sphere means `mean=(1/(4*pi)) int dOmega F`, their exact geometric conversion is

`int dPhi2 F = mean/(8*pi)`.

Validated run `33754035543`, job `100644020489`, artifact `9892688060`, artifact digest `sha256:eaa23f7411d63f0d66216498b750a20609fa19a478662f9fde1f1e14bce0165e`, scientific JSON SHA-256 `5f84fd4616dcca8eb3bd5beeb396718a74caab9637f77758e4e63aa529f07e53`; exact closure error `0.0`.

Authority: `PASS_EXACT_4D_MASSLESS_TWO_PARTICLE_PHASE_SPACE_NORMALIZATION`.

## 2026-09-03 — Iterations 337-339

### Iteration 337 — repository-normalized simple-cut bridge
The Iteration-336 geometric factor was calibrated against the frozen Iteration-296 scalar-bubble convention. For an ordinary two-simple-line channel with normalized angular mean `m`,

`D_s I[F] = -8*pi int(dPhi2 F) = -m`.

Authority: `PASS_REPOSITORY_NORMALIZED_SIMPLE_TWO_PARTICLE_CUT_CONVERSION__DET_OUTER_EFFECTIVE_ACTION_FACTOR_REMAINS_BLOCKED`.

Validated run `33756194728`, job `100651082826`, artifact `9893533178`, digest `sha256:aaeca20e2906d240417b6c9d301639068c62076f11281694525a5263d1096161`, scientific JSON SHA-256 `7d6ba8fd46c01fb9af79b21932daa49787587122c47e51af85d8d7997bad64`.

### Iteration 338 — determinant effective-action prefactor
The reduced one-loop convention is reconciled with `C_det=(1/2)Tr_H-Tr_N`, giving

`Gamma_det=+i*C_det`, hence `D_s Gamma_det=-i*m`

for ordinary two-simple-line determinant channels. This cross-checks the independently frozen Iteration-307 `Tr U1` coefficient `-i/2` and prevents double application of determinant weights.

Authority: `PASS_SAME_PARENT_DETERMINANT_EFFECTIVE_ACTION_OUTER_PLUS_I_PREFactor__TRU1_MINUS_I_OVER_2_CROSSCHECK`.

Validated run `33756324238`, job `100651503806`, artifact `9893580250`, digest `sha256:54eb5733ebfd08afeaccfbe7c775968436136f9ae05f5cbddfee96b53ca86da4`, scientific JSON SHA-256 `2a0a99466b08ce30ff639739079c97461078e80429b42e92f95c90367f902f6b`.

### Iteration 339 — U2 graviton Green H0/H1 bridge PASS
While the independent Iteration-335 determinant calculation remained in progress, the old `e=2,c<=1` U2 blocker was revisited without duplicating that Action. Iteration 309 denotes the field-space Green operator inside `U2=N_L V1_L H V1_R N_R Y` by `H`, whereas Iteration 319 uses `H` for the minimal graviton differential operator. Iteration 339 calls the latter `K` and freezes the Green expansion

`G0(p)=K0(p)^-1`,

`G1(q;p)=-G0(p+q) K1(q;p) G0(p)`.

The actual physical Iteration-319 `K1` matrix in `D=4, Lambda=0, a=-1/2` is used. Flat `K0` is reconstructed independently at `p` and `p+q`, and an explicit two-momentum-sector block inverse provides the independent routing oracle.

Numerical closure:
- flat `K0(p)` error `0.0`;
- flat `K0(p+q)` error `5.551115123125783e-17`;
- maximum block-inverse error `8.881784197001252e-16`;
- finite-difference inverse derivative error `1.7763568394002505e-15`;
- correct shifted vs incorrect unshifted-left Green separation norm `78.53690403309817`.

Authority: `PASS_E2C1_U2_GRAVITON_GREEN_H0_H1_SAME_PARENT_ROUTING_BRIDGE__V1_KERNELS_REMAIN_BLOCKED`.

Validated run `33759581615`, job `100662270347`, artifact `9894856112`, digest `sha256:9e8593512de6fbef0238b0c1001950a34183d5f6484b179dd34c9e0f46528b05`, scientific JSON SHA-256 `9cdbedc4897d4ed8be746ac0d2ac4fc3c73251b36dce23f7a243322ab779e318`.

Scientific consequence: same-parent graviton Green `H0/H1` is no longer part of the U2 blocker. Physical `V1_1/V1_2` remains BLOCKED; any required N/Y inverse-routing bridge remains unclosed; no physical U2 numerator is authorized.

### Guardrails
Iteration-297 remains binding for the full finite DR remainder. Family-level absorptive nonzero is not the full matched observable. No Source/Born subtraction before normalized cut/origin accounting. Unsupported U2 kernels are BLOCKED, never zero-filled. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5 and no reopening of closed `e=3`.

MODEL_READINESS: 24%

Change through Iteration 339: `0 pp`. Exact normalization and a genuine U2 Green-routing prerequisite closed, but no complete readiness-rubric bucket and no robust comparator-subtracted residual have closed.

## 2026-09-04 — Iteration 367

### Iteration 367 — physical timelike `Tr U1^2` pruning re-audit
Fresh Actions state first established that Iteration 364 had ended operationally cancelled before sentinel/schema validation and without an artifact; no scientific conclusion is assigned to its 48 cut-through-double-pole channels.

Iteration 367 then re-audited only the historical Iteration-310 singleton-soft pruning premise on the current matched timelike common-background fixture. Raw run `33806321673` completed successfully; artifact `9913046693` has digest `sha256:4361ce81fb2be3863b030a4eab5a686c69aceeab0160b229d307353031393e50`, and the raw scientific JSON SHA-256 is `e71b895495d3e00187372430427895e56423ea1be576991cb99e5fdd6f35f87d`. Sentinel/schema authority passed.

The historical null-soft control reproduces `||U1^(1)[s]||_F=4.172141756553574e-16`, but on the timelike fixture the same singleton is decisively nonzero: `||U1^(1)[s]||_F=0.5850412233520722` at `q_s^2=-1`, with nonzero margin `585041.2233520722` over the frozen `1e-6` threshold. Independent derivative checks are stable: step relative spread `9.488417057724452e-16`, two-point versus five-point relative error `7.760065778909101e-10` under frozen `2e-4` tolerances. The other timelike legs are also nonzero: `0.2519141158697874` at `q_a^2=-0.14` and `1.2355711687033575` at `q_b^2=-0.34`.

Authority: `PASS_TRU1SQ_TIMELIKE_REBASE_INVALIDATES_OLD_SINGLETON_SOFT_PRUNING__FULL_PREPRUNING_PHYSICAL_ROUTING_REQUIRED`.

Scientific consequence: the historical Iteration-310 reduction `42 raw ordered placements -> 16 survivors -> 8 cyclic classes` is not transferable to the current physical timelike fixture. Physical `Tr U1^2` must restart from all 42 pre-pruning ordered placements, with route-by-route same-parent `U1=N_L V2 N_R Y` contraction and exact cumulative incoming momenta before any cyclic quotient or cut integration. This is a scoped negative pruning result, not a Candidate Gravity consistency FAIL or comparator identity.

MODEL_READINESS: 24%

Change through Iteration 367: `0 pp`. A false historical shortcut is removed and the physical `Tr U1^2` starting space is now fixed correctly, but no complete readiness-rubric bucket and no robust comparator-subtracted residual have closed. `ANSATZ-003` remains uncreated; Fisher/resources remain forbidden.
