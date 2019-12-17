from fractions import Fraction


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
    #preserve sign (+/-) of rise/run
    if rise < 0:
        signRise = -1 
        rise *= -1
    if run < 0:
        signRun = -1 
        run *= -1

    x = Fraction(rise, run)#this does greatest common devisor, but flips sign if neg on bottm

    return x.numerator*signRise, x.denominator*signRun


def pointInMap(spots, p1):
    return 0 <= p1[0] < len(spots[0]) and 0 >= p1[1] >= (-1*len(spots)+1)


def getTotalForPoint(points, point):
    es = allEdgePoints(points)
    totals = {}

    for idx, val in enumerate(es):
        if val == point:
            continue
        rise, run = returnRiseRun(point, val)
        slope = tuple([rise, run])
        #valt = tuple(val)
        match = 0
        p2 = [point[0]+run, point[1]+rise]
        while(pointInMap(points, p2)):
            if(isAsteroid(points, p2)):
                match = 1
                d2 = distance(point, p2)
                if(slope in totals):
                    if d2 < totals[slope]:
                        totals[slope] = d2
                    else:
                        break  # min found dont test more
                else:
                    totals[slope] = d2
                    break  # first is min dont test more
            p2 = [p2[0]+run, p2[1]+rise]

        # if our p2 was too large and edge point is asteroid
        # use that. 100 is arbitrary int
        if match == 0 and isAsteroid(points, val):
            totals[slope] = 100
        print(idx, point, val, match)
    return len(totals.keys())


f = open("AC2019/Day10.in")
s = f.readlines()
lines = [l.strip() for l in s]

assert pointInMap(lines, [1, -1])
assert pointInMap(lines, [0, -1])
assert pointInMap(lines, [500, 500]) == False

totals = {}
for y in range(0, -1*len(lines), -1):
    for x in range(0, len(lines[y])):
        point = [x, y]
        if isAsteroid(lines, point):
            totals[tuple(point)] = getTotalForPoint(lines, point)

# print(sorted(totals,key=totals.get))
# print(totals)
#print(sorted( ((v,k) for k,v in totals.iteritems()), reverse=True))
#print({k: v for k, v in sorted(x.items(), key=lambda item: item[1])})
for w in sorted(totals, key=totals.get, reverse=True):
    print(w, totals[w])
print("Done")
