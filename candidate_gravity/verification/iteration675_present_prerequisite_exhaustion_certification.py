#!/usr/bin/env python3
from pathlib import Path
import json
R=Path(__file__).resolve().parents[2]
fail=[]
a=R/'candidate_gravity/results/iteration674_repository_authority_graph_audit_authority.json'
f=R/'candidate_gravity/recovery/CURRENT_QG_FRONT.md'
if not a.exists(): fail.append('missing Iter674 authority')
else:
 d=json.loads(a.read_text())
 if d.get('scientific_gate_pass') is not True or d.get('candidate_count')!=0: fail.append('Iter674 authority drift')
front=f.read_text(errors='ignore') if f.exists() else ''
required=[
 'MODEL_READINESS:** **24%',
 'PREREQUISITE_BLOCKED_NO_SAME_PARENT_CONCRETE_DETECTOR_GEOMETRY',
 'zero_fill=false',
 'Source/Born/source-completion subtraction remains `NOT_PERFORMED`',
 'No `ANSATZ-003`',
 'no Fisher/resources',
 'no blind full-C5',
 'Closed C5 e=3 remains closed',
 'weighted-B3 proxy residues are never actual Tr U1 authority']
for x in required:
 if x not in front: fail.append('front missing guardrail:'+x)
missing_authorities=[
 {'id':'M1_PHYSICAL_OBSERVABLE_BRIDGE','need':'Concrete same-parent MSSC001 conserved detector/asymptotic observable geometry with normalization/boundary/IR convention and compatibility with the frozen non-collinear soft family.'},
 {'id':'M2_MATCHED_SOURCE_BORN_COMPLETION','need':'Same-parent Source/Born/contact completion in the identical physical observable, with pole/cut origin classified before subtraction.'},
 {'id':'M3_ROBUST_COMPARATOR_SUBTRACTED_RESIDUAL','need':'A concrete nonzero algebraic residual after M1/M2; until then ANSATZ-003 and all downstream model promotion remain forbidden.'},
 {'id':'M4_ACTUAL_TR_U1_IF_REOPENED_BY_NEW_AUTHORITY','need':'Any future C5 path requiring Tr U1 must supply actual Tr U1 authority; historical weighted-B3 proxy residues cannot substitute.'}]
out={'iteration':675,'date':'2026-09-09','MODEL_READINESS':'24%','scientific_gate_pass':not fail,'failures':fail,'blocked':not fail,
 'classification':('BLOCKED_ITER675_PRESENT_REPOSITORY_PREREQUISITE_EXHAUSTION_CERTIFIED__NO_SCIENTIFICALLY_AUTHORIZED_COMPUTE_GATE_REMAINS_UNDER_FROZEN_GUARDRAILS__WAIT_FOR_NEW_AUTHORITY__NON_RESIDUAL' if not fail else 'FAIL_ITER675_PREREQUISITE_EXHAUSTION_CERTIFICATION'),
 'certified_scope':'Current committed repository authority under frozen guardrails as of Iter675; this is not a no-go theorem for Candidate Gravity and can be reopened only by genuinely new authority satisfying a missing prerequisite.',
 'missing_authorities':missing_authorities,
 'readiness_rubric':{'comparator_foundation':'24/25','robust_unique_residual':'0/20','frozen_parent_dynamics_ansatz':'0/20','consistency_positivity_ward_causality':'0/15','identifiability_fisher':'0/10','resource_experiment_closure':'0/10'},
 'anti_idle_resolution':'BLOCKED_PREREQUISITES_PROVED_AND_RECORDED__NO_OTHER_INDEPENDENT_ADMISSIBLE_STEP_PRESENT',
 'soft_tcut_branch':'FROZEN_PREREQUISITE_BLOCKED','source_born_subtraction':'NOT_PERFORMED','zero_fill':False,'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN','blind_full_C5':'FORBIDDEN','C5_e3':'CLOSED',
 'exact_next_gate':'No compute gate is scientifically authorized at present. Resume only when repository authority changes with one of the enumerated missing prerequisites or a genuinely new independent admissible branch; first raw-audit that new authority before launching computation.'}
p=R/'candidate_gravity/results/iteration675_present_prerequisite_exhaustion_certification.json'; p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
if fail: raise SystemExit(2)
