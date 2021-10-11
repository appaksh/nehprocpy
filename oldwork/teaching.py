# age = int(input("What is your age: "))
# if age < 12:
#     print("I am a kid ")
# elif age < 18:
#     print("I am a teenager ")
# else:
#     print("I am an adult ")
#
# thisDict = {
#     "name ": "Aakash ",
#     "place ": "Roundrock ",
#     "Birth ": 2009
#
# }
# print(thisDict)
#
# myList = [9, 5, 9, 2, 7]
# myList.remove(9)
# print(myList)
# age = 10
# name = "Aakash "
#
# print(f"My name is {name}, I am {age} years old ")
#
#
# def calculateInterest(principle, rate, duration):
#     total = ((principle * rate) * duration) + principle
#     print("principle: {} ; interest = {} : years = {} : total = {} ".format(principle, rate, duration, total))
#
#     print("---------------------------------------------------------------------------------------------")
#
#     return total
#
#
# principleAmount = int(11)
#
# p1 = 1000.00
# p2 = 2000
# title = "Aakash's Total amount is: "
#
# t1 = calculateInterest(p1, 0.08, 2)
# t2 = calculateInterest(p2, 0.08, 20)
# print("Total value is {principleAmount}".format(principleAmount=t1))
#
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
# print('''{0}
# {1} '''.format(a // b, a / b))
#
# if __name__ == '__main__':
#     n = int(input())
#     for x in range(n):
#         print(x * x)
#
# if __name__ == '__main__':
#     n = int(input())
#     output = ""
#     for x in range(1, n + 1):
#         print(x, end="")
#
# #Replace all ______ with rjust, ljust or center.
#
# thickness = int(input()) #This must be an odd number
# c = 'H'
#
# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#
# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))
#
# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
