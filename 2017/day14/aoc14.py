import timeit
from functools import reduce
import networkx as nx

sTime = timeit.default_timer()

testing = 0

if testing:
    input = 'flqrgnkx'
else:
    input = 'oundnydw'

def hashRound(values, lengths, cPos, offset):
    for l in lengths:
        if (cPos + l) > 256:
            fArray = values[cPos:]
            bArray = values[:(cPos+l)%256]
            rArray = list(reversed(fArray + bArray))
            
            values[cPos:] = rArray[:len(fArray)]
            values[:(cPos+l)%256] = rArray[len(fArray):]

        else:
            tArray = values[(cPos):(cPos+l)]
            values[(cPos):(cPos+l)] = list(reversed(tArray))
        
        cPos = cPos + l + offset
        cPos = cPos % 256
        offset += 1
    
    return values, cPos, offset

def knotHash(input):
    lengths = [ord(l) for l in input] + [17, 31, 73, 47, 23]

    offset = 0
    cPos = 0
    values = [i for i in range(0,256)]

    for i in range(0,64):
        sparseHash, cPos, offset = hashRound(values, lengths, cPos, offset)

    denseHash = []
    for i in range(0,16):
        tx = reduce(lambda x, y: x ^ y, sparseHash[(i*16):((i+1)*16)])
        denseHash += [tx]

    hash = ''
    for i in denseHash:
        hash += hex(i)[2:].zfill(2)

    return hash

binHash = []
for r in range(0,128):
    hexHash = knotHash(input+'-'+str(r))
    binHash.append([int(c) for c in bin(int(hexHash, base=16))[2:].zfill(128)])


# usedSquares = 0
# for h in binHash:
#     for b in h:
#         if b:
#             usedSquares += 1

# Here goes nothing...
G = nx.Graph()
for row in range(0,128):
    for column in range(0,128):
        if binHash[row][column]:
            G.add_node((row,column))


for row in range(0,128):
    for column in range(0,128):
        if column > 0:
            if binHash[row][column] and binHash[row][column-1]:
                G.add_edge((row, column), (row, column-1))
        if row > 0:
            if binHash[row][column] and binHash[row-1][column]:
                G.add_edge((row, column), (row-1, column))


# ## Seen on https://www.reddit.com/r/adventofcode/comments/7jpelc/2017_day_14_solutions/
# ## Create a 128 x 128 node graph with all connected edges, and delete nodes if they're not in the hash.
# ## A bit simpler to code, but logically working backwards a bit. Runtimes seem slower, actually.

# G = nx.generators.lattice.grid_2d_graph(128, 128)
# for row in range(0,128):
#     for column in range(0,128):
#         if not binHash[row][column]:
#             G.remove_node((row, column))
# ##

usedSquares = nx.number_of_nodes(G)
numConnected = nx.number_connected_components(G)

print('Input: {0}\nUsed Squares: {1}\nConnected regions: {2}'.format(input, usedSquares, numConnected))

eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
