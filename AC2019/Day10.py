from fractions import Fraction
import math


def allEdgePoints(points):
    allEdgePoints = []
    maxx = len(points[0])-1
    maxy = (len(points)-1) * -1
    for i in range(0, maxx+1):
        allEdgePoints.append([i, 0])
        allEdgePoints.append([i, maxy])
    for j in range(-1, maxy, -1):
        allEdgePoints.append([0, j])
        allEdgePoints.append([maxx, j])
    return allEdgePoints


def isPointMatch(points, p1, char):
    assert p1[0] != None and p1[1] != None
    if pointInMap(points, p1):
        return points[-1*p1[1]][p1[0]] == char
    return False


def isPointOpen(points, p1):
    return isPointMatch(points, p1, '.')


def isAsteroid(points, p1):
    return isPointMatch(points, p1, '#')

# readme


def distance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


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


def pointInMap(spots, p1):
    return 0 <= p1[0] < len(spots[0]) and 0 >= p1[1] >= (-1*len(spots)+1)


def isWhole(numToCheck):
    return numToCheck % 1 == 0


def getNearestYOnLineWithAsteroid(points, slope, point, x, end):
    sl = 0 if slope[1] == 0 else Fraction(slope[0], slope[1])
    noResult = None

    if sl == 0 and end[1] > point[1]:
        for y in range(point[1]+1, 1, 1):
            checkPoint = [x, y]
            if pointInMap(points, checkPoint):
                if isAsteroid(points, checkPoint):
                    return y
            else:
                return noResult

    if sl == 0 and point[1] > end[1]:
        for y in range(point[1]-1, -1*len(points), -1):
            checkPoint = [x, y]
            if pointInMap(points, checkPoint):
                if isAsteroid(points, checkPoint):
                    return y
            else:
                return noResult

    gety = (sl * (x - point[0])) + point[1]
    if isWhole(gety):
        p2 = [x, int(gety)]
        if p2 == point:
            return noResult
        if(isAsteroid(points, p2)):
            return p2[1]
    return noResult


def getTotalForPoint(points, point):
    es = allEdgePoints(points)
    totals = {}

    for idx, val in enumerate(es):
        if val == point:
            continue
        rise, run = returnRiseRun(point, val)
        slope = tuple([rise, run])
        match = 0

        start = point[0]
        stop = val[0]+1
        step = -1 if val[0] < point[0] else 1

        for x in range(start, stop, step):

            gety = getNearestYOnLineWithAsteroid(points, slope, point, x, val)
            if gety == None:
                continue
            else:
                p2 = [x, gety]
                d2 = distance(point, p2)
                match = 1
                if slope in totals:
                    if d2 < totals[slope][1]:
                        totals[slope] = [point, d2]

                else:
                    totals[slope] = d2
                break
        if match == 0 and isAsteroid(points, val):
            totals[slope] = [point, 100]
            match = 1
        print(idx, point, val, slope, match)
        print(totals)
    return len(totals.keys())

def getTotalsForAsteroid(asteroids, asteroid):
    totals = {}

    for a in asteroids:
        if a == asteroid:
            continue
        
        rise, run = returnRiseRun(asteroid, a)
        slope = tuple([rise, run])
        d2 = distance(asteroid,a)
        if slope in totals:
            if d2 < totals[slope][1]:
                totals[slope] = [a, d2]
        else:
            totals[slope] = [a, d2]
    return len(totals.keys())

def getSlopesForAsteroid(asteroids, asteroid):
    totals = {}

    for a in asteroids:
        if a == asteroid:
            continue
        
        rise, run = returnRiseRun(asteroid, a)
        slope = tuple([rise, run])
        d2 = distance(asteroid,a)
        if slope in totals:
            if d2 < totals[slope][1]:
                totals[slope] = [a, d2]
        else:
            totals[slope] = [a, d2]
    return totals           

f = open("AC2019/Day10.in")
s = f.readlines()
lines = [l.strip() for l in s]

assert pointInMap(lines, [1, -1])
assert pointInMap(lines, [0, -1])
assert pointInMap(lines, [500, 500]) == False

totals = {}
asteroids = []
for y in range(0, -1*len(lines), -1):
    for x in range(0, len(lines[y])):
        point = [x, y]
        if isAsteroid(lines, point):
            asteroids.append(point)


for a in asteroids:
        totals[tuple(a)] = getTotalsForAsteroid(asteroids,a)

slopeDic = getSlopesForAsteroid(asteroids,[22,-28])

to_sort = []
for slope in slopeDic.keys():
    dr = slope[0]
    dc = slope[1]
    key = math.atan2(dr,dc)
    if key > math.pi/2.0:
        key -= 2*math.pi
    to_sort.append((key,slopeDic[slope][0]))

to_sort = list(reversed(sorted(to_sort)))
winner = to_sort[199][1]
print(winner)


#for a in asteroids:
#        totals[tuple(a)] = getTotalsForAsteroid(asteroids,a)
            #totals[tuple(point)] = getTotalForPoint(lines, point)


for w in sorted(totals, key=totals.get, reverse=True):
   print(w, totals[w])
print("Done")


