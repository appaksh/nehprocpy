# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=false
from itertools import combinations_with_replacement

inputList = input().split()
data = sorted(list((inputList[0])))
lens = int(inputList[1])
I = 1
for x in range(I):
    com = ["".join(myTuple)for myTuple in list(combinations_with_replacement(data, lens))]
    print(*com, sep="\n")