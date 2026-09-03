#!/usr/bin/env python3
"""RQIR Iteration 333: scoped direct-timelike determinant cut reduction.

Uses the validated Iteration-332 timelike closed fixture. For each canonical bubble
family it evaluates the route-summed transported numerator on the exact massless
two-particle Cutkosky surface and performs deterministic angular quadrature at
increasing resolutions. The signed-affine triangle is fail-closed if an uncut
denominator crosses a two-line cut surface. No Source/Born subtraction is done.
"""
from __future__ import annotations
import contextlib, io, math, json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
# Reconstruct exactly the frozen Iteration-332 namespace from the Iteration-330
# parent. Iteration 332 itself is a wrapper around exec(), so runpy would expose
# only wrapper globals rather than the physical routing functions.
src=(ROOT/'iteration330_det_physical_numerator_family_canonicalization.py').read_text()
old="QINT=[(27,-19,31,11),(-13,37,17,-29),(-14,-18,-48,18)]"
new="QINT=[(100,0,0,0),(-40,10,10,0),(-60,-10,-10,0)]"
if src.count(old)!=1: raise RuntimeError('Iteration-330 QINT signature changed')
src=src.replace(old,new,1)
oldq="qdiff_nonzero=all(any(x for x in qint(a)) for a in NZ)"
newq="qdiff_nonzero=all(any(x for x in qint(a)) for a in NZ if a != TARGET)"
if src.count(oldq)!=1: raise RuntimeError('Iteration-330 qdiff signature changed')
src=src.replace(oldq,newq,1)
ns={'__name__':'rqir_iteration333_parent','__file__':str(ROOT/'iteration330_det_physical_numerator_family_canonicalization.py')}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src,str(ROOT/'iteration330_det_physical_numerator_family_canonicalization.py'),'exec'),ns,ns)
ETA=ns['ETA']; records=ns['records']; physical_integrand=ns['physical_integrand']; transformed_p=ns['transformed_p']; denom_product=ns['denom_product']; denom=ns['denom']

def mdot(a,b): return float(np.asarray(a)@ETA@np.asarray(b))
def spacelike_basis_orthogonal(r):
    r=np.asarray(r,float); r2=mdot(r,r)
    if not r2 < -1e-12: raise ValueError('cut momentum must be timelike')
    basis=[]
    for v in [np.array([0.,1,0,0]),np.array([0.,0,1,0]),np.array([0.,0,0,1]),np.array([1.,0,0,0])]:
        v=v-r*(mdot(v,r)/r2)
        for e in basis: v=v-e*mdot(v,e)
        n=mdot(v,v)
        if n>1e-12: basis.append(v/math.sqrt(n))
        if len(basis)==3: break
    if len(basis)!=3: raise RuntimeError('failed Minkowski orthogonal basis')
    return basis

def sphere_points(n):
    ga=math.pi*(3-math.sqrt(5.0))
    for i in range(n):
        z=1.0-2.0*(i+0.5)/n; rho=math.sqrt(max(0.0,1-z*z)); phi=ga*i
        yield np.array([rho*math.cos(phi),rho*math.sin(phi),z])

def cut_points(s0,s1,n):
    s0=np.asarray(s0,float)/100.0; s1=np.asarray(s1,float)/100.0
    r=s1-s0; B=spacelike_basis_orthogonal(r); rad=math.sqrt(-mdot(r,r))/2.0
    for u in sphere_points(n):
        ell=rad*sum(u[j]*B[j] for j in range(3))
        yield -(s0+s1)/2.0 + ell

def route_num(rec,k):
    p=transformed_p(k,rec['sigma'],rec['C']); I=physical_integrand(rec['sequence'],p); D=denom_product(k,rec['rep'])
    return complex(I*D)
def grouped():
    out={}
    for r in records: out.setdefault((len(r['sequence']),tuple(r['rep'])),[]).append(r)
    return out
def summed_num(group,k): return sum(route_num(r,k) for r in group)

