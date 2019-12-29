
def printGrid(currentSpot, orientation, whiteSpots):
    for y in range(0,-10,-1):
        for x in range(0,51):
            if [x,y] == currentSpot:
                if orientation == 'N':
                    print('^',end='')
                elif orientation == 'E':
                    print('>',end='')
                elif orientation == 'W':
                    print('<',end='')
                elif orientation == 'S':
                    print('v',end='')

            elif [x,y] in whiteSpots:
                print('#',end='')
            else:
                print(' ',end='')
        print(' ')

def moveShip(moveCode, currentSpot, orientation):
    #moveCode=0 is left, else right
    assert moveCode == 0 or moveCode == 1
    x = currentSpot[0]
    y = currentSpot[1]
    newSpot = None
    newOrientation = 'T'
    if moveCode == 1:#right
        if orientation == 'N':
            newSpot = [x+1,y]
            newOrientation ='E'
        elif orientation == 'E':
            newSpot = [x,y-1]
            newOrientation ='S'
        elif orientation == 'S':
            newSpot = [x-1,y]
            newOrientation ='W'
        else:
            newSpot = [x,y+1]
            newOrientation = 'N'
    else:#left
        if orientation == 'N':
            newSpot = [x-1,y]
            newOrientation = 'W'
        elif orientation == 'E':
            newSpot = [x,y+1]
            newOrientation ='N'
        elif orientation == 'S':
            newSpot = [x+1,y]
            newOrientation ='E'
        else:
            newSpot = [x,y-1]
            newOrientation ='S'

    assert newOrientation != 'T'
    assert newSpot != None
    return newSpot,newOrientation

def paintSpot(currentSpot, whiteSpots, colorToPaint, paintedOnce):
    assert colorToPaint == 0 or colorToPaint == 1
    #if currentSpot not in paintedOnce and colorToPaint == 1:
    #    paintedOnce.append(currentSpot)
    paintedOnce[tuple(currentSpot)] = 1

    if colorToPaint == 0 and currentSpot in whiteSpots: #color is black 
        paintedSpots.remove(currentSpot)
    elif colorToPaint == 1 and currentSpot not in whiteSpots:  #color is white
        paintedSpots.append(currentSpot)

def getParameters(val):
    newVal = str(val.zfill(5))
    opcode = int(newVal[-2:])
    p1mode = int(newVal[-3])
    p2mode = int(newVal[-4])
    p3mode = int(newVal[-5])
    return opcode, p1mode, p2mode, p3mode

def setValue(mylist, index, value):
    if index >= len(mylist):
        mylist.extend('0' * (index+1 - len(mylist)))
    mylist[index] = str(value)

def getValue(mylist,index):
    if index >= len(mylist):
        mylist.extend('0' * (index+1 - len(mylist)))
        return 0
    else:
        return int(mylist[index])

ns,no = moveShip(0,[1,1],'N')
assert ns == [0,1] and no == 'W'
ns,no = moveShip(0,[1,1],'E')
assert ns == [1,2] and no == 'N'
ns,no = moveShip(0,[1,1],'S')
assert ns == [2,1] and no == 'E'
ns,no = moveShip(0,[1,1],'W')
assert ns == [1,0] and no == 'S'

ns,no = moveShip(1,[1,1],'N')
assert ns == [2,1] and no == 'E'
ns,no = moveShip(1,[1,1],'E')
assert ns == [1,0] and no == 'S'
ns,no = moveShip(1,[1,1],'S')
assert ns == [0,1] and no == 'W'
ns,no = moveShip(1,[1,1],'W')
assert ns == [1,2] and no == 'N'

f = open("AC2019/Day11.in")
s = f.readline()
inputs = s.split(',')
i = 0
relativeBase = 0

currentSpot = [2,-3]
orientation = 'N'
paintedSpots = []
paintedOnce = {}

firstOutputFlag = True
output1 = None
output2 = None

