studentsCount = int(input())
studentDict = {}
for rep in range(studentsCount):
    line = input().split()
    name = line[0]
    marks = list(map(float, line[1:]))
    studentDict[name] = marks

queryName = input()
values = studentDict.get(queryName)
if values is None:
    print('Query name not found.')
else:
    print('{:.2f}'.format(sum(values)/len(values)))
