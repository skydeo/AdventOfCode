import timeit
from functools import reduce
sTime = timeit.default_timer()

testing = 0

if testing:
    lengths = 'AoC 2017'
    lengths = [ord(l) for l in lengths]
    lengths += [17, 31, 73, 47, 23]
else:
    with open("10.in") as inputFile:
        lengths = [ord(l) for l in inputFile.read().rstrip()]
        lengths += [17, 31, 73, 47, 23]

if testing:
    print(lengths)

def hashRound(values, lengths, cPos, offset):
    for l in lengths:
        if (cPos + l) > size:
            fArray = values[cPos:]
            bArray = values[:(cPos+l)%size]
            rArray = list(reversed(fArray + bArray))
            
            values[cPos:] = rArray[:len(fArray)]
            values[:(cPos+l)%size] = rArray[len(fArray):]

        else:
            tArray = values[(cPos):(cPos+l)]
            values[(cPos):(cPos+l)] = list(reversed(tArray))
        
        cPos = cPos + l + offset
        cPos = cPos%size
        offset += 1
    
    return values, cPos, offset

size = 256
offset = 0
cPos = 0
values = [i for i in range(0,size)]


for i in range(0,64):
    sparseHash, cPos, offset = hashRound(values, lengths, cPos, offset)

if testing:
    print(sparseHash)

denseHash = []
for i in range(0,16):
    tx = reduce(lambda x, y: x ^ y, sparseHash[(i*16):((i+1)*16)])
    denseHash += [tx]

if testing:
    print(denseHash)

hash = ''
for i in denseHash:
    hash += hex(i)[2:].zfill(2)

print("Hexadecimal hash: {0}".format(hash))

eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
