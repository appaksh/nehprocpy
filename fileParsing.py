def parseLine(myLine):
    pairs = myLine.split(", ")
    myDictionary = {}
    for pair in pairs:
        (key, value) = pair.split("=")
        myDictionary[key] = value

    return myDictionary


myList = []
myFile = open("testData.txt", mode="r+")
try:
    pass
except RuntimeError:
    pass
lines = myFile.readlines()

for line in lines:
    lineReplacement = line.replace("\n", " ")
    lineResult = parseLine(lineReplacement)
    myList.append(lineResult)

for newList in myList:
    print(newList)

myFile.close()

