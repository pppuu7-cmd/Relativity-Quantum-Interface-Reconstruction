# RQIR Recovery Delta — Iteration 099

**Date:** 2026-08-30

Paper III primitive apparatus-certificate closure.

New result: the repository now has an explicit minimum common-normalization certificate for Toy009/Toy014.

Required per architecture:

- science `(a2,a4,rho)`;
- seven physical calibration rates `k1...k7` or equivalent full `2x2` Fisher blocks;
- common absolute detector/calibration throughput scale `R0`;
- source apparatus `(p_E,Omega_E,t_reset,V)` or directly certified robust `R_src`;
- duty/control interval `d`;
- for characterization scheduling: uncertainty/covariance, `R_char`, irreducible floor and duty/cost.

New labels:

- APP-003: close all common-normalization dependency cuts before an absolute RESOURCE-045/NG-030 architecture claim;
- NG-052: complete toy-source coefficients do not constitute a complete experiment certificate.

Current status: source-model quantities are well populated, but the absolute apparatus certificate is still incomplete; the Toy009/Toy014 absolute winner is data-underdetermined, not algebra-underdetermined.

Files: `analysis/primitive_certificate_iteration099.py`, `docs/PAPER_III_PRIMITIVE_APPARATUS_CERTIFICATE_ITERATION099.md`, research log.
