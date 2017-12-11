import timeit
sTime = timeit.default_timer()

testing = 1

if testing:
    filename = "testInput.txt"
else:
    filename = "input.txt"

data = []
with open(filename) as f:
    i = f.read().splitlines()
    for j in i:
        data.append(j.split())

children = []
words = []
weights = {}
hierarchy = {}

for r in data:
    print(r)
    weights[r[0]] = int(r[1][1:-1])
    if '->' in r:
        kids = []
        for c in r[r.index('->')+1:]:
            children.append(c.strip(','))
            kids.append(c.strip(','))
        words.append(r[0])

        hierarchy[r[0]] = kids
    else:
        children.append(r[0])

for w in words:
    if w not in children:
        root = w
        print("Root program: {0}".format(w))

def calculateWeights(rootProgram):
    weight = weights[rootProgram] 
    for p in hierarchy[rootProgram]:
        if p in hierarchy:
            weight += calculateWeights(p)
        else:
            weight += weights[p]
    return weight



print(calculateWeights('ugml'))
print(calculateWeights('padx'))
print(calculateWeights('fwft'))
print(calculateWeights(root))

diskWeights = {}

for p in hierarchy:
    diskWeights[p] = calculateWeights(p)

print(diskWeights)

# I'm so far deep at this point in not building a tree, a foolish decision made thinking it would be
# unnecessarily laborious. I don't know if I should just give in and make a tree, use a library, or
# charge needlessly forward.

for x in hierarchy:
    print(x)







eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
