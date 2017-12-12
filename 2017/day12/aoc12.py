import timeit
sTime = timeit.default_timer()

testing = 0

if testing:
    filename = "12test.in"
else:
    filename = "12.in"

f = open(filename, "r")
pipes = [p.replace(',','').split() for p in f.read().splitlines()]

# Remove '<->'
for n, p in enumerate(pipes):
    p = [int(p[0])] + [int(n) for n in p[2:]]
    pipes[n] = p


# This feels messier than it needs to be. Building connection lists.
connections = {}

for pipe in pipes:
    p = pipe[0]
    for q in pipe[1:]:
        if p in connections:
            connections[p] += [q]
        else:
            connections[p] = [q]
        
        if q in connections:
            connections[q] += [p]
        else:
            connections[q] = [p]

# Remove duplicates
for c in connections:
    connections[c] = set(connections[c])

if testing:
    print(connections)

def countConnections(dict, root, checked):
    connects = 0
    for i in connections[root]:
        if i not in checked:
            connects += 1
            checked += [i]
            connects += countConnections(dict, i, checked)
    
    return connects
        

rootProgram = 0         # Not sure this needs to be configurable.
connectedPrograms = 1   # Connected to itself at start.
checked = [rootProgram] # Already checked itself (before it...)

connectedPrograms += countConnections(connections, rootProgram, checked)

print('Root program {0} is connected to {1} other programs.'.format(rootProgram,connectedPrograms))

### Part 2

programs = sorted(connections.keys())

groups = set()
for program in programs:
    # Abuse the unused checked list from countConnections as a group list
    checked = []
    # Don't need this variable, but oh well.
    connectedPrograms = 1 + countConnections(connections, program, checked)

    # Lists can't be added to sets because they're mutable, so convert to tuple.
    checked = tuple(sorted(checked))

    groups.add(checked)

# Get count of number of distinct groups.
print('There are {0} separate groups.'.format(len(groups)))

eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
