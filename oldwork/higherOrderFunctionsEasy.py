def myUpper(car):
    return car.upper()


def myCapitalize(car):
    return car.capitalize()


def formatName(userFunc, first, second):
    return f"First car:  {userFunc(first)} \nSecond car: {userFunc(second)} "


fCar = "bugatti"
sCar = "venom"

print(formatName(myUpper, fCar, sCar))
print("------------------------------------------------------------------------------------------------------------")
print(formatName(myCapitalize, fCar, sCar))
