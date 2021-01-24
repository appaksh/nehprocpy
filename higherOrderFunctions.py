# Input will have list of Students
# Each Student will have name, grade, sport
# You should
#  print students in the following format
#   student <name in Capitals> with grade <grade in upper case> plays <sport in capitals>
#  before printing you should be able apply one of these filters
#  1. grade filter, which filters for students with Grade "A"
#  2. sport filter, which filters for students with sport "running"

# Return list of grade _ students
def gradeFilter(allStudents, filterValue):
    return list([student for student in allStudents if student[1].upper() == filterValue.upper()])

# Return list of sport _ students
def sportFilter(allStudents, filterValue):
    return list([student for student in allStudents if student[2].upper() == filterValue.upper()])


def printStudentsInfo(students, filterFunc, filterValue):
    filteredStudents = filterFunc(students, filterValue)
    for student in filteredStudents:
        print(f'student {student[0].capitalize()} with grade {student[1].upper()} plays {student[2].capitalize()}')


myStudents = [
    ["aakash", "a", "basketball"],
    ["kaushik", "b", "tennis"],
    ["siri", "c", "volleyball"],
]

printStudentsInfo(myStudents, gradeFilter, "b")
printStudentsInfo(myStudents, sportFilter, "volleyball")
