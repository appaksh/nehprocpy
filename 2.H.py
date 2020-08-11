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
