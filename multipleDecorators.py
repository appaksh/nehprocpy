import urllib.request


def getNames1(functionToBeDecorated):
    def names(*args):
        firstName = "Aakash"
        lastName = "Appalaneni"
        studentGrade = "6"
        data = functionToBeDecorated(*args)
        print(
            f'Tracking function: {functionToBeDecorated.__name__}, first name: {firstName}, first name: {lastName} grade: {studentGrade} ')
        return data

    return names


def getNames2(functionToBeDecorated):
    def names(*args):
        lastName = "Appalaneni"
        firstName = "Aakash"
        studentGrade = "6"
        data = functionToBeDecorated(*args)
        print(
            f'Tracking function: {functionToBeDecorated.__name__}, last name: {lastName}, first name: {firstName} grade: {studentGrade} ')
        return data

    return names


# @trackingOverallTime
def getWeatherData(inputUrl):
    handle = urllib.request.urlopen(inputUrl)
    data = handle.read().decode()
    return data


url = "https://api.weather.gov/gridpoints/TOP/31,80/forecast/hourly"
# weather = getWeatherData(url)
decoratorStartAndEndTime = getNames2(getWeatherData)
decoratorStartAndEndTime(url)
print("---------------------------------------------------------------------------------------------------------------")
finalTimeTaken = getNames1(getWeatherData)
finalTimeTaken(url)
