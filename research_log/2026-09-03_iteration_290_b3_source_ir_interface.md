# RQIR Research Log — Iteration 290

**Date:** 2026-09-03  
**MODEL_READINESS:** 24%

## Question

Can the robust Iteration-289 `B3` pole be classified or subtracted directly using the frozen MSSC-001 source-cut Born-factorization residue?

## Result

No. The current `B3` pole and the `R=-8 M_Born` source residue are not yet in the same observable/normalization convention. The former is a scoped off-shell/1PI same-parent Vilkovisky contribution before source/Ward/contact completion; the latter is an on-shell connected source-cut result.

The Iteration-218 Ward identity

`k_mu V^{mu nu}=(p'^2-m^2)p^nu-(p^2-m^2)p'^nu`

shows why the on-shell source result cannot fix the missing off-shell EOM/contact coefficient: the relevant longitudinal terms vanish on shell.

## Classification

`PASS_SOURCE_IR_INTERFACE_AUTHORITY_MAP__B3_POLE_ORIGIN_STILL_BLOCKED`.

This is an operational/interface BLOCKED result. It is not a consistency FAIL, exact comparator identity, near-degeneracy, or novelty certificate. The earlier regime-specific non-identifiability boundary is retained.

## Consequence

The next calculation must be pole-level and linked:

`T_cut = D Gamma3_ret,soft - W[D K2]`.

Derive the `1/epsilon` coefficient of the linked two-point/Ward/source/contact completion in the same convention before using any finite master term. Only after Ward/EOM pole separation may the already frozen physical Born/inclusive IR prescription be applied to a matched connected observable.

No Candidate Gravity residual is declared.

MODEL_READINESS: 24%

Change from Iteration 289: 0 percentage points; the interface is now authority-clean, but no readiness-rubric block is closed.