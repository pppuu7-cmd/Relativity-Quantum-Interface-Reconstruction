# RQIR research log — Iteration 252

Date: 2026-09-01

Recovered authoritative Candidate Gravity front at Iteration 251 with MODEL_READINESS 24%. Instead of immediately differentiating the remaining `R(DR)` kernel, audited the notation against Giacchini–de Paula Netto–Shapiro (2020), because Eq. (16) uses the inverse orbit metric while Eq. (53) gives the minimal ghost matrix.

Result: freeze the distinction

- `N_orb = R G R`;
- `Nhat = Y^up N_orb`;
- `N_orb^-1 = Nhat^-1 Y^up`;
- `N_orb^-1 Y_down = Nhat^-1`;
- `U1 = Nhat^-1 Y^up [R.(D R).E] Nhat^-1`.

Therefore Iteration 251's two `delta(Nhat^-1)` placements survive. The remaining gauge-weight variation is a single explicit `delta Y^up` insertion.

For the frozen TT hard mode, `delta sqrt(|g|)=0` and

`delta[sqrt(|g|) g^{mu nu}] = -epsilon^{mu nu}`

up to the fixed global weight normalization. Central finite difference at step `1e-6` agrees to `5.44e-11` maximum component error. Matrix orientation certificate error: `1.11e-16`.

Classification: `PASS_SCOPED_U1_ORBIT_GHOST_WEIGHT_FACTORIZATION_AND_TT_DELTA_WEIGHT`.

Readiness remains 24%. Heavy C5 run remains unauthorized. Next gate: explicit `delta[R(DR)] E^(2)` and assembly/Ward test of the complete `E^(2)K^(1)` `Tr U1` numerator.
