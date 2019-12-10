import itertools
class IntCodeAmplifier(object):
    def __init__(self,phaseSetting):
        self.inputs = []
        self.f = open("AC2019/Day7input.txt")
        self.s = self.f.readline()
        self.inputs = self.s.split(',')
        #self.inputSignalSecond = inputSignal
        self.phaseFirst = phaseSetting
        self.firstInput = True

    def getParameters(self,val):
        newVal = str(val.zfill(5))
        opcode = int(newVal[-2:])
        p1mode = int(newVal[-3])
        p2mode = int(newVal[-4])
        p3mode = int(newVal[-5])
        return opcode, p1mode, p2mode, p3mode

    def setValue(self,mylist, index, value):
        mylist[index] = str(value)

    # Python function to print permutations of a given list 
    def permutation(self, lst): 
    
        # If lst is empty then there are no permutations 
        if len(lst) == 0: 
            return [] 
    
        # If there is only one element in lst then, only 
        # one permuatation is possible 
        if len(lst) == 1: 
            return [lst] 
    
        # Find the permutations for lst if there are 
        # more than 1 characters 
    
        l = [] # empty list that will store current permutation 
    
        # Iterate the input(lst) and calculate the permutation 
        for i in range(len(lst)): 
            m = lst[i] 
    
        # Extract lst[i] or m from the list.  remLst is 
        # remaining list 
            remLst = lst[:i] + lst[i+1:] 
    
        # Generating all permutations where m is first 
        # element 
            for p in self.permutation(remLst): 
                l.append([m] + p) 
            return l 


    def getOutput(self, inputSignal, ip):
        i = ip
        while i < len(self.inputs):
            increment = 4
            opcode,p1mode,p2mode,p3mode = self.getParameters(self.inputs[i])
            if opcode==1 or opcode==2:
                
                fi = int(self.inputs[i+1])
                si = int(self.inputs[i+2])
                ci = int(self.inputs[i+3])

                if p1mode == 1:
                    left = fi
                else:
                    left = int(self.inputs[fi])
                if p2mode == 1:
                    right = si
                else:
                    right = int(self.inputs[si])
                if(opcode==1):
                    self.setValue(self.inputs,ci, left + right)
                else:
                    self.setValue(self.inputs,ci, left * right)
            elif opcode==3:
                increment = 2
                ci = int(self.inputs[i+1])

                if self.firstInput:
                    incode = self.phaseFirst
                    self.firstInput = False
                else:
                    incode = inputSignal 

                self.setValue(self.inputs,ci,incode)
                #print("3 got:" + str(incode))
                
            elif opcode==4:
                increment = 2
                if p1mode == 1:
                    #print("4 ouput:" + self.inputs[i+1])
                    return int(self.inputs[i+1]), i+2
                else:
                    #print("4 ouput:" + self.inputs[int(self.inputs[i+1])])
                    return int(self.inputs[int(self.inputs[i+1])]), i+2
            elif opcode==5:
                increment = 3
                p1 = int(self.inputs[i+1]) if p1mode == 1  else int(self.inputs[int(self.inputs[i+1])])
                p2 = int(self.inputs[i+2]) if p2mode == 1  else int(self.inputs[int(self.inputs[i+2])])
                if p1 != 0:
                    i = p2
                    increment = 0
            elif opcode==6:
                increment = 3
                p1 = int(self.inputs[i+1]) if p1mode == 1  else int(self.inputs[int(self.inputs[i+1])])
                p2 = int(self.inputs[i+2]) if p2mode == 1  else int(self.inputs[int(self.inputs[i+2])])
                if p1 == 0:
                    i = p2
                    increment = 0
            elif opcode==7:
                p1 = int(self.inputs[i+1]) if p1mode == 1  else int(self.inputs[int(self.inputs[i+1])])
                p2 = int(self.inputs[i+2]) if p2mode == 1  else int(self.inputs[int(self.inputs[i+2])])
                p3 = int(self.inputs[i+3])
                if p1 < p2:
                    self.setValue(self.inputs,p3,1)
                else:
                    self.setValue(self.inputs,p3,0)
            elif opcode==8:
                p1 = int(self.inputs[i+1]) if p1mode == 1  else int(self.inputs[int(self.inputs[i+1])])
                p2 = int(self.inputs[i+2]) if p2mode == 1  else int(self.inputs[int(self.inputs[i+2])])
                p3 = int(self.inputs[i+3])
                if p1 == p2:
                    self.setValue(self.inputs,p3,1)
                else:
                    self.setValue(self.inputs,p3,0)   
            else:
                #assert self.inputs[i] == "99"
                print("Exit: got opcode 99. " + str(opcode))
                return -1,-1
            print(i,opcode)
            i+=increment


ampTotal = {}
amps=[]

lastOutput = 0

for p in itertools.permutations([5,6,7,8,9]):
    for phase in p:
        amps.append(IntCodeAmplifier(phase))
    
    ampInputs = [0,0,0,0,0]
    ampInsPtrs = [0,0,0,0,0]

    output = 0
    while(output != -1):
        ampCount = 0
        for amp in amps:
            output,ip = amp.getOutput(ampInputs[ampCount],ampInsPtrs[ampCount])
            if output == -1:
                break
            ampInputs[(ampCount+1)%5] = output
            ampInsPtrs[ampCount] = ip
            ampCount += 1
            #print("phase:" + str(phase) + " input:" + str(inputSignal) + " output:"+str(output))
        lastOutput = output if output != -1 else lastOutput
    amps.clear()
    ampTotal[p]=int(lastOutput)

#ampTotal.sort()
print(sorted(ampTotal,key=ampTotal.get))
print(ampTotal)
