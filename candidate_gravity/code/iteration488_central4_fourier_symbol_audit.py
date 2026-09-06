from sympy import I, Rational, symbols, exp, simplify, sin, cos, series

th = symbols('theta', real=True)
nodes = [-2, -1, 1, 2]
c = [Rational(1,12), Rational(-2,3), Rational(2,3), Rational(-1,12)]
A = simplify(sum(ci*exp(I*ni*th) for ci,ni in zip(c,nodes)))
A_expected = I*sin(th)*(4-cos(th))/3
assert simplify(A - A_expected) == 0
R = simplify(A/(I*th))
R_series = series(R, th, 0, 12)
print('A(theta)=', A_expected)
print('R(theta)=', R)
print('R series=', R_series)
print('Zeros on real theta are inherited from sin(theta), since 4-cos(theta)>0.')
print('For mixed tensor product: D_h symbol = -A(theta_x) A(theta_y)/h^2 after removing the explicit i factors consistently.')
