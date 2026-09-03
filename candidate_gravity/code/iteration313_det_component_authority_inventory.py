#!/usr/bin/env python3
"""RQIR Iteration 313: fail-closed repository authority inventory.

This is not a physics-kernel derivation. It searches the checked-out repository
for explicit determinant graviton/ghost component authority and reports
candidate evidence paths. Keyword hits never count as formula authority.
Promotion requires an explicit machine-readable authority declaration in an
existing repository file containing all required component labels, frozen
parent/convention scope, and an affirmative authority marker.
"""
from __future__ import annotations
import json, pathlib, re

ROOT=pathlib.Path('.')
EXCLUDE={'.git','.venv','venv','__pycache__'}
required_grav=['H1','H2','H3']
required_ghost=['N1','N2','N3']
patterns=[re.compile(r'\bH[123]\b'),re.compile(r'\bN[123]\b'),re.compile(r'ghost',re.I),re.compile(r'determinant',re.I)]
authority_markers=('AUTHORITATIVE_COMPONENT_FORMULAS','PHYSICAL_COMPONENT_AUTHORITY: PASS','COMPONENT_FORMULA_AUTHORITY=true')
frozen_scope_markers=('D=4','Lambda=0','a=-1/2')

candidates=[]
authority_files=[]
for p in ROOT.rglob('*'):
    if not p.is_file() or any(part in EXCLUDE for part in p.parts):
        continue
    if p.suffix.lower() not in {'.md','.txt','.json','.py','.yaml','.yml','.tex'}:
        continue
    try: text=p.read_text(encoding='utf-8',errors='ignore')
    except Exception: continue
    hits=[pat.pattern for pat in patterns if pat.search(text)]
    if hits:
        candidates.append({'path':str(p),'hits':hits[:8]})
    has_all=all(re.search(rf'\b{x}\b',text) for x in required_grav+required_ghost)
    has_authority=any(m in text for m in authority_markers)
    has_scope=all(m in text for m in frozen_scope_markers)
    if has_all and has_authority and has_scope:
        authority_files.append(str(p))

# This gate deliberately does not treat its own script/workflow or current-front
# prose as physical formula authority.
authority_files=[p for p in authority_files if 'iteration313_' not in p and 'CURRENT_QG_FRONT.md' not in p]
physical_authority_present=bool(authority_files)
classification=('PASS_DETERMINANT_COMPONENT_AUTHORITY_INVENTORY__EXPLICIT_AUTHORITY_FOUND'
                if physical_authority_present else
                'PASS_DETERMINANT_COMPONENT_AUTHORITY_INVENTORY__PHYSICAL_COMPONENT_FORMULAS_BLOCKED_ABSENT_EXPLICIT_AUTHORITY')
result={
 'iteration':313,
 'model_readiness_percent':24,
 'scientific_gate_pass':True,
 'classification':classification,
 'candidate_residual':False,
 'inventory_contract':{
   'keyword_hits_are_authority':False,
   'promotion_requires_all_components':required_grav+required_ghost,
   'promotion_requires_scope':list(frozen_scope_markers),
   'promotion_requires_explicit_authority_marker':list(authority_markers)
 },
 'authority_files':authority_files,
 'candidate_evidence_paths':candidates[:200],
 'physical_component_status':{
   'graviton_H1_H2_H3':'PROVIDED_WITH_EXPLICIT_AUTHORITY' if physical_authority_present else 'BLOCKED_EXPLICIT_SAME_PARENT_FORMULAS_NOT_FOUND',
   'ghost_N1_N2_N3':'PROVIDED_WITH_EXPLICIT_AUTHORITY' if physical_authority_present else 'BLOCKED_EXPLICIT_SAME_PARENT_FORMULAS_NOT_FOUND',
   'U2_V1_1_V1_2_H0_H1':'BLOCKED_UNCHANGED',
   'source_contact_completion':'BLOCKED_DOWNSTREAM'
 },
 'guardrails':['UNSUPPORTED_IS_BLOCKED_NOT_ZERO_FILLED','KEYWORD_PRESENCE_IS_NOT_AUTHORITY','NO_BLIND_HEAVY_FULL_C5','NO_ANSATZ003_FISHER_RESOURCES'],
 'next_gate':('validate and freeze exact same-parent determinant component conventions/routing from the explicit authority file(s) before scoped numerator/cut evaluation'
              if physical_authority_present else
              'determinant physical numerator/cut gate is BLOCKED on explicit same-parent H1/H2/H3 and ghost N1/N2/N3 formulas; inspect CURRENT_QG_FRONT for an independent permitted prerequisite, otherwise retain typed blocker')
}
print(json.dumps(result,indent=2,sort_keys=True))
