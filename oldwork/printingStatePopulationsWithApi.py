import json
import urllib.request


def cacheDecorator(functionToBeDecorated):
    def dataWrapper(*args):
        if allPopDict.get(args[0]):
            print("reading from local cache ")
        else:
            allPop = functionToBeDecorated(*args)
            allPopDict[args[0]] = allPop

        print(allPopDict[args[0]])
        return allPopDict[args[0]]

    return dataWrapper


@cacheDecorator
def getStatePopulationData(inputYear):
    print("reading from url ")
    url = f'https://datausa.io/api/data?drilldowns=State&measures=Population&year={inputYear}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    handle = urllib.request.urlopen(req)
    data = handle.read().decode()
    jsonPopulation = json.loads(data)
    dataJson = jsonPopulation["data"]
    populationDict = {}
    for element in dataJson:
        state = element["State"]
        pop = element["Population"]
        populationDict[state] = pop
    return populationDict


allPopDict = {}
for _ in range(4):
    year = int(input())
    statePopulation = getStatePopulationData(year)
    allPopDict[year] = statePopulation

print(f'All state populations = {allPopDict} ')
