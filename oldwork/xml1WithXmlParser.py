# https://www.hackerrank.com/challenges/xml-1-find-the-score/problem
import xml.etree.ElementTree as etree


def get_attr_number(node):
    return len(node.attrib) + sum(get_attr_number(child) for child in node)


if __name__ == '__main__':
    myXml = "\n".join(input() for _ in range(int(input())))
    tree = etree.ElementTree(etree.fromstring(myXml))
    root = tree.getroot()
    print(get_attr_number(tree.getroot()))
