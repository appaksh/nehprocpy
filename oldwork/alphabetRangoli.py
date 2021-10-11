# You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)
#
# Different sizes of alphabet rangoli are shown below:
#
# #size 3
#
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

import string

alphaArr = list(string.ascii_lowercase)


def print_rangoli(size):
    for i in range(size - 1, 0, -1):
        print(("-".join(alphaArr[i: size][:: - 1] + alphaArr[i + 1: size])).center((4 * size) - 3, "-"))

    for i in range(1, size):
        print(("-".join(alphaArr[i: size][:: - 1] + alphaArr[i + 1: size])).center((4 * size) - 3, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
