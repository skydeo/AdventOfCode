import timeit
from collections import deque
sTime = timeit.default_timer()

testing = 0

if testing:
    steps = 3
else:
    steps = 369

iterations = 2017

def createBuffer(iterations):
    buffer = deque([0])
    for i in range(0,iterations):
        buffer.rotate(-steps)
        buffer.append(i+1)
    return buffer[0]

print('Value after last created buffer: {0}'.format(createBuffer(iterations)))

eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
