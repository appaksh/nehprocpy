numberOfTestCases = int(input())
for repetition in range(numberOfTestCases):
    elementANum = input()
    elementA = set(input().split())
    elementBNum = input()
    elementB = set(input().split())
    print(elementA.issubset(elementB))
