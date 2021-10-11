import json
import os
import urllib.request
from urllib.error import HTTPError

from decouple import config

YOUTUBE_APIKEY = 'YOUTUBE_APIKEY'
YT_ETAG = 'YT_ETAG'

apiKey = os.getenv(YOUTUBE_APIKEY)
part = "snippet"


def getRecentVideoId(channelId):
    url = f'https://www.googleapis.com/youtube/v3/search?part={part}&channelId={channelId}&maxResults=10&order=date&type=video&key={apiKey}'
    idList = []
    etagInput = config(YT_ETAG) or ''
    hdr = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)',
        'If-None-Match': etagInput
    }
    req = urllib.request.Request(url, headers=hdr)
    try:
        response = urllib.request.urlopen(req)
        data = response.read().decode()
        respData = json.loads(data)
        items = respData["items"]
        os.environ[YT_ETAG] = respData["etag"]
        print("New etag is: ", etagInput)
        for item in items:
            videoId = item["id"]["videoId"]
            idList.append(videoId)
    except HTTPError as he:
        print(f'Http status code 304: No new data, http status code: {he.code} for URL: {he.url} ')
    except Exception as e:
        print("Error ", e)

    return idList


inputId = input("Enter channel id: ")
videoIds = getRecentVideoId(inputId)
if videoIds:
    print(f'Http status code 200: new data: {videoIds} ')
