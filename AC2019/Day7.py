import itertools
class IntCodeAmplifier(object):
    def __init__(self,phaseSetting,inputSignal):
        self.inputs = []
        self.f = open("AC2019/Day7input.txt")
        self.s = self.f.readline()
        self.inputs = self.s.split(',')
        self.inputSignalSecond = inputSignal
        self.phaseFirst = phaseSetting 

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

    def _heap_perm_(self,n,A):
        if n == 1: yield A
        else:
            for i in range(n-1):
                for hp in self._heap_perm_(n-1, A): yield hp
                j = 0 if (n % 2) == 1 else i
                A[j],A[n-1] = A[n-1],A[j]
            for hp in self._heap_perm_(n-1, A): yield hp

    def getOutput(self):
        i = 0
        inputCount = 1
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

                if inputCount == 1:
                    incode = self.phaseFirst
                    inputCount += 1
                else:
                    incode = self.inputSignalSecond 

                self.setValue(self.inputs,ci,incode)
                #print("3 got:" + str(incode))
                
            elif opcode==4:
                increment = 2
                if p1mode == 1:
                    #print("4 ouput:" + self.inputs[i+1])
                    return self.inputs[i+1]
                else:
                    #print("4 ouput:" + self.inputs[int(self.inputs[i+1])])
                    return self.inputs[int(self.inputs[i+1])]
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
                assert self.inputs[i] == "99"
                print("Exit: got opcode 99. " + str(self.inputs[0]))
                exit()
            i+=increment


v = IntCodeAmplifier(1,2)
v.getOutput()

ampDict = []
data = list('123') 
for p in itertools.permutations([0,1,2,3,4]):
    output = 0
    for phase in p:
        inputSignal = output
        t = IntCodeAmplifier(phase,inputSignal)
        output = t.getOutput()
        #print("phase:" + str(phase) + " input:" + str(inputSignal) + " output:"+str(output))
    print(p)
    print(output)
    ampDict.append(int(output))
ampDict.sort()
print(ampDict)
