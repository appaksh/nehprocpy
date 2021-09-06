first = 0
second: int = 1
nextNum = first + second
fib = int(input("How many numbers do you want? "))

for x in range(int(fib)):
    nextNum = first + second
    first = second
    second = nextNum
    print(nextNum)

print(f'{fib} fibonacci numbers have been printed. ')
