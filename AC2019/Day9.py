
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

f = open("AC2019/Day9.in")
s = f.readline()
inputs = s.split(',')
i = 0
relativeBase = 0
while i < len(inputs):
    #print(inputs[i])
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
        incode = input("Enter Code:")
        print("3 got:" + incode)
        setValue(inputs,ci,incode)
    elif opcode==4: #output
        increment = 2
        if p1mode == 1:
            print("4 ouput:" + str(getValue(inputs,i+1)))
        else:
            rb = relativeBase if p1mode == 2 else 0
            firstCall = getValue(inputs,i+1)
            print("4 ouput:" + str(getValue(inputs,firstCall + rb)))
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
        print("Exit: got opcode 99. " + str(inputs[0]))
        exit()
    i+=increment

#part 1 is complete - the answer was 4601506 for my input
#part 2 is complete - got it 5525561 and it was correct based on my input