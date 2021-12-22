# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
from collections import defaultdict


n, m = list(map(int, input().split()))
defVal = defaultdict(list)
for idx in range(1, n + 1):
    defVal[input()].append(str(idx))

for rep in range(m):
    print(" ".join(defVal.get(input(), ["-1"])))
