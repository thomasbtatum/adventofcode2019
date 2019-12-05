
def doesnotdecrease(val):
    sval = str(val)
    min = 0
    for i in range(0,len(sval)):
        mintest = int(sval[i])
        if mintest < min:
            return False
        min = mintest
    return True

# #now find double cant be part of triple of fivekind
# #quads are ok, cause they are doubles
# def nofivekindortrips(val):
#     fk = ["00000","11111","22222","33333","44444","55555","66666","77777","88888","99999"]
#     frk = ["0000","1111","2222","3333","4444","5555","6666","7777","8888","9999"]
#     tk = ["000","111","222","333","444","555","666","777","888","999"]
#     sval = str(val)
    
#     for x in fk:
#         if sval.find(x):
#             return False
#     foundFour = False
#     for y in tk:
#         if sval.find(y):
#             return False


def finddouble(val):
    sval = str(val)
    c = sval[0]
    sameCount = 1
    hasPair = False
    for i in range(1,len(sval)):
        if c == sval[i]:
            sameCount+=1
        else:
            if sameCount == 2:
                hasPair = True
            sameCount = 1
        c = sval[i]

    if hasPair or sameCount == 2:
        return True
    return False

meetcriteria = []
assert doesnotdecrease(111111)
assert doesnotdecrease(110111) == False
assert doesnotdecrease(123789)
assert finddouble(111111) == False
assert finddouble(110111)
assert finddouble(222222) == False
assert finddouble(122222) == False
assert finddouble(212222) == False
assert finddouble(221222)
assert finddouble(222122)
assert finddouble(222212) == False
assert finddouble(222221) == False
assert finddouble(113456)
assert finddouble(122456)
assert finddouble(123356)
assert finddouble(123446)
assert finddouble(123455)
assert finddouble(123551)
assert finddouble(125512)
assert finddouble(155121)
assert finddouble(112345)
assert finddouble(111123) == False
assert finddouble(111122)
assert finddouble(211113) == False
assert finddouble(121111) == False
assert finddouble(111111) == False
assert finddouble(222222) == False
assert finddouble(100003) == False
assert finddouble(100100)
assert finddouble(333333) == False
assert finddouble(334467)
assert finddouble(334444)
assert finddouble(111111) == False
assert finddouble(123456) == False
assert finddouble(123789) == False
assert finddouble(111110) == False
assert finddouble(211111) == False
assert finddouble(111345) == False
assert finddouble(211135) == False
assert finddouble(221113) 
assert finddouble(223111)
for i in range(134564,585159):
    if finddouble(i):
        if doesnotdecrease(i):
            meetcriteria.append(i)

print(str(len(meetcriteria)) + " meet criteria")