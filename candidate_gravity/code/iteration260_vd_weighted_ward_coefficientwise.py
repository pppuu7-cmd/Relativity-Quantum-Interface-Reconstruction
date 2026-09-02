import json
import numpy as np

SEED = 260
DIM = 6


def symmetric_random(rng, n):
    x = rng.normal(size=(n, n))
    return 0.5 * (x + x.T)


def main():
    rng = np.random.default_rng(SEED)
    x = rng.normal(size=(DIM, DIM))
    n0 = x.T @ x + 3.0 * np.eye(DIM)
    n1 = symmetric_random(rng, DIM)
    n2 = symmetric_random(rng, DIM)
    a1 = symmetric_random(rng, DIM)
    a2 = symmetric_random(rng, DIM)
    a3 = symmetric_random(rng, DIM)

    q0 = np.linalg.inv(n0)
    q1 = -q0 @ n1 @ q0
    q2 = q0 @ n1 @ q0 @ n1 @ q0 - q0 @ n2 @ q0

    terms = [
        q0 @ a3 @ q0,
        q1 @ a2 @ q0,
        q0 @ a2 @ q1,
        q2 @ a1 @ q0,
        q0 @ a1 @ q2,
        q1 @ a1 @ q1,
    ]
    b3 = sum(terms)

    out = {
        "seed": SEED,
        "dimension": DIM,
        "max_Q0_sym": float(np.max(np.abs(q0 - q0.T))),
        "max_Q1_sym": float(np.max(np.abs(q1 - q1.T))),
        "max_Q2_sym": float(np.max(np.abs(q2 - q2.T))),
        "pair_Q1A2Q0_vs_Q0A2Q1": float(np.max(np.abs(terms[1].T - terms[2]))),
        "pair_Q2A1Q0_vs_Q0A1Q2": float(np.max(np.abs(terms[3].T - terms[4]))),
        "term_Q0A3Q0_sym": float(np.max(np.abs(terms[0] - terms[0].T))),
        "term_Q1A1Q1_sym": float(np.max(np.abs(terms[5] - terms[5].T))),
        "max_B3_sym": float(np.max(np.abs(b3 - b3.T))),
        "interpretation": "Regression certificate only. Exact coefficientwise symmetry follows analytically from symmetric N_orb(t), Q(t)=N_orb(t)^-1, and complete same-parent A(t).",
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
