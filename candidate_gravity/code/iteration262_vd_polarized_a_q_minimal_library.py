from itertools import permutations
import json

LEGS = ("s", "a", "b")


def A1_terms(x):
    return [
        f"Rg1[{x}] Rd0 H0",
        f"Rg0 Rd1[{x}] H0",
        f"Rg0 Rd0 H1[{x}]",
    ]


def A2_terms(x, y):
    return [
        f"Rg0 Rd0 H2[{x},{y}]",
        f"Rg1[{x}] Rd0 H1[{y}]",
        f"Rg1[{y}] Rd0 H1[{x}]",
        f"Rg0 Rd1[{x}] H1[{y}]",
        f"Rg0 Rd1[{y}] H1[{x}]",
        f"Rg1[{x}] Rd1[{y}] H0",
        f"Rg1[{y}] Rd1[{x}] H0",
    ]


def A3_terms(a, b, c):
    legs = (a, b, c)
    out = [f"Rg0 Rd0 H3[{a},{b},{c}]"]
    for x in legs:
        yz = [z for z in legs if z != x]
        out.extend([
            f"Rg1[{x}] Rd0 H2[{yz[0]},{yz[1]}]",
            f"Rg0 Rd1[{x}] H2[{yz[0]},{yz[1]}]",
        ])
    for g, d in permutations(legs, 2):
        h = next(z for z in legs if z not in (g, d))
        out.append(f"Rg1[{g}] Rd1[{d}] H1[{h}]")
    return out


def q2_formula(x, y):
    return [
        f"+ Q0 N1[{x}] Q0 N1[{y}] Q0",
        f"+ Q0 N1[{y}] Q0 N1[{x}] Q0",
        f"- Q0 N2[{x},{y}] Q0",
    ]


def main():
    a1 = A1_terms("s")
    a2 = A2_terms("s", "a")
    a3 = A3_terms(*LEGS)

    assert len(a1) == 3
    assert len(a2) == 7
    assert len(a3) == 13
    assert len(set(a3)) == 13

    # Affine generator means no R2/R3 structures can appear.
    assert all("Rg2" not in t and "Rd2" not in t and "Rg3" not in t and "Rd3" not in t for t in a3)

    result = {
        "iteration": 262,
        "A1_subterm_count": len(a1),
        "A2_subterm_count": len(a2),
        "A3_subterm_count": len(a3),
        "A1_s_terms": a1,
        "A2_s_a_terms": a2,
        "A3_s_a_b_terms": a3,
        "Q1_formula": "Q1[x] = -Q0 N1[x] Q0",
        "Q2_s_a_formula_terms": q2_formula("s", "a"),
        "higher_generator_variations_required": False,
        "Q3_required_for_B3_when_A0_zero": False,
        "minimal_dynamic_inputs": [
            "N1[x]", "N2[x,y]", "R1[x]", "H1[x]", "H2[x,y]", "H3[s,a,b]"
        ],
        "soft_guardrail": "A1[s]=0 applies to the complete three-term sum, not term-by-term"
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
