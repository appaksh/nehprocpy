from collections import OrderedDict


ordDict = OrderedDict()
intInp = int(input())
for rep in range(intInp):
    inputData = input().split()
    itemName = " ".join(inputData[:-1])
    netPrice = int(inputData[-1])
    ordDict[itemName] = ordDict.get(itemName, 0) + netPrice

for key, value in ordDict.items():
    print(f'{key} {value}')
