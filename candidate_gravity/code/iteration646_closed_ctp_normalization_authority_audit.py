#!/usr/bin/env python3
"""Iteration 646: fail-closed authority audit for absolute closed-CTP loop normalization.

This gate does not inspect Candidate/comparator values and does not modify the
Iter645 reduced densities.  It asks only whether the already committed parent
authority fixes the single global factor needed to promote those reduced
numerator-weighted densities to absolute native D_s densities.
"""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[2]
ITERATION=646

def read(p):
    return (ROOT/p).read_text()

p627=read('candidate_gravity/results/iteration627_combined_sk_contract.json')
p630=read('candidate_gravity/results/iteration630_closed_retarded_loop_keldysh_gate.json')
p632=read('candidate_gravity/results/iteration632_minkowski_vacuum_gk_contract.json')
p311=read('candidate_gravity/code/iteration311_det_e0c3_cubic_logdet_operator_contract.py')
p645=read('candidate_gravity/code/iteration645_closed_gamma3_reduced_cut_density.py')

checks={
 'iter627_ctp_exponent_present':'exp{i S[g+,phi+] - i S[g-,phi-]' in p627,
 'iter627_explicit_W_minus_i_logZ':('W=-i' in p627 or 'W = -i' in p627),
 'iter627_explicit_Gamma_legendre_normalization':('Legendre' in p627 and 'Gamma' in p627),
 'iter630_exactly_one_GK_per_closed_family':'exactly one G_K' in p630,
 'iter632_GK_absolute_distribution':'G_K_vac' in p632 and '2*pi*i*delta(D)' in p632,
 'iter311_logdet_topology_present':'log(1+X)=X-X^2/2+X^3/3' in p311,
 'iter311_explicit_real_scalar_i_over_2_prefactor':('i/2' in p311 or '0.5j' in p311 or '1j/2' in p311),
 'iter645_reduced_factor_only':'beta/(16*pi*pi)' in p645 and 'BLOCKED_NOT_ASSUMED' in p645,
 'iter645_absolute_prefactor_deliberately_unfixed':'absolute_closed_CTP_effective_action_phase_prefactor' in p645,
}

# Existing authority fixes causal slots, G_K normalization, relative logdet topology,
# and the reduced phase-space kernel, but it does not explicitly bind W=-i ln Z /
# the CTP Legendre map plus its global one-loop real-scalar prefactor to the native
# Gamma3 normalization.  Since Iter645 values have already been evaluated, choosing
# that missing factor now would be a post-result convention change rather than an
# inherited authority derivation.
required_present=(checks['iter627_explicit_W_minus_i_logZ'] and
                  checks['iter627_explicit_Gamma_legendre_normalization'] and
                  checks['iter311_explicit_real_scalar_i_over_2_prefactor'])
failures=[]
for k in ('iter627_ctp_exponent_present','iter630_exactly_one_GK_per_closed_family',
          'iter632_GK_absolute_distribution','iter311_logdet_topology_present',
          'iter645_reduced_factor_only','iter645_absolute_prefactor_deliberately_unfixed'):
    if not checks[k]: failures.append('authority drift: '+k)

classification=('BLOCKED_ITER646_ABSOLUTE_CLOSED_CTP_TO_NATIVE_GAMMA3_NORMALIZATION_NOT_EXPLICITLY_BOUND__ONE_GLOBAL_FACTOR_REMAINS__NON_RESIDUAL'
                if not failures and not required_present else
                ('PASS_ITER646_EXISTING_AUTHORITY_ALREADY_BINDS_ABSOLUTE_CLOSED_CTP_NORMALIZATION__NON_RESIDUAL'
                 if not failures else 'FAIL_ITER646_NORMALIZATION_AUTHORITY_AUDIT_DRIFT'))

result={
 'iteration':ITERATION,
 'date':'2026-09-09',
 'MODEL_READINESS':'24%',
 'readiness_change':'0 percentage points',
 'classification':classification,
 'scientific_gate_pass':False if classification.startswith('BLOCKED_') else (not failures),
 'candidate_residual':False,
 'checks':checks,
 'failures':failures,
 'authority_conclusion':{
   'fixed':'Iter627 CTP exponent/ra rotation; Iter630 one-GK closed-loop causal structure; Iter632 G_K=2*pi*i delta(D); Iter311 relative Tr-log cubic topology; Iter645 reduced beta/(16*pi^2) kernel.',
   'missing':'an explicit same-parent W=-i ln Z / Legendre-to-native-Gamma3 normalization statement carrying the real-scalar Gaussian one-loop global phase/prefactor into the exact native Gamma3 convention.',
   'degrees_of_freedom_remaining':'exactly one common nonzero complex/global scalar factor; no root-, family-, or q2-dependent normalization is licensed.',
   'post_result_freeze_forbidden':True
 },
 'literature_role':'Standard Gaussian functional-integral conventions can motivate i/2 Tr log for a real scalar, but literature cannot retroactively replace missing same-parent repository authority after Iter645 reduced values have been evaluated.',
 'candidate_values_used':False,
 'zero_fill':False,
 'source_born_subtraction':'NOT_PERFORMED',
 'native_Y_Tcut_projection':'NOT_PERFORMED',
 'comparator_quotient':'NOT_PERFORMED',
 'ANSATZ_003':'FORBIDDEN',
 'Fisher_resources':'FORBIDDEN',
 'next_gate':'Recover an earlier explicit same-parent CTP W/Gamma normalization or an earlier Fourier/loop-measure convention that uniquely binds the one remaining global factor. If none predates Iter645, retain BLOCKED; do not choose i/2, +/-i, or any fitted factor post hoc.'
}
out=ROOT/'results'/'iteration646_closed_ctp_normalization_authority_audit'
out.mkdir(parents=True,exist_ok=True)
(out/'result.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
if failures: raise SystemExit(2)
