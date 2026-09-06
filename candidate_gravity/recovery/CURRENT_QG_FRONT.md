# Candidate Gravity Current Front

**Updated:** 2026-09-06  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest validated physical/operator authority: Iteration 411.
- Latest validated structural authority: Iteration 410.
- Latest raw-valid physical blocker: Iteration 421 — `BLOCKED_CONVERGENCE`, unresolved double-double index 2 / class 3 / `q^2=-1`.
- Exact unresolved physical set: `[2]`.
- Latest completed numerical mass-support authority: **Iteration 486**, raw-consumed frozen Iteration-455 rank 13 `(u,v)=(+1e-5,-5e-6)`, multiplicity 1.
- Latest authoritative research iteration: **Iteration 489**.
- Frozen support: 32 source occurrences, 28 distinct mass coordinates, five training-z, NPHI16; occurrence denominator `32 x 5 x 16 = 2560` rows.
- Certified occurrence-weighted precision coverage: **`18/32 = 56.25%`**, i.e. **`1440/2560`** row occurrences pending rank14 raw-consume.
- Frozen rank 10 `(+5e-6,+5e-6)`, multiplicity 2, was already `CERTIFIED` in the initial baseline and must not be relaunched.

## Iteration 489 exact BASE↔HALF spectral-transfer authority
For the frozen central4 symbol

`A(theta)=i sin(theta)(4-cos(theta))/3`,

define, away from BASE zeros,

`rho(theta)=2 A(theta/2)/A(theta)`.

Using `sin(theta)=2 sin(theta/2) cos(theta/2)`, the exact closed form is

`rho(theta)=(4-cos(theta/2))/(cos(theta/2)*(4-cos(theta)))`.

Hence at the same physical wave numbers

`D_half/D_base = rho(theta_x) rho(theta_y)`.

For `0<|theta|<pi`, `cos(theta/2)>0` and `4-cos(theta)>0`, so `rho(theta)>0`. It is not constant; near zero

`rho(theta)=1+theta^4/32-theta^6/256+469 theta^8/368640+O(theta^10)`.

Therefore there is no exact mode-independent scalar mapping BASE to HALF over the resolved spectrum. Generic multimode BASE↔HALF data do not authorize a universal Richardson factor. Classification: `PASS_BASE_HALF_SPECTRAL_TRANSFER_RATIO_EXACT__NON_PROMOTING`.

This is estimator/provenance authority only. It does not promote physical index 2, identify a comparator residual, change thresholds, reorder support, or create ANSATZ-003. Implementation violation is `BLOCKED`, not Candidate-Gravity consistency FAIL.

## Retained Iteration 488 Fourier-symbol authority
For central4 coefficients `c=[1/12,-2/3,2/3,-1/12]` on nodes `[-2,-1,+1,+2]`, the exact dimensionless Fourier symbol is

`A(theta)=i sin(theta)(4-cos(theta))/3`.

There is no additional interior Fourier blind spot for `0<|theta|<pi`; within the Nyquist cell the only zeros are `theta=0` and `theta=±pi`. Mixed symbols are `D_h=A(theta_x)A(theta_y)/h^2` and `D_half=4 A(theta_x/2)A(theta_y/2)/h^2`. Classification: `PASS_CENTRAL4_FOURIER_SYMBOL_EXACT__NON_PROMOTING`.

## Retained Iteration 487 two-level truncation authority
Exact central4 moments through k=11 are `[0,1,0,0,0,-4,0,-20,0,-84,0,-340]`, giving `a5=-1/30`, `a7=-1/252`, `a9=-1/4320`. For `D_h=L_h^x L_h^y`,

`D_h-D_{h/2}=-(h^4/32)(f_51+f_15)-(h^6/256)(f_71+f_17)+h^8[-17/73728(f_91+f_19)+17/15360 f_55]+O(h^10)`.

Thus BASE↔HALF discrepancy generically mixes independent higher-derivative tensors. Two levels do not identify one truncation power and do not authorize Richardson promotion. Frozen `ds=-d_base`, assembled MP80↔MP120 threshold `2e-6`, and BASE↔HALF threshold `2e-5` remain unchanged.

## Latest raw-consumed numerical authority — Iteration 486
Rank13 run `34003038811`, job `101405200967`, artifact `9981274527`, artifact digest `sha256:020b0bcc7f5dc9addb305d999996c60dce3b39755df0d33ab621567e82eb7e6a`, scientific JSON SHA-256 `a4dda8d7e6ec15a40f09bc8d996850a5d13eba078ed6f14fb91aebdcba9ff2f1`.

