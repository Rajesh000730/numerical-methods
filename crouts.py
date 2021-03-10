
import numpy as np
from sympy import symbols
# Creating an array using array
# function
a = np.array([[2, 3, 1], [5, 1, 1], [3, 2, 4]])
b = np.array([-1, 9, 11])
l11, l21, l22, l31, l32, l33 = symbols('l11 l21 l22 l31 l32 l33', real=True)
u12, u13, u23 = symbols('u12 u13 u23', real=True)
#step1
l11 = a[0][0]
l21 = a[1][0]
l31 = a[2][0]

print('l11={} l21={} l33={}'.format(l11, l21, l31))
#step2
u12 = a[0][1]/l11
u13 = a[0][2]/l11
y1 = b[0]/l11 
print(' u12={} u13={} y1={}'.format(u12, u13, y1))
#step3
l22 = (a[1][1] - l21*u12)
l32 = a[2][1] - l31*u12
print('l22={} l32={}'.format(l22, l32))
#step4
u23 = (a[1][2] - l21*u13)/l22
y2 = (b[1] - l21*y1)/l22 
print('u23={} y2={}'.format(u23, y2))
#step5
l33 = a[2][2] - l31*u13 - l32*u23
print('l33 ={}'.format(l33))
#step6

y3 = (b[2] - l31*y1 - l32*y2)/l33
print(y3) 
Y = np.array([y1, y2, y3])
U = np.array([[1, u12, u13], [0, 1, u23], [0, 0, 1]])

X = np.linalg.solve(U, Y)
print('x={} y={} z={}'.format(X[0], X[1], X[2]))