# https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true
from collections import deque

deque = deque()
for num in range(int(input())):
    a = input().split()
    if a[0] == "append":
        deque.append(a[1])
    elif a[0] == "pop":
        deque.pop()
    elif a[0] == "appendleft":
        deque.appendleft(a[1])
    elif a[0] == "popleft":
        deque.popleft()

print(*deque)
