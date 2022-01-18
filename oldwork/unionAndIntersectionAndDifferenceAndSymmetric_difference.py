# https://www.hackerrank.com/challenges/py-set-union/problem
# Union
engSub, engStud = input(), set(input().split())
frenSub, frenStud = input(), set(input().split())
print(len(engStud.union(frenStud)))

# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=false
# intersection
engSub2, engStud2 = input(), set(input().split())
frenSub2, frenStud2 = input(), set(input().split())
print(len(engStud2.intersection(frenStud2)))

# https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=false
# difference
engSub3, engStud3 = input(), set(input().split())
frenSub3, frenStud3 = input(), set(input().split())
print(len(engStud3.difference(frenStud3)))

# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=false
# symmetric_difference
engSub4, engStud4 = input(), set(input().split())
frenSub4, frenStud4 = input(), set(input().split())
print(len(engStud4.symmetric_difference(frenStud4)))
