import math
# for x = kthroot(N)
x = 1
N = 1
k = 1
a = ((k-1)*x + (N)/pow(x, k-1))/k
print(a)

import math
# for x = sqrt(N)
x = 1
N = 1
a = (pow(x, 2) + N)/(2*x)
print(a)

# for x = 1/N
x = 1
N = 1
a = 2*x - N*(pow(x, 2))
print(a)

#newton raphson method
from sympy import Symbol
import numpy as np
a = 0
x = Symbol('x')
y = x #enter the function here
y_ = y.diff(x)
a = a - ((y.doit().subs({x:a})/y_.doit().subs({x:a})))

print(a)
#newton raphson method for repeated roots
from sympy import Symbol
import numpy as np
a = 0
n = 0
x = Symbol('x')
y = x #enter the function here
y_ = y.diff(x)
a = a - (n*(y.doit().subs({x:a})/y_.doit().subs({x:a})))#n is the no of repeated roots
print(a)