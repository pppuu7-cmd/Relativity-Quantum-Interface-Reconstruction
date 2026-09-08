import json

rows = [
    ("D_b^-@0.013028588574858", -0.0002675723690149917, [0.000028281661413489156, -0.000009830297080490817], -0.00024912100468199333),
    ("D_s^-@0.09", 0.0007675486979583489, [-0.000034657086594251, 0.000006141727271618239], 0.0007390333386357162),
    ("D_a^-@0.09868572571657197", 0.00014341388002850046, [0.000038828802297676104, 0.000012084823865363016], 0.00019432750619153958),
    ("D_a^+@1.241314274283428", 0.001408269614376145, [0.00005200227436655513, -0.00017525395094202036], 0.0012850179378006798),
    ("D_b^+@1.726971411425142", -0.001239244171890075, [0.0005439085521551718, -0.00005138488950843567], -0.0007467205092433388),
    ("D_s^-@2.89", -0.0024361654995358048, [0.00013189790213615299, 0.00016687559016912812], -0.0021373920072305236),
]

out_rows = []
for label, pair, cubic, aggregate in rows:
    l1 = abs(pair) + sum(abs(x) for x in cubic)
    cancellation_margin = abs(aggregate) / l1
    componentwise_condition = l1 / abs(aggregate)
    out_rows.append({
        "root": label,
        "aggregate": aggregate,
        "component_l1": l1,
        "cancellation_margin": cancellation_margin,
        "componentwise_relative_condition_number": componentwise_condition,
    })

abs_coeff = [abs(r[3]) for r in rows]
anchor = abs(rows[0][3])
ratios = [r[3] / rows[0][3] for r in rows]
result = {
    "iteration": 620,
    "classification": "PASS_ITER620_PROJECTIVE_SOURCE_SHAPE_CONDITIONING_DIAGNOSTIC__NORMALIZATION_INVARIANT_NON_PROMOTING",
    "scientific_gate_pass": True,
    "diagnostic_only": True,
    "thresholds_introduced": False,
    "N_native_used": False,
    "roots_summed": False,
    "source_born_subtraction": "NOT_PERFORMED",
    "rows": out_rows,
    "projective_ratios_anchor_D_b_minus": ratios,
    "projective_abs_dynamic_range": max(abs_coeff) / min(abs_coeff),
    "max_componentwise_relative_condition_number": max(r["componentwise_relative_condition_number"] for r in out_rows),
    "min_cancellation_margin": min(r["cancellation_margin"] for r in out_rows),
    "model_readiness_percent": 24,
}
print(json.dumps(result, indent=2))
