# Input Format
# A single line containing integer, .
#
# Constraints
#
# Output Format
# Print  lines as explained above.
#
# Sample Input
#
# 5
# Sample Output
#
# 1
# 22
# 333
# 4444

for i in range(1, int(input())):
    print(int(((10 ** i) // 9) * i))
