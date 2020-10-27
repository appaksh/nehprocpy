def print_rangoli(size):
    myString = "abcdefghijklmnopqrstuvwxyz"
    for i in range(size - 1, -size, -1):
        finalString = '-'.join(myString[size - 1:abs(i): - 1] + myString[abs(i):size])
        print(finalString.center(4 * size - 3, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
