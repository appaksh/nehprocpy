listInput = [58, 40, 36, 22, 11, 10, 5, 4]
for idx in range(int(len(listInput) / 2)):
    tempVar = listInput[idx]
    listInput[idx] = listInput[-idx - 1]
    listInput[-idx - 1] = tempVar

print(listInput)
