import time
import urllib.request


def getStudentOfTheDay():
    return {
        "firstName": "Aakash",
        "lastName": "Appalaneni",
        "studentGrade": "6"
    }


def printStudentInfo(functionToBeDecorated):
    def studentDecoratorOther(*args):
        student = functionToBeDecorated(*args)
        print(
            f'First name: {student["firstName"]}, last name = {student["lastName"]}, student grade: {student["studentGrade"]} ')
        return student

    return studentDecoratorOther


def printStudentInfoOther(functionToBeDecorated):
    def studentDecorator(*args):
        student = functionToBeDecorated(*args)
        print(
            f'Last name: {student["lastName"]}, first name = {student["firstName"]}, student grade: {student["studentGrade"]} ')
        return student

    return studentDecorator


def trackingOverallTime(functionToBeDecorated):
    def timeTracker(*args):
        startTime = int(time.time() * 1000)
        data = functionToBeDecorated(*args)
        endTime = int(time.time() * 1000)
        print(f'Tracking function: {functionToBeDecorated.__name__}, overall time: {endTime - startTime} milliseconds ')
        return data

    return timeTracker


def trackStartAndEndTime(functionToBeDecorated):
    def timeTracker(*args):
        startTime = int(time.time() * 1000)
        data = functionToBeDecorated(*args)
        endTime = int(time.time() * 1000)
        print(f'Tracking function: {functionToBeDecorated.__name__}, start time: {startTime}, and end time: {endTime}')
        return data

    return timeTracker


# @trackingOverallTime
def getWeatherData(inputUrl):
    handle = urllib.request.urlopen(inputUrl)
    data = handle.read().decode()
    return data


url = "https://api.weather.gov/gridpoints/TOP/31,80/forecast/hourly"
decoratorStartAndEndTime = trackStartAndEndTime(getWeatherData)
decoratorStartAndEndTime(url)

finalTimeTaken = trackingOverallTime(getWeatherData)
finalTimeTaken(url)
print("--------------------------------------------------------------------------------------------------------------")
decoratorStudentInfo = printStudentInfo(getStudentOfTheDay)
decoratorStudentInfo()
decoratorStudentInfoOther = printStudentInfoOther(getStudentOfTheDay)
decoratorStudentInfoOther()
