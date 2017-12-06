import timeit
sTime = timeit.default_timer()

testing = 0

if testing:
    banks = [0, 2, 7, 0]
else:
    with open('input.txt') as inputFile:
        banks = [int(i) for i in inputFile.read().splitlines()[0].split('\t')]

numBanks = len(banks)
bankHistory = []
rCycles = 0

while banks not in bankHistory:
    bankHistory.append(list(banks))
    
    
    bigBank = banks.index(max(banks))
    blocks = max(banks)

    if testing:
        print("Bank {0} is largest with {1} blocks.".format(bigBank+1, blocks))

    banks[bigBank] = 0

    for cb in range(0,blocks):
        banks[(cb+1+bigBank)%numBanks] += 1
        blocks -= 1
    
    if testing:
        print("Banks rebalanced: {0}".format(banks))

    
    rCycles += 1

print("Detected infinite loop in {0} cycles.".format(rCycles))

eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))