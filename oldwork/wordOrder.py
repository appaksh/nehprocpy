# https://www.hackerrank.com/challenges/word-order/problem

# wordDict = defaultdict(int)
# wordCount = int(input())
# for myNumber in wordCount:
#     myString = input()
#     wordDict[myString] += 1
#     # if wordDict.keys().__contains__(myString):
#     #     wordDict[myString] += 1
#     # else:
#     #     wordDict[myString] = 1
# print(*wordDict.values())

from collections import defaultdict

wordDict = defaultdict(int)
wordCount = int(input())
x = range(wordCount)
for myNumber in x:
    myString = input()
    wordDict[myString] += 1

length = len(wordDict)
print(length)
print(*wordDict.values())
