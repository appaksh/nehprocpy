# https://www.hackerrank.com/challenges/designer-door-mat/problem
#
# Sample Designs
#
#     Size: 7 x 21
#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------

di = list(map(int, input().split()))
rows = di[0]
columns = di[1]
# print the top half
for i in range(int(rows / 2)):
    printString = ".|." * ((i * 2) + 1)
    print(printString.center(columns, "-"))

# print the middle line
mid = 'WELCOME'.center(columns, '-')
print(mid)

# print the bottom half
for i in reversed(range(int(rows / 2))):
    printString = ".|." * ((i * 2) + 1)
    print(printString.center(columns, "-"))
