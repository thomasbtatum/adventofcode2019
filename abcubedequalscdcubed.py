
max = 1001

# for a in range(1,max):
#     for b in range(1,max):
#         for c in range(1,max):
#             for d in range(1,max):
#                 if(a**3+b**3 == c**3+d**3):
#                     print("a: " + str(a) + " b:" + str(b) + " c:" + str(c) + " d:" + str(d))
#above is 1st approach - brute force O(n**4) - not good

# def is_perfect_cube(n):
#     chk = n**(1/3.)
#     if isinstance(chk,complex):
#         return False
#     else:
#         c = int(chk)
#         return (c**3 == n) or ((c+1)**3 == n)

# for a in range(1,max):
#     #print("a: " + str(a))
#     for b in range(1,max):
#         for c in range(1,max):
#             dsum = a**3 + b**3 - c**3
#             if(is_perfect_cube(dsum)):
#                 d = int(dsum**(1/3.))
#                 #print(d)
#                 if(a**3+b**3 == c**3+d**3) & (1 <= d <= 1000):
#                     print("a: " + str(a) + " b:" + str(b) + " c:" + str(c) + " d:" + str(d))
# above takes out one loop and this is O(n**3)

values = {0:[]}
for a in range(1,max):
    for b in range(1,max):
        sum = a**3 + b**3
        if(sum in values.keys()):
            values[sum].append([a,b])
        else:
            values[sum] = [[a,b]]

count = 1
for result in values.keys():
    for list1 in values[result]:
        for list2 in values[result]:
            print(str(count) + " Tot:" + str(result) + " 1:" + str(list1) + " 2:" + str(list2))
            count = count + 1
#best approach - solves in O(n**2)