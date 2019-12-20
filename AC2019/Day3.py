def findIntersection(l1, l2, ilist):
    l1hor = l1[0][1] == l1[1][1]
    l1ver = l1[0][0] == l1[1][0]
    l2hor = l2[0][1] == l2[1][1]
    l2ver = l2[0][0] == l2[1][0]
    if l1ver and l2ver:
        return
    if l1hor and l2hor:
        return

    if l1hor:
        if l1[0][0] > l1[1][0]:
            l1start = l1[1][0]
            l1stop = l1[0][0]
        else:
            l1start = l1[0][0]
            l1stop = l1[1][0]
        if l1start < l2[0][0] < l1stop:
            if l2[0][1] > l2[1][1]:
                l2start = l2[1][1]
                l2stop = l2[0][1]
            else:
                l2start = l2[0][1]
                l2stop = l2[1][1]
            if l2start < l1[0][1] < l2stop:
                firstsum = abs(l1[0][0] - l2[0][0]) + l1[2]
                secondsum = abs(l2[0][1] - l1[0][1]) + l2[2]
                ilist.append(firstsum + secondsum)
    else:
        if l2[0][0] > l2[1][0]:
            l2start = l2[1][0]
            l2stop = l2[0][0]
        else:
            l2start = l2[0][0]
            l2stop = l2[1][0]
        if l2start < l1[0][0] < l2stop:
            if l1[0][1] > l1[1][1]:
                l1start = l1[1][1]
                l1stop = l1[0][1]
            else:
                l1start = l1[0][1]
                l1stop = l1[1][1]
            if l1start < l2[0][1] < l1stop:
                firstsum = abs(l2[0][0] - l1[0][0]) + l2[2]
                secondsum = abs(l1[0][1] - l2[0][1]) + l1[2]
                ilist.append(firstsum + secondsum)


def createLines(llist):
    coords = []
    x = 0
    y = 0
    fullPath = 0
    # coords.append([x,y])
    for l in llist:
        x1, y1, diff = returnEnd(x, y, l)
        coords.append([[x, y], [x1, y1], fullPath])
        fullPath += diff
        x = x1
        y = y1
    return coords


def returnEnd(sx, sy, inp):
    diff = int(inp[1:])
    if inp[0] == 'R':
        return sx+diff, sy, diff
    if inp[0] == 'L':
        return sx-diff, sy, diff
    if inp[0] == 'U':
        return sx, sy+diff, diff
    if inp[0] == 'D':
        return sx, sy-diff, diff


f = open("Day3input.txt")
s = f.readlines()
firstLine = s[0].split(',')
secondLine = s[1].split(',')
first = createLines(firstLine)
second = createLines(secondLine)
intersections = []
for i in first:
    for j in second:
        findIntersection(i, j, intersections)

intersections.sort()
print("Done " + str(intersections[0]))
