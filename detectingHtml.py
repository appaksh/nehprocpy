from abc import ABC
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser, ABC):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print(f"-> {attr[0]} > {attr[1]}") for attr in attrs]


html = '\n'.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
parser.close()
