import xml.etree.ElementTree as etree

maxDepth = 0


def depth(elem, level):
    global maxDepth
    if level >= maxDepth:
        maxDepth += 1

    for child in elem:
        depth(child, level + 1)


if __name__ == '__main__':
    xml = "\n".join(input() for _ in range(int(input())))
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxDepth)
