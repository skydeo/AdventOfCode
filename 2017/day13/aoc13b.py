import timeit
import itertools
sTime = timeit.default_timer()

testing = 0

if testing:
    filename = "13test.in"
else:
    filename = "13.in"

f = open(filename, "r")
firewall = {int(r.split(': ')[0]): int(r.split(': ')[1]) for r in f.read().splitlines()}

def zeroScanner(range, time):
    return (time % ((range-1)*2)) == 0

t = 0
while(True):
    if not any([zeroScanner(firewall[f], t + f) for f in firewall]):
        print('Clean escape with {0} picosecond delay.'.format(t))
        break
    t += 1

eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
