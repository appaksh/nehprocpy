# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
def performSetOperation(dataSet, operation, element) -> set:
    try:
        # if operation == "pop":
        #     dataSet.pop()
        # elif operation == "remove":
        #     dataSet.remove(element)
        # elif operation == "discard":
        #     dataSet.discard(element)
        func = getattr(set, operation)
        func(dataSet, element)
    except BaseException as error:
        try:
            func(dataSet)
        except AttributeError:
            print(f'Operation Name: {operation}, error: {error}')
        pass
    return dataSet


setSum = int(input())
infoSet = set(map(int, input().split()))
otherOperationLen = int(input())
for repetition in range(otherOperationLen):
    data = input().split()
    operationName = data[0]
    dataElement = int(data[1]) if len(data) > 1 else None
    infoSet = performSetOperation(infoSet, operationName.strip(), dataElement)

print(sum(infoSet))
