# RQIR Iteration 118 — Exact Toy009/Toy014 Calibration-Span Audit

**Date:** 2026-08-31  
**Status:** Paper-III source/calibration structural closure. No apparatus forecast and no new-physics claim.

## 1. Purpose

Iteration 117 derived a general rank/span gate for same-state reference settings. The next step is to stop reasoning with generic dimensional examples and reconstruct the **actual current calibration nuisance space** used by Toy009 and Toy014.

The established hard-constraint basis removes trace, mean-energy and the hidden signal direction, leaving

`Zu.shape=(25,22)`.

Thus the calibrated source-nuisance space is 22-dimensional.

## 2. Current calibration rows

The mature centered calibration construction contains

- `14` normalized mean rows: two probe channels at each of seven time layers;
- `8` normalized centered-covariance rows.

Projecting into the hard-constrained nuisance basis gives

`A_m = pm Zu`, shape `14 x 22`,

`A_c = pc Zu`, shape `8 x 22`.

The corresponding calibration Fisher contribution used by the physical spectral-tilt audit is

`K_cal = gamma_m A_m^T A_m + gamma_c A_c^T A_c`,

with positive `gamma_m,gamma_c` on the retained branch.

## 3. Exact rank result

For **both Toy009 and Toy014** the deterministic reconstruction gives

`rank(A_m)=14`,

`rank(A_c)=8`,

`rank([A_m;A_c])=22`.

Therefore the current mean+covariance calibration requirement is full rank on the entire 22-dimensional source-nuisance space.

### RQIR-RESOURCE-087 — full 22D calibration-span certificate

> After the current hard constraints, the retained mean and centered-covariance calibration families together span all 22 source-nuisance directions for Toy009 and Toy014.

Because both calibration weights are strictly positive, the current `K_cal` is positive definite on that 22D space.

## 4. Seven same-time mean layers are individually nonredundant

Pair the mean rows by physical time layer:

`L_j={probe0(t_j), probe1(t_j)}`, `j=1,...,7`.

For Toy009 and Toy014:

- every layer pair has rank `2`;
- adding the seven pairs sequentially increases cumulative rank by

`(2,2,2,2,2,2,2)`;
- the final mean-only span has rank `14`.

### RQIR-NG-075 — no removable mean layer in the current exact span

Within the present row construction, none of the seven same-time dual-probe mean layers is linearly redundant in the hard-constrained nuisance space. Deleting any one loses two score directions before covariance information is considered.

This does not prove that no redesigned calibration protocol could replace a layer; it proves that the **current** seven-layer basis has no exact linear redundancy to exploit.

## 5. Centered covariance supplies eight indispensable complementary directions

After the entire 14D mean span is present, add the eight centered-covariance rows one at a time.

For both Toy009 and Toy014 the rank increments are exactly

`(1,1,1,1,1,1,1,1)`.

Hence every covariance row contributes a new direction outside the span accumulated before it, and the final rank reaches `22`.

### RQIR-NG-076 — mean-only calibration cannot replace centered covariance

The seven mean layers span only 14 of the 22 source-nuisance directions. The eight centered-covariance rows supply the missing complementary rank.

Therefore the current full calibration cannot be reduced to seven mean layers by increasing their SNR or repetition count.

This is the concrete Toy009/Toy014 realization of Iteration-117 NG-074.

## 6. Consequence for one four-real transfer block

Suppose, optimistically, that one same-state four-real dual-tone transfer block also carries derivatives with respect to source-calibration nuisances. One unchanged setting can add at most four Fisher directions.

Starting from the 14D mean span, the dimensional ceiling would then be

`rank <= 14+4=18 < 22`.

Thus **one** four-real transfer setting cannot replace the entire eight-direction centered-covariance complement of the current calibration basis.

At least two distinct four-real settings would be required even dimensionally to supply eight missing directions, and that lower bound would still be insufficient unless their score orientations cover the covariance complement.

This is a structural statement about the current 22D calibration requirement. It does not assume that the transfer block actually couples to those source-nuisance directions; the repository presently does not provide such a physical joint Jacobian, so no overlap credit is taken.

### RQIR-RESOURCE-088 — covariance-complement replacement lower bound

> Relative to the current 14D mean span, replacing all eight independent covariance-complement directions using four-real reference settings requires at least two distinct settings, and only if their stacked score span covers the full 8D complement.

## 7. Conditioning of the actual spans

The rank is exact, but conditioning matters for wall-clock cost.

For Toy009:

- mean-span smallest singular value: `0.0033759149871`;
- covariance rows restricted to the mean-null complement: smallest singular value `~0.00423377`;
- full 22-row calibration smallest singular value: `0.00212667906656`;
- full condition number: `~409.926`.

For Toy014:

- mean-span smallest singular value: `0.00212542458324`;
- covariance-on-mean-null smallest singular value: `~0.00236475`;
- full smallest singular value: `0.00150105788788`;
- full condition number: `~650.582`.

Thus Toy014's full normalized calibration span is more weakly conditioned than Toy009's in this exact basis, consistent with Toy014's larger physical calibration cost found earlier. This is a geometry statement, not yet an apparatus time prediction.

## 8. What this iteration closes

Closed:

- actual hard-constrained source-nuisance dimension for the current calibration problem: `22`;
- exact mean/covariance ranks for Toy009 and Toy014;
- proof that all seven mean layer pairs are nonredundant in the current span;
- proof that all eight centered-covariance rows add complementary directions;
- proof that one four-real transfer setting cannot replace the entire covariance complement;
- conditioning diagnostics for Toy009 and Toy014.

Still open:

- whether some covariance observables can share a physical acquisition without backaction/double-counting;
- whether a redesigned multi-output reference protocol can cover several covariance-complement directions per setting;
- a physical joint transfer/source-calibration Jacobian;
- geometry/additive SI control rates;
- final non-double-counted detector-side `u` interval.

## 9. Readiness snapshot after Iteration 118

Project-management estimates, not statistical quantities:

- **Repository readiness for writing Paper III — scientific content:** **91%**.
- **Paper III submission-ready state:** **72%**.
- **Repository readiness to begin a concrete Candidate-Gravity model:** **84%**.
- **Concrete Candidate-Gravity model itself:** **~10%**.

Paper III increases because the generic rank uncertainty has been replaced by an exact Toy009/Toy014 calibration-span result. Candidate-Gravity readiness is unchanged because no QG dynamical or consistency gate was closed.

## 10. Next admissible gate

Audit the **physical sharing graph** of the eight covariance rows and seven mean layers using the already stored endpoint/backaction results:

1. group rows that occur at the same source time;
2. retain noncommutation/backaction restrictions from the covariance endpoint graph;
3. determine which same-time observables can legitimately share one physical record;
4. derive the minimum number of physically distinct calibration acquisitions/settings compatible with the exact 22D span;
5. insert that cover into RESOURCE-083.

No simultaneous credit should be given merely because rows share a timestamp.

## 11. Reproducibility

Run

`python analysis/toy009_toy014_calibration_span_iteration118.py`.

The script reconstructs Toy009 and Toy014, projects all current calibration rows into the 22D hard-constrained basis, checks layer-by-layer rank increments and records the complementary singular-value diagnostics.
