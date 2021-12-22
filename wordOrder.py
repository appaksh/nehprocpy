from collections import defaultdict

intDict = defaultdict(lambda: 0)
for line in range(int(input())):
    word = input()
    intDict[word] = intDict[word] + 1
print(len(intDict))
print(*intDict.values())
