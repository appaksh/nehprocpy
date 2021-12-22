from itertools import combinations

lenOfString, strElements, numOfIndices = input(), input().split(), int(input())
combinations = list(combinations(strElements, numOfIndices))
combinationCheck = [combinationList for combinationList in combinations if 'a' in combinationList]
print(len(combinationCheck)/len(combinations))
