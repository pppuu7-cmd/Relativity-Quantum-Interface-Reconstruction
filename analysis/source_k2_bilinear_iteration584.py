#!/usr/bin/env python3
"""Iteration584: polarize frozen Iter583 K2 into explicit K2(h1,h2).

No comparator or Source/Born subtraction is performed.  This is the unique
mixed bilinear contact implied by MSSC-001 and the Iter583 quadratic expansion.
"""
import hashlib, json
from pathlib import Path
import numpy as np

ETA=np.diag([1.,-1.,-1.,-1.]); EI=ETA.copy()

def mixed_coeff(h1,h2):
    H1=EI@h1; H2=EI@h2
    t1=float(np.trace(H1)); t2=float(np.trace(H2))
    bs=t1*t2/4.0-float(np.trace(H1@H2))/2.0
    bt=(EI@h1@EI@h2@EI + EI@h2@EI@h1@EI
        -0.5*t1*(EI@h2@EI)-0.5*t2*(EI@h1@EI)+bs*EI)
    return bs,bt

def exact(h1,h2,e1,e2):
    g=ETA+e1*h1+e2*h2
    d=float(np.linalg.det(g))
    if d>=0: raise RuntimeError('left Lorentzian determinant branch')
    s=float(np.sqrt(-d))
    return s,s*np.linalg.inv(g)

def central(h1,h2,e):
    vals={}
    for a,b in [(1,1),(1,-1),(-1,1),(-1,-1)]: vals[(a,b)]=exact(h1,h2,a*e,b*e)
    cs=(vals[(1,1)][0]-vals[(1,-1)][0]-vals[(-1,1)][0]+vals[(-1,-1)][0])/(4*e*e)
    ct=(vals[(1,1)][1]-vals[(1,-1)][1]-vals[(-1,1)][1]+vals[(-1,-1)][1])/(4*e*e)
    return cs,ct

def main():
    rng=np.random.default_rng(584218)
    eps=[1e-2,5e-3,2.5e-3]
    rec=[]; failures=[]
    for i in range(6):
        a=rng.normal(size=(4,4)); b=rng.normal(size=(4,4))
        h1=.1*(a+a.T)/2; h2=.1*(b+b.T)/2
        bs,bt=mixed_coeff(h1,h2)
        errs=[]
        for e in eps:
            cs,ct=central(h1,h2,e)
            es=abs(cs-bs); et=float(np.max(np.abs(ct-bt)))
            errs.append((es,et)); rec.append({'sample':i,'eps':e,'scalar_error':es,'tensor_error':et})
        # second-order central mixed derivative: halving e should reduce truncation ~4x.
        if not errs[-1][0] <= errs[0][0]/8.0: failures.append(f'sample {i}: scalar mixed-derivative convergence failed')
        if not errs[-1][1] <= errs[0][1]/8.0: failures.append(f'sample {i}: tensor mixed-derivative convergence failed')
    result={
      'iteration':584,'date':'2026-09-08','parent_authority':'Iter583 / MSSC-001',
      'mixed_k2':{
        'sqrt_minus_g':'trH1*trH2/4 - Tr(H1 H2)/2',
        'densitized_inverse':'E h1 E h2 E + E h2 E h1 E - (trH1/2)E h2 E - (trH2/2)E h1 E + [trH1 trH2/4-Tr(H1H2)/2]E',
        'symmetry':'K2(h1,h2)=K2(h2,h1)'
      },
      'regression':{'samples':6,'eps':eps,'records':rec},'failures':failures,
      'raw_result_integrity_valid':not failures,
      'classification':'PASS_MSSC001_MIXED_BILINEAR_K2_CONTACT__NON_RESIDUAL' if not failures else 'FAIL_MSSC001_MIXED_BILINEAR_K2_CONTACT',
      'source_born_subtraction':'NOT_PERFORMED','ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN','model_readiness_percent':24,
      'next_gate_if_pass':'construct matched conserved-source tree/Ward object from frozen K1 exchange plus this K2 contact; classify pole/cut origin before mapping to Iter582 and comparator subtraction'
    }
    out=Path('results/iteration584_source_k2_bilinear'); out.mkdir(parents=True,exist_ok=True)
    rp=out/'result.json'; rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    sha=hashlib.sha256(rp.read_bytes()).hexdigest()
    audit={'iteration':584,'result_sha256':sha,'failures':failures,'classification':'PASS_RAW_AUTHORITY_AUDIT_ITER584_K2_BILINEAR' if not failures else 'FAIL_RAW_AUTHORITY_AUDIT_ITER584_K2_BILINEAR'}
    (out/'authority_audit.json').write_text(json.dumps(audit,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    if failures: raise SystemExit(2)
if __name__=='__main__': main()
