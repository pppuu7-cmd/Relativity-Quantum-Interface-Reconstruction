#!/usr/bin/env python3
"""RQIR Iteration 094 — robust crossover value-of-information.

Deterministic algebra/regression certificate. Synthetic interval boxes are used
only to test the formulas; they are not apparatus forecasts.

Reproducibility correction (Iteration 096): active endpoint selection for
R_src interval contractions must use R_lo on the architecture entering as the
upper branch and R_hi on the architecture entering as the lower branch. The
published Iteration-094 formulas/numbers already correspond to this mapping;
this file now implements it explicitly.
"""
from dataclasses import dataclass, replace
from math import isclose

C_SRC = 225.0

@dataclass(frozen=True)
class ArchBox:
    A_lo: float; A_hi: float
    R_lo: float; R_hi: float
    d_lo: float; d_hi: float
    @property
    def m_lo(self): return 1.0/(1.0-self.d_lo)
    @property
    def m_hi(self): return 1.0/(1.0-self.d_hi)


def coeffs(i, k):
    D = i.m_hi*i.A_hi - k.m_lo*k.A_lo
    S = C_SRC*(i.m_hi/i.R_lo - k.m_lo/k.R_hi)
    return D, S


def boundary(i, k):
    D, S = coeffs(i, k)
    assert D*S < 0.0
    return -D/S


def dB_dDS(D, S):
    # B=-D/S
    return -1.0/S, D/(S*S)


def endpoint_gradient(i, k):
    """Gradient of B(i upper vs k lower) wrt active interval endpoints."""
    D, S = coeffs(i, k)
    gD, gS = dB_dDS(D, S)
    out = {}
    out['i.A_hi'] = gD*i.m_hi
    out['k.A_lo'] = gD*(-k.m_lo)
    out['i.R_lo'] = gS*(-C_SRC*i.m_hi/(i.R_lo**2))
    out['k.R_hi'] = gS*(+C_SRC*k.m_lo/(k.R_hi**2))
    out['i.d_hi'] = gD*(i.A_hi*i.m_hi**2) + gS*(C_SRC*i.m_hi**2/i.R_lo)
    out['k.d_lo'] = gD*(-k.A_lo*k.m_lo**2) + gS*(-C_SRC*k.m_lo**2/k.R_hi)
    return out


def contract(a, field, eta):
    lo, hi = field+'_lo', field+'_hi'
    c = 0.5*(getattr(a,lo)+getattr(a,hi)); h=0.5*(getattr(a,hi)-getattr(a,lo))
    return replace(a, **{lo:c-eta*h, hi:c+eta*h})


def width(a09, a14):
    return boundary(a14,a09)-boundary(a09,a14)


def contraction_derivative(a09,a14,arch,field):
    """dW/deta at eta=1, eta scales only one interval half-width.

    The active endpoint depends on both branch role and monotonicity:
      A,d: upper branch uses *_hi, lower branch uses *_lo;
      R:   upper branch uses R_lo, lower branch uses R_hi.
    """
    gU=endpoint_gradient(a14,a09)
    gL=endpoint_gradient(a09,a14)
    a = a09 if arch=='09' else a14
    h=0.5*(getattr(a,field+'_hi')-getattr(a,field+'_lo'))

    if arch=='14':
        # U: i=14 (upper envelope); L: k=14 (lower envelope).
        if field=='R':
            dU = gU['i.R_lo']*(-h)
            dL = gL['k.R_hi']*(+h)
        else:
            dU = gU[f'i.{field}_hi']*(+h)
            dL = gL[f'k.{field}_lo']*(-h)
    else:
        # U: k=09 (lower envelope); L: i=09 (upper envelope).
        if field=='R':
            dU = gU['k.R_hi']*(+h)
            dL = gL['i.R_lo']*(-h)
        else:
            dU = gU[f'k.{field}_lo']*(-h)
            dL = gL[f'i.{field}_hi']*(+h)
    return dU-dL


def finite_diff(a09,a14,arch,field,eps=1e-6):
    if arch=='09':
        wp=width(contract(a09,field,1+eps),a14)
        wm=width(contract(a09,field,1-eps),a14)
    else:
        wp=width(a09,contract(a14,field,1+eps))
        wm=width(a09,contract(a14,field,1-eps))
    return (wp-wm)/(2*eps)


def main():
    a09=ArchBox(1.0,1.1,1.0,1.1,0.02,0.04)
    a14=ArchBox(3.3,3.8,1.4,1.6,0.03,0.06)
    L=boundary(a09,a14); U=boundary(a14,a09); W=U-L
    assert isclose(L,0.025237237237237236,rel_tol=1e-12)
    assert isclose(U,0.08006274509803925,rel_tol=1e-12)
    assert W>0

    rows=[]
    for arch in ('09','14'):
        for field in ('A','R','d'):
            ana=contraction_derivative(a09,a14,arch,field)
            num=finite_diff(a09,a14,arch,field)
            assert isclose(ana,num,rel_tol=2e-8,abs_tol=2e-10)
            rows.append((arch,field,ana,ana/W))

    # Synthetic ranking only.
    ranked=sorted(rows,key=lambda x:x[2],reverse=True)
    assert [x[:2] for x in ranked] == [('14','R'),('09','R'),('14','A'),('14','d'),('09','d'),('09','A')]

    # Exact half-width and zero-width contractions show the local ranking is useful.
    for arch,field,_,_ in rows:
        if arch=='09':
            W50=width(contract(a09,field,0.5),a14); W0=width(contract(a09,field,0.0),a14)
        else:
            W50=width(a09,contract(a14,field,0.5)); W0=width(a09,contract(a14,field,0.0))
        assert W50 <= W+1e-15 and W0 <= W50+1e-15

    print('PASS Iteration 094 crossover value-of-information')
    print(f'lower={L:.15g} upper={U:.15g} width={W:.15g}')
    for arch,field,val,frac in ranked:
        print(f'{arch}.{field}: dW/deta={val:.12g}, leverage={frac:.6f}')

if __name__=='__main__':
    main()
