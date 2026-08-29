"""RQIR Iteration 058: reset-aware Toy012 QND pointer vs Ramsey source metrology.

Iteration 057 found that on balanced Toy012 the best four extra force-covariance
rows are worth acquiring only if independent source-amplitude metrology is
slower than R_alpha ~= 2.20253e-5 s^-1 in the transparent y_ref=-4 benchmark.

This script places two independent/sacrificial QND source-metrology protocols
on that same physical Fisher-rate target:

1. Gaussian energy pointer: y|i ~ N(r E_i,1), with r=2 sqrt(Gamma_E T) where
   Gamma_E=eta*kappa_E; rate p F(r)/(t_reset+r^2/(4 Gamma_E)).
2. Ramsey ancilla: controlled phase phi=Omega_E T; rate
   p F_R(phi)/(t_reset+phi/Omega_E).

The coupling rates Gamma_E and Omega_E are protocol-specific and cannot be
numerically identified without a hardware Hamiltonian.  The comparison instead
extracts protocol-independent reset ceilings and zero-reset coupling targets.
"""
from __future__ import annotations

import math
import numpy as np

import toy011_local_nearest_neighbor_source as t11
import toy011_centered_profiled_resource_audit_iteration054 as i54
import qnd_energy_pointer_fisher_iteration049 as i49
import qnd_ramsey_ancilla_metrology_iteration051 as i51

Q0=np.array([0.182446543760,0.684368939221,0.165591352865,
             0.679324856717,0.097209344214])
Y1=-2.948786569910398
TIMES=np.array([0.,1.038867458294,2.985962997881,4.875819177097,
                4.150899563476,1.623915172581,5.275220686287])

P_ACCEPT=0.5
R_TARGET=2.2025278726983266e-5  # Iteration 057 branch0/best4 break-even


def hidden_diagonal():
    Q=t11.lanczos_q(Q0)
    pack=i54.make_pack(Q,Y1,TIMES)
    return np.real(np.diag(pack['d0']))


def pointer_rate(r,Gamma,t_reset,p,d):
    if Gamma<=0 or t_reset<0:
        raise ValueError
    f=i49.pointer_fisher(r,+1.0,d)
    return p*f/(t_reset+r*r/(4.0*Gamma))


def optimize_pointer_rate(Gamma,t_reset,p,d):
    # Coarse deterministic grid then golden refinement around best bin.
    grid=np.geomspace(0.02,8.0,700)
    vals=np.array([pointer_rate(r,Gamma,t_reset,p,d) for r in grid])
    j=int(np.argmax(vals))
    lo=grid[max(0,j-2)]; hi=grid[min(len(grid)-1,j+2)]
    return i49.golden_max(lambda r:pointer_rate(r,Gamma,t_reset,p,d),lo,hi)


def ramsey_rate(phi,Omega,t_reset,p,d):
    if Omega<=0 or t_reset<0:
        raise ValueError
    f=i51.ramsey_fisher(phi,+1.0,d,1.0)
    return p*f/(t_reset+phi/Omega)


def optimize_ramsey_rate(Omega,t_reset,p,d):
    grid=np.linspace(1e-5,2.0*math.pi-1e-5,9000)
    vals=np.array([ramsey_rate(ph,Omega,t_reset,p,d) for ph in grid])
    j=int(np.argmax(vals)); step=grid[1]-grid[0]
    lo=max(1e-8,grid[j]-3*step); hi=min(2.0*math.pi-1e-8,grid[j]+3*step)
    return i49.golden_max(lambda ph:ramsey_rate(ph,Omega,t_reset,p,d),lo,hi)


def solve_coupling(kind,t_reset,p,d):
    opt=(optimize_pointer_rate if kind=='pointer' else optimize_ramsey_rate)
    lo,hi=1e-8,1.0
    while opt(hi,t_reset,p,d)[1]<R_TARGET and hi<1e6:
        hi*=10.0
    if opt(hi,t_reset,p,d)[1]<R_TARGET:
        return np.inf,np.nan
    for _ in range(55):
        mid=np.sqrt(lo*hi)
        if opt(mid,t_reset,p,d)[1]>=R_TARGET: hi=mid
        else: lo=mid
    x,rate=opt(hi,t_reset,p,d)
    return hi,x


