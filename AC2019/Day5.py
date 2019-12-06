
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
    else:
        assert inputs[i] == "99"
        print("Exit: got opcode 99. " + str(inputs[0]))
        exit()
    i+=increment

#part 1 is complete - the answer was 4601506 for my input