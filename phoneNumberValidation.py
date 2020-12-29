import re


def isValidPhoneNumber(phoneNumber):
    if re.match(r"[7-9]\d{9}$", phoneNumber):
        return "YES"
    else:
        return "NO"


print("\n".join([isValidPhoneNumber(input()) for myNumbers in range(int(input()))]))
