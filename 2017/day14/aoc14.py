import timeit
from functools import reduce
import numpy as np
sTime = timeit.default_timer()

testing = 0

if testing:
    input = 'flqrgnkx'
else:
    input = 'oundnydw'

def hashRound(values, lengths, cPos, offset):
    for l in lengths:
        if (cPos + l) > 256:
            fArray = values[cPos:]
            bArray = values[:(cPos+l)%256]
            rArray = list(reversed(fArray + bArray))
            
            values[cPos:] = rArray[:len(fArray)]
            values[:(cPos+l)%256] = rArray[len(fArray):]

        else:
            tArray = values[(cPos):(cPos+l)]
            values[(cPos):(cPos+l)] = list(reversed(tArray))
        
        cPos = cPos + l + offset
        cPos = cPos % 256
        offset += 1
    
    return values, cPos, offset

def knotHash(input):
    lengths = [ord(l) for l in input] + [17, 31, 73, 47, 23]

    offset = 0
    cPos = 0
    values = [i for i in range(0,256)]

    for i in range(0,64):
        sparseHash, cPos, offset = hashRound(values, lengths, cPos, offset)

    denseHash = []
    for i in range(0,16):
        tx = reduce(lambda x, y: x ^ y, sparseHash[(i*16):((i+1)*16)])
        denseHash += [tx]

    hash = ''
    for i in denseHash:
        hash += hex(i)[2:].zfill(2)

    return hash

# hashList = []
binHash = []
for r in range(0,128):
    hexHash = knotHash(input+'-'+str(r))
    # hashList += [hexHash]
    # binHash.append([c for c in bin(int(hexHash, 16))[2:].zfill(128)])
    binHash += ([bin(int(hexHash, 16))[2:].zfill(128)])

usedSqaures = sum(h.count('1') for h in binHash)

print('Input: {0}\t\tUsed Squares: {1}'.format(input,usedSqaures))



eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
