import timeit
sTime = timeit.default_timer()

testing = 0

if testing:
    line = ['a','b','c','d','e']
    instructions = ['s1','x3/4','pe/b']
else:
    line = [l for l in 'abcdefghijklmnop']
    f = open('16.in','r')
    instructions = f.read().rstrip().split(',')

for i in instructions:
    m = i[0]
    if m == 's':
        v = int(i[1:])
        line = line[-v:] + line[:-v]
    elif m == 'x':
        pos1, pos2 = [int(n) for n in i[1:].split('/')]
        p1 = line[pos1]
        line[pos1] = line[pos2]
        line[pos2] = p1
    elif m == 'p':
        p1, p2 = i[1:].split('/')
        pos1 = line.index(p1)
        pos2 = line.index(p2)
        line[pos1] = p2
        line[pos2] = p1
    else:
        print('Unrecognized move: {}'.format(i))

print(''.join(line))

eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
