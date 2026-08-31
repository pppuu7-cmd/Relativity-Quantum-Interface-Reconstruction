# Research Log — RQIR Iteration 214

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

Started from the actual repository authority rather than the stale front pointer: latest recovery/commits showed Iteration 213 as authoritative and prescribed universal gravitational IR subtraction for the frozen five-graviton total-s cut.

Literature audit of Weinberg's gravitational IR theorem and Donoghue–Torma's graviton-graviton one-loop analysis shows that the cancellation is a statement about the correctly assembled amplitude/inclusive observable, with soft bremsstrahlung and a declared regulator/subtraction convention. It does not authorize an arbitrary local subtraction on one isolated unitarity-cut channel.

Direct tree-level endpoint analysis of the exact Iteration-213 KLT cut engine gives equal north/south collinear residues at `epsilon=0.01`:

`r_N ~= r_S ~= -498.842246 - 2582.060295 i`,

with relative endpoint mismatch `~2.5e-14` at the frozen probe. The implied leading angular log coefficient has magnitude `3.3047e4`, quantitatively explaining the Iteration-213 cap-growth slope `3.2231e4` without fitting the subtraction coefficient from the cap integral.

Scientific classification:

- endpoint factorization: `PASS_SCOPED_TREE_CUT_DIAGNOSTIC`;
- raw isolated s-cut: `IR_COLLINEAR_LOG_DIVERGENT`;
- local endpoint subtraction of this one cut: `NOT_AUTHORIZED_AS_PHYSICAL_IR_COMPLETION`;
- physical regular+log C5 control: `BLOCKED_FULL_IR_SAFE_OR_EXPLICIT_HARD_REMAINDER`;
- Candidate Gravity residual: none.

Retain `IR-NG-003`, `C5-CUT-013`, `IR-NG-004`, `NG-FUNNEL-071`.

`MODEL_READINESS: 23%`, unchanged from Iteration 213. The blocker is now sharper, but no comparator block or unique residual has closed. `ANSATZ-003` remains uncreated; Fisher/resources remain forbidden.
