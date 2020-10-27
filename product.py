from itertools import product

an1 = list(map(int, input().split()))
an2 = list(map(int, input().split()))
af = product(an1, an2)

print(*af)

# print("Menu: ")
# print([f"{arrayMenu[0]} - {arrayMenu[1]} " for arrayMenu in arrayDishes])
