# https://www.hackerrank.com/challenges/the-minion-game/problem
# Print one line: the name of the winner and their score separated by a space.
#
# If the game is a draw, print Draw.
#
# Sample Input
#
# BANANA
# Sample Output
#
# Stuart 12


def minion_game(s):
    vowels = ["A", "E", "I", "O", "U"]

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s) - i)
        else:
            stusc += (len(s) - i)

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
