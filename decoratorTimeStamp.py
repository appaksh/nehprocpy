import time


def trackingOverallTime(functionToBeDecorated):
    print("Time:")

    def timeTracker():
        print("Start")
        startTime = int(time.time() * 1000)
        functionToBeDecorated()
        endTime = int(time.time() * 1000)
        print(f"Tracking function: {functionToBeDecorated.__name__}, start and end time: {endTime - startTime} milliseconds")

    return timeTracker


@trackingOverallTime
def printTimeFuncDecorated():
    print("And end")
    time.sleep(1)


printTimeFuncDecorated()
