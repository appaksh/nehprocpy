import re


def isFloatingNumber(floatingNumber):
    if re.match(r"^[-+]?[0-9]*\.[0-9]+$", floatingNumber):
        return "True"
    else:
        return "False"


print("\n".join([isFloatingNumber(input()) for myFloat in range(int(input()))]))
