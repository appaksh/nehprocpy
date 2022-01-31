if __name__ == '__main__':
    n = int(input())
    intList = map(int, input().split())
    print(hash(tuple(i for i in intList)))
