def calcWeight(fuel, total):
    if fuel <= 0:
        return 0
    else:
        check = fuel // 3 - 2
        total += calcWeight(check, check)
        return total

f = open("Day1Input.txt")
inputs = f.readlines()
totalWeights = 0
for t in inputs :
    totalWeights += calcWeight(int(t),0)

print(str(totalWeights))
