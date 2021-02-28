import json

import time
import urllib.request


def trackingOverallTime(functionToBeDecorated):
    def timeTracker(*args):
        startTime = int(time.time() * 1000)
        data = functionToBeDecorated(*args)
        endTime = int(time.time() * 1000)
        print(f"Tracking function: {functionToBeDecorated.__name__}, overall time: {endTime - startTime} milliseconds ")
        return data

    return timeTracker


@trackingOverallTime
def getWeatherData():
    url = "https://api.weather.gov/gridpoints/TOP/31,80/forecast/hourly"
    handle = urllib.request.urlopen(url)
    data = handle.read().decode()
    return data


@trackingOverallTime
def parseWeatherData(data):
    jsonWeather = json.loads(data)
    periods = jsonWeather["properties"]["periods"]
    [print(f'{period["startTime"][11:16]} {period["temperature"]}{period["temperatureUnit"]} ') for period in periods]


weather = getWeatherData()
parseWeatherData(weather)
