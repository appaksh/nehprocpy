# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=false
from collections import namedtuple


numOfStud = int(input())
columnNames = input()
Student = namedtuple("Student", columnNames)
totalMarks = 0
for rep in range(numOfStud):
    st1 = Student(*input().split())
    totalMarks = totalMarks + int(st1.MARKS)

avg = totalMarks/numOfStud
print("{:.2f}".format(avg))


