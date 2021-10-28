# https://www.hackerrank.com/challenges/py-the-captains-room/problem?h_r=internal-search
numberPerRoom = int(input())
rooms = input().split()
dataDict = {}
for room in rooms:
    dataDict[room] = dataDict.get(room, 0) + 1
for room in dataDict.keys():
    if dataDict[room] < numberPerRoom:
        print(room)
        break
