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
    print('i: {}\tins: {}'.format(i,ins))
    c = ins.split()[0]

    if c == 'set':
        x, y = ins.split()[1:]
        if not is_int(y):
            y = regs[y]
        regs[x] = int(y)
        print('\tSetting register {} to {}.'.format(x,y))
    elif c == 'add':
        x, y = ins.split()[1:]
        if not is_int(y):
            y = regs[y]
        regs[x] += int(y)
        print('\tAdding {} to register {}.'.format(y,x))        
    elif c == 'mul':
        x, y = ins.split()[1:]
        if not is_int(y):
            y = regs[y]
        regs[x] *= int(y)
        print('\tMultiplying register {} by {}.'.format(x,y))   
    elif c =='mod':
        x, y = ins.split()[1:]
        if not is_int(y):
            y = regs[y]
        regs[x] %= int(y)
        print('\tModulo-ing register {} by {}.'.format(x,y))   
    elif c == 'jgz':
        x, y = ins.split()[1:]
        if not is_int(x):
            x = regs[x]
        if not is_int(y):
            y = regs[y]
        if x > 0:
            i += int(y) - 1
        else:
            print('\t{} not greater than 0. Not jumping.'.format(x))
        print('\tJump\tins:{0}, x: {1}, y: {2}'.format(ins,x,y))
    elif c == 'snd':
        x = ins.split()[1]
        freq = regs[x]
        print('\tSound played: {0}'.format(freq))
    elif c == 'rcv':
        x = ins.split()[1]
        if regs[x] != 0:
            print('Recovered sound frequency: {0}'.format(freq))
            break
    else:
        print('Unrecognized instruction: {0}'.format(ins))
    
    i += 1
    # print(i)
    print('\t',dict(regs))

eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
