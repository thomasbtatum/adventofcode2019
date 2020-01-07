#Day12 B - the other Day12 was not scaling - this one moves away from moon class

f = open("AC2019/Day12.in")
s = f.readlines()

moons = []
MP = []
MV=[]
moonCount = 0
for line in s:
    moonstr = line.strip().replace("<","").replace(">","").replace(" ","")
    words = moonstr.split(',')
    moon = {}
    for w in words:
        k,v = w.split('=')
        if v.endswith(','):
            v = v[:-1]
        moon[k] = int(v)
    MP.append(moon)
    MV.append({'x':0,'y':0,'z':0})

SEEN = {k: {} for k in MP[0]}
CNT = {k: 0 for k in MP[0]}

t = 0
while True:
    for i in range(len(MP)):
        for j in range(len(MP)):
            for k in MP[i]:
                if MP[i][k] < MP[j][k]:
                    MV[i][k] += 1
                if MP[i][k] > MP[j][k]:
                    MV[i][k] -= 1
    for i in range(len(MP)):
        for k in MP[i]:
            MP[i][k] += MV[i][k]
    KEY = {k: [] for k in MP[0]}
    for i in range(len(MP)):
        for k in MP[i]:
            KEY[k].append(MP[i][k])
            KEY[k].append(MV[i][k])
    KEY = {k: tuple(v) for k,v in KEY.items()}
    for k in KEY:
        if KEY[k] in SEEN[k]:
            if CNT[k] <= 5:
                print(t,k,SEEN[k][KEY[k]])
            CNT[k] += 1
        SEEN[k][KEY[k]] = t

    t += 1

#take the top x y z result and do the following:
#Type "help", "copyright", "credits" or "license" for more information.
#>>> import math
#>>> 60424*186028/math.gcd(60424,186028)
#2810138968.0
#>>> 2810138968*231614/math.gcd(2810138968,231614)
#325433763467176.0

#Thanks to Jonathan Paulson for how to solve this:
#https://www.youtube.com/watch?v=9UcnA2x5s-U