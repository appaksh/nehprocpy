import re


def getScheme(pattern):
    return pattern.group(1) or "http"


def getDomain(pattern):
    return pattern.group(2)


def getPort(pattern):
    return pattern.group(3) or defaultDictPort.get(getScheme(pattern), "")


def getPath(pattern):
    return pattern.group(4) or ""


def parseUrl(url):
    patternText = r'(\w+)://([\w.]+.+):?(\d+)*(/.*)'
    return re.match(patternText, url.lower())


def printUrl(pattern):
    print("Scheme : ", getScheme(pattern))
    print("Domain : ", getDomain(pattern))
    print("Port : ", getPort(pattern))
    print("Path : ", getPath(pattern))
    print("")


def compareUrls(url1, url2):
    pattern1 = parseUrl(url1)
    pattern2 = parseUrl(url2)
    url1Parts = [getScheme(pattern1), getDomain(pattern1), getPort(pattern1), getPath(pattern1)]
    url2Parts = [getScheme(pattern2), getDomain(pattern2), getPort(pattern2), getPath(pattern2)]

    if url1Parts == url2Parts:
        return True or False


defaultDictPort = {
    "http": "80",
    "https": "443",
    "ftp": "21",
    "sftp": "22"
}

urls = input("Enter urls: ").split(";")
print("urls equal : ", compareUrls(urls[0].strip(), urls[1].strip()))
