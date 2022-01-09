from collections import Counter

inp = input()
for letter in Counter(sorted(inp)).most_common(3):
    print(*letter)
