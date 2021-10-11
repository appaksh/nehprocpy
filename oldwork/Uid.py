import re


def isValidUid(validUid):
    if not re.match(r"\w{10}$", validUid):  # max 10, alphanumerics
        return "Invalid"

    if len(re.findall(r"\d", validUid)) < 3: # 3 or more, numbers
        return "Invalid"

    if len(re.findall(r"[A-Z]", validUid)) < 2: # 2 or more, capital letters
        return "Invalid"

    if re.match(r".*(.).*\1", validUid): # no repetition
        return "Invalid"

    return "Valid"


print("\n".join([isValidUid(input()) for myNumbers in range(int(input()))]))
