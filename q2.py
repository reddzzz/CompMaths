import math
import numpy as np

print("#2")         #root equation algorithm

def f(x):
    return math.pow(x,3) + 7 *math.pow(x,2) - 36
def df(x):
    return 3*math.pow(x,2) + 14*x
def bi(f,a,b,e0):
    if(f(a) * f(b) < 0):
        while True:
            c = 0.5 * (a + b)
            if(f(a) * f(c) < 0):
                b = c
            else:
                a = c
            if np.abs(f(c) < e0):
                break
        return c

print(bi(f,-4,-2,0.05))

def new(f,f1,x,e0):
    while True:
        x = x - f(x)/f1(x)
        if np.abs(f(x)) < e0:
            break
    return x


print(new(f,df,-3,0.05))
