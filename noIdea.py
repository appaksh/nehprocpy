# No Idea!
# Input Format
#
# The first line contains integers  and  separated by a space.
# The second line contains  integers, the elements of the array.
# The third and fourth lines contain  integers,  and , respectively.
#
# Output Format
#
# Output a single integer, your total happiness.
#
# Sample Input
#
# 3 2
# 1 5 3
# 3 1
# 5 7
# Sample Output
#
# 1

array = input().split()
m = input().split()
a = set(input().split())
b = set(input().split())
print(sum([(i in a) - (i in b) for i in m]))
