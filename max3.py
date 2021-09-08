numList = [12, 52, 33, 21, 56]
maxNum = numList[0]
for element in numList:
    # maxNum = element if element > maxNum else maxNum
    if maxNum < element:
        maxNum = element

print(maxNum)
