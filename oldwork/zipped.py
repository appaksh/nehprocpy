marksList = []
[marksList.append(list(map(float, input().split()))) for rep in range(list(map(int, input().split()))[1])]
[print(sum(result) / len(result)) for result in zip(*marksList)]
