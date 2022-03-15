def wrap(string, subString):
    return "\n".join([string[rep: rep + subString] for rep in range(0, len(string), subString)])


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
