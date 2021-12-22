# https://www.hackerrank.com/challenges/maximize-it/problem
#
# You have to pick one element from each list so that the value from the equation below is maximized:
# Output a single integer denoting the value .
#
# Sample Input
#
# 3 1000
# 2 5 4
# 3 7 8 9
# 5 5 7 8 9 10
# Sample Output
#
# 206

from itertools import product
from itertools import repeat


def dataSum(array, modVar) -> int:
    return sum(element ** 2 for element in array) % modVar


listResult = []
intInp1, intInp2 = list(map(int, input().split()))
for repetition in range(intInp1):
    elementNumProduct = set(map(int, input().split()[1:]))
    listResult.append(elementNumProduct)

prodN = list(product(*listResult))

resultArray = list(map(dataSum, prodN, repeat(intInp2)))
print(max(resultArray))
