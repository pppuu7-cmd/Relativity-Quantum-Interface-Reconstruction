# RQIR Research Log — Iteration 100

**Date:** 2026-08-30  
**Track:** Paper III single-platform apparatus-certificate population.

Audited Gosling et al., *Phys. Rev. Research* 6, 013129 (2024) as a stronger single-platform spectral anchor than a scalar-ASD-only experiment.

Positive result:

- the same levitated platform measures ordinary PSDs and an off-diagonal x-y cross-correlation spectrum;
- the paper provides a susceptibility-based force-domain calibration relation and calibrated directional-force inference;
- therefore a non-diagonal spectral likelihood is experimentally realizable in one force-sensing platform.

New guardrail:

- **APP-004:** same-platform cross-spectral measurement is a legitimate apparatus primitive;
- **NG-053:** covariance is coordinate-specific. A spatial x-y cross-spectrum cannot be inserted as the RQIR temporal f,2f cross-PSD without an explicit transfer/normalization/acquisition map.

APP-003 remains incomplete: exact f,2f input-referred force matrix, seven calibration Fisher blocks/rates, Toy009/Toy014 source-preparation throughput, and campaign duty/control/characterization rates remain open.

Reproducibility: `analysis/single_platform_cross_spectral_audit_iteration100.py`.
