import re

myStrData = str(input())
consonants = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
vowels = "aeiouAEIOU"
matches = re.findall(r"(?<=[%s])[%s]{2,}(?=[%s])" % (consonants, vowels, consonants), myStrData)
print("\n".join(matches or ["-1"]))
