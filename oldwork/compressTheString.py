from itertools import groupby

dls = list(input())
dli = list(map(int, dls))
print(*[(len(list(value)), key) for key, value in groupby(dli, lambda x: x)])