def main():
    d=hidden_diagonal()
    fproj=i49.projective_energy_fisher(+1.0,d)
    assert abs(fproj-0.006297270760383117)<3e-13

    # Zero-reset pointer throughput coefficient R/(p Gamma_E).
    rstar,metric=i49.golden_max(
        lambda r:i49.pointer_fisher(r,+1.0,d)/r**2,0.02,8.0)
    fptr=i49.pointer_fisher(rstar,+1.0,d)
    cptr=4.0*metric

    # Zero-reset Ramsey throughput coefficient R/(p Omega_E).
    grid=np.linspace(1e-5,2.0*math.pi-1e-5,12000)
    vals=np.array([i51.ramsey_fisher(ph,+1.0,d,1.0)/ph for ph in grid])
    j=int(np.argmax(vals)); step=grid[1]-grid[0]
    phir,cram=i49.golden_max(
        lambda ph:i51.ramsey_fisher(ph,+1.0,d,1.0)/ph,
        max(1e-8,grid[j]-3*step),min(2.0*math.pi-1e-8,grid[j]+3*step))

    Gamma0=R_TARGET/(P_ACCEPT*cptr)
    Omega0=R_TARGET/(P_ACCEPT*cram)

    print('pointer zero-reset r*, F, coeff, Gamma threshold',rstar,fptr,cptr,Gamma0)
    print('Ramsey zero-reset phi*, coeff, Omega threshold',phir,cram,Omega0)

    assert abs(rstar-1.44273038)<3e-6
    assert abs(fptr-0.0022125687575)<3e-12
    assert abs(cptr-0.00425193298956)<3e-12
    assert abs(Gamma0-0.01036037878)<3e-10
    assert abs(phir-1.57507926)<3e-6
    assert abs(cram-0.002134292844)<3e-12
    assert abs(Omega0-0.02063941580)<3e-10

    # Per-copy ceilings imply hard reset ceilings independent of coupling rate.
    # Pointer approaches projective energy Fisher as Gamma->infinity.
    phi_copy,f_ram_max=i51.optimize_phi(+1.0,d,1.0)
    reset_max_pointer=P_ACCEPT*fproj/R_TARGET
    reset_max_ramsey=P_ACCEPT*f_ram_max/R_TARGET
    print('Ramsey per-copy max phi/F',phi_copy,f_ram_max)
    print('hard reset ceilings pointer/Ramsey [s]',reset_max_pointer,reset_max_ramsey)

    assert abs(f_ram_max-0.00349867283092)<3e-12
    assert abs(reset_max_pointer-142.9555293815)<3e-7
    assert abs(reset_max_ramsey-79.4240307760)<3e-7

    # Representative finite-reset thresholds.  These are useful regression
    # points but not a cross-protocol hardware comparison because Gamma and
    # Omega have different physical normalization.
    gp1,rp1=solve_coupling('pointer',1.0,P_ACCEPT,d)
    gr1,rr1=solve_coupling('ramsey',1.0,P_ACCEPT,d)
    gp10,rp10=solve_coupling('pointer',10.0,P_ACCEPT,d)
    gr10,rr10=solve_coupling('ramsey',10.0,P_ACCEPT,d)
    print('reset1 pointer Gamma/r, Ramsey Omega/phi',gp1,rp1,gr1,rr1)
    print('reset10 pointer Gamma/r, Ramsey Omega/phi',gp10,rp10,gr10,rr10)

    assert abs(gp1-0.0105682)<3e-5
    assert abs(gr1-0.0209134)<3e-5
    assert abs(gp10-0.0125865)<4e-5
    assert abs(gr10-0.0237328)<4e-5


if __name__=='__main__':
    main()
