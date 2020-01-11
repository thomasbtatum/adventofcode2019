f = open("AC2019/Day14.0")
s = f.readlines()

def findInputChem(outChem, rdict):
    for k,v in rdict.items():
        if k[1] == outChem:
            return v

def getOreInputCnt(outChem, rdict):
    inList = findInputChem(outChem, rdict)
    if len(inList) == 1 and inList[0][1] == 'ORE':
        return inList[0][0]
    else:
        return -1

def buildreduxList(chem, reduxList, rdict, oreList):
    inChemList = findInputChem(chem,rdict)
    for inChem in inChemList:
        cnt = getOreInputCnt(inChem[1],rdict)
        hasOreIn = False if cnt == -1 else True
        ic = tuple([inChem[0],tuple([inChem[1],hasOreIn])])
        if hasOreIn:
            addOrrList(ic, oreList)
        else:
            reduxList.append(ic)

def addOrrList(chem, oreList):
    #if chem exist, add, else append
    for o in oreList:
        if o[1][0] == chem[1][0]:
            o[0] += int(chem[0])
            return
    newOre = [int(chem[0]),chem[1][0]]
    oreList.append(newOre)

reactions = {}
totalOre = 0
reduxList = []
oreList = []

for line in s:
    rewords = line.split('=>')
    leftSplit = rewords[0].strip().split(',')
    keys = rewords[1].strip().split(' ')
    key = tuple([keys[0],keys[1]])
    tupList = []
    
    for val in leftSplit:
        lword = val.strip().split(' ')
        tupList.append(tuple([lword[0],lword[1]]))
    assert key not in reactions
    reactions[key] = tupList
print(reactions)

#phase 0 - build reduxList with 1 FUEL inputs
#list is tuple(cnt,tuple(chem,hasOreIn))
buildreduxList('FUEL',reduxList, reactions, oreList)
print(reduxList, oreList)
# phase 1 - while list has chems that dont have ore input
# replace with input chems * count, adding any new ones that 
# have ore input to oreList
while len(reduxList) > 0:
    f = reduxList.pop(0)
    inChemList = findInputChem(f[1][0],reactions)
    for inChem in inChemList:
        cnt = getOreInputCnt(inChem[1],reactions)
        hasOreIn = False if cnt == -1 else True
        ic = tuple([inChem[0],tuple([inChem[1],hasOreIn])])
        if hasOreIn:
            addOrrList(ic,oreList)
        else:
            reduxList.append(ic)
    print(reduxList, oreList)

while len(oreList) > 0:
    o = oreList.pop(0)
    cnt = getOreInputCnt(o[1][0],reactions)
    totalOre += int(cnt) * int(o[0])
    print(oreList, totalOre)


# phase 2 add up ore to get count

#11 RVCS => 8 CBMDT
#29 QXPB, 8 QRGRH => 8 LGMKD
#3 VPRVD => 6 PMFZG
#print(reactions, totalFuel)