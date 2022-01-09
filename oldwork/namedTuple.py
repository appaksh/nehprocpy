from collections import namedtuple


numOfStudents = int(input())
entries = input().split()
total = 0
classmates = namedtuple("classmates", entries)
for i in range(numOfStudents):
    student = classmates(*input().split())
    total += int(student.MARKS)
print('{:.2f}'.format(total/numOfStudents))
