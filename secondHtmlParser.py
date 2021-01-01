#https://www.hackerrank.com/challenges/html-parser-part-2/problem

from abc import ABC
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser, ABC):

    def handle_comment(self, data):
        dl = data.split("\n")
        if len(dl) > 1:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()
