# https://www.hackerrank.com/challenges/list-comprehensions/submissions/code/171762875



# (x, y, z) = [1, 1, 2]
# n = 3
#
# for i in range(x + 1):
#     for j in range(y + 1):
#         for k in range(z + 1):
#             if (i + j + k) != n:
#                 print([i, j, k])
# var = [[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1) if (a + b + c) != n]
# print(var)
#
#






# def bubbleSort(myList):
#     lengthOfList = len(myList)
#
#     # Traverse through all array elements
#     for passedNumber in range(lengthOfList - 1):
#         # range(n) also work but outer loop will repeat one time more than needed.
#
#         # Last i elements are already in place
#         for condition in range(0, lengthOfList - passedNumber - 1):
#
#             # traverse the array from 0 to n-i-1
#             # Swap if the element found is greater
#             # than the next element
#             if myList[condition] > myList[condition + 1]:
#                 myList[condition], myList[condition + 1] = myList[condition + 1], myList[condition]
#
#             # Driver code to test above
#
#
# myInput = input("What number(s) do you want sorted: ").split(" ")
# # myList = list(map(int, myInput))
#
#
# try:
#     bubbleSort(myList)
#     print(myList)
# except RuntimeError:
#     print("Error ")
#
