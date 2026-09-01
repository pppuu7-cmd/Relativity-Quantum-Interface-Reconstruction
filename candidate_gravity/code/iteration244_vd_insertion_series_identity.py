#!/usr/bin/env python3
"""Iteration 244: exact noncommutative trace-log identity for the VD U1/U2 series.

We assign weighted EOM degrees deg(U1)=1, deg(U2)=2 and expand

    -1/2 Tr log(1 - U1 + U2)

through total EOM degree five.  Noncommutative words are combined only after
cyclic trace equivalence.  This reproduces Cho--Kantowski's general-gauge-
theory series (their Eq. 36) through O(E^5).

The Giacchini--de Paula Netto--Shapiro 4D convention Eq. (14) has the opposite
connection-series sign (with the standard i factor):

    Gamma_conn = +(i/2) Tr log(1 - U1 + U2).

Its degree <=2 expansion is exactly Eq. (14), fixing the mapped cubic terms
without guessing from a truncated polynomial.
"""

from collections import defaultdict
from fractions import Fraction
import json

MAX_DEG = 5
WEIGHT = {"1": 1, "2": 2}


def degree(word):
    return sum(WEIGHT[x] for x in word)


def multiply(a, b):
    out = defaultdict(Fraction)
    for wa, ca in a.items():
        for wb, cb in b.items():
            w = wa + wb
            if degree(w) <= MAX_DEG:
                out[w] += ca * cb
    return dict(out)


def canonical_cyclic(word):
    if not word:
        return word
    rotations = [word[i:] + word[:i] for i in range(len(word))]
    return min(rotations)


def trace_log_series(prefactor):
    # X=-U1+U2 in log(1+X)
    X = {("1",): Fraction(-1), ("2",): Fraction(1)}
    powers = {1: X}
    for n in range(2, MAX_DEG + 1):
        powers[n] = multiply(powers[n - 1], X)

    raw = defaultdict(Fraction)
    for n, poly in powers.items():
        log_factor = Fraction((-1) ** (n + 1), n)
        for word, coeff in poly.items():
            raw[word] += prefactor * log_factor * coeff

    cyclic = defaultdict(Fraction)
    for word, coeff in raw.items():
        cyclic[canonical_cyclic(word)] += coeff
    return {w: c for w, c in cyclic.items() if c}


def label(word):
    # Only labels present through degree five in this two-generator series.
    if word == ("1",): return "Tr(U1)"
    if word == ("1","1"): return "Tr(U1^2)"
    if word == ("2",): return "Tr(U2)"
    if word == ("1","1","1"): return "Tr(U1^3)"
    if word == ("1","2"): return "Tr(U1 U2)"
    if word == ("1","1","1","1"): return "Tr(U1^4)"
    if word == ("1","1","2"): return "Tr(U1^2 U2)"
    if word == ("2","2"): return "Tr(U2^2)"
    if word == ("1","1","1","1","1"): return "Tr(U1^5)"
    if word == ("1","1","1","2"): return "Tr(U1^3 U2)"
    if word == ("1","2","2"): return "Tr(U1 U2^2)"
    return "Tr(" + " ".join("U"+x for x in word) + ")"


# Cho--Kantowski source convention.
cho = trace_log_series(Fraction(-1, 2))
expected_cho = {
    ("1",): Fraction(1,2),
    ("1","1"): Fraction(1,4),
    ("2",): Fraction(-1,2),
    ("1","1","1"): Fraction(1,6),
    ("1","2"): Fraction(-1,2),
    ("1","1","1","1"): Fraction(1,8),
    ("1","1","2"): Fraction(-1,2),
    ("2","2"): Fraction(1,4),
    ("1","1","1","1","1"): Fraction(1,10),
    ("1","1","1","2"): Fraction(-1,2),
    ("1","2","2"): Fraction(1,2),
}
assert cho == expected_cho, (cho, expected_cho)

# 2020 Eq.(14) convention: + i/2 times the same logarithm.  Store the real
# coefficients multiplying i.
g2020 = trace_log_series(Fraction(1, 2))
expected_quad_2020 = {
    ("1",): Fraction(-1,2),
    ("2",): Fraction(1,2),
    ("1","1"): Fraction(-1,4),
}
assert {w:c for w,c in g2020.items() if degree(w)<=2} == expected_quad_2020

expected_cubic_2020 = {
    ("1","1","1"): Fraction(-1,6),
    ("1","2"): Fraction(1,2),
}
assert {w:c for w,c in g2020.items() if degree(w)==3} == expected_cubic_2020

result = {
    "iteration": 244,
    "model_readiness_percent": 24,
    "source_identity": "-1/2 Tr log(1-U1+U2)",
    "source_series_match_through_eom_degree_5": True,
    "source_series": [
        {"degree": degree(w), "term": label(w), "coefficient": str(c)}
        for w,c in sorted(cho.items(), key=lambda kv:(degree(kv[0]), kv[0]))
    ],
    "mapped_2020_connection_identity": "+(i/2) Tr log(1-U1+U2)",
    "eq14_quadratic_match": True,
    "mapped_2020_cubic_terms": [
        {"term": "i Tr(U1 U2)", "coefficient": "1/2"},
        {"term": "i Tr(U1^3)", "coefficient": "-1/6"}
    ],
    "primitive_U3_required_in_reduced_series": False,
    "iteration243_U3_placeholder_status": "SUPERSEDED_BY_EXPLICIT_U1_U2_SERIES_AUTHORITY",
    "classification": "PASS_EXACT_VD_OEPS3_INSERTION_SERIES_IDENTITY",
    "remaining_blocker": "COMPOSITE_U1_U2_TRACES_TO_FINITE_CPT3_MASTER_MAP_AND_PURE_GRAVITY_PROJECTION",
    "heavy_full_CPT3_run_authorized": False,
    "next_gate": 245
}

print(json.dumps(result, indent=2, sort_keys=True))
