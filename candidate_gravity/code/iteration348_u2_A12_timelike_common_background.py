#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 348.

Re-specialize the frozen Iteration-341 physical Vilkovisky A=(D R)*epsilon
A1/A2 construction onto the exact Iteration-332 timelike triad AND the same
three metric-background tensors used by the Iteration-319/330 determinant
common-background parent (seed 319, amplitude 0.12).

The Iteration-341 exact-geometry oracle and its thresholds remain unchanged.
This gate freezes only the matched-timelike A1/A2 provider; N/Y, Hinv and the
12-route physical family assembly remain separate downstream requirements.
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parent
p=ROOT/'iteration341_u2_v1_a12_same_parent_geometry.py'
src=p.read_text()
old=r"D=4; M=2; ZERO=\(0,0\)\neta=np\.diag\(\[-1\.,1\.,1\.,1\.\]\)\.astype\(complex\)\nrng=np\.random\.default_rng\(341\)\nhs=\[\]\nfor _ in range\(M\):\n    x=rng\.normal\(size=\(D,D\)\); hs\.append\(0\.08\*\(x\+x\.T\)/2\)\nqs=\[np\.array\(\[\.31,-\.17,\.23,\.11\]\), np\.array\(\[-\.19,\.29,\.13,-\.37\]\)\]\np=np\.array\(\[\.43,-\.27,\.39,\.21\]\)"
new="""D=4; M=3; ZERO=(0,0,0)
eta=np.diag([-1.,1.,1.,1.]).astype(complex)
rng=np.random.default_rng(319)
hs=[]
for _ in range(M):
    x=rng.normal(size=(D,D)); hs.append(0.12*(x+x.T)/2)
qs=[np.array([1.0,0.0,0.0,0.0]),np.array([-0.4,0.1,0.1,0.0]),np.array([-0.6,-0.1,-0.1,0.0])]
p=np.array([.43,-.27,.39,.21])"""
src,n=re.subn(old,new,src,count=1)
if n!=1:
    raise RuntimeError(f'Iteration-341 fixture signature drift: {n}')
# Retag sentinel/classification while preserving the exact oracle and thresholds.
if src.count("'iteration':341")!=1:
    raise RuntimeError('Iteration-341 result sentinel drift')
src=src.replace("'iteration':341","'iteration':348",1)
src=src.replace(
 'PASS_U2_PHYSICAL_SAME_PARENT_V1_A1_A2_BACKGROUND_KERNELS_EQ55_EXACT_GEOMETRY_ORACLE__NY_ROUTING_REMAINS_BLOCKED',
 'PASS_U2_A1_A2_MATCHED_TIMELIKE_COMMON_BACKGROUND_PROVIDER_EQ55_EXACT_GEOMETRY_ORACLE__NY_HINV_ROUTE_ASSEMBLY_NEXT')
src=src.replace(
 'FAIL_U2_V1_A1_A2_BACKGROUND_KERNEL_ORACLE',
 'FAIL_U2_A1_A2_MATCHED_TIMELIKE_COMMON_BACKGROUND_PROVIDER_ORACLE')
src=src.replace("'background_modes':2","'background_modes':3",1)
src=src.replace(
 "'next_gate':'close same-parent N/Y inverse-routing bridge in the a=-1/2 minimal ghost convention, using Eq57 and the already-frozen ghost operator; then assemble first-background-order Tr U2 with A.T/A and Hinv_VD=-K^-1'",
 "'next_gate':'re-specialize frozen N/Y and shifted Hinv providers on this exact common timelike background, then substitute A/N/Y/Hinv into all 12 Iteration-346 routes and canonicalize physical numerator/denominator families before cut integration'",1)
# Add explicit fixture provenance to the JSON without altering the oracle.
needle="'candidate_residual':False,'primary_authority':"
rep="'candidate_residual':False,'matched_timelike_common_background':{'q_squared':[-1.0,-0.14,-0.34],'metric_tensor_seed':319,'metric_tensor_scale':0.12,'source_parent':'Iteration319/330 common background'},'primary_authority':"
if src.count(needle)!=1:
    raise RuntimeError('Iteration-341 JSON signature drift')
src=src.replace(needle,rep,1)
exec(compile(src,str(p),'exec'),{'__name__':'__main__','__file__':str(p)})
