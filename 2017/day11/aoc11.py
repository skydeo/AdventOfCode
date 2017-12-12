# Super helpful link that explains hex coordinate systems and distance calculations:
# https://www.redblobgames.com/grids/hexagons/

import timeit
sTime = timeit.default_timer()

testing = 0

if testing:
    # moves = ['se','sw','se','sw','sw']
    # moves = ['ne','ne','s','s']
    moves = ['ne','ne','sw','sw']
else:
    f = open("11.in", "r")
    moves = f.read().rstrip().split(",")

c = {'x': 0, 'y': 0, 'z': 0}
distances = []

for m in moves:
    if m == "ne":
        c['x'] += 1
        c['z'] -= 1
    elif m == "n":
        c['y'] += 1
        c['z'] -= 1
    elif m == "nw":
        c['x'] -= 1
        c['y'] += 1
    elif m == "sw":
        c['x'] -= 1
        c['z'] += 1
    elif m == "s":
        c['y'] -= 1
        c['z'] += 1
    elif m == "se":
        c['x'] += 1
        c['y'] -= 1
    else:
        print("ERROR: {0} is not a valid instruction.".format(m))
    
    distances += [int((abs(c['x']) + abs(c['y']) + abs(c['z'])) / 2)]

print("Distance from origin: {0}".format(distances[-1]))
print("Maximum distance from origin: {0}".format(max(distances)))

eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
