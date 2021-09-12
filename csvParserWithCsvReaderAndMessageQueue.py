import json
from csv import DictReader

from azure.servicebus import ServiceBusMessage

USER_REGISTRATION = "User registration"


def parseCsvLine(line):
    user = {
        "name": line["name"],
        "favoriteGame": line["favoriteGame"],
        "grade": line["grade"],
        "placeAddress": {
            "street": line["street"],
            "city": line["city"],
            "state": line["state"]
        }
    }
    return user


def sendMessage(senderRef, content):
    message = ServiceBusMessage(content, subject=USER_REGISTRATION, content_type="application/json")
    senderRef.send_messages(message)


sbusConnString = "<connection-string-here>"
queueName = "<Queue name here>"
dictList = []
with open("csvSample1.csv", mode="r+") as readCvsLines:
    csvDictReader = DictReader(readCvsLines)
    # azureServiceBusClient = ServiceBusClient.from_connection_string(sbusConnString, logging_enable=True)
    # with azureServiceBusClient:
    #     sender = azureServiceBusClient.get_queue_sender(queue_name=queueName)
    #     with sender:
    for row in csvDictReader:
        person = parseCsvLine(row)
        dictList.append(person)
        # sendMessage(sender, json.dumps(person, indent=2))
        print(f'Sent message for user: {person["name"]}')

jsonString = json.dumps(dictList, indent=2)
print(jsonString)
