import json
import time
import urllib.request
from datetime import datetime


def trackingOverallTime(functionToBeDecorated):
    def timeTracker(*args):
        startTime = int(time.time() * 1000)
        data = functionToBeDecorated(*args)
        endTime = int(time.time() * 1000)
        print(f'Tracking function: {functionToBeDecorated.__name__}, overall time: {endTime - startTime} milliseconds ')
        return data

    return timeTracker


@trackingOverallTime
def getWeatherData():
    url = "https://api.weather.gov/gridpoints/TOP/31,80/forecast/hourly"
    handle = urllib.request.urlopen(url)
    data = handle.read().decode()
    return data


def getHourFromDate(date):
    dateObject = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z")
    return str(dateObject.hour).rjust(2, "0") + ":" + str(dateObject.minute).rjust(2, "0")

def getHourFromDateWithStringParsing(date):
    return date[11:16]

@trackingOverallTime
def parseWeatherData(data):
    jsonWeather = json.loads(data)
    periods = jsonWeather["properties"]["periods"]
    [print(f'{getHourFromDate(period["startTime"])} {period["temperature"]}{period["temperatureUnit"]} ') for period in
     periods]


weather = getWeatherData()
parseWeatherData(weather)
