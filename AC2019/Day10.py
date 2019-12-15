from fractions import Fraction

def allEdgePoints(points):
    allEdgePoints = []
    maxx = len(points[0])
    maxy = len(points)
    for i in range(0,maxx):
        allEdgePoints.append([i,0])
        allEdgePoints.append([i,maxy])
    for j in range(1,maxy-1):
        allEdgePoints.append([0,j])
        allEdgePoints.append([maxx,j])
    return allEdgePoints

def isPointMatch(points, p1, char):
    assert p1[0] != None and p1[1] != None
    if pointInMap(points,p1):
        return points[p1[1]][p1[0]] == char
    return False

def isPointOpen(points, p1):
    return isPointMatch(points,p1,'.')

def isAsteroid(points, p1):
    return isPointMatch(points,p1,'#')

# readme
def distance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def returnRiseRun(p1,p2):
    rise = p1[1]-p2[1]
    run = p1[0]-p2[0]
    if run == 0:
        if rise > 0:
            return 1,0 
        else:
            return -1,0
    x = Fraction(rise, run)
    return x.numerator, x.denominator 

def pointInMap(spots,p1):
    return p1[0] >= 0 and p1[1] <= 0 and p1[0] < len(spots[0]) and p1[1] > -1 * len(spots)

def getTotalForPoint(points, point):
    es = allEdgePoints(points)
    totals={}
    
    for idx,val in enumerate(es):
        if val == point:
            continue
        rise,run = returnRiseRun(point,val)
        slope = (rise,run)
        p2 = [point[0]+run,point[1]+rise]
        while(pointInMap(points,p2)):
            if(isAsteroid(points,p2)):
                d2 = distance(point,p2)
                if(slope in totals):
                    if d2 < totals[slope]:
                        totals[slope] = d2
                else:
                    totals[slope] = d2
            p2 = [p2[0]+run,p2[1]+rise]
    return len(totals.keys())

f = open("AC2019/Day10.in")
s = f.readlines()
lines = [l.strip() for l in s]

assert pointInMap(lines,[5,-5])
assert pointInMap(lines,[500,500]) == False

totals = {}
for y in range(0,len(lines)):
    for x in range(0,len(lines[y])):
        point = [x,y]
        if isAsteroid(lines,point):
            totals[tuple(point)] = getTotalForPoint(lines, point)

#print(sorted(totals,key=totals.get))
print(totals)
print("Done")