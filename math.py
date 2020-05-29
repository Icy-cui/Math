from sympy import *

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
# 等同于 x, y, z, a, b, c = symbols('x, y, z, a, b, c')
# 建议用下面这种表达，因为一个一个导入符号实在是太麻烦了。
f = (2/3)*x**2 + (1/3)*x**2 + x + x + 1