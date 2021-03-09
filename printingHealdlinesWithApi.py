import json
import urllib.request

def weatherWrapper(*args):
    if weatherDict.get(args[0]):
        print("Reading from local cache ")
    else:
        alerts = getWeatherData(*args)
        weatherDict[args[0]] =  alerts

    return weatherDict[args[0]]


def getWeatherData(stateName):
    print("Reading from url ")
    url = f'https://api.weather.gov/alerts/active?area={stateName}'
    handle = urllib.request.urlopen(url)
    data = handle.read().decode()
    jsonWeather = json.loads(data)
    features = jsonWeather["features"]
    return [feature["properties"]["headline"] for feature in features]


weatherDict = {}
for _ in range(4):
    state = str(input()).upper()
    alerts = weatherWrapper(state)
    print(f'Total alerts for {state} = {len(alerts)} ')
