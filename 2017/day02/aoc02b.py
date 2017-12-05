import csv
import timeit
import itertools

sTime = timeit.default_timer()

testing = 0

if testing:
    inputFileName = "testInputB.txt"
    answer = 9
else:
    inputFileName = "input.txt"

s = []

with open(inputFileName, 'r') as inputFile:
    fileReader = csv.reader(inputFile, delimiter='\n')
    for row in fileReader:
        s.append(row[0].split('\t'))

s = [[int(n) for n in r] for r in s]

checksums = []

# for r in s:
#     r.sort(reverse=True)
#     l = len(r)
#     print("Length: {0}".format(l))
#     print(r)
#     for x in range(0,l):
#         c = r.pop(x)
#         print("Popped {0}, list is {1}".format(c,r))
#         r.insert(x, c)
#     print(r)

for r in s:
    combos = itertools.combinations(sorted(r, reverse=True), 2)
    for a, b in combos:
        if (a%b == 0):
            checksums.append(a/b)

checksum = int(sum(checksums))

if testing:
    if (checksum ==  answer):
        print("Test passed.")
    else:
        print("Test failed.")
else:
    print("Checksum: {0}".format(checksum))

eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))