# https://www.hackerrank.com/challenges/compress-the-string/problem?h_r=internal-search
# Sample Input
#
# 1222311
# Sample Output
#
# (1, 1) (3, 2) (1, 3) (2, 1)

from itertools import groupby

# items = [('ak', 1), ('aa', 1), ('ka', 2), ('ts', 2), ('sc', 2), ('as', 3), ('sa', 3), ('ab', 3), ('va', 3)]
# ranksDict = {}
# for item in items:
#     name = item[0]
#     rank = item[1]
#     ranksDict.setdefault(rank, 0)
#     ranksDict[rank] += 1
#
# print(ranksDict)

items = [('ak', 1), ('aa', 1), ('ka', 2), ('ts', 2), ('sc', 2), ('as', 3), ('sa', 3), ('ab', 3), ('va', 3)]
lambdaFunc = lambda x: x[1]

print(*[(key, len(list(value))) for key, value in groupby(items, lambdaFunc)])

data = "11222334444"
dl = list(data)
print(*[(len(list(value)), key) for key, value in groupby(dl, lambda x: int(x))])
