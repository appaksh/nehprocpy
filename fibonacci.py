first = 0
second = 1
fib = int(input("How many numbers do you want? "))
print(first)
print(second)

for x in range(int(fib) - 2):
    nextNum = first + second
    first = second
    second = nextNum
    print(nextNum)

print("--------------------------------------------------------------------------------------------------------------")
print(f'({fib} fibonacci numbers have been printed.) ')
