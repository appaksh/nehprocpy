import re

mySyntax = re.search(r"([a-zA-Z0-9$])\1", input().strip())
print(mySyntax.group(1) if mySyntax else -1)
