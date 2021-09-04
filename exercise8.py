# Exercise 1:
#
#
# Write a simple MyMath class with, instance methods for addition, subtraction, multiplication,
# division and power functions.

class MyMath(object):

    def addVars(self, int1, int2):
        return int1 + int2

    def subtractVars(self, int1, int2):
        return int1 - int2

    def multiplyVars(self, int1, int2):
        return int1 * int2

    def divideVars(self, int1, int2):
        if int2:
            return int1 / int2
        else:
            return f'Cannot divide by 0, value is: {None} '

    def powVars(self, int1, int2):
        return int1 ** int2


mathMethods = MyMath()
print(mathMethods.addVars(1, 0))
print(mathMethods.subtractVars(1, 0))
print(mathMethods.multiplyVars(1, 0))
print(mathMethods.divideVars(1, 0))
print(mathMethods.powVars(1, 0))
