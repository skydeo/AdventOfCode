import timeit
sTime = timeit.default_timer()

testing = 0

if testing:
    lengths = [3, 4, 1, 5]
    size = 5
else:
    with open("10.in") as inputFile:
        lengths = [int(l) for l in inputFile.read().split(",")]
    size = 256

values = [i for i in range(0,size)]
offset = 0
cPos = 0

for l in lengths:
    if testing:
        print("length: {0}, cPos: {1}".format(l,cPos))
    
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

print("Hash: {0}".format(values[0] * values[1]))

eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
