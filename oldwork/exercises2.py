# Exercise 1: Print ‘Hello World’

print('Hello World')

# Exercise 2: Say Hello to user, Expected, ‘Hello John’, “Hello Mary” etc…

userInput = input('Enter name: ')
print(f'Hello {userInput}')

# Exercise 3: Take two numbers from user, print the sum.

num1 = int(input('Enter number: '))
num2 = int(input('Enter number: '))

print(num1 + num2)

# Exercise 4: Print even numbers below 100.

num = 0
for idx in range(50):
    num += 2
    print(num)

# Exercise 5: Print odd numbers below 50, in descending order

num2 = 50
for idx in range(25):
    num2 -= 2
    print(num2)

# Exercise 6: Print prime numbers below 100.

numIdx = 2
newNum = numIdx + 1
print(newNum)
for idx in range(48):
    newNum += 2
    print(newNum)

# Exercise 7: Take two numbers from user, and print the biggest.

numInput = input('Enter 2 numbers: ').split(' ')

if numInput[0] < numInput[1]:
    print(numInput[1])
else:
    print(numInput[1])

# Exercise 8: Take three numbers from user, and print the biggest.

intInput = numInput = input('Enter 3 numbers: ').split(' ')

if numInput[0] < numInput[1]:
    if intInput[1] < intInput[2]:
        print(intInput[2])
    else:
        print(intInput[1])
else:
    if intInput[0] < intInput[2]:
        print(intInput[2])
    else:
        print(intInput[0])

# Exercise 9: Ask the user for a number, to pick the color from the list. Blue, Green, Orange, Red and print the color.

userInt = int(input('Enter a number: '))
colorList = ['Blue', 'Green', 'Orange', 'Red']

if userInt == 1:
    print(colorList[0])

if userInt == 2:
    print(colorList[1])

if userInt == 3:
    print(colorList[2])

if userInt == 4:
    print(colorList[3])
