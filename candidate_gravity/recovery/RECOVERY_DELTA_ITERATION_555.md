# RQIR Candidate Gravity — Recovery Delta Iteration 555

Date: 2026-09-07

## Authority advanced
Iteration 555 derives an exact midpoint/antisymmetric decomposition of the already established u↔v routing distinction.

Define `m=(u+v)/2`, `d=(v-u)/2`. Then for the frozen parent kinematics,

`alpha(u,v)=-1/2+d/s`,
`alpha(v,u)=-1/2-d/s`,

while the Kallen combination becomes

`lambda=s^2-4 s m+4 d^2`,

so rho is even in `d`.

With

`p_mid=-a-q/2+rho(m,d^2)n`,

exactly

`p(u,v)=p_mid+(d/s)q`,
`p(v,u)=p_mid-(d/s)q`.

Thus the exchange midpoint has alpha=-1/2 exactly and the swap displacement is purely q-directed. This is a routing/provenance diagnostic only; it does not imply general observable linearity/parity in `d` and does not authorize u↔v support substitution.

Classification: `PASS_ITER424_UV_SWAP_MIDPOINT_ANTISYMMETRIC_DECOMPOSITION_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`.

Machine-readable authority: `candidate_gravity/results/iteration555_iter424_uv_swap_midpoint_antisymmetric_decomposition_exact.json`.
Reproducible audit: `candidate_gravity/code/iteration555_uv_swap_midpoint_decomposition_audit.py`.

## Active heavy route
Rank8 canonical run `34153849866`, coordinate `(+1.25e-6,-1.25e-6)`, remains the only authorized heavy successor pending terminal completion and fail-closed raw consumption. No duplicate was launched during this iteration.

## Frozen blockers retained
Physical unresolved set remains `[2]`. The concrete `Source/Ward/contact+K2` algebraic target and robust comparator-subtracted residual remain absent. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden.

MODEL_READINESS: 24%
ITERATION_TASK_COMPLETION: 100%
Readiness change: 0 percentage points; an exact routing/provenance subgate closed, but no additional stable model-readiness rubric sector completed.

## Exact next gate
Raw-consume rank8 after terminal completion. Only raw-valid PASS permits frozen rank9 `(+1.25e-6,+1.25e-6)`.
