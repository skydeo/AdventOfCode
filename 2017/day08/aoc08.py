import timeit
import numpy as np
sTime = timeit.default_timer()

testing = 0

if testing:
    filename = "testInput.txt"
else:
    filename = "input.txt"

instructions = []
with open(filename) as inputFile:
    f = inputFile.read().splitlines()
    for r in f:
        instructions.append(r.split(' '))

instructions = np.array(instructions)
if testing:
    print(instructions)

# Initialize registers dictionary to 0
registers = dict.fromkeys(list(instructions[:,0]) + list(instructions[:,4]), 0)

for i in instructions:
    l = 'registers[\'' + i[4] + '\'] ' + ' '.join(i[5:])
    if eval(l):
        m = 'registers[\'' + i[0] + '\']'
        m += ' += ' if i[1] == 'inc' else ' -= '
        m += i[2]
        exec(m)

if testing:
    print("Final registers: {0}".format(registers))

print("Maximum value after instructions: {0}".format(max(registers.values())))


eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
