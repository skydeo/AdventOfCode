import timeit

sTime = timeit.default_timer()

input = 265149

coords = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

x = y = dx = dy =  0

grid = {(0,0) : 1}

while (max(grid.values()) < input):
    if (x == 0 and y == 0):
        dx, dy = 1, 0
    elif (x > 0 and x==1-y):
        dx, dy = 0, 1
    elif (x==y and x > 0):
        dx, dy = -1, 0
    elif (-x == y and x < 0):
        dx, dy = 0, -1
    elif (x==y and x < 0):
        dx, dy = 1, 0
    
    x += dx
    y += dy

    total = 0

    for coord in coords:
        cx, cy = coord
        if (x+cx, y+cy) in grid:
            total += grid[(x+cx, y+cy)]

    grid[(x, y)] = total

print("First value greater than {0}: {1}".format(input,max(grid.values())))

eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
