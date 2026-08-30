#!/usr/bin/env python3
"""RQIR Iteration 090 — external multimode frequency-compatibility audit.

Uses only explicitly published frequency intervals/bands recorded in the
Iteration-090 document. No apparatus sensitivity is inferred.
"""
from itertools import combinations

MODES_KHZ = {
    "x": (222.0, 226.0),  # 224 +/- 2 kHz
    "y": (266.0, 270.0),  # 268 +/- 2 kHz
    "z": (79.0, 81.0),    # 80 +/- 1 kHz
}


def ratio_interval(a, b):
    """Ratio larger/smaller for positive independent intervals a,b."""
    # determine using central ordering; intervals here do not overlap
    if sum(a)/2 >= sum(b)/2:
        hi, lo = a, b
    else:
        hi, lo = b, a
    return hi[0]/lo[1], hi[1]/lo[0]


def contains_target(interval, target=2.0):
    return interval[0] <= target <= interval[1]


def main():
    for p,q in combinations(MODES_KHZ,2):
        ri=ratio_interval(MODES_KHZ[p],MODES_KHZ[q])
        print(f"{p}/{q} ratio interval={ri}, contains 2={contains_target(ri)}")
        assert not contains_target(ri)

    # A frequency band can contain both f and 2f only if f <= fmax/2 and
    # f >= fmin, requiring fmax/fmin >= 2.
    band=(70.0,95.0)
    ratio=band[1]/band[0]
    print("70-95 kHz band span ratio",ratio)
    assert ratio < 2.0
    print("PASS")

if __name__ == "__main__":
    main()
