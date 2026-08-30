"""RQIR Iteration 119: all-eight covariance endpoint graph and optimal partition.

Cross-covariance-only Gaussian output bound.  It does not waive the existing
quantum noncommutation/backaction gate for shared source trajectories.
"""
from __future__ import annotations

import numpy as np

GAMMA_COV_009 = 5.901272925e5
GAMMA_COV_014 = 2.7186736e6

VERTICES = (
    "G0@0", "G1@0", "G0@TR", "G0@T1",
    "G1@T5", "G1@TR", "G1@T3", "G0@T6",
)
IDX = {v: i for i, v in enumerate(VERTICES)}

# Exact eight centered-covariance rows from the established operator_rows list.
EDGES = (
    ("G0@TR", "G0@0"),
    ("G0@T1", "G1@0"),
    ("G1@T5", "G1@0"),
    ("G1@TR", "G0@0"),
    ("G0@TR", "G1@0"),
    ("G1@T3", "G0@0"),
    ("G0@T6", "G0@0"),
    ("G0@T6", "G1@0"),
)


def adjacency(edge_ids):
    a = np.zeros((len(VERTICES), len(VERTICES)))
    for e in edge_ids:
        u, v = EDGES[e]
        i, j = IDX[u], IDX[v]
        a[i, j] = a[j, i] = 1.0
    return a


def rho2(edge_ids) -> float:
    ev = np.linalg.eigvalsh(adjacency(edge_ids))
    return float(np.max(np.abs(ev)) ** 2)


def partitions(seq):
    if not seq:
        yield []
        return
    first = seq[0]
    for rest in partitions(seq[1:]):
        yield [[first]] + [b[:] for b in rest]
        for i in range(len(rest)):
            new = [b[:] for b in rest]
            new[i] = [first] + new[i]
            yield new


def endpoint_disjoint(edge_ids) -> bool:
    used = set()
    for e in edge_ids:
        for v in EDGES[e]:
            if v in used:
                return False
            used.add(v)
    return True


def main() -> None:
    all_ids = list(range(8))
    a = adjacency(all_ids)
    ev = np.linalg.eigvalsh(a)
    print("all-eight adjacency eigenvalues", ev)
    assert abs(rho2(all_ids) - 6.0) < 1e-12

    # Under Sigma=I and uniform affine cross-covariance edge amplitude a,
    # full-hypercube positivity requires a < 1/rho(A).  Edge Fisher is a^2.
    f_edge_ceiling = 1.0 / rho2(all_ids)
    assert abs(f_edge_ceiling - 1.0 / 6.0) < 1e-13

    # Exhaustive set-partition regression: minimize sum rho(G_k)^2.
    best_value = float("inf")
    best = None
    count = 0
    for part in partitions(all_ids):
        count += 1
        value = sum(rho2(block) for block in part)
        if value < best_value - 1e-12:
            best_value = value
            best = part
    assert count == 4140
    assert abs(best_value - 4.0) < 1e-12
    assert best is not None
    assert len(best) == 4
    assert all(endpoint_disjoint(block) and len(block) == 2 for block in best)

    # A transparent matching partition with the same exact optimum.
    matching_partition = ([3, 4], [2, 5], [1, 6], [0, 7])
    assert abs(sum(rho2(b) for b in matching_partition) - 4.0) < 1e-12
    assert all(endpoint_disjoint(b) for b in matching_partition)

    # Accepted-trajectory lower bounds in the normalized cross-covariance class.
    for name, gamma in (("Toy009", GAMMA_COV_009), ("Toy014", GAMMA_COV_014)):
        all_joint = 6.0 * gamma
        optimal_partition = 4.0 * gamma
        separate = 8.0 * gamma
        print(name, "all8 joint >", all_joint,
              "optimal four-matchings >", optimal_partition,
              "eight separate >", separate)
        assert optimal_partition < all_joint < separate

    print("optimal partition", matching_partition)
    print("optimal sum rho^2", best_value)


if __name__ == "__main__":
    main()
