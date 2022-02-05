from datetime import datetime as dt

if __name__ == '__main__':
    testCases = int(input())
    formatting = '%a %d %b %Y %H:%M:%S %z'
    for rep in range(testCases):
        testCase1 = input()
        testCase2 = input()
        t1 = dt.strptime(testCase1, formatting)
        t2 = dt.strptime(testCase2, formatting)
        print(int(abs(t1 - t2).total_seconds()))
