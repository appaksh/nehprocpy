if __name__ == '__main__':
    dataList = []
    N = int(input())

    for x in range(N):
        commandStart = list(input().split(" "))
        commandWords = commandStart[0]

        if commandWords == "insert":
            index = int(commandStart[1])
            value = int(commandStart[2])
            try:
                dataList.insert(index, value)
            except ValueError:
                continue

        if commandWords == "print":
            print(dataList)

        if commandWords == "remove":
            value = int(commandStart[1])
            try:
                dataList.remove(value)
            except ValueError:
                continue

        if commandWords == "append":
            value = int(commandStart[1])
            try:
                dataList.append(value)
            except ValueError:
                continue

        if commandWords == "sort":
            value = commandStart[0]
            try:
                dataList.sort()
            except ValueError:
                continue

        if commandWords == "pop":
            value = commandStart[-1]
            try:
                dataList.pop()
            except ValueError:
                continue

        if commandWords == "reverse":
            value = commandStart[0]
            try:
                dataList.reverse()
            except ValueError:
                continue
