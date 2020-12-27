import re

n, m = list(map(int, input().split()[:2]))
inputMatrix = []

for dimensions in range(n):
    inputMatrix.append(list(input())[:m])

allStr = "".join("".join(x) for x in list(zip(*inputMatrix)))
print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", allStr))
