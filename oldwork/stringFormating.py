# https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=false
def print_formatted(number):
    width = len("{0:b}".format(number))
    for rep in range(1, number + 1):
        print("{0:{fill}{align}{width}d} {0:{fill}{align}{width}o} {0:{fill}{align}{width}X} {0:{fill}{align}{width}b}".format(rep, width=width, fill=' ', align='>'))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
