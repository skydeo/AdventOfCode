import timeit
from collections import defaultdict
sTime = timeit.default_timer()

testing = 0

if testing:
    filename = '18test.in'
else:
    filename = '18.in'

f = open(filename,'r')
instructions = f.read().splitlines()

regs = defaultdict(lambda: 0)

def is_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

i = 0
while i in range(0,len(instructions)):
    ins = instructions[i]
    c = ins.split()[0]

    if c == 'set':
        x, y = ins.split()[1:]
        if not is_int(y):
            y = regs[y]
        regs[x] = int(y)
    elif c == 'add':
        x, y = ins.split()[1:]
        if not is_int(y):
            y = regs[y]
        regs[x] += int(y)
    elif c == 'mul':
        x, y = ins.split()[1:]
        if not is_int(y):
            y = regs[y]
        regs[x] *= int(y)
    elif c =='mod':
        x, y = ins.split()[1:]
        if not is_int(y):
            y = regs[y]
        regs[x] %= int(y)
    elif c == 'jgz':
        x, y = ins.split()[1:]
        if not is_int(x):
            x = regs[x]
        if not is_int(y):
            y = regs[y]
        if x > 0:
            i += int(y) - 1
    elif c == 'snd':
        x = ins.split()[1]
        freq = regs[x]
    elif c == 'rcv':
        x = ins.split()[1]
        if regs[x] != 0:
            print('Recovered sound frequency: {0}'.format(freq))
            break
    else:
        print('Unrecognized instruction: {0}'.format(ins))
    
    i += 1

eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
