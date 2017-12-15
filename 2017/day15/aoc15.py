import timeit
import math
sTime = timeit.default_timer()

testing = 0

part1 = 1
part2 = 1

if testing:
    starting_value_a = 65
    starting_value_b = 8921
else:
    starting_value_a = 873
    starting_value_b = 583

a_factor = 16807
b_factor = 48271

a_multiple = 4
b_multiple = 8

divisor = 2147483647

values = (starting_value_a, starting_value_b)
iterations = 5000000
judge = 0

def generate_values(previous_values):
    a = (previous_values[0] * a_factor) - (math.floor((previous_values[0] * a_factor) / divisor) * divisor)
    b = (previous_values[1] * b_factor) - (math.floor((previous_values[1] * b_factor) / divisor) * divisor)

    return (a, b)

def generate_values_multiple(previous_values):
    a = previous_values[0]
    b = previous_values[1]
    
    while True:
        a = (a * a_factor) - (math.floor((a * a_factor) / divisor) * divisor)
        if (a % a_multiple == 0):
            break
    while True:
        b = (b * b_factor) - (math.floor((b * b_factor) / divisor) * divisor)
        if (b % b_multiple == 0):
            break

    return (a, b)

def generate_binary(int_values):
    a = bin(int_values[0]).zfill(16)[-16:]
    b = bin(int_values[1]).zfill(16)[-16:]

    return (a, b)

if part1:
    for i in range(0,iterations):
        values = generate_values(values)
        binary = generate_binary(values)
        if binary[0] == binary[1]:
            judge += 1

    # Remove starting values
    values = values[1:]

    print('Part 1: The were {0} matches in {1} iterations.'.format(judge, iterations))

if part2:
    for i in range(0,iterations):
        # if (i % 100000) == 0:
            # print('Iteration: {0}'.format(i))
        values = generate_values_multiple(values)
        binary = generate_binary(values)
        if binary[0] == binary[1]:
            judge += 1

    # Remove starting values
    values = values[1:]

    print('Part 2: The were {0} matches in {1} iterations.'.format(judge, iterations))


eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