At `(u,v)=(+1e-5,-5e-6)`: `80/80` finite; max scaled MP80↔MP120 `2.73638650835045783979016930046e-80 <= 1e-30`; max radial Richardson scaled error `2.57164812525073028434007436334e-15 <= 5e-4`. Classification: `PASS_RAW_CONSUMED_MANIFEST_RANK13_FULL_Z_MP80_MP120__NON_PROMOTING`.

## Rank14 action state
Canonical rank14 `(u,v)=(+1e-5,+5e-6)`, multiplicity 1, run **`34008118612`**, job **`101418951867`**, head SHA `1f0b876dc4178e4aaa4935c01455741dd81fd2c9`, has now reached `completed/success`. Artifact **`9982729453`**, artifact digest **`sha256:125d9302521f6d8f54705d99f8310560454950fc92c0ad861574f1fe6bef6915`**.

This is **not yet scientific PASS** because the raw artifact payload has not yet been independently fail-closed consumed into repository authority. Therefore certified support remains `18/32 = 56.25%`; do not advance coverage or launch rank15 solely from workflow colour.

## Retained physical authority and blocker
Timelike `Tr U2` before `+i/2` weight: `q^2=-1 -> +0.0005345424186332474`; `q^2=-0.34 -> -0.000734101259784574`; `q^2=-0.14 -> -0.001572666890130343`.

Frozen timelike `Tr U1^2` census: 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per q^2. Retained closures include Iteration 374 simple-simple 6/6, Iteration 393 simple-double 36/36, Iteration 399 index 5 / `q^2=-0.14 = +0.000119747535002548`, Iteration 409 index 4 / `q^2=-1 = +0.003562716046166582`, and Iteration 411 index 11 / `q^2=-0.34 = +0.013050543643260309`.

Iteration 421 remains blocker authority: run `33871920373`, raw-valid `BLOCKED_CONVERGENCE`. Diagnostic index-2 value `~+0.0035843041850530683` is not authority. Frozen failures remain `max_stability_scaled=2.2720400683804223e-05 > 2e-05` and `max_required_fit_residual_scaled=2.585665489102237e-05 > 2e-05`. No zero fill.

## Frozen numerical/assembly contracts
Iterations 436/437 close `N1/Q1`; 438 exact `A_finite`; 440 `Acoef/Asub`; 442 same-h representation/truncation; 445 Y-site; 446 post-parent contraction arithmetic; 447 localized the remaining Iteration-407 spectral/sample boundary. Iterations 449/450/453/456/459/461/463/466/468/470/473/475/480/484/486 progressively close direct-parent full-training-z mass support. Iteration 454 forbids unsupported `u<->v` deduplication. Iteration 455 freezes exact source order and coordinate states. Iteration 457 permits shared local precision certificates only for exact BASE/HALF coordinate overlaps while keeping derivative weights distinct. Iteration 485 fixes the exact shared-coordinate weight ratio `w_HALF=w_BASE/16`. Iterations 487–489 fix the two-level truncation, exact Fourier symbol, and exact mode-dependent BASE↔HALF transfer ratio.

After all 28 distinct support coordinates are locally certified, BASE and HALF central4 assemblies must be evaluated independently at MP80 and MP120. Retain `ds=-d_base`; no Richardson promotion. Require all finite, assembled scaled MP80↔MP120 discrepancy `<=2e-6`, retained BASE↔HALF mass-step discrepancy `<=2e-5`, plus retained provenance and conditioning contracts.

## Active gate — Iteration 489
Fail-closed raw-consume rank14 artifact `9982729453`. Workflow success and artifact metadata digest are insufficient by themselves. Only if the scientific JSON passes the frozen authority contract may coverage advance and the next explicit `UNTESTED` Iteration-455 coordinate be authorized. If raw consumption is BLOCKED or scientific fields fail, localize the first failing `z/phi/radial` sample without changing frozen dynamics, thresholds, support order, or precision conventions.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 489 closes an exact estimator/provenance subgate but no additional stable readiness-rubric component.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct q^2 variables are never summed. Same i0 is mandatory. No effective-action weight before operator-coordinate closure. No `u<->v` support deduplication without an exact frozen identity. Local MP sample PASS never substitutes for assembled derivative MP closure. Large cancellation condition number is diagnostic only. Exact BASE/HALF coordinate overlap may share the local sampled precision certificate but never the derivative weight. `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists. Fisher/resources remain forbidden until a nonzero algebraic residual exists. No blind heavy full-C5. Do not reopen the already-closed C5 null-soft e=3 sector. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Source/Born subtraction is allowed only in a matched observable after pole/cut-origin classification.
