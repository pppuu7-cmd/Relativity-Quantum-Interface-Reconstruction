#!/usr/bin/env python3
"""Iteration 598: fail-closed audit of Iter597 against frozen Iter596 routing.

This gate does not re-evaluate the nonlinear Ward identity.  It asks whether the
implemented Iter597 object actually instantiated the prospectively frozen Iter596
contract.  Negative Iter597 numbers are preserved, but they may only be promoted to
scientific Ward authority if the implementation used the required one-leg symmetric
route p=-q_g/2, p'=+q_g/2 for the mandatory reduction anchor and did not substitute
arbitrary probe momenta for that contract.
"""
from __future__ import annotations
import hashlib, json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ITER=598
src_path=ROOT/'analysis'/'nonlinear_ward_full_response_iteration597.py'
contract_path=ROOT/'candidate_gravity'/'contracts'/'ITERATION596_NONLINEAR_WARD_CONTRACT.md'
outdir=ROOT/'results'/'iteration598_iter597_contract_conformance'
outdir.mkdir(parents=True,exist_ok=True)

src=src_path.read_text()
contract=contract_path.read_text()
failures=[]
findings=[]

required_contract_strings=['p=-q_g/2','p\'=+q_g/2','Mandatory reduction anchor']
for s in required_contract_strings:
    if s not in contract:
        failures.append(f'Iter596 contract drift: missing {s!r}')

# The shipped Iter597 implementation defines arbitrary PROBES and then loops over
# those PROBES in its "Mandatory one-leg reduction" block.  That is not the
# prospectively frozen symmetric route.
probe_def=bool(re.search(r'^PROBES\s*=\s*\[',src,re.M))
anchor_marker='Mandatory one-leg reduction of the IMPLEMENTED matrix covariance identity.'
anchor_i=src.find(anchor_marker)
assembly_i=src.find('Independent cross-check that this Fourier-matrix G reproduces Iter594')
anchor_block=src[anchor_i:assembly_i] if anchor_i>=0 and assembly_i>anchor_i else ''
anchor_uses_probes='for p0 in PROBES:' in anchor_block
anchor_builds_symmetric=('p0=-0.5*qs[g]' in anchor_block or 'p0 = -0.5*qs[g]' in anchor_block or 'p0=-qs[g]/2' in anchor_block or 'p0 = -qs[g]/2' in anchor_block)

findings.append({'probe_definition_present':probe_def,
                 'anchor_uses_arbitrary_PROBES':anchor_uses_probes,
                 'anchor_constructs_frozen_symmetric_route':anchor_builds_symmetric})

if not probe_def:
    failures.append('Iter597 source structure drift: PROBES definition not found')
if not anchor_uses_probes:
    failures.append('Iter597 source structure drift: expected audited anchor loop not found')
if anchor_uses_probes and not anchor_builds_symmetric:
    failures.append('CONTRACT_MISMATCH: Iter597 mandatory one-leg anchor used arbitrary PROBES instead of frozen p=-q_g/2 symmetric route')

# The implementation also evaluates the full Ward rows on PROBES.  Because Iter596
# explicitly binds the scalar route attached to each gauge singleton to Iter587's
# symmetric route, this requires a prospective repair before a frozen-contract Ward
# PASS/FAIL can be assigned.
ward_i=src.find('ward=[];')
result_i=src.find('result={',ward_i)
ward_block=src[ward_i:result_i] if ward_i>=0 and result_i>ward_i else ''
ward_uses_probes='for p0 in PROBES:' in ward_block
ward_builds_symmetric=('p0=-0.5*qs[g]' in ward_block or 'p0 = -0.5*qs[g]' in ward_block or 'p0=-qs[g]/2' in ward_block or 'p0 = -qs[g]/2' in ward_block)
findings.append({'full_ward_uses_arbitrary_PROBES':ward_uses_probes,
                 'full_ward_constructs_frozen_symmetric_route':ward_builds_symmetric})
if ward_uses_probes and not ward_builds_symmetric:
    failures.append('CONTRACT_MISMATCH: Iter597 full Ward rows used arbitrary PROBES instead of frozen gauge-attached symmetric scalar route')

classification=('BLOCKED_ITER597_IMPLEMENTATION_DOES_NOT_INSTANTIATE_FROZEN_ITER596_ROUTE__NEGATIVE_NUMBERS_PRESERVED_NONAUTHORITATIVE'
                if failures else
                'PASS_ITER597_IMPLEMENTATION_CONFORMS_TO_FROZEN_ITER596_ROUTE__NON_RESIDUAL')
result={
 'iteration':ITER,'date':'2026-09-08','model_readiness_percent':24,
 'classification':classification,'scientific_gate_pass':not failures,
 'failures':failures,'findings':findings,
 'iter597_source_sha256':hashlib.sha256(src_path.read_bytes()).hexdigest(),
 'iter596_contract_sha256':hashlib.sha256(contract_path.read_bytes()).hexdigest(),
 'negative_iter597_numbers':'PRESERVED_AS_IMPLEMENTED_OBJECT_DIAGNOSTIC_NOT_FROZEN_CONTRACT_AUTHORITY' if failures else 'ELIGIBLE_FOR_RAW_AUTHORITY_REVIEW',
 'source_born_subtraction':'NOT_PERFORMED','candidate_residual':False,
 'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
 'next_gate':'prospectively repair Iter597 evaluator so mandatory anchor and full Ward rows use exact p=-q_g/2,p\'=+q_g/2 route for each gauge leg; retain all 13 source families and Iter596 transformations; then rerun raw-valid full Ward gate' if failures else 'raw-consume Iter597 as frozen-contract result'
}
rp=outdir/'result.json'
rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
sha=hashlib.sha256(rp.read_bytes()).hexdigest()
audit={'iteration':ITER,'classification':'PASS_RAW_INTEGRITY_ITER598_CONFORMANCE_AUDIT','failures':[], 'result_sha256':sha}
(outdir/'authority_audit.json').write_text(json.dumps(audit,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
# BLOCKED is the expected scientifically useful result here, not an operational error.
