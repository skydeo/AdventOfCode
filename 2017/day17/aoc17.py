import timeit
from collections import deque
sTime = timeit.default_timer()

testing = 0

if testing:
    steps = 3
else:
    steps = 369

p1i = 2_017
p2i = 50_000_000

def createBuffer(iterations):
    buffer = deque([0])
    for i in range(0,iterations):
        buffer.rotate(-steps)
        buffer.append(i+1)
    return buffer

print('Value after last created buffer on iteration {0}: {1}'.format(p1i, createBuffer(p1i)[0]))
part2 = createBuffer(p2i)
print('Value after 0 on iteration {0}: {1}'.format(p2i,part2[part2.index(0)+1]))

eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
