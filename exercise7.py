# Exercise 1:
#
# Find whether a given string has unique characters, return True, if duplicates return False
#
# sample input
#
# ‘just’ => has unique characters
#
# Alexander => has duplicates

strInput = input()


def uniqueStr(usrInp):
    charSet = set()
    for char in usrInp:
        if char in charSet:
            return False
        else:
            charSet.add(char)

    return True


uniqueSet = set([char for char in strInput])

print(f'Test case variation 1, {uniqueStr(strInput)} ')
print(f'Test case variation 2, {True if len(uniqueSet) == len(strInput) else False} ')
