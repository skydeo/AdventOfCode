import timeit
sTime = timeit.default_timer()

testing = 0

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
diskWeights = {}


for r in data:
    # print(r)
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
        diskWeights[r[0]] = r[1][1:-1]

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



# print("Weight of ugml: {0}".format(calculateWeights('ugml')))
# print("Weight of padx: {0}".format(calculateWeights('padx')))
# print("Weight of fwft: {0}".format(calculateWeights('fwft')))
# print("Weight of root word ({0}): {1}".format(root, calculateWeights(root)))


for p in hierarchy:
    diskWeights[p] = calculateWeights(p)

# print("diskWeights: ",diskWeights)
# print("hierarcy: ",hierarchy)

# I'm so far deep at this point in not building a tree, a foolish decision made thinking it would be
# unnecessarily laborious. I don't know if I should just give in and make a tree, use a library, or
# charge needlessly forward.
# Should've learned https://networkx.github.io

def findImbalance(word):
    imbalancedWord = ''
    # print("Working on word: {0}".format(word))
    if word in hierarchy:
        tWeights = {}
        for x in hierarchy[word]:
            # print(x, diskWeights[x])
            w = diskWeights[x]
            if w in tWeights:
                tWeights[diskWeights[x]] += 1
            else:
                tWeights[diskWeights[x]] = 1
        
        wrongValue = min(tWeights, key=tWeights.get)

        for x in hierarchy[word]:
            if diskWeights[x] == wrongValue:
                imbalancedWord = x
                findImbalance(x)

    return imbalancedWord

# print(hierarchy)

ibw = findImbalance(root)

for w in hierarchy:
    if ibw in hierarchy[w]:
        ibwp = w


tWeights = {}
for x in hierarchy[ibwp]:
    w = diskWeights[x]
    if w in tWeights:
        tWeights[diskWeights[x]] += 1
    else:
        tWeights[diskWeights[x]] = 1
print(tWeights)
correction = max(tWeights, key=tWeights.get) - min(tWeights, key=tWeights.get)


print(correction)

cpv = weights[ibwp] + correction

print(cpv)


eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
