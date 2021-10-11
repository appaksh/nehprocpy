def insertionSort(array):
    for increment in range(1, len(array)):
        idx = increment - 1
        while idx > 0 and array[idx] < array[idx - 1]:
            array[idx], array[idx - 1] = array[idx - 1], array[idx]
            idx -= 1
    return array


numList = [5, 55, 12, 52, 33, -2, 56, 6, 52]
maxNum = numList[0]
for element in numList:
    if maxNum < element:
        maxNum = element

print(insertionSort(numList))
