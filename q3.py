import math
import numpy as np

print("\n\n#3")         #derivation

#cen = (f(x+h) - f(x-h))/2h
#bac = (f(x) - f(x-h))/h
#for = (f(x+h)-f(x))/h

def f(x):
    return math.pow(x,4) - 3 * math.pow(x,3) + 6* math.pow(x,2) - 10*x - 9
def d1(f,x,h):
    return ( f(x + h) - f(x - h) ) / ( 2 * h )
def d2(f,x,h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / math.pow(h, 2)

print("Derived1 Exact: ", -10)
print("Derived2 Exact: ", 12)

print("h = 0.5\n")
print("derived1: ", d1(f,0,0.5))
print("deroved2: ", d2(f,0,0.5))

print("Error1: ", abs((-10 - d1(f,0,0.5))/10)*100)
print("Error2: ", abs((12 - d2(f,0,0.5))/12)*100)

print("Backward: ", (f(0+0.5)-f(0)/0.5))
print("Forward: ",(f(0+0.5)-f(0)/0.5))
print("Central: ",f(0+0.5) - f(0 - 0.5)/2*0.5)

# print("derived1 Exact: ", -10)
# print("derived2 Exact: ", 12)
#
# print("h = 0.5\n")
# print("first d: ", d1(f,0,0.5))
# print("second d: ", d2(f,0,0.5))
#
# # abs((exact - derived)/exact)*100)
# print("Error1: ", abs((-10 - d1(f,0,0.5))/-10)*100)
# print("Error2: ", abs((12 - d2(f,0,0.5))/12)*100)
#
# print("[b]\n")
# #f(0) - f(0 - h)
# print("BackWard: ", f(0) - f(0 - 0.5))
# #f(0 + h) - f(0)
# print("Forward: ", f(0 + 0.5) - f(0))
# #f(0 + h * h) - f(0 - h * h)
# print("Central: ", f(0 + 0.5 * 0.5) - f(0 - 0.5 * 0.5))


# def func(x):
#     return math.pow(x, 4) - 3 * math.pow(x, 3) + 6 * math.pow(x, 2) - 10 * x - 9
#
# def derived1(f, x, h):
#     return ( f(x + h) - f(x - h) ) / ( 2 * h )
#
# def derived2(f, x, h):
#     return ( f(x + h) - 2 * f(x) + f(x - h) ) / math.pow(h, 2)
#
# print("\n[a]")
#
# print("first derivation, exact: ", -10)
# print("second derivation, exact: ", 12)
#
# print("\nh = 0.5")
# print("first derivation: ", derived1(func, 0, .5))
# print("relative error: ", abs( (-10 - derived1(func, 0, .5)) / -10) * 100 )
# print("second derivation: ", derived2(func, 0, .5))
# print("relative error: ", abs( (12 - derived2(func, 0, .5)) / 12) * 100 )
#
# print("\nh = 0.25")
# print("first derivation: ", derived1(func, 0, .25))
# print("relative error: ", abs( (-10 - derived1(func, 0, .25)) / -10) * 100 )
# print("second derivation: ", derived2(func, 0, .25))
# print("relative error: ", abs( (12 - derived2(func, 0, .25)) / 12) * 100 )
#
# print("\nh = 0.125")
# print("first derivation: ", derived1(func, 0, .125))
# print("relative error: ", abs( (-10 - derived1(func, 0, .125)) / -10) * 100 )
# print("second derivation: ", derived2(func, 0, .125))
# print("relative error: ", abs( (12 - derived2(func, 0, .125)) / 12) * 100 )
#
# print("\n[b]")
#
# print("exact: ", -10)
#
# print("\nh = 0.5")
# print("backward difference: ", func(0) - func(0 - .5))
# print("forward difference: ", func(0 + .5) - func(0))
# print("central difference: ", func(0 + .5 * .5) - func(0 - .5 * .5))
#
# print("\nh = 0.25")
# print("backward difference: ", func(0) - func(0 - .25))
# print("forward difference: ", func(0 + .25) - func(0))
# print("central difference: ", func(0 + .5 * .25) - func(0 - .5 * .25))
#
# print("\nh = 0.125")
# print("backward difference: ", func(0) - func(0 - .125))
# print("forward difference: ", func(0 + .125) - func(0))
# print("central difference: ", func(0 + .5 * .125) - func(0 - .5 * .125))
