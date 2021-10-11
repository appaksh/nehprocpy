# https://www.hackerrank.com/challenges/most-commons/problem?h_r=internal-search
# Sample Input 0
#
# aabbbccde
# Sample Output 0
#
# b 3
# a 2
# c 2
# Explanation 0

# !/bin/python3


if __name__ == '__main__':
    s = input()
from itertools import groupby

ls = list(s.lower())
# print(ls)
ms = "--------------------------------------------------------------------------------------------------------------- "
# print(ms)
ls.sort()
sls = "".join(ls)
# print(sls)
# print(ms)

letterGroups = [(key, len(list(value))) for key, value in groupby(ls, lambda x: x)]
letterGroups.sort(key=lambda x: x[1], reverse=True)
# print(letterGroups)

for x in range(3):
    item = letterGroups[x]
    print(*item)
