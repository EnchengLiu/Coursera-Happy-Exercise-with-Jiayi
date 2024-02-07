import sympy as sp

k11, k12, k13, k14, k21, k22, k23, k24 = sp.symbols('k11 k12 k13 k14 k21 k22 k23 k24')
M = sp.Matrix([[0,0,1,0],[0,0,0,1],[k11, k12, k13, k14], [k21, k22, k23, k24]])
eigenvals = M.eigenvals()
char_poly = M.charpoly()
print(f"Characteristic polynomial: {char_poly.as_expr()}")