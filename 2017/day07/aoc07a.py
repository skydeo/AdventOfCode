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
for r in data:
    if '->' in r:
        for c in r[r.index('->')+1:]:
            children.append(c.strip(','))
        words.append(r[0])
    else:
        children.append(r[0])

for w in words:
    if w not in children:
        print("Root program: {0}".format(w))


eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
