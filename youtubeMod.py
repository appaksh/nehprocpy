import json
import os
import urllib.request

tagsList = []
apiKey = os.getenv('YOUTUBE_APIKEY')
part = "snippet"


def readVideoLink(videoId):
    url = f'https://youtube.googleapis.com/youtube/v3/videos?part={part}&key={apiKey}&id={videoId}'
    try:
        hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
        req = urllib.request.Request(url, headers=hdr)
        response = urllib.request.urlopen(req)
        data = response.read().decode()
        jsonTags = json.loads(data)
        items = jsonTags["items"]
        for item in items:
            title = item["snippet"]["title"]
            description = item["snippet"]["description"]
            tagsList.append({
                "Title": title,
                "Description": description
            })
    except Exception as e:
        print("Error ", e)

    return tagsList


inputId = input("Enter your Video Id: ")
parts = readVideoLink(inputId)
print(json.dumps(parts, indent=2))
