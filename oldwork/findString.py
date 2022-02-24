# https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    matchCnt = 0
    for repNum in range(len(string) - len(sub_string) + 1):
        if sub_string == string[repNum: repNum + len(sub_string)]:
            matchCnt += 1

    return matchCnt


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
