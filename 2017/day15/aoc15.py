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



a_factor = 16807
b_factor = 48271

divisor = 2147483647

values = [(starting_value_a, starting_value_b)]
binary = []
iterations = 40000000
judge = 0

def generate_values(previous_values):
    a = previous_values[0]
    b = previous_values[1]

    a = (a * a_factor) - (math.floor((a * a_factor) / divisor) * divisor)
    b = (b * b_factor) - (math.floor((b * b_factor) / divisor) * divisor)

    return (a, b)

def generate_binary(int_values):
    a = bin(int_values[0])[2:].zfill(32)[-16:]
    b = bin(int_values[1])[2:].zfill(32)[-16:]

    return (a, b)

for i in range(0,iterations):
    values += [generate_values(values[-1])]
    binary += [generate_binary(values[-1])]
    if binary[-1][0] == binary[-1][1]:
        judge += 1

# Remove starting values
values = values[1:]

print('The were {0} matches in {1} iterations.'.format(judge, iterations))

eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
