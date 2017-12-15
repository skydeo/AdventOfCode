import timeit
import math
sTime = timeit.default_timer()

testing = 0

if testing:
    starting_value_a = 65
    starting_value_b = 8921
else:
    starting_value_a = 873
    starting_value_b = 583

divisor = 2147483647    

a_factor = 16807
b_factor = 48271

a_multiple = 4
b_multiple = 8

iterations_a = 40000000
iterations_b = 5000000

def a_generator(a = starting_value_a):
    while True:
        a = (a * a_factor) - (math.floor((a * a_factor) / divisor) * divisor)
        yield a

def b_generator(b = starting_value_b):
    while True:
        b = (b * b_factor) - (math.floor((b * b_factor) / divisor) * divisor)
        yield b

def a_generator_multiple(a = starting_value_a):
    while True:
        a = (a * a_factor) - (math.floor((a * a_factor) / divisor) * divisor)
        if (a % a_multiple) == 0:
            yield a

def b_generator_multiple(b = starting_value_b):
    while True:
        b = (b * b_factor) - (math.floor((b * b_factor) / divisor) * divisor)
        if (b % b_multiple) == 0:
            yield b

def judge(A, B, i):
    c = 0
    for _ in range(i):
        if next(A) & 0xFFFF == next(B) & 0xFFFF:
            c += 1
    return c

count = judge(a_generator(), b_generator(), iterations_a)
print('Part 1: The were {0} matches in {1} iterations.'.format(count, iterations_a))

count = judge(a_generator_multiple(), b_generator_multiple(), iterations_b)
print('Part 2: The were {0} matches in {1} iterations.'.format(count, iterations_b))

eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
