n = int(input("Enter the Power of (a-b) "))
from sympy import init_printing , Symbol ,expand
init_printing()
a = Symbol('a')
b = Symbol('b')
e = (a-b)**n
print( expand(e) )