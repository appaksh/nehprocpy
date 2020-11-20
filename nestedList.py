myList = []

for n in range(int(input())):
    myList.append([input(), float(input())])

secondLowest = sorted(list(set(score for (name, score) in myList)))[1]

print("\n".join(sorted(list(name for (name, score) in myList if score == secondLowest))))

# list(name for (name, score) in myList if score == secondLowest])
# [
# ['Harry', 37.21],
# ['Berry', 37.21],
# ['Tina', 37.2],
# ['Akriti', 41],
# ['Harsh', 39]
# ]