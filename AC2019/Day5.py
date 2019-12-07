
def getParameters(val):
    newVal = str(val.zfill(5))
    opcode = int(newVal[-2:])
    p1mode = int(newVal[-3])
    p2mode = int(newVal[-4])
    p3mode = int(newVal[-5])
    return opcode, p1mode, p2mode, p3mode

def setValue(mylist, index, value):
    #zi = len(mylist) - mylist[::-1].index("99")
    mylist[index] = str(value)

f = open("AC2019/Day5input.txt")
s = f.readline()
inputs = s.split(',')
#inputs[1]="12"
#inputs[2]="2"
i = 0
while i < len(inputs):
    #print(inputs[i])
    increment = 4
    opcode,p1mode,p2mode,p3mode = getParameters(inputs[i])
    if opcode==1 or opcode==2:
        
        fi = int(inputs[i+1])
        si = int(inputs[i+2])
        ci = int(inputs[i+3])

        if p1mode == 1:
            left = fi
        else:
            left = int(inputs[fi])
        if p2mode == 1:
            right = si
        else:
            right = int(inputs[si])
        if(opcode==1):
            #print("1")
            setValue(inputs,ci, left + right)
        else:
            #print("2")
            setValue(inputs,ci, left * right)
    elif opcode==3:
        increment = 2
        ci = int(inputs[i+1])
        incode = input("Enter Code:")
        print("3 got:" + incode)
        setValue(inputs,ci,incode)
    elif opcode==4:
        increment = 2
        if p1mode == 1:
            print("4 ouput:" + inputs[i+1])
        else:
            print("4 ouput:" + inputs[int(inputs[i+1])])
    elif opcode==5:
        increment = 3
        p1 = int(inputs[i+1]) if p1mode == 1  else int(inputs[int(inputs[i+1])])
        p2 = int(inputs[i+2]) if p2mode == 1  else int(inputs[int(inputs[i+2])])
        if p1 != 0:
            i = p2
            increment = 0
    elif opcode==6:
        increment = 3
        p1 = int(inputs[i+1]) if p1mode == 1  else int(inputs[int(inputs[i+1])])
        p2 = int(inputs[i+2]) if p2mode == 1  else int(inputs[int(inputs[i+2])])
        if p1 == 0:
            i = p2
            increment = 0
    elif opcode==7:
        p1 = int(inputs[i+1]) if p1mode == 1  else int(inputs[int(inputs[i+1])])
        p2 = int(inputs[i+2]) if p2mode == 1  else int(inputs[int(inputs[i+2])])
        p3 = int(inputs[i+3])
        if p1 < p2:
            setValue(inputs,p3,1)
        else:
            setValue(inputs,p3,0)
    elif opcode==8:
        p1 = int(inputs[i+1]) if p1mode == 1  else int(inputs[int(inputs[i+1])])
        p2 = int(inputs[i+2]) if p2mode == 1  else int(inputs[int(inputs[i+2])])
        p3 = int(inputs[i+3])
        if p1 == p2:
            setValue(inputs,p3,1)
        else:
            setValue(inputs,p3,0)   
    else:
        assert inputs[i] == "99"
        print("Exit: got opcode 99. " + str(inputs[0]))
        exit()
    i+=increment

#part 1 is complete - the answer was 4601506 for my input
#part 2 is complete - got it 5525561 and it was correct based on my input