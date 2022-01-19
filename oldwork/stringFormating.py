# https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=false
def print_formatted(number):
    width = len("{0:b}".format(number))
    for rep in range(1, number + 1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(rep, width=width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
