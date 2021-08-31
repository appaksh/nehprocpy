# https://www.justlearnpython.com/docs/exercises/tuples-exercises/

# Exercise 1: print the number in words
#
# Ex: 1234 => One Two Three Four

num = int(input())

strNum = ("Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine")
print(strNum[0])

for digit in str(num):
    print(strNum[int(digit)], end=" ")
