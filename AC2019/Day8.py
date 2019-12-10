def CountZeros(l):
    count = 0
    for i in l:
        count += i.count('0')
    return count

def countOnesCrossCountTwos(l):
    countOnes = 0
    countTwos = 0
    for i in l:
        countOnes += i.count('1')
        countTwos += i.count('2')
    
    return countOnes * countTwos

def checkMatrix(target,source):
    returnString = ''
    for i in range(0,len(target)):
        s = int(source[i:i+1])
        t = int(target[i:i+1])
        if s == 2 and (t ==1 or t==0):
            returnString += str(t)
        else:
            returnString += str(s)
    return returnString

def checkForTwos(ls):
    for l in ls:
        for i in l:
            if i.count('2') > 0:
                return True
    return False

layers=[]
try:
    with open("AC2019/Day8.in") as fp:
        while(True):
            layer = []
            for i in range(0,6):
                layer.append(fp.read(25))
            if len(layer[0]) == 0:
                break
            layers.append(layer)

except IOError as err:
    print("Error reading the file: " + err)
    fp.close()
    

print(len(layers))

matrix = [['2222222222222222222222222'] for i in range(6)]

#countzero={}
layerCount = 0
for l in layers:
    rowCount = 0
    for x in l:
        matrix[rowCount][0] = checkMatrix(x,matrix[rowCount][0])
        rowCount += 1
    #countzero[layerCount] = CountZeros(l)
    layerCount += 1
    if not checkForTwos(matrix):
        print("Done")

for i in range(0,6):
    print(matrix[i][0])


print("Exit")
#key_min = min(countzero.keys(), key=(lambda k: countzero[k]))
# print("Layer " + str(key_min) + " has least: " + str(countzero[key_min]))
# print("num Ones x Num twos:" + str(countOnesCrossCountTwos(layers[key_min])))