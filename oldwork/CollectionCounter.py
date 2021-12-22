from collections import Counter


intList = int(input())
availableShoeSizes = Counter(map(int, input().split()))
totalMoney = []
numOfCustomers = int(input())
for element in range(numOfCustomers):
    shoeSize, shoePrice = list(map(int, input().split()))
    if availableShoeSizes[shoeSize] > 0:
        totalMoney.append(shoePrice)
        availableShoeSizes.subtract(Counter([shoeSize]))
    else:
        pass

print(sum(totalMoney))
