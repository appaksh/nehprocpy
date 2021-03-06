import email.utils
import re


def isValidEmail(emailAddress):
    emailRegex = r"[a-zA-Z][a-zA-Z0-9-,\.,_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$"
    return re.match(emailRegex, emailAddress)


# allEmails = []
# for emailParse in range(int(input())):
#     emailInput = email.utils.parseaddr(str(input()))
#     allEmails.append(emailInput)

allEmails = [email.utils.parseaddr(str(input())) for x in range(int(input()))]
print("\n".join([email.utils.formataddr(emailItem) for emailItem in allEmails if isValidEmail(emailItem[1])]))
