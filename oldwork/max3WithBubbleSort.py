def bubbleSorter(array):
    arrayLength = len(array)
    for idx in range(arrayLength - 1):
        for idx2 in range(arrayLength - idx - 1):
            if array[idx2] > array[idx2 + 1]:
                array[idx2], array[idx2 + 1] = array[idx2 + 1], array[idx2]

    return array


numList = [5, 55, 12, 52, 33, -2, 56, 6, 52]
maxNum = numList[0]
for element in numList:
    if maxNum < element:
        maxNum = element

print(bubbleSorter(numList))
