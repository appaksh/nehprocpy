def isSuperSet(set1, set2) -> bool:
    if set1.issuperset(set2) and not set2.issuperset(set1):
        return not set2.issuperset(set1)
    else:
        return False


result = True
setA = set(input().split())
otherSetCount = int(input())
for repetition in range(otherSetCount):
    otherSet = set(input().split())
    if result and not isSuperSet(setA, otherSet):
        result = False

print(result)

