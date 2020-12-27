# https://www.hackerrank.com/challenges/piling-up/problem
# Output Format
#
# For each test case, output a single line containing either "Yes" or "No" without the quotes.
#
# Sample Input
#
# 2
# 6
# 4 3 2 1 3 4
# 3
# 1 3 2
# Sample Output
#
# Yes
# No

for x in range(int(input())):
    mi = int(input())
    ml = list(map(int, input().split()))
    i = 0
    while i < len(ml) - 1 and ml[i] >= ml[i + 1]:
        i += 1
    while i < len(ml) - 1 and ml[i] <= ml[i + 1]:
        i += 1
    print("Yes" if i == len(ml) - 1 else "No")
