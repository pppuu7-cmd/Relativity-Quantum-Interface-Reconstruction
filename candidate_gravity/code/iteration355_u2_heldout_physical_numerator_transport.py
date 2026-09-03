#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 355.

Test physical numerator transport for every multi-member denominator-translation
candidate from Iteration 354.  Denominators are stripped only through the frozen
flat scalar propagator identities already used in the determinant/U2 chain.

A denominator class is merged only when its traced additive physical numerator
is transported by the same common loop-momentum translation at every held-out
loop momentum.  Failure of numerator equivalence is a valid scientific result:
the corresponding members remain separate families.  No cut integration occurs.
"""
from __future__ import annotations
import contextlib, io, itertools, json, runpy
from pathlib import Path
import numpy as np

ITERATION=355
ROOT=Path(__file__).resolve().parent

# Load the frozen Iteration-352 physical providers without treating its printed
# result as this iteration's authority.
with contextlib.redirect_stdout(io.StringIO()):
    P=runpy.run_path(str(ROOT/'iteration352_u2_timelike_full_physical_30route_products.py'), run_name='iteration355_parent352')

LEGS=P['LEGS']; ORDER=P['ORDER']; APPLY=P['APPLY']; raw=P['raw']
canonical=P['canonical']; qkey=P['qkey']; mdot=P['mdot']; maxabs=P['maxabs']
AR=P['AR']; AT=P['AT']; Ylower=P['Ylower']; Yupper=P['Yupper']
ghost_N1=P['ghost_N1']; Hst=P['Hst']; multi=P['multi']

# Held-out points are deterministic, off all obvious flat poles for the closed
# timelike triad, and distinct from the Iteration-352/353 reference P0.
HELDOUT=[
 np.array([0.71,-0.22,0.33,0.17]),
 np.array([0.29,0.41,-0.37,0.23]),
 np.array([-0.83,0.26,0.19,-0.31]),
 np.array([1.17,-0.46,0.28,0.35]),
]

def kt(x): return tuple(float(np.round(v,12)) for v in np.asarray(x,float))

def factor_num_terms(name,key,kin):
    """Return additive stripped numerator matrices plus propagator labels."""
    key=canonical(key); kin=np.asarray(kin,float); kout=kin+qkey(key)
    if name=='AR': return [('local_vertex',AR(key,kin),[])]
    if name=='AT': return [('local_vertex',AT(key,kin),[])]
    if name=='Y':  return [('local_vertex',Ylower(key),[])]
    if name in ('NL','NR'):
        if len(key)==0:
            return [('Q0_Y0',np.asarray(Yupper(()),complex),[('ghost',kin)])]
        if len(key)==1:
            return [
              ('Q0out_Y1',np.asarray(Yupper(key),complex),[('ghost',kout)]),
              ('minus_Q0out_N1_Q0in_Y0',-np.asarray(ghost_N1(key,kin),complex)@np.asarray(Yupper(()),complex),[('ghost',kout),('ghost',kin)]),
            ]
        raise ValueError((name,key))
    if name=='H':
        if len(key)==0:
            return [('minus_G0',-np.eye(10,dtype=complex),[('graviton',kin)])]
        if len(key)==1:
            K1=np.asarray(Hst(kin)['H'][multi(key)],complex)
            return [('plus_G0out_K1_G0in',K1,[('graviton',kout),('graviton',kin)])]
        raise ValueError((name,key))
    raise KeyError(name)

def prop_den(sp,k):
    s=mdot(k)
    return (-s if sp=='ghost' else s)

def factor_reconstruction(name,key,kin):
    terms=factor_num_terms(name,key,kin)
    val=None
    for _,num,props in terms:
        d=1+0j
        for sp,k in props: d*=prop_den(sp,k)
        if abs(d)<1e-10: raise RuntimeError(('heldout_flat_pole',name,key,kin.tolist(),d))
        piece=num/d
        val=piece if val is None else val+piece
    exact=np.asarray(P['component'](name,key,kin),complex)
    return maxabs(val-exact)/max(1.0,maxabs(val),maxabs(exact))

def enumerate_subterms(assign,p):
    cur=np.asarray(p,float).copy(); factor_terms=[]
    for name in APPLY:
        key=assign[name]
        factor_terms.append((name,key,factor_num_terms(name,key,cur)))
        cur=cur+qkey(key)
    out=[]
    for sid,choice in enumerate(itertools.product(*[x[2] for x in factor_terms])):
        M=np.eye(4,dtype=complex); props=[]; pieces=[]
        for (name,key,_),(piece,num,ps) in zip(factor_terms,choice):
            M=np.asarray(num,complex)@M
            props += [(sp,np.asarray(k,float)) for sp,k in ps]
            pieces.append((name,tuple(key),piece))
        out.append({'route':None,'subterm':sid,'numerator_matrix':M,'numerator_trace':complex(np.trace(M)),
                    'props':props,'pieces':pieces})
    return out

def relative_signature(props):
    ps=sorted(props,key=lambda x:(x[0],kt(x[1])))
    ref=ps[0][1]
    return tuple((sp,kt(k-ref)) for sp,k in ps),np.asarray(ref,float)

# Rebuild the Iteration-354 candidate classes at an arbitrary reference point.
pref=np.array([.43,-.27,.39,.21])
subs=[]
for rid,a in enumerate(raw):
    for s in enumerate_subterms(a,pref):
        sig,ref=relative_signature(s['props'])
        subs.append({'route':rid,'subterm':s['subterm'],'sig':sig,'ref':ref})
classes={}
for s in subs: classes.setdefault(s['sig'],[]).append(s)
class_items=sorted(classes.items(),key=lambda kv:(len(kv[0]),str(kv[0])))
assert len(subs)==42 and len(class_items)==30

# Validate the stripped decomposition itself on every factor encountered at all
# held-out points before trusting any transport comparison.
max_recon=0.0
for p in HELDOUT:
    for a in raw:
        cur=p.copy()
        for name in APPLY:
            max_recon=max(max_recon,factor_reconstruction(name,a[name],cur))
            cur=cur+qkey(a[name])

transport_threshold=2e-10
reconstruction_threshold=2e-10
records=[]; multi_count=0; equivalent_classes=0; distinct_classes=0; max_transport=0.0
for cid,(sig,members) in enumerate(class_items):
    base=members[0]
    member_records=[]; class_equiv=True
    if len(members)>1: multi_count+=1
    for m in members:
        shift=np.asarray(m['ref'])-np.asarray(base['ref'])
        errs=[]; samples=[]
        for p in HELDOUT:
            # D_member(p) = D_base(p+shift), therefore numerator transport is
            # tested under exactly the same loop-variable translation.
            nb=enumerate_subterms(raw[base['route']],p+shift)[base['subterm']]['numerator_trace']
            nm=enumerate_subterms(raw[m['route']],p)[m['subterm']]['numerator_trace']
            err=float(abs(nm-nb)/max(1.0,abs(nm),abs(nb)))
            errs.append(err); max_transport=max(max_transport,err)
            samples.append({'p':p.tolist(),'base_shifted_real':float(nb.real),'base_shifted_imag':float(nb.imag),
                            'member_real':float(nm.real),'member_imag':float(nm.imag),'scaled_error':err})
        member_ok=max(errs)<=transport_threshold
        if not member_ok: class_equiv=False
        member_records.append({'route':m['route'],'subterm':m['subterm'],'shift_from_base':shift.tolist(),
                               'transport_pass':member_ok,'max_scaled_error':max(errs),'samples':samples})
    if len(members)>1:
        if class_equiv: equivalent_classes+=1
        else: distinct_classes+=1
    records.append({'candidate_class':cid,'member_count':len(members),'propagator_count':len(sig),
                    'transport_classification':('NUMERATOR_TRANSLATION_EQUIVALENT' if class_equiv else 'DISTINCT_NUMERATORS_PRESERVE_SEPARATE'),
                    'members':member_records})

# Scientific PASS means the requested classification was resolved fail-closed;
# it does NOT require all denominator candidates to have equivalent numerators.
passed=bool(max_recon<=reconstruction_threshold and multi_count==9 and all(np.isfinite(r['members'][0]['max_scaled_error']) for r in records))
result={
 'iteration':ITERATION,'model_readiness_percent':24,'scientific_gate_pass':passed,'candidate_residual':False,
 'classification':('PASS_U2_HELDOUT_PHYSICAL_NUMERATOR_TRANSLATION_TRANSPORT_CLASSIFICATION__ONLY_PROVEN_EQUIVALENCES_MERGED' if passed else 'FAIL_U2_HELDOUT_NUMERATOR_TRANSPORT_GATE'),
 'census':{'additive_subterms':42,'denominator_candidate_classes':30,'multi_member_candidate_classes':multi_count,
           'numerator_equivalent_multi_classes':equivalent_classes,'numerator_distinct_multi_classes':distinct_classes,
           'max_factor_stripped_reconstruction_scaled_error':max_recon,'max_numerator_transport_scaled_error':max_transport,
           'heldout_points':len(HELDOUT)},
 'thresholds':{'factor_stripped_reconstruction_scaled_max':reconstruction_threshold,'numerator_transport_scaled_max':transport_threshold},
 'classes':records,
 'scope':'HELDOUT_TRACED_PHYSICAL_ADDITIVE_NUMERATOR_TRANSPORT_ONLY__NO_CUT_INTEGRATION',
 'guardrails':['NEGATIVE_NUMERATOR_EQUIVALENCE_IS_VALID_AND_PRESERVED','DENOMINATOR_EQUIVALENCE_ALONE_NEVER_MERGES','UNSUPPORTED_IS_BLOCKED_NOT_ZERO','NO_CUT_INTEGRATION_IN_THIS_GATE','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],
 'next_gate':'freeze the proven numerator+denominator family partition; classify each resulting family as local/scaleless/rational versus cut-capable from its propagator topology and kinematic origin before any Tr U2 discontinuity integration'
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
