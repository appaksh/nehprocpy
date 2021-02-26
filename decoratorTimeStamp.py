import time
import urllib.request


def trackingOverallTime(functionToBeDecorated):
    print("Time:")

    def timeTracker():
        print("Start")
        startTime = int(time.time() * 1000)
        functionToBeDecorated()
        endTime = int(time.time() * 1000)
        print(
            f"Tracking function: {functionToBeDecorated.__name__}, overall time: {endTime - startTime} milliseconds")

    return timeTracker


@trackingOverallTime
def printTimeFuncDecorated():
    url = "https://api.weather.gov/gridpoints/TOP/31,80/forecast/hourly"
    file = urllib.request.urlopen(url)
    print("Result code: " + str(file.getcode()))


time.sleep(1)

printTimeFuncDecorated()
