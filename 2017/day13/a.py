# Another answer from /u/sciyoshi on https://www.reddit.com/r/adventofcode/comments/7jgyrt/2017_day_13_solutions/
# permalink: https://www.reddit.com/r/adventofcode/comments/7jgyrt/2017_day_13_solutions/dr6bxce/

import itertools

filename = "13.in"
f = open(filename, "r")

lines = [line.split(': ') for line in f.read().splitlines()]

heights = {int(pos): int(height) for pos, height in lines}

def scanner(height, time):
    offset = time % ((height - 1) * 2)

    return 2 * (height - 1) - offset if offset > height - 1 else offset

part1 = sum(pos * heights[pos] for pos in heights if scanner(heights[pos], pos) == 0)

part2 = next(wait for wait in itertools.count() if not any(scanner(heights[pos], wait + pos) == 0 for pos in heights))
print(part2)
