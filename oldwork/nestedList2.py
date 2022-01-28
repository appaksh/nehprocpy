# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=false

students = []
gradesSet = set()
for rep in range(int(input())):
    student = [input(), float(input())]
    students.append(student)
    gradesSet.add(student[1])

runnerUpGrade = sorted(list(gradesSet))[1]
runnerUpStudentNames = [student[0] for student in students if student[1] == runnerUpGrade]

sortedNames = sorted(runnerUpStudentNames)
print("\n".join(sortedNames))
