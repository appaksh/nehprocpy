import re

for myInput in range(int(input())):
    myValidMatches = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())
    if myValidMatches:
        print("\n".join(myValidMatches))
