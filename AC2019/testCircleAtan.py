
from fractions import Fraction
import math

def returnRiseRun(p1, p2):
    rise = p2[1]-p1[1]
    run = p2[0]-p1[0]
    if run == 0:
        if rise > 0:
            return 1, 0
        else:
            return -1, 0

    signRise = 1
    signRun = 1
    # preserve sign (+/-) of rise/run
    if rise < 0:
        signRise = -1
        rise *= -1
    if run < 0:
        signRun = -1
        run *= -1

    # this does greatest common devisor, but flips sign if neg on bottm
    x = Fraction(rise, run)

    return x.numerator*signRise, x.denominator*signRun

y = 0
for x in range (5,11):
    slope = returnRiseRun([5,-5],[x,y])
    print(x,y,slope,math.atan2(slope[0],slope[1]))
for y in range(-1,-11,-1):
    slope = returnRiseRun([5,-5],[x,y])
    print(x,y,slope,math.atan2(slope[0],slope[1]))
for x in range(10,-1,-1):
    slope = returnRiseRun([5,-5],[x,y])
    print(x,y,slope,math.atan2(slope[0],slope[1]))
for y in range(-10,1):
    slope = returnRiseRun([5,-5],[x,y])
    print(x,y,slope,math.atan2(slope[0],slope[1]))
for x in range(0,6):
    slope = returnRiseRun([5,-5],[x,y])
    print(x,y,slope,math.atan2(slope[0],slope[1]))
