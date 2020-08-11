# print("Hello, World! ")
# def swapCase(data):
#     return data.swapcase()
#
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
# print('''{0}
# {1} '''.format(a//b, a/b))
#
# word = input("Write any letter(s): ")
# result = swapCase(word)
# print(result)
#
# import math
# import os
# import random
# import re
# import sys
#
# if __name__ == '__main__':
#
#     n = int(input("Enter the Number: ").strip())
#
#     if n % 2 == 1:
#         print("Weird ")
#     elif 2 <= n <= 5:
#         print("Not Weird ")
#     elif 6 <= n <= 20:
#         print("Weird ")
#     else:
#         print("Not Weird ")
#
#
# def print_full_name(a, b):
#     print("Hello {firstName} {lastName}! You just delved into python.".format(firstName=a, lastName=b))
#
#
# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)
#
#
# def split_and_join(line):
#     # write your code here
#     lineList = line.split(" ")
#     joinedLineList = "-".join(lineList)
#     return joinedLineList
#
#
# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)
#
#
# def runnerUp(myArr):
#     newList = []
#     counter = 0
#     while myArr:
#         highest = myArr[0]
#         for x in myArr:
#             counter = counter + 1
#             if x > highest:
#                 highest = x
#         if highest not in newList:
#             newList.append(highest)
#         myArr.remove(highest)
#
#     print("runnerup() - The total operations are : ", counter)
#     if len(newList) >= 2:
#         return newList[1]
#     else:
#         return newList[0]
#
# def runnerUp2(myArr):
#     counter = 0
#     highest = myArr[0]
#     lowest = myArr[0]
#     for x in myArr:
#         counter = counter + 1
#         if x > highest:
#             highest = x
#         if x < lowest:
#             lowest = x
#
#     runnerup = lowest
#     for x in myArr:
#         counter = counter + 1
#         if (x > runnerup) and (x < highest):
#             runnerup = x
#
#     print("runnerup2() - The total operations are: ", counter)
#     return runnerup
#
#
# if __name__ == '__main__':
#     n = int(input("How many number(s) do you want?: "))
#     arr = list(map(int, input("What are/is the number(s): ").split(" ")))
# # first =
# funcVar = runnerUp2(arr)
# functionVariable = runnerUp(arr)
#
# print(f"runnerup() -  The runner up score is: {functionVariable} ")
# print(f"runnerup2() - The runner up score is: {funcVar} ")
# if __name__ == '__main__':
#     dataList = []
#     N = int(input("How many command(s) do you want: "))
#
#     for x in range(N):
#         commandStart = list(input("Enter command(s): ").split(" "))
#         commandWords = commandStart[0]
#
#         if commandWords == "insert":
#             index = int(commandStart[1])
#             value = int(commandStart[2])
#             try:
#                 dataList.insert(index, value)
#             except ValueError:
#                 continue
#
#         if commandWords == "print":
#             print(dataList)
#
#         if commandWords == "remove":
#             value = int(commandStart[1])
#             try:
#                 dataList.remove(value)
#             except ValueError:
#                 continue
#
#         if commandWords == "append":
#             value = int(commandStart[1])
#             try:
#                 dataList.append(value)
#             except ValueError:
#                 continue
#
#         if commandWords == "sort":
#             value = commandStart[0]
#             try:
#                 dataList.sort()
#             except ValueError:
#                 continue
#
#         if commandWords == "pop":
#             value = commandStart[-1]
#             try:
#                 dataList.pop()
#             except ValueError:
#                 continue
#
#         if commandWords == "reverse":
#             value = commandStart[0]
#             try:
#                 dataList.reverse()
#             except ValueError:
#                 continue
