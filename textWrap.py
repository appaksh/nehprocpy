# https://www.hackerrank.com/challenges/text-wrap/problem
# Output Format
#
# Print the text wrapped paragraph.
#
# Sample Input 0
#
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Sample Output 0
#
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

def wrap(data, max_width):
    for c in range(0, len(data), max_width):
        print(data[c:c + max_width])
    return ""


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
