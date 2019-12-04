
def setValue(mylist, index, value):
    #zi = len(mylist) - mylist[::-1].index("99")
    mylist[index] = str(value)

f = open("Day2input.txt")
s = f.readline()
inputs = s.split(',')
inputs[1]="12"
inputs[2]="2"
i = 0
while i < len(inputs):
    #print(inputs[i])
    if inputs[i]=="1":
        fi = int(inputs[i+1])
        si = int(inputs[i+2])
        ci = int(inputs[i+3])
        setValue(inputs,ci,int(inputs[fi]) + int(inputs[si]))
    elif inputs[i]=="2":
        print("2")
        fi = int(inputs[i+1])
        si = int(inputs[i+2])
        ci = int(inputs[i+3])
        setValue(inputs,ci,int(inputs[fi]) * int(inputs[si]))
    else:
        print("99 " + str(inputs[0]))
        exit()
    i+=4

