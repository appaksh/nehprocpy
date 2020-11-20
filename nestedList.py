# https://www.hackerrank.com/challenges/nested-list/problem?h_r=internal-search
# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.
#
# Sample Input 0
#
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0
#
# Berry
# Harry

myList = []

for n in range(int(input())):
    myList.append([input(), float(input())])

secondLowest = sorted(list(set(score for (name, score) in myList)))[1]

print("\n".join(sorted(list(name for (name, score) in myList if score == secondLowest))))
