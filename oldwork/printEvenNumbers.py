start, end = map(int, input().split())
print(*[num for num in range(start, end + 1) if num % 2 == 0])
