import csv, timeit

sTime = timeit.default_timer()

testing = 0

if testing:
    inputFileName = "testInputA.txt"
    answer = 18
else:
    inputFileName = "input.txt"

s = []

with open(inputFileName, 'r') as inputFile:
    fileReader = csv.reader(inputFile, delimiter='\n')
    for row in fileReader:
        s.append(row[0].split('\t'))


s = [[int(n) for n in r] for r in s]

checksums = []

for r in s:
    # This changes the input matrix -- don't care for now, might for second part.
    r.sort()
    checksums.append(r[-1]-r[0])

checksum = sum(checksums)

if testing:
    if (checksum ==  answer):
        print("Test passed.")
    else:
        print("Test failed.")
else:
    print("Checksum: {0}".format(checksum))

eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