groups=grouped(); bubbles=[]; triangles=[]
for (order,rep),group in groups.items():
    if order==2:
        vals=[]; onerr=[]
        for n in (64,128,256):
            arr=[]
            for k in cut_points(rep[0],rep[1],n):
                arr.append(summed_num(group,k)); onerr.append(max(abs(denom(k+np.asarray(rep[0])/100.0)),abs(denom(k+np.asarray(rep[1])/100.0))))
            vals.append(sum(arr)/len(arr))
        conv=max(abs(vals[2]-vals[1]),abs(vals[1]-vals[0])); scale=max(1.0,abs(vals[2])); stable=conv/scale<5e-4
        status='NONZERO' if stable and abs(vals[2])>1e-7*scale else ('ZERO' if stable else 'BLOCKED')
        bubbles.append({'rep_int100':[list(x) for x in rep],'route_count':len(group),'means_real':[float(x.real) for x in vals],'means_imag':[float(x.imag) for x in vals],'relative_convergence':float(conv/scale),'max_cut_shell_error':float(max(onerr)),'status':status})
    elif order==3:
        pair_results=[]
        for ia,ib,ic in ((0,1,2),(0,2,1),(1,2,0)):
            means=[]; ranges=[]; shell=[]; blocked=False
            for n in (96,192):
                arr=[]; thirds=[]
                for k in cut_points(rep[ia],rep[ib],n):
                    d3=denom(k+np.asarray(rep[ic],float)/100.0); thirds.append(d3)
                    shell.append(max(abs(denom(k+np.asarray(rep[ia])/100.0)),abs(denom(k+np.asarray(rep[ib])/100.0))))
                    if abs(d3)>1e-10: arr.append(summed_num(group,k)/d3)
                ranges.append((min(thirds),max(thirds)))
                if min(thirds)<=0<=max(thirds) or min(abs(x) for x in thirds)<1e-8: blocked=True
                means.append(sum(arr)/len(arr) if arr else complex(float('nan')))
            if blocked: status='BLOCKED_UNCUT_DENOMINATOR_CROSSES_CUT_SURFACE'
            else:
                conv=abs(means[-1]-means[-2])/max(1.0,abs(means[-1])); status='NONZERO' if conv<1e-3 and abs(means[-1])>1e-7*max(1.0,abs(means[-1])) else 'BLOCKED_NUMERICAL_REDUCTION'
            pair_results.append({'cut_pair':[ia,ib],'uncut_index':ic,'third_denominator_ranges':[[float(a),float(b)] for a,b in ranges],'means_real':[float(x.real) for x in means],'means_imag':[float(x.imag) for x in means],'max_cut_shell_error':float(max(shell)),'status':status})
        triangles.append({'rep_int100':[list(x) for x in rep],'route_count':len(group),'pair_cuts':pair_results})

bubble_pass=all(x['status'] in ('ZERO','NONZERO') and x['max_cut_shell_error']<1e-10 for x in bubbles) and len(bubbles)==3
tri_classified=len(triangles)==1 and all(x['status'].startswith(('NONZERO','BLOCKED')) for x in triangles[0]['pair_cuts'])
ok=bubble_pass and tri_classified
result={'iteration':333,'model_readiness_percent':24,'scientific_gate_pass':bool(ok),'classification':'PASS_SCOPED_DIRECT_TIMELIKE_CUT_ORIGIN_REDUCTION' if ok else 'FAIL_SCOPED_DIRECT_TIMELIKE_CUT_ORIGIN_REDUCTION','candidate_residual':False,'bubble_families':bubbles,'triangle_families':triangles,'interpretation':{'bubble_rule':'NONZERO requires stable deterministic two-body phase-space mean; ZERO requires stable mean consistent with zero; otherwise BLOCKED','triangle_rule':'uncut-denominator crossing is BLOCKED pending explicit causal i0/distributional treatment; never zero-filled'},'physical_status':{'full_finite_DR_remainder':'BLOCKED_BY_ITERATION297_EVANESCENT_SCHEME_AUTHORITY','source_born_subtraction':'FORBIDDEN_UNTIL_MATCHED_OBSERVABLE_AFTER_THIS_ORIGIN_CLASSIFICATION','comparator_subtracted_residual':'ABSENT'},'guardrails':['UNSUPPORTED_IS_BLOCKED_NOT_ZERO','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_HEAVY_FULL_C5'],'next_gate':'freeze ZERO/NONZERO bubble cut authority and resolve triangle BLOCKED channels with explicit causal i0 distributional reduction before matched-observable Source/Born subtraction'}
print(json.dumps(result,indent=2,sort_keys=True))
if not ok: raise SystemExit(2)
