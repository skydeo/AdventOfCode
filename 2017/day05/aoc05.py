import copy
import timeit
sTime = timeit.default_timer()

testing = 0

if testing:
    data = [0, 3, 0, 1, -3]
    data2 = list(data)
else:
    with open('input.txt') as inputFile:
        data = [int(i) for i in inputFile.read().splitlines()]
    data2 = list(data)

stepCount = 0
cb = 0
while cb in range(0,len(data)):
    if testing:
        print("Step: {0}\t\tPosition: {1}\tInstruction: {2}\tData: {3}".format(stepCount, cb, data[cb], data))
    data[cb] += 1
    cb += (data[cb] - 1)

    stepCount += 1

print("Exited the maze in {0} steps under initial rules.".format(stepCount))

stepCount = 0
cb = 0
data = data2
while cb in range(0,len(data)):
    if testing:
        print("Step: {0}\t\tPosition: {1}\tInstruction: {2}\tData: {3}".format(stepCount, cb, data[cb], data))
    
    if data[cb] < 3:
        data[cb] += 1
        cb += (data[cb] - 1)
    else:
        data[cb] -= 1
        cb += (data[cb] + 1)
    
    stepCount += 1

print("Exited the maze in {0} steps under updated rules.".format(stepCount))

eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))