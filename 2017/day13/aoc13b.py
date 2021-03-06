import timeit
sTime = timeit.default_timer()

testing = 0

if testing:
    filename = "13test.in"
else:
    filename = "13.in"

f = open(filename, "r")
firewall = {int(r.split(': ')[0]): int(r.split(': ')[1]) for r in f.read().splitlines()}

def caught(fw, time):
    return any([((t+f) % ((fw[f]-1)*2)) == 0 for f in fw])

t = 0
while(True):
    if not caught(firewall, t):
        print('Clean escape with {0} picosecond delay.'.format(t))
        break
    t += 1

eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
