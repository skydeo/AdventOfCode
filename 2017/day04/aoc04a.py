import timeit
sTime = timeit.default_timer()

with open('input.txt') as f:
    data = []
    for line in f.read().splitlines():
        data.append(line.split(' '))


validCount = 0
for r in data:
    if len(r) == len(set(r)):
        validCount += 1

print("{0} passphrases are valid under initial policies.".format(validCount))

validCount = 0
for r in data:
    sortedWordList = []
    for w in r:
        sortedWordList.append(''.join(sorted(list(w))))
    if len(r) == len(set(sortedWordList)):
        validCount += 1

print("{0} passphrases are valid under strict policies.".format(validCount))

eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
