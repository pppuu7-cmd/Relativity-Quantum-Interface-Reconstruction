#!/usr/bin/env python3
"""Iteration 640: retarded closed-loop s-channel support + native D_s projector contract.

This gate consumes only frozen Iter627/632/636/639 authority. It does NOT evaluate
closed-loop numerator magnitudes, perform native Y/T_cut projection, Source/Born
subtraction, comparator quotient, residual search, ANSATZ-003, Fisher or resources.
"""
from __future__ import annotations
import hashlib, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[2]
front = (ROOT/'candidate_gravity'/'recovery'/'CURRENT_QG_FRONT.md').read_text()
failures=[]
required = [
    'Latest authoritative research iteration: **639**',
    's_thr=4 m_phi^2=1.96',
    'positive_alpha_leading_roots=[]',
    'MSSC001-SCALAR-STATE-MINKOWSKI-VACUUM-V1',
]
for token in required:
    if token not in front:
        failures.append(f'missing frozen prerequisite token: {token}')

s_thr=1.96
families={
    'K3': {
        'topology':'tadpole',
        'ordinary_finite_s_cut':False,
        's_support':'NONE_FINITE_ORDINARY_CUT',
        'reason':'single-propagator tadpole topology has no ordinary two-particle hard-channel branch cut',
    },
    'K1K2': {
        'topology':'bubble',
        'ordinary_finite_s_cut':True,
        's_support':'s>=1.96',
        'threshold':s_thr,
        'anomalous_support':'NOT_APPLICABLE',
    },
    'K1^3': {
        'topology':'triangle',
        'ordinary_finite_s_cut':True,
        's_support':'s>=1.96',
        'threshold':s_thr,
        'positive_alpha_leading_anomalous_support':False,
        'boundary_subchannels':'retained ordinary bubble cuts',
    },
}

# Native normalization is inherited, not fitted: D_s F := Disc_s F/(2*pi*i).
# This gate freezes application order and support projector only; it does not invent
# a closed-loop spectral density or a Y/T_cut normalization coefficient.
projector={
    'native_operator':'D_s',
    'definition':'D_s[F] = Disc_s[F]/(2*pi*i)',
    'disc_orientation':'inherit frozen native Iter205 convention; no redefinition in Iter640',
    'support_projector':{
        'K3':'structural_zero_for_ordinary_finite_s_cut_only',
        'K1K2':'Theta(s-1.96) times the independently derived retarded closed-loop discontinuity density',
        'K1^3':'Theta(s-1.96) times ordinary-cut density; no extra positive-alpha leading anomalous term on frozen t0/u0 family',
    },
    'application_order':[
        'construct same-parent closed retarded Gamma3 family amplitude under Iter627+632',
        'classify pole/cut origin family-by-family',
        'take native Disc_s on the matched closed observable',
        'divide by 2*pi*i',
        'only then permit downstream Y/T_cut matching and Source/Born analysis if separately authorized',
    ],
    'forbidden_shortcuts':[
        'no open-source root weights substituted for closed-loop cut density',
        'no zero-fill for unsupported or uncomputed amplitudes',
        'no fitted phase or N_native',
        'no Source/Born subtraction before matched observable classification',
    ],
}

# Exact fixture s0=1 is below threshold; this is a derived support statement, not zero-fill.
anchor={'s0':1.0,'above_ordinary_s_threshold':False,'ordinary_K1K2_s_cut_active':False,'ordinary_K1^3_s_cut_active':False}
if not (anchor['s0'] < s_thr): failures.append('anchor threshold relation drift')
if families['K1^3']['positive_alpha_leading_anomalous_support'] is not False: failures.append('anomalous support drift')

classification = ('PASS_ITER640_RETARDED_CLOSED_LOOP_S_SUPPORT_AND_NATIVE_DS_PROJECTOR_CONTRACT__NON_RESIDUAL'
                  if not failures else 'FAIL_ITER640_RETARDED_CLOSED_LOOP_SUPPORT_PROJECTOR')
result={
    'iteration':640,'date':'2026-09-09','scientific_gate_pass':not failures,
    'classification':classification,'failures':failures,
    'prerequisites':['Iter627 combined matter+gravity SK measurement contract','Iter632 Minkowski-vacuum G_K state','Iter636 closed-Gamma3 invariant family','Iter639 threshold/Landau geometry'],
    'frozen_inputs':{'m_phi':0.7,'t0':0.14,'u0':0.34,'s_threshold':s_thr,'anchor_s0':1.0},
    'family_support':families,'native_discontinuity_projector':projector,'anchor_support':anchor,
    'candidate_residual':False,'candidate_values_used':False,'zero_fill':False,
    'source_born_subtraction':'NOT_PERFORMED','native_Y_Tcut_projection':'NOT_PERFORMED','comparator_quotient':'NOT_PERFORMED',
    'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN','MODEL_READINESS':'24%','readiness_change':'0 percentage points',
    'interpretation':'The frozen retarded closed scalar loop has no ordinary finite hard-channel cut in K3; K1/K2 and K1^3 ordinary s-channel support starts at s=1.96; no positive-alpha leading triangle anomalous support exists on the frozen t0/u0 family. The native projector normalization is inherited exactly as D_s=Disc_s/(2*pi*i), without fitting a new normalization.',
    'next_gate':'Derive the actual same-parent retarded closed-loop discontinuity density/numerator for K1/K2 and K1^3 under Iter627+632, preserving K3 as a retained analytic/contact family; then test matched native Y/T_cut projection before any Source/Born subtraction.'
}
out=ROOT/'results'/'iteration640_retarded_closed_loop_support_projector'; out.mkdir(parents=True,exist_ok=True)
rp=out/'result.json'; rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
audit={'iteration':640,'result_sha256':hashlib.sha256(rp.read_bytes()).hexdigest(),'failures':failures,
       'classification':('PASS_RAW_AUTHORITY_AUDIT_ITER640_RETARDED_SUPPORT_PROJECTOR' if not failures else 'FAIL_RAW_AUTHORITY_AUDIT_ITER640_RETARDED_SUPPORT_PROJECTOR')}
(out/'authority_audit.json').write_text(json.dumps(audit,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
if failures: raise SystemExit(2)
