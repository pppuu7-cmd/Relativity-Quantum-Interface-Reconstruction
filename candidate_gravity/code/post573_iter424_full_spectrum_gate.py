#!/usr/bin/env python3
"""Collision-safe binding wrapper for the post573 full-spectrum consumer.

The initial consumer commit was authored concurrently with Iteration573 and
therefore guessed the Iter573 result filename/schema before the race-created
scoped audit landed. This wrapper changes only those two prerequisite bindings:
actual filename + exact scoped-audit classification/status. Numerical formulas,
artifacts, nodes, precision and Iteration424 thresholds are untouched.
"""
from pathlib import Path
P=Path(__file__).resolve().parent/'post573_iter424_full_spectrum_from_raw_artifacts.py'
s=P.read_text()
old="iteration573_iter424_frozen_clause_authority_mapping.json"
new="iteration573_iter424_authority_mapping_audit.json"
if s.count(old)!=1: raise SystemExit(('iter573_filename_binding_drift',s.count(old)))
s=s.replace(old,new,1)
old_check="if q573.get('scientific_gate_pass') is not True: raise RuntimeError(('iteration573_prerequisite_not_passed',q573.get('classification')))"
new_check="if q573.get('classification')!='PASS_ITER424_AUTHORITY_MAPPING_AUDIT__DIRECT_INHERITED_PASS__TENSOR11_OPERATIONAL_BLOCKED__NON_PROMOTING' or q573.get('status')!='PASS_SCOPED_AUDIT': raise RuntimeError(('iteration573_prerequisite_not_passed',q573.get('classification'),q573.get('status')))"
if s.count(old_check)!=1: raise SystemExit(('iter573_schema_binding_drift',s.count(old_check)))
s=s.replace(old_check,new_check,1)
ns={'__name__':'__main__','__file__':str(P)}
exec(compile(s,str(P),'exec'),ns,ns)
