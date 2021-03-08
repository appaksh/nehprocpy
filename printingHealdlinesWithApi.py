import json
import urllib.request


def getWeatherData():
    url = f'https://api.weather.gov/alerts/active?area={str(input()).upper()} '
    handle = urllib.request.urlopen(url)
    data = handle.read().decode()
    return data


def parseWeatherData(data):
    jsonWeather = json.loads(data)
    features = jsonWeather["features"]
    return [feature["properties"]["headline"] for feature in features]


print("\n".join(parseWeatherData(getWeatherData())))
