#!/bin/python3

import os

# Complete the solve function below.
def solve(s):
    mySplit  = s.split(" ")
    return " ".join(myCapNum.capitalize() for myCapNum in mySplit)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
