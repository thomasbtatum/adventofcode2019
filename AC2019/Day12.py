
import itertools

class Moon:
    x = None
    y = None
    z = None
    velx = 0
    vely = 0
    velz = 0

    def __init__(self,init):
        temp = init.split(',')
        self.x = int(temp[0].split('=')[1])
        self.y = int(temp[1].split('=')[1])
        self.z = int(temp[2].split('=')[1])
    
    def __str__(self):
        return "x="+str(self.x)+" y="+str(self.y)+" z="+str(self.z)+" velx="+str(self.velx)+" vely="+str(self.vely)+" velz="+str(self.velz)+" tot-e="+str(self.totalEnergy())

    def totalEnergy(self):
        return ((abs(self.x) + abs(self.y) + abs(self.z)) * (abs(self.velx) + abs(self.vely) + abs(self.velz)))

def applyVelocity(moon):
    moon.x += moon.velx
    moon.y += moon.vely
    moon.z += moon.velz

def calcGravity(moon1, moon2):
    if moon1.x < moon2.x:
        moon1.velx += 1
        moon2.velx += -1
    elif moon1.x > moon2.x:
        moon1.velx += -1
        moon2.velx += 1

    if moon1.y < moon2.y:
        moon1.vely += 1
        moon2.vely += -1
    elif moon1.y > moon2.y:
        moon1.vely += -1
        moon2.vely += 1

    if moon1.z < moon2.z:
        moon1.velz += 1
        moon2.velz += -1
    elif moon1.z > moon2.z:
        moon1.velz += -1
        moon2.velz += 1

def printMoons(moons):
    counter = 1
    for moon in moons:
        print(str(counter) + ". " + str(moon))
        counter += 1

f = open("AC2019/Day12.in")
s = f.readlines()

moons = []
for line in s:
    moonstr = line.strip().replace("<","").replace(">","").replace(" ","")
    moons.append(Moon(moonstr))


printMoons(moons)   


for step in range(1,1001):
    moonCombos = itertools.combinations('0123',2)
    for moonCombo in moonCombos:
        moon1 = moons[int(moonCombo[0])]
        moon2 = moons[int(moonCombo[1])]
        calcGravity(moon1,moon2)

    for moon in moons:
        applyVelocity(moon)

    if(step%100==0):
        printMoons(moons)
        print("after step "+str(step))   
