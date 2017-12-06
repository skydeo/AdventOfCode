import timeit
sTime = timeit.default_timer()

testing = 0

if testing:
    banks = [0, 2, 7, 0]
else:
    with open('input.txt') as inputFile:
        banks = [int(i) for i in inputFile.read().splitlines()[0].split('\t')]

numBanks = len(banks)
banksHistory = []

rCycles = 0



def rebalanceBanks(banks, bankHistory):
    banksHistory.append(list(banks))
    
    bigBank = banks.index(max(banks))
    blocks = max(banks)

    if testing:
        print("Cycle {0}: Bank {1} is largest with {2} blocks.".format(rCycles, bigBank+1, blocks))

    banks[bigBank] = 0

    for cb in range(0,blocks):
        banks[(cb+1+bigBank)%numBanks] += 1
        blocks -= 1
    
    if testing:
        print("Banks rebalanced: {0}".format(banks))




while (banks not in banksHistory):

    rebalanceBanks(banks, banksHistory)

    rCycles += 1    

print("Detected infinite loop in {0} cycles.".format(rCycles))

magicBanks = list(banks)

rebalanceBanks(banks, banksHistory)
rCycles = 1

while banks != magicBanks:
    rebalanceBanks(banks, banksHistory)

    rCycles += 1

print("Detected recurrence in {0} cycles.".format(rCycles))


eTime = timeit.default_timer()
print("Completed in {0} seconds".format(round(eTime - sTime,5)))
