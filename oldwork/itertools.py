from collections import OrderedDict


def merge_the_tools(string, k):
    for x in range(0, len(string), k):
        print(''.join(list(OrderedDict.fromkeys(string[x:x + k]))))


def permutations():
    return None


def repeat(intInp2):
    return None