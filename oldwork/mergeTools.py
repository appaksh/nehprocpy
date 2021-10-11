# Merge The Tools link: https://www.hackerrank.com/challenges/merge-the-tools/problem?h_r=internal-search
# Remove all of the duplicates (part 1)
def removeDuplicates(piece):
    result = ""
    for letter in piece:
        if result.find(letter) == -1:
            result += letter

    return result


# Split the string
def merge_the_tools(inputString, maxWidth):
    parts = []
    for idx in range(0, len(inputString), maxWidth):
        singlePart = inputString[idx: idx + maxWidth]
        parts.append(singlePart)

    # Remove all of the duplicates (part 2)
    for part in parts:
        ans = removeDuplicates(part)
        print(ans)


# Get the input
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
