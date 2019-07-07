import math
import numpy as np


print("#1")           #interpolation method

# x = np.array([44 * math.pi/180, 46 * math.pi/180])
# y = np.ones(len(x))
# for i in range(len(x)):
#     y[i] = math.tan(x[i])
#
# #newton
# def newton(x,y, x1):
#     b0 = y[0]
#     b1 = (y[1] - y[0])/(x[1]-x[0])
#
#     order1 = b0
#     order2 = b0 + b1 * (x1 - x[0])
#     return order2
#
# print("Newton second order method: ", newton(x,y, 45*math.pi/180))
#
#lagrange
# def lagrange(x, y, x1):
#     b0 = y[0]*( (x1-x[1]) / (x[0]-x[1]))
#     b1 = y[0]*( (x1-x[0]) / (x[1]-x[0]))
#
#     result = b0 + b1
#     return result
#
# print("Lagrange second order method: ", lagrange(x, y, 45*math.pi/180))

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
print(Newton(x,y,45*math.pi/180))

def lang(x,y,x1):
    b0 = y[0] * ((x1 - x[1]) / (x[0] - x[1]))
    b1 = y[0] * ((x1 - x[0]) / (x[1] - x[0]))

    result = b0 + b1
    return result

print(lang(x,y,45*math.pi/180))

