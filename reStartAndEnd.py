import re

s = input()
k = input()
pattern = re.compile(k)
match = pattern.search(s)
if not match:
    print("(-1, -1)")
while match:
    print(f"({match.start()}, {match.end() - 1})")
    match = pattern.search(s, match.start() + 1)
