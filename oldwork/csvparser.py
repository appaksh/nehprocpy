import json


def removeNewLine(data):
    return data.replace("\n", "")


def parseLine(line):
    parts = line.split(", ")
    person = {
                "name": parts[0],
                "favoriteGame": parts[1],
                "grade": parts[2],
                "address": {
                  "street": parts[3],
                  "city": parts[4],
                  "state": parts[5]
                }
             }
    return person


dictList = []
csvFile = open("../csvSample1.csv", mode="r+")
csvLines = csvFile.readlines()

for idx in range(1, len(csvLines)):
    csvDict = parseLine(removeNewLine(csvLines[idx]))
    dictList.append(csvDict)

jsonString = json.dumps(dictList, indent=2)
print(jsonString)
