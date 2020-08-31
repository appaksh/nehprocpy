# https://www.hackerrank.com/challenges/word-order/problem?h_r=internal-search

from collections import defaultdict

wordDict = defaultdict(int)
wordCount = int(input())
for myNumber in range(wordCount):
    myString = input()
    wordDict[myString] += 1

length = len(wordDict)
print(length)
print(*wordDict.values())
