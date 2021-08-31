if __name__ == '__main__':
    dataList = []
    inputLine = int(input())

    for x in range(inputLine):
        commandStart = list(input().split(" "))
        commandWords = commandStart[0]

        if commandWords == "insert":
            index = int(commandStart[1])
            value = int(commandStart[2])
            try:
                dataList.insert(index, value)
            except ValueError:
                continue

        elif commandWords == "print":
            print(dataList)

        elif commandWords == "remove":
            value = int(commandStart[1])
            try:
                dataList.remove(value)
            except ValueError:
                continue

        elif commandWords == "append":
            value = int(commandStart[1])
            try:
                dataList.append(value)
            except ValueError:
                continue

        elif commandWords == "sort":
            value = commandStart[0]
            try:
                dataList.sort()
            except ValueError:
                continue

        elif commandWords == "pop":
            value = commandStart[-1]
            try:
                dataList.pop()
            except ValueError:
                continue

        elif commandWords == "reverse":
            value = commandStart[0]
            try:
                dataList.reverse()
            except ValueError:
                continue
