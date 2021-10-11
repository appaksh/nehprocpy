def shellSort(array):
    gap = len(array) // 2
    while gap > 0:
        idx = 0
        gapData = gap
        while gapData < len(array):
            if array[idx] > array[gapData]:
                array[idx], array[gapData] = array[gapData], array[idx]
            gapData += 1
            idx += 1
        idx2 = idx
        while idx2 - gap > -1:
            if array[idx2 - gap] > array[idx2]:
                array[idx2 - gap], array[idx2] = array[idx2], array[idx2 - gap]
            idx2 -= 1
    gap //= 2

    return array


numList = [5, 55, 12, 52, 33, -2, 56, 6, 52]
maxNum = numList[0]
for element in numList:
    if maxNum < element:
        maxNum = element

print(shellSort(numList))
