# https://www.hackerrank.com/challenges/nested-list/submissions/code/172584509


# myList = []
# if __name__ == '__main__':
#     for _ in range(int(input("How many: "))):
#         name = str(input("Name(s): "))
#         score = float(input("Scores(s): "))
#         studentInfo = [name, score] 
#         myList.append(studentInfo)
#
# print(myList)
# scoreList = []
#
# for newList in myList:
#     if (scoreList.count(newList[1])) == 0:
#         scoreList.append(newList[1])
#
# scoreLength = len(scoreList)
# if scoreLength >= 1:
#     secondScore = scoreList[1]
# else:
#     secondScore = scoreList[0]
#
# nameList = []
# for student in myList:
#     if student[1] == secondScore:
#         nameList.append(student[0])
#     else:
#         pass
# nameList.sort()
#
# for name in nameList:
#     print(name)
#
#
# def count_substring(string, sub_string):
#     lN = len(string)
#     l2 = len(sub_string)
#     counts = 0
#     for idx in range(lN - l2 + 1):
#         stringIdx = string[idx: idx + l2]
#         if stringIdx == sub_string:
#             counts = counts + 1
#     return counts
#
#
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)

x = str(input("Roses are: "))
y = str(input("Violets are: "))
z = str(input("I am a: "))
b = str(input("My name is: "))
a = f'''Roses are: {x}, Violets are: {y}, I am a: {z}. 


To,
{b} '''
print(a)
print('''
''')

SOS = "I got your info. HAHAHAHAHAHAHAHAHAAAAAAA!!!!!!!! "
dots = "... "
print(SOS)
print(dots)
