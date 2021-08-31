# Input
str1 = "this was a sample DatTaa"

# Exercise 1: Check if ‘is’ present in str1

if 'is' in str1:
    print(True)
else:
    print(False)

# Exercise 2: Check if ‘was’ not present in str1

if 'was' not in str1:
    print(True)
else:
    print(False)

# Exercise 3: Print str1 in uppercase

print(str(str1).upper())

# Exercise 4: Print str1 in lowercase

print(str(str1).lower())

# Exercise 5: Print str1 as title

print(str1.title())

# Exercise 6:  Get a new string from str1 ‘DatTaa’ as ‘Data’
newString = str1.replace('DatTaa', 'Data')
print(newString)

# Exercise 7: Get a new string from str1 with extra ‘a’ removed from ‘DatTaa’
data = str1[:-1]
print(data)

# Exercise 8: Display date, month and year form 10-Jan-2020'

date = '15-Feb-2025'.split('-')
day = date[0]
month = date[1]
year = date[2]
print(f'Day = {day}, Month = {month}, Year = {year}')

# Exercise 9: Display ‘sample’ word from ‘ this is another sample string ‘

sampleString = ' this is another sample string '.split(' ')
print(sampleString[4])

# Exercise 10: arr = “10,20,30,40,50,60,70”, get “50,60”
arr = '10,20,30,40,50,60,70'.split(',')
print(f'{arr[4]},{arr[5]}')

# Exercise 11: Find the sum of elements arr = “10,20,30,40,50,60,70”

arr = "10,20,30,40,50,60,70"
total = sum(map(int, arr.split(',')))
print(total)

# Exercise 12: From credit_str = “xxxx—-xxxx-8888——xxxx” get ‘8888’

creditString = 'xxxx—-xxxx-8888——xxxx'
creditString2 = creditString[creditString.index('8'): creditString.index('8') + len('8888')]
print(creditString2)

# Exercise 13: From credit_str = “1234-5678-9878-0434” get ‘0’

creditStr = '1234-5678-9878-0434'.split('-')
print(creditStr[3][0])

# Exercise 14: From given list gadgets = [“Mobile”, “Laptop”, 100, “Camera”, 310.28, “Speakers”, 27.00, “Television”, 1000, “Laptop Case”, “Camera Lens”]creat separate lists of strings and numbers.


gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00, "Television", 1000, "Laptop Case",
           "Camera Lens"]

str_items = []
num_items = []

for item in gadgets:

    if isinstance(item, str):
        str_items.append(item)

    if isinstance(item, int) or isinstance(item, float):
        num_items.append(item)

print(str_items)
print(num_items)

# Exercise 15: Given two strings check first is reverse of second. Ex ‘ABC’, ‘CBA’

string1 = 'ABC'
string2 = 'CBA'

if string2 == reversed(string1):
    print('string2 is the reversed version of string1 ')
else:
    print('string2 is not the reversed version of string1 ')

# Exercise 16: Given a strings check first and last words are same. Ex: ” Apples should compared with Apples” => should print same

string = input('Type a sentence: ').split(' ')

if string[0] == string[-1]:
    print('same')
else:
    print('not the same')

# Exercise 17: From the given list calculate total scores.

studentScores = ['Alex|75 50 90 80 90 70',
                 'Mary|76 72 71 68 85 69',
                 'John|69 67 68 71 68 67',
                 'Anne|80 69 59 82 71 81',
                 'Mark|79 81 74 71 69 73'
                 ]


def totalStudentScores(allScores):
    for tools in allScores:
        f, s = tools.split("|")
        print(f, sum(map(int, s.split())))


totalStudentScores(studentScores)

# Exercise 18: write a function encrypt a given string, input sample : 1) abcaaadddbvvsscccc => abca3d3bv2c4 2) abc => abc 3) wwww => w4 4) abcaaddbbvvsscd => abca2d2b2v2cd

userInp = input()
result = ''
idx = 0

while idx < len(userInp):
    count = 1
    while idx + 1 < len(userInp) and userInp[idx] == userInp[idx + 1]:
        count += 1
        idx += 1
    if count > 1:
        result = f'{result}{userInp[idx]}{count}'
    else:
        result = f'{result}{userInp[idx]}'
    idx += 1

print(result)
