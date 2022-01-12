# https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=false
testCases = int(input())
for rep in range(testCases):
    cubeCount = int(input())
    cubes = list(map(int, input().split()))
    cubeLen = len(cubes)
    idx = 0
    while idx < cubeLen - 1 and cubes[idx] >= cubes[idx + 1]:
        idx += 1

    while idx < cubeLen - 1 and cubes[idx] <= cubes[idx + 1]:
        idx += 1

    print("Yes" if idx == cubeLen - 1 else "No")
