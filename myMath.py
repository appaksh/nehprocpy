# https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
#Output Format
#
# Print the three lines as explained above.
#
# Sample Input 0
#
# 3
# 2
# Sample Output 0
#
# 5
# 1
# 6


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    f = map(str, [(a + b), (a - b), (a * b)])
    print("\n".join(f))
