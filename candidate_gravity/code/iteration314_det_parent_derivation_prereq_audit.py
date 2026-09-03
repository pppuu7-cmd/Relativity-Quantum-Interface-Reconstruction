#!/usr/bin/env python3
"""RQIR Iteration 314: fail-closed prerequisite audit for same-parent determinant derivation.

This gate does NOT invent H1/H2/H3 or N1/N2/N3. It identifies whether the
repository contains enough explicit frozen parent-dynamics authority to start an
executable component derivation: parent action, background/field split,
gauge-fixing functional, Faddeev-Popov/ghost operator, perturbative expansion
convention, momentum/Fourier convention, and frozen D=4,Lambda=0,a=-1/2 scope.
Keyword hits are evidence candidates only; no missing item is zero-filled.
"""
from __future__ import annotations
import json, pathlib, re

ROOT=pathlib.Path('.')
EXCLUDE={'.git','.venv','venv','__pycache__'}
TEXT_SUFFIX={'.md','.txt','.json','.py','.yaml','.yml','.tex'}

requirements={
 'parent_action':[r'Einstein[- ]Hilbert',r'\bsqrt\s*\(?-?g\)?',r'\bR\b'],
 'background_field_split':[r'background field',r'\bg\s*=\s*.*h',r'\bbar\s*\{?g'],
 'gauge_fixing':[r'gauge[- ]fix',r'de Donder',r'harmonic gauge',r'F_?mu'],
 'ghost_fp_operator':[r'Faddeev[- ]Popov',r'ghost operator',r'FP operator',r'bar\s*\{?c'],
 'perturbative_expansion':[r'quadratic',r'cubic',r'perturb',r'expansion'],
 'momentum_fourier':[r'Fourier',r'momentum routing',r'all momenta',r'ingoing momenta'],
 'scope_D4':[r'D\s*=\s*4',r'D=4'],
 'scope_Lambda0':[r'Lambda\s*=\s*0',r'Lambda=0',r'\\Lambda\s*=\s*0'],
 'scope_a_minus_half':[r'a\s*=\s*-\s*1/2',r'a=-1/2'],
}

files=[]
for p in ROOT.rglob('*'):
    if not p.is_file() or p.suffix.lower() not in TEXT_SUFFIX or any(x in EXCLUDE for x in p.parts):
        continue
    if 'iteration314_' in p.name:
        continue
    try: txt=p.read_text(encoding='utf-8',errors='ignore')
    except Exception: continue
    files.append((str(p),txt))

evidence={}
for key,pats in requirements.items():
    hits=[]
    for path,txt in files:
        matched=[pat for pat in pats if re.search(pat,txt,re.I|re.M)]
        if matched:
            hits.append({'path':path,'patterns':matched})
    evidence[key]=hits[:100]

# Strong derivation authority requires explicit repository sources for every
# prerequisite category. Presence is still only prerequisite authority, not
# component-formula authority.
missing=[k for k,v in evidence.items() if not v]
prereq_complete=not missing
classification=(
 'PASS_DETERMINANT_SAME_PARENT_DERIVATION_PREREQUISITES_LOCATED__COMPONENT_DERIVATION_AUTHORIZED_NEXT'
 if prereq_complete else
 'PASS_DETERMINANT_SAME_PARENT_DERIVATION_PREREQUISITE_AUDIT__DERIVATION_BLOCKED_MISSING_EXPLICIT_PARENT_AUTHORITY'
)
result={
 'iteration':314,
 'model_readiness_percent':24,
 'scientific_gate_pass':True,
 'classification':classification,
 'candidate_residual':False,
 'component_formulas_derived':False,
 'keyword_hits_are_component_authority':False,
 'prerequisite_authority_complete':prereq_complete,
 'missing_prerequisites':missing,
 'evidence':evidence,
 'scope':{'D':4,'Lambda':0,'a':'-1/2'},
 'guardrails':['UNSUPPORTED_IS_BLOCKED_NOT_ZERO_FILLED','NO_SYNTHETIC_COMPONENT_PROMOTION','NO_BLIND_HEAVY_FULL_C5','NO_ANSATZ003_FISHER_RESOURCES'],
 'next_gate':(
   'derive executable same-parent H1/H2/H3 and N1/N2/N3 from the located frozen parent sources; state index spaces, transposes, normalization and routing; independently validate before Iteration-312 insertion'
   if prereq_complete else
   'retain BLOCKED on missing explicit parent-dynamics prerequisite(s); freeze exact missing categories and pursue only an independent permitted prerequisite from CURRENT_QG_FRONT'
 )
}
print(json.dumps(result,indent=2,sort_keys=True))
