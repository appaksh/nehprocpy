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

K, M = list(map(int, input().split()))
N = list(map(int, input().split()[1:]) for _ in range(K))

prodN = list(product(*N))


def f1(array):
    return sum(y ** 2 for y in array) % M


resultArray = list(map(f1, prodN))
print(max(resultArray))
