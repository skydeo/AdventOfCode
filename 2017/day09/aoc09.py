import timeit
import numpy as np
sTime = timeit.default_timer()

testing = 0

if testing:
    # stream = "{{<a>},{<!a>},{<a>},{<aba>}}"
    # stream = "{{{}}}"
    # stream = "{{{!a!b<ab>ab}}}"
    stream = "{{<a!>},{<a!>},{<a!>},{<ab>}}"
    
else:
    filename = "input.txt"
    with open(filename) as inputFile:
        stream = inputFile.read()


def cleanStream(input):
    if testing:
        print("Input stream:   {0}".format(input))

    i = 0
    while i < len(input):
        char = input[i]
        if char == "!":
            input = input[:i] + input[i+2:]
        else:
            i += 1

    if testing:
        print("Cleaned stream: {0}".format(input))
    
    return input
    

def groupCount(input):
    groupScore = 0
    removedChars = 0

    if testing:
        print(input)
    
    i = 0
    ob = 0
    while i < len(input):
        char = input[i]
        
        if testing:
            print("char: {0}, pos: {1}".format(char, i))

        if char == "<":
            closingSign = input[i+1:].find(">")
            i += closingSign
            removedChars += closingSign
        elif char == "{":
            ob += 1
        elif char == "}" and ob > 0:
            groupScore += ob            
            ob -= 1
        
        i += 1
        
    return groupScore, removedChars

stream = cleanStream(stream)
groupScore, removedChars = groupCount(stream)

print("Group score: {0}\tRemoved chars: {1}".format(groupScore, removedChars))


eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
