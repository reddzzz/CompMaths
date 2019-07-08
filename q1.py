import math
import numpy as np


print("#1")           #interpolation method

x = np.array([44*math.pi/180, 46*math.pi/180])
y = np.ones(len(x))
for i in range(len(x)):
    y[i] = math.tan(x[i])

def Newton(x,y,x1):
    b0 = y[0]
    b1 = (y[1] - y[0])/(x[1] - x[0])

    order1 = b0
    order2 = b0 + b1 * (x1 - x[0])
    return order2
print("Newton: ",Newton(x,y,45*math.pi/180))

def lang(x,y,x1):
    n = len(x)
    result = 0
    for i in range(0,n):
        subtot = 1
        for j in range(0,n):
            if(i != j):
                subtot *= ((x1 - x[j]) / (x[i] - x[j]))
        result += subtot * y[i]
    return result


print("Langarange ", lang(x,y,45*math.pi/180))

