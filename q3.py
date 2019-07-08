import math
import numpy as np

print("\n\n#3")         #derivation

#cen = (f(x+h) - f(x-h))/2h
#bac = (f(x) - f(x-h))/h
#for = (f(x+h)-f(x))/h
#abs((exact - derived)/exact)*100)

def f(x):
    return math.pow(x,4) - 3 * math.pow(x,3) + 6* math.pow(x,2) - 10*x - 9
def d1(f,x,h):
    return ( f(x + h) - f(x - h) ) / ( 2 * h )
def d2(f,x,h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / math.pow(h, 2)

print("Derived1 Exact: ", -10)
print("Derived2 Exact: ", 12)

print("h = 0.5\n")
print("E1: ", abs((-10 - d1(f,0,0.5))/-10)*100)
print("E2: ", abs((12 - d2(f,0,0.5))/12)*100)

print("Cen: ", (f(0+0.5) - f(0 - 0.5))/2*0.5)
print("Back: ", (f(0) - f(0-0.5))/0.5)
print("For: ", (f(0+0.5) - f(0))/0.5)
print("=====================================")
