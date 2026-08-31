# Candidate Gravity — Iteration 205: linked nonanalytic retarded-cut protocol

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Motivation

Iterations 202–204 exposed the central failure mode of finite analytic soft2 searches:

- an unbounded local derivative tower can interpolate any finite single-polarization analytic row set;
- restricting to deep IR can control powers only after an explicit Wilson-envelope assumption;
- the same deep IR makes analytic nonlocal shapes extremely near-degenerate with local EFT.

The next observable must therefore eliminate local analytic Wilson freedom **structurally**, not by choosing another finite polynomial cutoff.

## Normalized discontinuity

On a fixed positive timelike branch define

`D_s F = Disc_s F / (2 pi i)`.

For the retarded logarithm convention,

`D_s log_R(-s)=1`,

and therefore

`D_s[s^n log_R(-s)] = s^n`.

Inside a domain where a local counterterm is analytic,

`D_s P(s)=0`

for any finite polynomial and, more generally, for the local analytic derivative expansion term-by-term.

This is the key escape from the Iteration-202 finite interpolation theorem.

## Linked multi-point coordinate

Iteration 170 forbids treating a standalone positive two-point spectral density as gravity-specific: an ordinary positive-norm C4 mediator continuum can reproduce it exactly.

Iteration 171 also requires conditioning/amputation on the same two-point kernel.

Therefore the proposed new coordinate is not `D K2` alone. It is schematically

`T_cut = D Gamma3_ret,soft - W[D K2]`,

where

- `Gamma3_ret,soft` is the source-completed amputated retarded three-point/soft response object in the same physical field convention;
- `K2` is the measured/calibrated inverse two-point kernel from the same parent dynamics;
- `W` is the executable Ward/soft map that gives the part of the soft vertex fixed by the same K2.

The physical novelty carrier is the **linked nonanalytic remainder**, not the existence of a cut.

## Why the old local Ward/transverse ambiguity is reduced

Iteration 182 showed that a decomposition

`Gamma3 = W[K2] + B`

is not physically unique if one may shift an analytic transverse term `C` between the two pieces.

Under

`W -> W + C`, `B -> B - C`,

with C local/analytic in the cut variable,

`D C = 0`.

Hence the discontinuity-level linked coordinate is invariant under that analytic repartition.

For a local momentum-space Ward map made from differentiation and kinematic multiplication, discontinuity commutes with the map away from branch endpoints:

`D W[K2] = W[D K2]`.

A physical implementation still requires the actual source-completed gravitational Ward map; the toy validator in this iteration checks only the algebraic principle and does not pretend to compute that map.

## Local C5 theorem

### `CUT-NG-001 — DISCONTINUITY_ANNIHILATES_THE_UNBOUNDED_LOCAL_ANALYTIC_DERIVATIVE_TOWER_WITHIN_ITS_ANALYTIC_DOMAIN`

The dimension-12 cutoff problem of Iteration 202 disappears **for this projection**: all purely local analytic Wilson terms have zero discontinuity, independent of how high their derivative order is.

This statement does not eliminate loop-generated C5 cuts or thresholds. Those are physical comparator contributions and must be calculated.

## Decomposition theorem

### `CUT-NG-002 — LINKED_THREEPOINT_MINUS_WARD_OF_TWOPOINT_CUT_IS_INVARIANT_UNDER_ANALYTIC_WARD_TRANSVERSE_REPARTITION`

The nonanalytic linked remainder is insensitive to the local analytic ambiguity that blocked direct `W/B` separation in Iteration 182.

## Novelty guardrail

### `NG-FUNNEL-061 — NONANALYTICITY_MUST_BE_TESTED_AS_A_LINKED_MULTIPOINT_RELATION_NOT_A_STANDALONE_SPECTRAL_SIGNAL`

A branch cut, imaginary part or positive spectrum by itself remains non-promotable because of C4 and other quantum comparators.

The candidate target must be a relation involving at least the same-parent two-point cut and a higher-point retarded cut, with Ward/source completion and shared parameters.

## Literature anchors

- Cutkosky (1960): discontinuities across physical branch cuts are given by cut diagrams / on-shell intermediate states.
- Donoghue, Phys. Rev. D 50, 3874 (1994): in gravity EFT, universal low-energy quantum information is carried by nonlocal/nonanalytic terms; local high-energy contributions are analytic and cannot cancel the branch-cut structure.
- Bjerrum-Bohr, Donoghue, Vanhove, JHEP 02 (2014) 111: unitarity/on-shell methods extract universal quantum-gravity loop information from lower-order amplitudes.

## Current comparator status in the new protocol

- local analytic C5 tower: **exact null under D**;
- C5 massless-loop cut: **REQUIRED POSITIVE CONTROL — not yet instantiated**;
- C4 nonlinear mediator cut: **BLOCKED, not zero**;
- asymptotic-safety real-time three-graviton cut: **BLOCKED, not zero**;
- C3 ordered stochastic/MSR cut analogue: **BLOCKED, not zero**;
- nonlocal gravity loops/cuts: **BLOCKED unless the fixed parent supplies a causal loop prescription**.

## Readiness

`MODEL_READINESS: 23%`, unchanged.

The new protocol bypasses the local analytic tower structurally, but it has not yet produced a finite physical comparator matrix or residual.

## Exact next gate

Iteration 206 should instantiate the **C5 leading massless-loop positive control** for the linked cut as far as possible using unitarity/EFT authority. The first question is not its exact coefficient at every row, but the allowed functional/tensor rank of the leading C5 three-point discontinuity after conditioning on the same two-point cut.

In parallel:

- search for a fixed nonlinear C4 mediator cut realization;
- continue AS/C3 real-time authority audits;
- do not create `ANSATZ-003`, Fisher or resources.
