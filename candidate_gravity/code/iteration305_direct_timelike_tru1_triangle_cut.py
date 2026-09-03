#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 305.

Integrate the FOUR actual direct-timelike visible triangle numerator families
from Iteration 295 and extract their normalized common timelike cuts.

Scientific prerequisites are checked fail-closed at runtime:
  * immutable Iteration-295 artifact/run identity and exact legacy member hash;
  * exactly one embedded iteration=295 object with the frozen reconstruction PASS;
  * schema-valid Iteration-304 artifact proving all 274 HV-like hidden triangle
    polynomial coefficients are cut-null in the normalized discontinuity.

The numerator is NOT analytically continued from a spacelike fit.  Its
coefficients are the direct timelike coefficients reconstructed at s=0.016.
Only the denominator i0 branch is continued.  The D-dimensional scalar loop
measure is combined with the barred-4D polynomial Laplacian; Iteration 304 is
what makes the hidden evanescent polynomial ambiguity irrelevant for D_s in
this scoped HV-like cut calculation.

This remains Tr U1 only: no -i/2 effective-action prefactor, source/Ward/contact
completion, K2 subtraction, comparator residual or Candidate Gravity claim.
"""
import argparse, hashlib, json, math
from pathlib import Path
import numpy as np
from scipy.special import gamma, beta
from numpy.polynomial.legendre import leggauss

ETA=np.diag([-1.,1.,1.,1.])
EPS=np.array([.04,.02,.01,.005,.0025,.00125],float)
NQ_LOW=72
NQ_HIGH=144
EXPECTED_295_MEMBER_SHA256='99af1466a132d8c116b2ef5f8466fb67dbdd53e857e93a088ff53d4d577b3a7a'
EXPECTED_295_OBJECT_SHA256='eba0cc09055bd64998455847e3b2f6c5c1cc334915aec29801c40efb3011d53b'
EXPECTED_304_SCIENTIFIC_SHA256='27efdba75eee39591ed5be0d2a766627c8fb1bf38af901a7aa823c441fd1086d'


def mdot(a,b):
    return float(np.asarray(a,float)@ETA@np.asarray(b,float))


def repeated_json_objects(raw):
    dec=json.JSONDecoder(); pos=0; out=[]
    while True:
        while pos<len(raw) and raw[pos].isspace(): pos+=1
        if pos>=len(raw): break
        start=pos
        obj,end=dec.raw_decode(raw,pos)
        out.append((obj,start,end))
        pos=end
    return out


def load_sources(p295,p304,p304audit):
    b=Path(p295).read_bytes()
    member_sha=hashlib.sha256(b).hexdigest()
    assert member_sha==EXPECTED_295_MEMBER_SHA256,(member_sha,EXPECTED_295_MEMBER_SHA256)
    raw=b.decode('utf-8')
    objs=repeated_json_objects(raw)
    assert [o.get('iteration') for o,_,_ in objs]==[270,273,295]
    hits=[x for x in objs if x[0].get('iteration')==295]
    assert len(hits)==1
    r295,st,en=hits[0]
    obj_sha=hashlib.sha256(raw[st:en].encode()).hexdigest()
    assert obj_sha==EXPECTED_295_OBJECT_SHA256,(obj_sha,EXPECTED_295_OBJECT_SHA256)
    assert r295['classification']=='PASS_DIRECT_TIMELIKE_S0016_WEIGHT_COMPLETED_TRU1_ALL_FAMILY_NUMERATOR_RECONSTRUCTION'
    assert r295['non_scaleless_family_count']==8
    assert r295['max_heldout_relative_error']<1e-7

    r304=json.loads(Path(p304).read_text())
    a304=json.loads(Path(p304audit).read_text())
    assert r304['iteration']==304
    assert r304['classification']=='PASS_HV_TRIANGLE_EVANESCENT_CUT_PROTECTION_ALL_274_HIDDEN_POLYNOMIAL_COEFFICIENTS_CUT_NULL_WITHIN_SCOPE'
    assert a304['scientific_authority_pass'] is True
    assert a304['sha256']==EXPECTED_304_SCIENTIFIC_SHA256
    assert a304['found_iterations']==[304] and a304['top_level_object_count']==1
    return r295,r304,{'member_sha256':member_sha,'selected_iteration295_raw_object_sha256':obj_sha}


def laplacian(poly):
    out={}
    for e,c in poly.items():
        for mu in range(4):
            if e[mu]>=2:
                ee=list(e); fac=e[mu]*(e[mu]-1); ee[mu]-=2; ee=tuple(ee)
                out[ee]=out.get(ee,0.0)+c*ETA[mu,mu]*fac
    return out


def coeff_poly(exps,coeffs):
    return {tuple(e):float(c) for e,c in zip(exps,coeffs) if abs(c)>1e-14}


def linpow(a,b,p):
    out=np.array([1.0])
    for _ in range(p):
        out=np.convolve(out,np.array([a,b],float))
    return out


def poly_t(poly,A,B):
    # Polynomial coefficients in t of P(-(A*t+B)).
    out=np.zeros(7,float)
    for e,c in poly.items():
        arr=np.array([1.0])
        for mu,p in enumerate(e):
            if p:
                arr=np.convolve(arr,linpow(-A[mu],-B[mu],p))
        out[:len(arr)] += c*arr
    return out


def unique_nonzero_shifts(den):
    out=[]
    for x in den:
        v=np.asarray(x,float)
        if np.max(np.abs(v))<1e-12:
            continue
        if not any(np.max(np.abs(v-w))<2e-10 for w in out):
            out.append(v)
    return out


def denominator_geometry(f):
    den=[np.asarray(x,float) for x in f['canonical_denominator_shifts']]
    zero_count=sum(np.max(np.abs(x))<1e-12 for x in den)
    expected=1 if f['family']=='ordinary_triangle' else 2
    assert zero_count==expected,(f['family'],zero_count)
    q=unique_nonzero_shifts(den)
    assert len(q)==2
    q1,q2=q
    inv={(0,1):mdot(q1,q1),(0,2):mdot(q2,q2),(1,2):mdot(q1-q2,q1-q2)}
    null=min(inv,key=lambda ij:abs(inv[ij]))
    assert abs(inv[null])<2e-10,inv
    i,j=null; k=next(iter({0,1,2}-{i,j}))
    smag={ij:-v for ij,v in inv.items()}
    ski=smag[(min(k,i),max(k,i))]
    skj=smag[(min(k,j),max(k,j))]
    assert ski>0 and skj>0,(ski,skj,inv)
    powers=[zero_count,1,1]
    return q1,q2,inv,(i,j,k),ski,skj,powers


def evaluate_family(f,eps,nquad,override_poly=None):
    q1,q2,inv,(i,j,k),ski,skj,powers=denominator_geometry(f)
    Atot=sum(powers); D2=2.0-eps
    if override_poly is None:
        base=coeff_poly(f['monomial_exponents'],f['coefficients'])
    else:
        base=dict(override_poly)
    polys=[base]
    while True:
        nx=laplacian(polys[-1])
        if not nx: break
        polys.append(nx)
    nodes,weights=leggauss(nquad); us=(nodes+1.0)/2.0; ws=weights/2.0
    cut=0.0; ret=0j; adv=0j
    for jj,poly in enumerate(polys):
        alpha=D2+jj-Atot
        pref=gamma(Atot-D2-jj)/(4**jj*math.factorial(jj)*np.prod([gamma(x) for x in powers]))
        integ=0.0
        for u,w in zip(us,ws):
            # x_v = A_v t + B_v for null-edge parametrization.
            Av=np.zeros(3); Bv=np.zeros(3)
            Av[k]=1.0
            Av[i]=-u; Bv[i]=u
            Av[j]=-(1.0-u); Bv[j]=1.0-u
            Aq=Av[1]*q1+Av[2]*q2
            Bq=Bv[1]*q1+Bv[2]*q2
            pc=poly_t(poly,Aq,Bq)
            tsum=0.0
            for n,coef in enumerate(pc):
                if abs(coef)>1e-18:
                    tsum += coef*beta(powers[k]+alpha+n,powers[i]+powers[j]+alpha)
            L=u*ski+(1.0-u)*skj
            integ += w*(u**(powers[i]-1))*((1.0-u)**(powers[j]-1))*(L**alpha)*tsum
        mag=pref*integ
        # Convention calibrated to Iteration 288: ret=M exp(+i*pi*alpha),
        # adv=M exp(-i*pi*alpha), D_s=(adv-ret)/(2*pi*i).
        rj=mag*np.exp(1j*np.pi*alpha)
        aj=mag*np.exp(-1j*np.pi*alpha)
        ret+=rj; adv+=aj
        cut+=(aj-rj)/(2j*np.pi)
    return float(cut.real),ret,adv,{
      'pair_invariants':[float(inv[(0,1)]),float(inv[(0,2)]),float(inv[(1,2)])],
      'null_edge_vertices':[i,j],
      'hard_invariant_magnitudes':[float(ski),float(skj)],
      'denominator_powers':powers,
      'laplacian_orders':len(polys),
    }


def laurent(vals,eps=EPS):
    y=np.asarray(vals,float); z=eps*y
    X=np.column_stack([np.ones_like(eps),eps,eps**2,eps**3,eps**4])
    c=np.linalg.lstsq(X,z,rcond=None)[0]
    fit=X@c
    return {
      'one_over_eps_residue':float(c[0]),
      'finite_cut_coefficient_if_residue_zero':float(c[1]),
      'eps_times_cut_fit_max_abs_residual':float(np.max(np.abs(fit-z))),
    }


def laurent_crosscheck(vals):
    a=laurent(vals,EPS)
    e=EPS[1:]; y=np.asarray(vals[1:],float); z=e*y
    X=np.column_stack([np.ones_like(e),e,e**2,e**3])
    c=np.linalg.lstsq(X,z,rcond=None)[0]
    return a,{
      'one_over_eps_residue_last5':float(c[0]),
      'finite_cut_coefficient_last5':float(c[1]),
      'pole_method_abs_difference':float(abs(a['one_over_eps_residue']-c[0])),
      'finite_method_abs_difference':float(abs(a['finite_cut_coefficient_if_residue_zero']-c[1])),
    }


def zero_limit(vals):
    y=np.asarray(vals,float)
    X=np.column_stack([np.ones_like(EPS),EPS,EPS**2,EPS**3,EPS**4])
    c=np.linalg.lstsq(X,y,rcond=None)[0]
    return float(c[0]),float(np.max(np.abs(X@c-y)))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--iteration295',default='iteration295_source/iteration295_result.json')
    ap.add_argument('--iteration304',default='iteration304_source/iteration304_result.json')
    ap.add_argument('--iteration304-audit',default='iteration304_source/iteration304_authority_audit.json')
    args=ap.parse_args()
    r295,r304,prov=load_sources(args.iteration295,args.iteration304,args.iteration304_audit)
    fam={k:v for k,v in r295['families'].items() if v['family'] in ('ordinary_triangle','raised_triangle')}
    assert len(fam)==4
    assert sum(v['basis_size'] for v in fam.values())==700

    rows={}; max_quad=0.0; max_conj=0.0; max_pole=0.0; max_polediff=0.0; max_findiff=0.0
    for name,f in sorted(fam.items()):
        high=[]; low=[]; conjs=[]; meta=None
        for e in EPS:
            vl,_,_,_=evaluate_family(f,float(e),NQ_LOW)
            vh,ret,adv,meta=evaluate_family(f,float(e),NQ_HIGH)
            low.append(vl); high.append(vh)
            conjs.append(abs(adv-np.conj(ret)))
        qerr=float(np.max(np.abs(np.asarray(high)-np.asarray(low))))
        cerr=float(max(conjs))
        lau,cross=laurent_crosscheck(high)
        max_quad=max(max_quad,qerr); max_conj=max(max_conj,cerr)
        max_pole=max(max_pole,abs(lau['one_over_eps_residue']))
        max_polediff=max(max_polediff,cross['pole_method_abs_difference'])
        max_findiff=max(max_findiff,cross['finite_method_abs_difference'])
        rows[name]={
          'family':f['family'],'basis_size':f['basis_size'],'degree_ceiling':f['degree_ceiling'],
          'primitive_branch_count':f['primitive_branch_count'],
          'heldout_relative_error':f['heldout_relative_max'],
          'geometry':meta,
          'raw_cut_scan_high_order':high,
          'raw_cut_scan_low_order':low,
          'max_low_vs_high_quadrature_abs_difference':qerr,
          'max_advanced_minus_conj_retarded_abs':cerr,
          'laurent':lau,'laurent_crosscheck':cross,
        }

    # Two independent scalar calibrations.
    ordinary=next(v for v in fam.values() if v['family']=='ordinary_triangle')
    one={(0,0,0,0):1.0}
    scalar_scan=[evaluate_family(ordinary,float(e),NQ_HIGH,one)[0] for e in EPS]
    scalar_lim,scalar_fit=zero_limit(scalar_scan)
    scalar_target=-np.log(.016/.216)/(.216-.016)
    scalar_res=abs(scalar_lim-scalar_target)

    lbar2={(2,0,0,0):-1.0,(0,2,0,0):1.0,(0,0,2,0):1.0,(0,0,0,2):1.0}
    cancel=[]
    for name,f in fam.items():
        if f['family']!='raised_triangle': continue
        sc=[evaluate_family(f,float(e),NQ_HIGH,lbar2)[0] for e in EPS]
        lim,err=zero_limit(sc)
        cancel.append({'family':name,'epsilon_to_zero_limit':lim,'target_ordinary_scalar_cut':scalar_target,
                       'abs_residual':abs(lim-scalar_target),'fit_max_abs_residual':err})
    max_cancel=max(x['abs_residual'] for x in cancel)

    total_finite=sum(v['laurent']['finite_cut_coefficient_if_residue_zero'] for v in rows.values())
    total_pole=sum(v['laurent']['one_over_eps_residue'] for v in rows.values())
    passed=(scalar_res<3e-6 and max_cancel<4e-6 and max_quad<2e-8 and max_conj<2e-10 and
            max_pole<2e-6 and max_polediff<2e-6 and max_findiff<8e-6)
    result={
      'iteration':305,'model_readiness_percent':24,
      'scope':'actual direct-timelike weight-completed TrU1 visible ordinary+raised triangle normalized cuts at s=0.016, protected by Iteration304 HV-like evanescent cut-null theorem',
      'epsilon_points':EPS.tolist(),
      'source_authority':{
        'iteration295_run_id':33688456731,'iteration295_artifact_id':9869280530,
        'iteration295_artifact_digest':'sha256:2c702d3aef66d052b63553590114900b2754b98e6871762ca3bda9ed8ec9ee77',
        'iteration295_member_sha256':prov['member_sha256'],
        'iteration295_selected_object_sha256':prov['selected_iteration295_raw_object_sha256'],
        'iteration304_run_id':33702437466,'iteration304_artifact_id':9873994705,
        'iteration304_artifact_digest':'sha256:3e5ea9c01327c47483664258162aaf1780615c8baf86433cb9db49426905ca18',
        'iteration304_scientific_json_sha256':EXPECTED_304_SCIENTIFIC_SHA256,
      },
      'ordinary_scalar_triangle_calibration':{
        'raw_cut_scan':scalar_scan,'epsilon_to_zero_limit':scalar_lim,
        'exact_target':scalar_target,'abs_residual':scalar_res,'fit_max_abs_residual':scalar_fit},
      'raised_lbar2_cancellation_calibrations':cancel,
      'triangle_families':rows,
      'sum_four_triangle_normalized_cut':float(total_finite),
      'sum_four_triangle_cut_one_over_eps_residue':float(total_pole),
      'max_abs_family_cut_one_over_eps_residue':float(max_pole),
      'max_family_pole_fit_method_abs_difference':float(max_polediff),
      'max_family_finite_fit_method_abs_difference':float(max_findiff),
      'max_low_vs_high_quadrature_abs_difference':float(max_quad),
      'max_advanced_minus_conj_retarded_abs':float(max_conj),
      'classification':('PASS_ACTUAL_DIRECT_TIMELIKE_WEIGHT_COMPLETED_TRU1_TRIANGLE_NORMALIZED_CUT_FINITE_IN_HV_SCOPE'
         if passed else 'BLOCKED_ACTUAL_DIRECT_TIMELIKE_TRU1_TRIANGLE_CUT_AUDIT'),
      'candidate_residual':False,
      'guardrails':[
        'ITERATION304_CUT_PROTECTION_DOES_NOT_PROMOTE_THE_FULL_FINITE_AMPLITUDE_SCHEME',
        'THIS_IS_TRU1_TRIANGLE_SUBSECTOR_ONLY_NO_MINUS_I_OVER_2_EFFECTIVE_ACTION_MULTIPLIER_APPLIED',
        'ITERATION289_WEIGHTED_B3_PROXY_POLE_IS_NOT_IMPORTED_AND_IS_SUPERSEDED_FOR_ACTUAL_TRU1_BY_THIS_WEIGHT_COMPLETED_DIRECT_TIMELIKE_ROUTE',
        'SOURCE_WARD_CONTACT_AND_K2_LINKED_COMPLETION_REMAIN_OPEN',
        'NO_COMPARATOR_SUBTRACTED_RESIDUAL_NO_ANSATZ003_NO_FISHER'
      ],
      'next_gate':'combine the schema-valid Iteration302 bubble cut with this Iteration305 triangle cut to freeze the complete e=1,c=2 weight-completed TrU1 normalized cut at the frozen row; then continue the remaining C5 e=2,c<=1 and determinant e=0,c<=3 pieces before source/Ward/K2 completion.'
    }
    assert passed,result
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
