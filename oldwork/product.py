# Input Format
#
# The first line contains the space separated elements of list .
# The second line contains the space separated elements of list .
#
# Both lists have no duplicate integer elements.
#
# Constraints
#
#
#
# Output Format
#
# Output the space separated tuples of the cartesian product.
#
# Sample Input
#
#  1 2
#  3 4
# Sample Output
#
#  (1, 3) (1, 4) (2, 3) (2, 4)

from itertools import product

an1 = list(map(int, input().split()))
an2 = list(map(int, input().split()))
af = product(an1, an2)

print(*af)

# print("Menu: ")
# print([f"{arrayMenu[0]} - {arrayMenu[1]} " for arrayMenu in arrayDishes])
