numList = [12, 52, 33, 21]
maxNum = numList[0]
for element in numList:
    if maxNum < element:
        maxNum = element

print(maxNum)
