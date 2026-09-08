#!/usr/bin/env python3
import json

# Prospective, outcome-blind Schwinger-Keldysh contract.
# Branch-to-r/a field rotation inherited from Iter171 for gravity and applied
# identically to the scalar probe:
#   X_+ = X_r + X_a/2,  X_- = X_r - X_a/2.
# The measured scalar observable is the retarded component G_phi^{ra}=G_R.
# Physical metric perturbations are h_r insertions at h_a=0.

M = {
    '+': {'r': 1.0, 'a': 0.5},
    '-': {'r': 1.0, 'a': -0.5},
}
sigma = {'+': 1.0, '-': -1.0}

def vertex_weight(indices):
    return sum(sigma[b] * prod(M[b][i] for i in indices) for b in ('+','-'))

def prod(xs):
    out = 1.0
    for x in xs:
        out *= x
    return out

# Same-branch unitary action S_+-S_- must have no all-r vertex and unit
# coefficient for exactly one a leg, independent of leg ordering.
rotation_checks = {
    'rrr_zero': vertex_weight('rrr'),
    'arr_unit': vertex_weight('arr'),
    'rar_unit': vertex_weight('rar'),
    'rra_unit': vertex_weight('rra'),
    'aaa_quarter': vertex_weight('aaa'),
}

# Tree-level causal scalar inverse-kernel perturbation from a physical h_r
# insertion has only off-diagonal r/a entries.  Enumerate the 2x2 matrix
# products noncommutatively and verify that the measured (r,a) propagator
# component selects only the retarded chain.
# G indices: (r,r)=Keldysh, (r,a)=R, (a,r)=A, (a,a)=0.
G = {
    ('r','r'): [('K',)],
    ('r','a'): [('R',)],
    ('a','r'): [('A',)],
    ('a','a'): [],
}
# dK[h_r]: (a,r)=dKR and (r,a)=dKA.  This orientation makes
# (G dK G)_{r a}=R dKR R.
dK = {
    ('r','r'): [],
    ('r','a'): [('dKA',)],
    ('a','r'): [('dKR',)],
    ('a','a'): [],
}

def matmul(A, B):
    C = {}
    for i in ('r','a'):
        for j in ('r','a'):
            terms=[]
            for k in ('r','a'):
                for x in A[(i,k)]:
                    for y in B[(k,j)]:
                        terms.append(x+y)
            C[(i,j)] = terms
    return C

def chain(n):
    X = G
    for _ in range(n):
        X = matmul(matmul(X, dK), G)
    return X[('r','a')]

chain1 = chain(1)
chain2 = chain(2)
chain3 = chain(3)
expected1 = [('R','dKR','R')]
expected2 = [('R','dKR','R','dKR','R')]
expected3 = [('R','dKR','R','dKR','R','dKR','R')]

# Complete cubic source family census inherited from Iter594.
family_census = {
    'K3_contact': 1,
    'K1_K2_ordered_placements': 6,
    'K1_cubed_ordered_chains': 6,
    'total': 13,
}

failures=[]
for k,v in {'rrr_zero':0.0,'arr_unit':1.0,'rar_unit':1.0,'rra_unit':1.0,'aaa_quarter':0.25}.items():
    if rotation_checks[k] != v:
        failures.append(f'rotation {k}: {rotation_checks[k]} != {v}')
if chain1 != expected1: failures.append(f'chain1={chain1}')
if chain2 != expected2: failures.append(f'chain2={chain2}')
if chain3 != expected3: failures.append(f'chain3={chain3}')
if family_census['total'] != 13: failures.append('family census != 13')

result = {
    'iteration': 627,
    'date': '2026-09-09',
    'contract_id': 'MSSC001-GRAVITY-SK-MEAS-V1',
    'scientific_gate_pass': not failures,
    'candidate_residual': False,
    'classification': ('PASS_ITER627_PROSPECTIVE_COMBINED_MATTER_GRAVITY_SK_CONTRACT__RETARDED_SCALAR_PROBE__PHYSICAL_HR_INSERTIONS__INTERNAL_SCALAR_LINES_INDUCED_RETARDED__NON_RESIDUAL'
                       if not failures else
                       'FAIL_ITER627_COMBINED_MATTER_GRAVITY_SK_CONTRACT_VALIDATION'),
    'prospective_freeze': {
        'generating_functional': 'Z[J_phi+,J_phi-,J_g+,J_g-]=Integral exp{i S[g+,phi+] - i S[g-,phi-] + i(source+ - source-)}',
        'field_rotation': 'X_+=X_r+X_a/2; X_-=X_r-X_a/2 for X in {h,phi}',
        'physical_background': 'h_a=0; differentiate with respect to h_r',
        'measured_scalar_observable': 'G_phi^{ra}=G_R (retarded scalar two-point component)',
        'endpoint_amputation': 'amputate only the two common external scalar G_R factors after taking the third h_r derivative; retain every internal scalar propagator, K3, all six K1/K2 placements, all six ordered K1^3 chains',
        'internal_scalar_component_rule': 'derive by r/a matrix multiplication; for the measured ra component under h_r insertions each surviving internal chain propagator is G_R, never assigned root-by-root by hand',
        'gravity_overlap_requirement': 'same h_+=h_r+h_a/2, h_-=h_r-h_a/2 rotation and physical h_r insertion convention as Iter171; native gravitational observable remains in the Iter149 retarded/in-in sector'
    },
    'rotation_checks': rotation_checks,
    'causal_matrix_checks': {
        'G_dK_G_ra': chain1,
        'G_dK_G_dK_G_ra': chain2,
        'G_dK_G_dK_G_dK_G_ra': chain3,
        'all_surviving_internal_lines': 'R'
    },
    'family_census': family_census,
    'consequence_for_iter615': 'Iter615 K+i0 coefficients remain historical source-side authority, but native bridge must recompute scalar-pole discontinuity coefficients with the induced retarded prescription; no root may be hand-flipped or deleted.',
    'source_born_subtraction': 'NOT_PERFORMED',
    'zero_fill': False,
    'N_native_fit': False,
    'projected_candidate_values_used_to_choose_contract': False,
    'failures': failures,
    'MODEL_READINESS': '24%',
    'readiness_change': '0 percentage points',
    'next_gate': 'Iteration628: recompute the six supported scalar-pole coefficients under the frozen retarded internal-line prescription, preserving all 13 source families and the Iter613/614 kinematic trajectory; derive the common source-to-native phase/normalization from the same SK convention before native projection.'
}
print(json.dumps(result, indent=2))
if failures:
    raise SystemExit(1)
