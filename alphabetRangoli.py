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


def print_rangoli(size):
    myString = "abcdefghijklmnopqrstuvwxyz"
    for i in range(size - 1, -size, -1):
        finalString = '-'.join(myString[size - 1:abs(i): - 1] + myString[abs(i):size])
        print(finalString.center(4 * size - 3, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# # e
# # e-d-e
# # e-d-c-d-e
# #
# # [e]
# # [e, d, e]
# # [e, d, c, d, e]
#
# arr = ['e', 'd', 'c', 'd', 'e']
