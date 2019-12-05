
def doesnotdecrease(val):
    sval = str(val)
    min = 0
    for i in range(0,len(sval)):
        mintest = int(sval[i])
        if mintest < min:
            return False
        min = mintest
    return True

def finddouble(val):
    sval = str(val)
    for i in range(0,len(sval)-1):
        if sval[i] == sval[i+1]:
            return True
    return False

meetcriteria = []
assert doesnotdecrease(111111)
assert doesnotdecrease(110111) == False
assert doesnotdecrease(123789)
assert finddouble(111111)
assert finddouble(110111)
assert finddouble(222222)
assert finddouble(122222)
assert finddouble(212222)
assert finddouble(221222)
assert finddouble(222122)
assert finddouble(222212)
assert finddouble(222221)
assert finddouble(113456)
assert finddouble(122456)
assert finddouble(123356)
assert finddouble(123446)
assert finddouble(123455)
assert finddouble(123456) == False
assert finddouble(123789) == False
for i in range(134564,585159):
    if finddouble(i):
        if doesnotdecrease(i):
            meetcriteria.append(i)

print(str(len(meetcriteria)) + " meet criteria")