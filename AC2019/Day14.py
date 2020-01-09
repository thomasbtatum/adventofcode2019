f = open("AC2019/Day14.0")
s = f.readlines()

def findInputChem(outChem, dict):
    for k,v in dict.items():
        if k[1] == outChem:
            return v

def getOre(count,outChem,dict):
    inList = findInputChem(outChem, dict)
    if len(inList) == 1 and inList[0][1] == 'ORE':
        return count * int(inList[0][0])
    else:
        total = 0
        for inChem in inList:
            total += (int(inChem[0]) // count) * int(getOre(int(inChem[0]),inChem[1],dict))
        return total

reactions = {}
totalFuel = 0
for line in s:
    rewords = line.split('=>')
    leftSplit = rewords[0].strip().split(',')
    keys = rewords[1].strip().split(' ')
    key = tuple([keys[0],keys[1]])
    tupList = []
    
    for val in leftSplit:
        lword = val.strip().split(' ')
        tupList.append(tuple([lword[0],lword[1]]))

    reactions[key] = tupList

totalFuel = getOre(1,'FUEL',reactions) 

#11 RVCS => 8 CBMDT
#29 QXPB, 8 QRGRH => 8 LGMKD
#3 VPRVD => 6 PMFZG
print(reactions, totalFuel)