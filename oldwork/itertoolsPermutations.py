import itertools


data, size = input().split()
permutationsList = itertools.permutations(sorted(data), int(size))
for item in permutationsList:
    print("".join(item))
