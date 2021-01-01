thousands = "(?:(M){0,3})?"
hundreds = "(?:(D?(C){0,3})|(CM)|(CD))?"
tens = "(?:(L?(X){0,3})|(XC)|(XL))?"
ones = "(?:(V?(I){0,3})|(IX)|(IV))?"

regex_pattern = r"^" + thousands + hundreds + tens + ones + "$"

import re
print(str(bool(re.match(regex_pattern, input()))))
