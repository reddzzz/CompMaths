import math
import numpy as np

print("\n\n#2")         #root equation algorithm

def f_1(x):
    return math.pow(x, 3) + 7 * math.pow(x, 2) - 36
#bisection method
def bisection(f, a, b, e0):
    if (f(a) * f(b) >= 0):
        print("You have not assumed right a and b\n")
        return

    c = a
    while ((b - a) >= e0):
        c = (a + b) / 2
        if (f(c) == 0.0):
            break
        if (f(c) * f(a) < 0):
            b = c
        else:
            a = c

    return c

print("Bisection algorithm: ", bisection(f_1, -4, -2, 0.05))

def f1_1(x):
    return 3 * math.pow(x, 2) + 14 * x

#newton raphson method
def newton_raphson(f, f1, x, es):
    h = f(x) / f1(x)

    while abs(h) >= es:
        h = f(x) / f1(x)
        x = x - h

    return x

print("Newton Rhapson algorithm: ", newton_raphson(f_1, f1_1, -3, 0.05))