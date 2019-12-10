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

countzero={}
layerCount = 0
for l in layers:
    countzero[layerCount] = CountZeros(l)
    layerCount += 1

key_min = min(countzero.keys(), key=(lambda k: countzero[k]))

print("Layer " + str(key_min) + " has least: " + str(countzero[key_min]))
print("num Ones x Num twos:" + str(countOnesCrossCountTwos(layers[key_min])))