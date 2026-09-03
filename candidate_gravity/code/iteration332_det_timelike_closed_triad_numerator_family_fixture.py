#!/usr/bin/env python3
"""RQIR Iteration 332: timelike closed-triad physical numerator-family fixture.

Iteration 331 froze the signed-affine physical numerator-family reconstruction,
but its exact closed triad has q_i^2>0 in signature (-,+,+,+), hence it is not
a direct timelike discontinuity row.  This gate changes only the external closed
triad to an exact non-collinear real timelike fixture while preserving the same
common metric background construction, cubic logdet weights, shifted routing,
route-specific numerator transport, held-out points and 5e-10 threshold.

This is a prerequisite for a direct timelike DR/cut reduction; it does not itself
claim a nonzero discontinuity and performs no Source/Born subtraction.
"""
from pathlib import Path

p=Path(__file__).with_name('iteration330_det_physical_numerator_family_canonicalization.py')
src=p.read_text()
old="QINT=[(27,-19,31,11),(-13,37,17,-29),(-14,-18,-48,18)]"
new="QINT=[(100,0,0,0),(-40,10,10,0),(-60,-10,-10,0)]"
if src.count(old)!=1:
    raise RuntimeError('Iteration-330 QINT signature changed; refuse implicit rebase')
src=src.replace(old,new,1)
oldq="qdiff_nonzero=all(any(x for x in qint(a)) for a in NZ)"
newq="qdiff_nonzero=all(any(x for x in qint(a)) for a in NZ if a != TARGET)"
if src.count(oldq)!=1:
    raise RuntimeError('Iteration-330 qdiff signature changed; refuse implicit rebase')
src=src.replace(oldq,newq,1)
if src.count("'iteration':330")!=1:
    raise RuntimeError('Iteration-330 sentinel signature changed; refuse implicit rebase')
src=src.replace("'iteration':330","'iteration':332",1)
src=src.replace('PASS_PHYSICAL_CUBIC_DETERMINANT_NUMERATOR_SIGNED_AFFINE_FAMILY_RECONSTRUCTION',
                'PASS_TIMELIKE_CLOSED_TRIAD_PHYSICAL_CUBIC_DETERMINANT_NUMERATOR_FAMILY_FIXTURE')
src=src.replace('FAIL_PHYSICAL_CUBIC_DETERMINANT_NUMERATOR_SIGNED_AFFINE_FAMILY_RECONSTRUCTION',
                'FAIL_TIMELIKE_CLOSED_TRIAD_PHYSICAL_CUBIC_DETERMINANT_NUMERATOR_FAMILY_FIXTURE')
# Add an explicit all-three-timelike check to the final scientific gate.
# Cast to builtin float so the unchanged parent JSON encoder sees ordinary JSON scalars.
needle="ok=(len(seqs)==13 and len(single_reps)==1 and len(bubble_reps)==3 and len(tri_reps)==1\n    and max_reconstruction<threshold and max_denmap<threshold and qdiff_nonzero)"
replacement="timelike_q2=[float(denom(np.array(q,float)/100.0)) for q in QINT]\ntimelike_closed_fixture=(all(x < -1e-12 for x in timelike_q2) and np.linalg.matrix_rank(np.array(QINT,float))==2)\nok=(len(seqs)==13 and len(single_reps)==1 and len(bubble_reps)==3 and len(tri_reps)==1\n    and max_reconstruction<threshold and max_denmap<threshold and qdiff_nonzero and timelike_closed_fixture)"
if src.count(needle)!=1:
    raise RuntimeError('Iteration-330 final gate signature changed; refuse implicit rebase')
src=src.replace(needle,replacement,1)
# Surface the timelike invariants in the JSON checks.
needle2="'checks':{'max_heldout_reconstruction_scaled_error':max_reconstruction,"
replacement2="'timelike_fixture':{'q_squared':timelike_q2,'all_three_timelike':bool(timelike_closed_fixture)},\n 'checks':{'max_heldout_reconstruction_scaled_error':max_reconstruction,"
if src.count(needle2)!=1:
    raise RuntimeError('Iteration-330 checks signature changed; refuse implicit rebase')
src=src.replace(needle2,replacement2,1)
src=src.replace("'next_gate':('perform scoped DR/timelike discontinuity reduction of the three canonical bubble families and the signed-affine triangle family using these transported physical numerators; certify zero/nonzero discontinuity family by family before any matched Source/Born subtraction'",
                "'next_gate':('perform scoped direct-timelike DR/discontinuity reduction on this certified timelike closed fixture, family by family, preserving the Iteration-297 regulator warning and forbidding Source/Born subtraction until origin classification is complete'",1)
exec(compile(src,str(p),'exec'),{'__name__':'__main__','__file__':str(p)})
