
class tNode(object):
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        self.depth = -1
    
    def add_child(self, obj):
        self.children.append(obj)

    def add_parent(self, obj):
        self.parent = obj

def findRoot(d):
    for k in d.keys():
        n = d[k]
        if n.parent is None:
            return n

def markDepthRecur(n,dep):
    n.depth = dep
    for n2 in n.children:
        markDepthRecur(n2,dep+1)

def markDownDepthRecur(n):
    assert n.depth > -1
    for n2 in n.children:
        if n2.depth == -1:
            n2.depth = n.depth + 1
        markDownDepthRecur(n2)

def markUpDepthRecur(n,dep):
    n.depth = dep
    if n.parent is None:
        return
    else:
        markUpDepthRecur(n.parent,dep+1)


f = open("AC2019/Day6input.txt")
rawOrbit = f.readlines()
print("Done Reading.")
nodes = {}

i = 0
while i < len(rawOrbit):
    parentChild = rawOrbit[i].split(")")
    parentString = parentChild[0]
    childString = parentChild[1].strip()

    if parentString not in nodes:
        pnode = tNode(parentString)
        nodes[parentString] = pnode
    pnode = nodes[parentString]

    if childString not in nodes:
        cnode = tNode(childString)
        nodes[childString] = cnode
    cnode = nodes[childString]

    cnode.add_parent(pnode)
    pnode.add_child(cnode)

    i += 1

#r = findRoot(nodes)
#markDepthRecur(r,0)

s = nodes["SAN"]
s.depth = 0
markUpDepthRecur(s.parent,0)
r = findRoot(nodes)
markDownDepthRecur(r)

y = nodes["YOU"]
print("Distance is: " + str(y.depth))

#The answer was 307.  1 minus the 308 that will print
#because we need the shortest from parent of You not YOU


# total = 0
# for k in nodes.keys():
#     total += nodes[k].depth

# print("Total: " + str(total))