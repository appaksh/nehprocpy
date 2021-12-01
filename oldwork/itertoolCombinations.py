from itertools import combinations

dataString, numberPerLine = input().split()

for repetition in range(1, int(numberPerLine) + 1):
    for combinedData in combinations(sorted(dataString), repetition):
        print(''.join(combinedData))
