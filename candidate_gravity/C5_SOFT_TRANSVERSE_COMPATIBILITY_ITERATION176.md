# Candidate Gravity — Iteration 176: C5 soft-transverse compatibility gate

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**  
**Decision:** Iteration-150 finite off-shell C5 cubic columns are scientifically valid but cannot be reused as Iteration-175 `B_T` columns

## 1. Question

Iteration 175 freezes the next relation space as the Ward-subtracted transverse soft coefficient

\[
B_T^{(i)}=P_T\left[\Gamma^{(3)}_{arr,i}-\mathcal W_i[K^{(2)}]\right]
\]

at sub-subleading `O(k_soft^2)` order.

Iteration 150 already contains two real local C5 curvature-cubic response columns, `Tr(Ricci^3)` and cyclic `Riemann^3`, of rank `2/2` on six finite off-shell momentum triplets. Can those numerical columns simply be treated as the first `B_T` comparator basis?

The answer is **no**.

## 2. Protocol mismatch

Iteration 150 freezes six finite off-shell triplets

`(p,-q,-r)`, with `p=q+r`,

and evaluates the full projected cubic response at those finite momenta. No external leg is defined as a deformation parameter tending to zero.

Iteration 175 instead requires a one-parameter soft family

\[
k_{soft}(\epsilon)=\epsilon k_0,
\qquad \epsilon\to0,
\]

with exact momentum conservation and the same physical metric/source convention for every `epsilon`.

At each `epsilon` one must:

1. evaluate the source-completed cubic vertex from the same covariant action;
2. evaluate and subtract the Ward-determined `W[K^(2)]` piece;
3. project the independent transverse tensor structure;
4. extract the `epsilon^2` coefficient.

A finite cubic value at one nonsoft kinematic point is not that Taylor coefficient.

## 3. Analytic non-identifiability proof

Even knowing the finite response, the leading soft value and the subleading soft derivative does not determine the sub-subleading coefficient.

Take any analytic reference response `f0(epsilon)` and define

\[
\boxed{
f_c(\epsilon)=f_0(\epsilon)+c\,\epsilon^2(1-\epsilon)^2
}
\]

for arbitrary real `c`.

For every `c`,

\[
f_c(0)=f_0(0),
\]

\[
f_c'(0)=f_0'(0),
\]

and

\[
f_c(1)=f_0(1).
\]

But the `epsilon^2` Taylor coefficient changes by exactly `c`.

Therefore the data set

`{soft0, soft1, one finite response point}`

still leaves `soft2` arbitrary.

This is a theorem-level protocol statement; it does not depend on numerical conditioning.

## 4. Reproducible toy certificate

Use

`f0(epsilon)=1.25-0.7 epsilon+2.4 epsilon^2`.

For `c=-5,-1,0,2,7.5`, every member has

- `f(0)=1.25`;
- `f'(0)=-0.7`;
- `f(1)=2.95`;

while the `epsilon^2` coefficients are respectively

`[-2.6,1.4,2.4,4.4,9.9]`.

Thus even exact agreement on the finite point and on soft0/soft1 does not identify the transverse soft2 coefficient.

## 5. What remains valid from Iterations 150–151

Nothing is revoked.

Iteration 150 remains a valid finite off-shell C5 cubic tangent certificate:

- `Tr(Ricci^3)`;
- cyclic `Riemann^3`;
- finite tangent rank `2/2`;
- singular values `[4.83562189,1.10930485]`;
- `s_min/s_max=0.2294027268`.

Iteration 151 remains a valid scoped source-completed EH Ward certificate. The completed action-level identity

`B3[L_xi,h2,h3] + B2[Lie_xi h2,h3] + B2[h2,Lie_xi h3] = 0`

passes with the expected second-order convergence.

Those results answer different questions from the new soft-transverse quotient.

## 6. Required C5 `B_T` computation

The first C5 transverse comparator must therefore be recomputed from the parent actions.

Freeze target-independently:

- the same physical metric/source convention;
- a six-row family of hard kinematics derived from the existing protocol;
- a declared null or controlled soft graviton direction `k0`;
- `k_soft=epsilon k0`;
- momentum conservation for every `epsilon`;
- the same TT/transverse tensor convention;
- the local curvature-cubic C5 operator subset.

For each operator and row:

1. compute the source-completed cubic action response as a function of `epsilon`;
2. subtract the two-point-determined Ward piece `W[K2]`;
3. project `P_T`;
4. fit or derive the `epsilon^2` coefficient with convergence checks;
5. form the six-row column;
6. compute the target-independent rank/SVD.

Only those columns may enter the C5 `B_T` comparator matrix.

## 7. Retained results

### `C5-NG-007 — FINITE_OFFSHELL_CUBIC_RESPONSE_DOES_NOT_DETERMINE_WARD_SUBTRACTED_SOFT2_COEFFICIENT`

A finite off-shell C5 cubic response column cannot be reinterpreted as a soft-transverse `O(k^2)` form-factor column without a controlled soft deformation of the same parent action.

### `SOFT-NG-003 — PRESERVING_SOFT0_SOFT1_AND_ONE_FINITE_POINT_STILL_LEAVES_SOFT2_FREE`

The analytic counterfamily `c epsilon^2(1-epsilon)^2` proves that even leading, subleading and one finite point do not identify the sub-subleading coefficient.

### `NG-FUNNEL-036 — TRANSVERSE_SOFT_COMPARATOR_COLUMNS_MUST_BE_RECOMPUTED_FROM_SOFT_DEFORMED_PARENT_ACTION`

Comparator reuse across finite and soft protocols is forbidden unless an explicit map proves equivalence.

## 8. Readiness

`MODEL_READINESS: 24%` — unchanged.

The compatibility question is closed, but the actual C5 `B_T` columns remain `BLOCKED_NEW_SOFT_DEFORMED_ACTION_LEVEL_COMPUTATION_REQUIRED`.

No `ANSATZ-003`. No Fisher. No resources.

## 9. Next gate

Iteration 177 should construct the first actual soft-deformed C5 operator columns, beginning with the two already authoritative curvature-cubic parent actions. The main deliverable is not a finite response value but the converged `epsilon^2` Ward-subtracted transverse coefficient on each of the six rows.
