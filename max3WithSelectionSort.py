def selectionSort(data):
    for idx in range(len(data)):
        minimumIdx = idx
        for idx2 in range(idx, len(data)):
            if data[minimumIdx] > data[idx2]:
                minimumIdx = idx2
        data[idx], data[minimumIdx] = data[minimumIdx], data[idx]

    return data


numList = [5, 55, 12, 52, 33, -2, 56, 6, 52]
maxNum = numList[0]
for element in numList:
    if maxNum < element:
        maxNum = element

print(selectionSort(numList))
