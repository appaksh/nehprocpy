# https://www.hackerrank.com/challenges/xml-1-find-the-score/problem
from abc import ABC
from html.parser import HTMLParser


class MyHtmlParser(HTMLParser, ABC):
    attrCount = 0

    def handle_starttag(self, tag, attrs):
        self.attrCount += len(attrs)

    def handle_startendtag(self, tag, attrs):
        self.attrCount += len(attrs)


myLines = "\n".join(input() for _ in range(int(input())))
myParser = MyHtmlParser()
myParser.feed(myLines)
print(myParser.attrCount)
myParser.close()
