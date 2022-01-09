# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
from collections import defaultdict


nSize, mSize = list(map(int, input().split()))
defDict = defaultdict(list)
for idx in range(1, nSize + 1):
    defDict[input()].append(str(idx))

for rep in range(mSize):
    print(" ".join(defDict.get(input(), ["-1"])))
