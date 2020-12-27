import re


def isValidCreditCardNumber(creditCardNumbers):
    if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", creditCardNumbers) and not re.search(r"([\d])\1\1\1", creditCardNumbers.replace("-", "")):
        return "Valid"
    else:
        return "Invalid"


print("\n".join([isValidCreditCardNumber(input()) for myNumbers in range(int(input()))]))
