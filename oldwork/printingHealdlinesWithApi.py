import json
import urllib.request


def cacheDecorator(functionToBeDecorated):
    def weatherWrapper(*args):
        if weatherDict.get(args[0]):
            print("Reading from local cache ")
        else:
            allAlerts = functionToBeDecorated(*args)
            weatherDict[args[0]] = allAlerts

        return weatherDict[args[0]]

    return weatherWrapper


@cacheDecorator
def getWeatherData(stateName):
    print("Reading from url ")
    headlinesList = []
    try:
        url = f'https://api.weather.gov/alerts/active?area={stateName}'
        handle = urllib.request.urlopen(url)
        data = handle.read().decode()
        jsonWeather = json.loads(data)
        features = jsonWeather["features"]
        for feature in features:
            headlinesList.append(feature["properties"]["headlines"])
    except Exception as exception:
        print("Error: ", exception)

    return headlinesList


weatherDict = {}
for _ in range(4):
    state = str(input()).upper()
    alerts = getWeatherData(state)
    print(f'Total alerts for {state} = {len(alerts)} ')