while i < len(inputs):

    increment = 4
    opcode,p1mode,p2mode,p3mode = getParameters(inputs[i])
    if opcode==1 or opcode==2:
        
        fi = getValue(inputs,i+1)
        si = getValue(inputs,i+2)
        ci = getValue(inputs,i+3)
        if p3mode == 2:
            ci += relativeBase
        if p1mode == 1:
            left = fi
        else:
            rb = relativeBase if p1mode==2 else 0
            left = getValue(inputs,fi+rb)
                    
        if p2mode == 1:
            right = si
        else:
            rb = relativeBase if p2mode == 2 else 0 
            right = getValue(inputs,si+rb)
        if(opcode==1):
            setValue(inputs,ci, left + right)
        else:
            setValue(inputs,ci, left * right)
    elif opcode==3:  #input

        increment = 2
        ci = getValue(inputs,i+1)
        if p1mode == 2:
            ci += relativeBase
        #incode = input("Enter Code:")
        incode = 0 if currentSpot in paintedSpots else 1
        print("3 got:" + str(incode))
        setValue(inputs,ci,incode)

    elif opcode==4: #output
        increment = 2
        ouput = None
        if p1mode == 1:
            output = getValue(inputs,i+1)
            print("4 ouput:" + str(output))
        else:
            rb = relativeBase if p1mode == 2 else 0
            firstCall = getValue(inputs,i+1)
            output = getValue(inputs,firstCall + rb)
            print("4 ouput:" + str(output))


        if firstOutputFlag:
            output1 = output
        else:
            output2 = output
            paintSpot(currentSpot, paintedSpots, output1, paintedOnce) #1 paint white - 0 black
            currentSpot,orientation = moveShip(output2, currentSpot, orientation)# 1 turn right, 0 left
            printGrid(currentSpot, orientation,paintedSpots)
        #colorToPaint,directionToTurn = getColorAndDirection(paintedSpots,currentSpot)
        #paintSpot(colorToPaint,paintedSpots)
        #currentSpot = getNextSpot(directionToTurn, )

        firstOutputFlag = False if firstOutputFlag == True else True

    elif opcode==5:  #move i param != 0
        increment = 3
        rb1 = relativeBase if p1mode==2 else 0
        rb2 = relativeBase if p2mode==2 else 0
        firstp  = getValue(inputs,i+1)
        secondp = getValue(inputs,i+2)
        p1 = firstp   if p1mode == 1  else getValue(inputs,firstp+rb1)
        p2 = secondp  if p2mode == 1  else getValue(inputs,secondp+rb2)
        if p1 != 0:
            i = p2
            increment = 0
    elif opcode==6: # move i if p1 == 0
        increment = 3
        rb1 = relativeBase if p1mode==2 else 0
        rb2 = relativeBase if p2mode==2 else 0
        firstp  = getValue(inputs,i+1)
        secondp = getValue(inputs,i+2)
        p1 = firstp   if p1mode == 1  else getValue(inputs,firstp+rb1)
        p2 = secondp  if p2mode == 1  else getValue(inputs,secondp+rb2)
        if p1 == 0:
            i = p2
            increment = 0
    elif opcode==7:
        rb1 = relativeBase if p1mode==2 else 0
        rb2 = relativeBase if p2mode==2 else 0
        rb3 = relativeBase if p3mode==2 else 0
        firstp  = getValue(inputs,i+1)
        secondp = getValue(inputs,i+2)
        p3  = getValue(inputs,i+3)
        p1 = firstp   if p1mode == 1  else getValue(inputs,firstp+rb1)
        p2 = secondp  if p2mode == 1  else getValue(inputs,secondp+rb2)
        
        if p1 < p2:
            setValue(inputs,p3+rb3,1)
        else:
            setValue(inputs,p3+rb3,0)
    elif opcode==8:
        rb1 = relativeBase if p1mode==2 else 0
        rb2 = relativeBase if p2mode==2 else 0
        rb3 = relativeBase if p3mode==2 else 0
        firstp  = getValue(inputs,i+1)
        secondp = getValue(inputs,i+2)
        p3   = getValue(inputs, i+3)
        p1 = firstp   if p1mode == 1  else getValue(inputs,firstp+rb1)
        p2 = secondp  if p2mode == 1  else getValue(inputs,secondp+rb2)
        if p1 == p2:
            setValue(inputs,p3+rb3,1)
        else:
            setValue(inputs,p3+rb3,0)
    elif opcode==9:
        increment = 2
        rb1 = relativeBase if p1mode==2 else 0
        firstp  = getValue(inputs,i+1)
        p1 = firstp   if p1mode == 1  else getValue(inputs,firstp+rb1)
        relativeBase += p1
    else:
        assert inputs[i] == "99"
        print("Exit: got opcode 99. len painted once " + str(len(paintedOnce.keys())))
        exit()
    i+=increment

#part 1 is complete - the answer was 4601506 for my input
#part 2 is complete - got it 5525561 and it was correct based on my input