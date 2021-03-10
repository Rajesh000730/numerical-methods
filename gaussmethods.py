import numpy as np
from sympy import symbols
#gauss siedel
""" x, y, z = symbols('x y z', real=True)
a1, a2, a3, d1 = 27, 6,-1, 85
b1, b2, b3,d2 = 6, 15, 2, 72
c1, c2, c3, d3 = 1, 1, 54, 110

f1 = (d1 - a2*y - a3*z)/a1
x = f1.subs({y:0, z:0})
print(x)
f2 = (d2 - b1*x - b3*z)/b2
y = f2.subs({x:x, z:0})
print(y)
f3 = (d3 - c1*x - c2*y)/c3
z = f3.subs({x:x, y:y})
print(z)
 """
#gauss jacobi
x, y, z = symbols('x y z', real=True)
a1, a2, a3, d1 = 27, 6,-1, 85
b1, b2, b3,d2 = 6, 15, 2, 72
c1, c2, c3, d3 = 1, 1, 54, 110

f1 = (d1 - a2*y - a3*z)/a1
x1 = f1.subs({y:4.8, z:2.0370})
print(x1)
f2 = (d2 - b1*x - b3*z)/b2
y1 = f2.subs({x:3.1481, z:2.0370})
print(y1)
f3 = (d3 - c1*x - c2*y)/c3
z1 = f3.subs({x:3.1481, y:4.8})
print(z1)

