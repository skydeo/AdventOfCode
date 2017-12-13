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
        # This doesn't account for a firewall with range 1, but I'm assuming that's outside scope.
        if cs[f][0] == (fw[f]-1):
            cs[f][1] = '-'
        elif cs[f][0] == 0:
            cs[f][1] = '+'
        st = 'cs[f][0] ' + cs[f][1] + '= 1'
        exec(st)

def evaluateSeverity(fw, cs, cd):
    ts = 0
    c = 0
    if (cd in fw) and (cs[cd][0] == 0):
        ts = (cd * fw[cd])
        c = 1
        if testing:
            print('Caught!')
    return ts, c

delay = 0
while(True):
    runState = copy.deepcopy(currentState)

    for d in range(0,delay):
        advanceState(firewall, runState)     

    tripSeverity = 0
    caught = 0

    for t in range(0,maxDepth+1):
        if testing:
            print('Time: {0}\t\tDepth: {1}\tState: {2}'.format(t, t, runState))
        
        ts, c = evaluateSeverity(firewall, runState, t)
        tripSeverity += ts
        caught += c

        advanceState(firewall, runState)
    
    # print('Delay: {0}\tCaught {1} times. Trip severity: {2}'.format(delay, caught, tripSeverity))
    if delay % 1000 == 0:
        print("Finished with delay {0}.".format(delay))

    if caught == 0:
        print('Clean exit with a {0} picosecond delay.'.format(delay))
        break
    
    delay += 1


# 3960702
eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
