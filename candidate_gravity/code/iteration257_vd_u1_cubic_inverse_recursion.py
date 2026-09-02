import json
import numpy as np

rng = np.random.default_rng(257)

def sym(n, scale=1.0):
    m = rng.normal(size=(n, n)) * scale
    return 0.5 * (m + m.T)

n = 5
m = rng.normal(size=(n, n))
N0 = m @ m.T + 3.0 * np.eye(n)
N1 = sym(n, 0.15)
N2 = sym(n, 0.07)
A1 = sym(n, 0.20)
A2 = sym(n, 0.10)
A3 = sym(n, 0.08)

Q0 = np.linalg.inv(N0)
Q1 = -Q0 @ N1 @ Q0
Q2 = Q0 @ N1 @ Q0 @ N1 @ Q0 - Q0 @ N2 @ Q0

T1 = Q0 @ A3 @ Q0
T2 = Q1 @ A2 @ Q0
T3 = Q0 @ A2 @ Q1
T4 = Q2 @ A1 @ Q0
T5 = Q0 @ A1 @ Q2
T6 = Q1 @ A1 @ Q1
B3 = T1 + T2 + T3 + T4 + T5 + T6

eps = 1.0e-5
N_eps = N0 + eps * N1 + eps**2 * N2
Q_eps_exact = np.linalg.inv(N_eps)
Q_eps_series = Q0 + eps * Q1 + eps**2 * Q2

result = {
    "seed": 257,
    "inverse_series_error_at_eps_1e-5": float(np.max(np.abs(Q_eps_exact - Q_eps_series))),
    "symmetry_residual_Q0": float(np.max(np.abs(Q0 - Q0.T))),
    "symmetry_residual_Q1": float(np.max(np.abs(Q1 - Q1.T))),
    "symmetry_residual_Q2": float(np.max(np.abs(Q2 - Q2.T))),
    "pair_residual_T2T3": float(np.max(np.abs(T2.T - T3))),
    "pair_residual_T4T5": float(np.max(np.abs(T4.T - T5))),
    "symmetry_residual_T1": float(np.max(np.abs(T1 - T1.T))),
    "symmetry_residual_T6": float(np.max(np.abs(T6 - T6.T))),
    "symmetry_residual_B3": float(np.max(np.abs(B3 - B3.T))),
}

print(json.dumps(result, indent=2, sort_keys=True))
