import timeit
sTime = timeit.default_timer()

testing = 0

if testing:
    filename = "13test.in"
else:
    filename = "13.in"

f = open(filename, "r")
firewall = {int(r.split(': ')[0]): int(r.split(': ')[1]) for r in f.read().splitlines()}

maxDepth = max(firewall.keys())

currentState = {}
for r in firewall.keys():
    currentState[r] = [0, '+']

def advanceState(fw, cs):
    for f in fw:
        if cs[f][0] == (fw[f]-1):
            cs[f][1] = '-'
        elif cs[f][0] == 0:
            cs[f][1] = '+'
        st = 'cs[f][0] ' + cs[f][1] + '= 1'
        exec(st)

tripSeverity = 0
caught = 0
for t in range(0,maxDepth+1):
    if testing:
        print('Time: {0}\t Current state: {1}'.format(t, currentState))
    
    if (t in firewall) and (currentState[t][0] == 0):
        tripSeverity += (t * firewall[t])
        caught += 1

    advanceState(firewall, currentState)

print('Caught {0} times. Trip severity: {1}'.format(caught, tripSeverity))


eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
