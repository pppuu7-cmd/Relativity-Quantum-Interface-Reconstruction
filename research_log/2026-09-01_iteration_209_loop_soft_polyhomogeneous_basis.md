# Research Log — RQIR Iteration 209

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

Loop-soft authority audit completed.

Key correction: the four-dimensional one-loop soft sector is not generically a pure Taylor expansion. Subleading and higher soft orders receive loop/IR corrections, and logarithms of the soft graviton energy appear in 4D. Generic sub-subleading soft behavior also contains non-universal information tied to two- and three-point functions.

Therefore:

- previous local/tree `soft2` results remain scoped-valid;
- loop/nonanalytic C5 and future Candidate Gravity columns must use explicit regular + log-soft coordinates;
- the hard-channel discontinuity must be evaluated at finite soft momentum before the polyhomogeneous soft extraction;
- no tree soft theorem may be used to infer the loop `T_cut` directly.

Next: executable conditioning/recovery test for the one-loop regular+log basis.
