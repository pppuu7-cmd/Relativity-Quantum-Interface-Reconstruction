from fractions import Fraction
import json

# Frozen central4 first-derivative coefficients on nodes [-2,-1,+1,+2].
nodes = [-2, -1, 1, 2]
c = [Fraction(1,12), Fraction(-2,3), Fraction(2,3), Fraction(-1,12)]

# Work in units where h_BASE=1 and h_HALF=1/2. Mixed derivative weights scale as c_i*c_j/h^2.
h_base = Fraction(1,1)
h_half = Fraction(1,2)
shared = [(-1,-1), (-1,1), (1,-1), (1,1)]

def idx(node):
    return nodes.index(node)

rows = []
for ub, vb in shared:
    # Same physical coordinate is inner node +/-1 on BASE and outer node +/-2 on HALF.
    ih_u = -2 if ub < 0 else 2
    ih_v = -2 if vb < 0 else 2
    wb = c[idx(ub)] * c[idx(vb)] / (h_base*h_base)
    wh = c[idx(ih_u)] * c[idx(ih_v)] / (h_half*h_half)
    assert wb != 0
    ratio = wh / wb
    assert ratio == Fraction(1,16)
    assert (wb > 0) == (wh > 0)
    rows.append({
        'base_node_pair': [ub, vb],
        'half_node_pair': [ih_u, ih_v],
        'base_weight_scaled': str(wb),
        'half_weight_scaled': str(wh),
        'half_over_base': str(ratio),
        'same_sign': True,
    })

result = {
    'iteration': 485,
    'classification': 'PASS_SHARED_BASE_HALF_CERTIFICATE_WEIGHT_RATIO_EXACT__NON_PROMOTING',
    'identity': 'For each exact BASE/HALF shared coordinate, w_HALF = w_BASE / 16 for the frozen central4 mixed derivative.',
    'derivation': {
        'central4_coefficients': [str(x) for x in c],
        'h_half_over_h_base': '1/2',
        'base_shared_node_coeff_magnitude': '2/3',
        'half_shared_node_coeff_magnitude': '1/12',
        'coefficient_product_ratio_half_over_base': '1/64',
        'inverse_h2_ratio_half_over_base': '4',
        'net_weight_ratio_half_over_base': '1/16'
    },
    'shared_coordinates_count': 4,
    'rows': rows,
    'guardrails': [
        'PRECISION_CERTIFICATE_MAY_BE_SHARED_ONLY_AT_EXACT_COORDINATE_OVERLAP',
        'DERIVATIVE_CONTRIBUTION_WEIGHT_MUST_NOT_BE_SHARED',
        'NO_SOURCE_REORDER',
        'NO_THRESHOLD_CHANGE',
        'NO_PHYSICAL_PROMOTION',
        'NO_ANSATZ003',
        'NO_FISHER_RESOURCES'
    ],
    'MODEL_READINESS': '24%',
    'readiness_change_pp': 0
}
print(json.dumps(result, indent=2, sort_keys=True))
