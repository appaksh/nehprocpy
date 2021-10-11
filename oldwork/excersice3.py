# https://www.justlearnpython.com/docs/exercises/list-exercises/

# Exercise 1: Given 2D array calculate the sum of diagonal elements.
#
# Ex: [[1,3,5],[1,4,6],[7,6,9] => sum of 1 + 4 + 9 => 14

sumList = [[1, 3, 5], [1, 4, 6], [7, 6, 9]]
x = sumList[0][0]
y = sumList[1][1]
z = sumList[2][2]
print(x + y + z)

# Exercise 2: From given list
#
# gadgets = [“Mobile”, “Laptop”, 100, “Camera”, 310.28, “Speakers”, 27.00,
# “Television”, 1000, “Laptop Case”, “Camera Lens”]
#
# a)create separate lists of strings and numbers.
#
# b)Sort the strings list in ascending order
#
# c)Sort the strings list in descending order
#
# d)Sort the number list from lowest to highest
#
# e)Sort the number list from highest to lowest

gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00, "Television", 1000, "Laptop Case",
           "Camera Lens"]

strItems = []
numItems = []

for item in gadgets:

    if isinstance(item, str):
        strItems.append(item)

    if isinstance(item, int) or isinstance(item, float):
        numItems.append(item)

print(sorted(strItems))
print(sorted(strItems, reverse=True))
print(sorted(numItems))
print(sorted(numItems, reverse=True))

# Exercise 3: Get first, second best scores from the list.
#
# List may contain duplicates.
#
# Ex: [86,86,85,85,85,83,23,45,84,1,2,0] => should get 86, 85

numList = [86, 86, 85, 85, 85, 83, 23, 45, 84, 1, 2, 0]
setNum = set(numList)
sortedNumList = sorted(setNum, reverse=True)
print(f'{sortedNumList[0]}, {sortedNumList[1]}')
