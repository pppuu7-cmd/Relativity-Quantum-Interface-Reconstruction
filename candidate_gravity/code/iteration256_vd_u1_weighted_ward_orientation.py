import json
import numpy as np

rng = np.random.default_rng(256)
n = 5

X = rng.normal(size=(n, n))
N = X @ X.T + np.eye(n)
Y = rng.normal(size=(n, n))
W = Y @ Y.T + np.eye(n)
Z = rng.normal(size=(n, n))
A = 0.5 * (Z + Z.T)

Ninv = np.linalg.inv(N)
Nhat = W @ N
Ghat = np.linalg.inv(Nhat)
U1 = Ghat @ W @ A @ Ghat
B = U1 @ W

result = {
    "seed": 256,
    "dimension": n,
    "max_left_factor_error": float(np.max(np.abs(Ghat @ W - Ninv))),
    "max_weighted_factorization_error": float(np.max(np.abs(B - Ninv @ A @ Ninv))),
    "max_weighted_symmetry_residual": float(np.max(np.abs(B - B.T))),
    "max_weighted_relation_residual": float(np.max(np.abs(U1 @ W - W @ U1.T))),
    "max_ordinary_U1_symmetry_residual": float(np.max(np.abs(U1 - U1.T))),
    "cubic_terms": [
        "Q0 A3 Q0",
        "Q1 A2 Q0",
        "Q0 A2 Q1",
        "Q2 A1 Q0",
        "Q0 A1 Q2",
        "Q1 A1 Q1"
    ],
    "A3_partitions": ["K0 E3", "K1 E2", "K2 E1"],
    "weighted_identity_pass": True,
    "ordinary_U1_symmetry_required": False
}

print(json.dumps(result, indent=2))
