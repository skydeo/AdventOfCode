import math

testing = 0

if testing:
    input = [1, 12, 23, 1024]
    answers = [0, 3, 2, 31]
    tDistances = []
else:
    input = [265149]

for i in input:
    sLength = math.ceil(math.sqrt(i)) + 1
    sLength = sLength - 1 if (sLength%2 == 0) else sLength

    tDistance = sLength - 1

    half = math.floor(sLength/2)
    
    diff = int(math.pow(sLength, 2)) - i
    
    if (sLength != 1):
        sideOffset = math.floor(diff/(sLength-1))
    else:
        sideOffset = 0

    correction = diff - sideOffset * (sLength-1)

    if correction > half:
        correction -= (correction-half)*2

    tDistance -= correction

    if testing:
        tDistances.append(tDistance)

    print("Input number: {0}\tManhattan Distance: {1}".format(i, tDistance))

if testing:
    if answers == tDistances:
        print("Tests passed.")
    else:
        print("Tests failed.")
