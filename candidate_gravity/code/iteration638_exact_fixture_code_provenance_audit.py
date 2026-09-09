#!/usr/bin/env python3
"""Iteration 638: recover the exact Iter368/588 three-mode fixture from committed code.

This is a provenance gate only. It does not evaluate a cut, residual, Candidate value,
source/Born subtraction, or native projection. The exact anchor is accepted only if
committed same-parent code uniquely binds leg labels (s,a,b) to an explicit closed
four-vector triplet and Iter588 explicitly inherits that Iter368 fixture.
"""
from __future__ import annotations
import ast, hashlib, json, pathlib, re

ROOT=pathlib.Path(__file__).resolve().parents[2]
P368=ROOT/'candidate_gravity'/'code'/'iteration368_tru1sq_timelike_full_prepruning_routing.py'
P588=ROOT/'analysis'/'source_k1_k2_fixture_binding_iteration588.py'


def literal_assignment(tree,name):
    vals=[]
    for node in ast.walk(tree):
        if isinstance(node,(ast.Assign,ast.AnnAssign)):
            targets=node.targets if isinstance(node,ast.Assign) else [node.target]
            if any(isinstance(t,ast.Name) and t.id==name for t in targets):
                v=node.value
                try: vals.append(ast.literal_eval(v))
                except Exception:
                    # TIMELIKE_Q is a list of np.array([...]); recover the literal payloads only.
                    if isinstance(v,ast.List):
                        out=[]
                        ok=True
                        for e in v.elts:
                            if isinstance(e,ast.Call) and isinstance(e.func,ast.Attribute) and e.func.attr=='array' and e.args:
                                try: out.append(ast.literal_eval(e.args[0]))
                                except Exception: ok=False
                            else: ok=False
                        if ok: vals.append(out)
    return vals


def mink(v):
    return float(v[0])**2-sum(float(x)**2 for x in v[1:])

s368=P368.read_text()
s588=P588.read_text()
t368=ast.parse(s368)
legs_vals=literal_assignment(t368,'LEGS')
q_vals=literal_assignment(t368,'TIMELIKE_Q')
failures=[]
if len(legs_vals)!=1: failures.append(f'Iter368 LEGS literal count {len(legs_vals)}')
if len(q_vals)!=1: failures.append(f'Iter368 TIMELIKE_Q literal count {len(q_vals)}')
legs=tuple(legs_vals[0]) if legs_vals else ()
qs=q_vals[0] if q_vals else []
if legs!=('s','a','b'): failures.append(f'Iter368 leg labels drift: {legs}')
if len(qs)!=3 or any(len(v)!=4 for v in qs): failures.append('Iter368 four-vector triplet malformed')

# Same-parent bridge must be explicit in committed Iter588 code, not inferred from names.
required_588=[
    "p368=CROOT/'iteration368_tru1sq_timelike_full_prepruning_routing.py'",
    "M=ns['M']",
    "expected={'s':-1.0,'a':-0.14,'b':-0.34}",
    "parent_operator_fixture':'Iter368 -> Iter370/372 -> Iter582'",
]
missing=[x for x in required_588 if x not in s588]
if missing: failures.append('Iter588 same-parent bridge drift: '+repr(missing))

closure=[]
anchor=None
if not failures:
    closure=[sum(float(qs[j][i]) for j in range(3)) for i in range(4)]
    cmax=max(abs(x) for x in closure)
    if cmax>1e-15: failures.append(f'fixture closure {cmax}')
    inv=[mink(v) for v in qs]
    target=[1.0,0.14,0.34]
    ierr=max(abs(a-b) for a,b in zip(inv,target))
    if ierr>2e-15: failures.append(f'+--- invariant drift {inv}')
    if not failures:
        anchor={'s0':inv[0],'t0':inv[1],'u0':inv[2]}

classification=('PASS_ITER638_UNIQUE_SAME_PARENT_EXACT_FIXTURE_ANCHOR_RECOVERED_FROM_COMMITTED_CODE__NON_RESIDUAL'
                if not failures else
                'BLOCKED_ITER638_EXACT_FIXTURE_CODE_PROVENANCE_NOT_UNIQUE_OR_DRIFTED__NO_ANCHOR_INVENTED__NON_RESIDUAL')
result={
 'iteration':638,'date':'2026-09-09','scientific_gate_pass':not failures,'candidate_residual':False,
 'classification':classification,'failures':failures,
 'provenance':{
   'iter368_path':str(P368.relative_to(ROOT)),
   'iter368_sha256':hashlib.sha256(P368.read_bytes()).hexdigest(),
   'iter588_path':str(P588.relative_to(ROOT)),
   'iter588_sha256':hashlib.sha256(P588.read_bytes()).hexdigest(),
   'bridge_claim':'Iter588 explicitly re-executes the Iter368 setup prefix and inherits M rather than retyping fixture momenta'
 },
 'leg_order':list(legs),'q_s':qs[0] if len(qs)>0 else None,'q_a':qs[1] if len(qs)>1 else None,'q_b':qs[2] if len(qs)>2 else None,
 'closure_vector':closure,'metric_signature':'+---','recovered_anchor':anchor,
 'iter368_candidate_signature_crosscheck':{'q_squared_minus_plus_plus_plus':[-1.0,-0.14,-0.34]},
 'candidate_values_used':False,'zero_fill':False,'source_born_subtraction':'NOT_PERFORMED','native_projection':'NOT_PERFORMED',
 'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN','MODEL_READINESS':'24%','readiness_change':'0 percentage points',
 'next_gate':('Evaluate frozen Iter636 K1/K2 equal-mass bubble threshold and K1^3 triangle Landau determinant / positive-Feynman-parameter support at fixed t0=0.14,u0=0.34, with s variable and m_phi=0.7.' if not failures else 'Remain BLOCKED; audit additional same-parent history without inventing t0/u0.')
}
out=ROOT/'results'/'iteration638_exact_fixture_code_provenance_audit'; out.mkdir(parents=True,exist_ok=True)
rp=out/'result.json'; rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
audit={'iteration':638,'result_sha256':hashlib.sha256(rp.read_bytes()).hexdigest(),'failures':failures,
       'classification':('PASS_RAW_AUTHORITY_AUDIT_ITER638_EXACT_FIXTURE_CODE_PROVENANCE' if not failures else 'BLOCKED_RAW_AUTHORITY_AUDIT_ITER638_EXACT_FIXTURE_CODE_PROVENANCE')}
(out/'authority_audit.json').write_text(json.dumps(audit,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
if failures: raise SystemExit(2)
