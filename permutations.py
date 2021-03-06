# https://www.hackerrank.com/challenges/itertools-permutations/problem
# Output Format
#
# Print the permutations of the string  on separate lines.
#
# Sample Input
#
# HACK 2
# Sample Output
#
# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH

from itertools import permutations

s,k = input().split()
for x in permutations(sorted(s),int(k)):
    print("".join(x))

