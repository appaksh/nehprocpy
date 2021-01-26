def carFilter(allCars, filterValue):
    return list([car for car in allCars if car[0].upper() == filterValue.upper()])


def speedFilter(allCars, filterValue):
    return list([car for car in allCars if car[2].upper() == filterValue.upper()])


def printCarInfo(cars, filterFunc, filterValue):
    filteredCars = filterFunc(cars, filterValue)
    print("\n".join([f"Car {car[0].capitalize()} {car[1].upper()} is {car[2].capitalize()}" for car in filteredCars]))


myCars = [
    ["hennessy", "F5", "fast"],
    ["bugatti", "super sport", "fast"],
    ["bugatti", "chiron", "Fast"],
]

printCarInfo(myCars, carFilter, "hennessy")
print("--------------------------------------------------------------------------------------------------------------")
printCarInfo(myCars, speedFilter, "fast")
