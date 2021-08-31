# Exercise 1: create a employee and dept database.
#
# Get employee details by employee id.
#
# Ex: dept-data
#
# Dept code Name
# —————–
# 101 ‘HRD’,
# 102 ‘FINANCE’,
# 103 ‘ACCOUNTS’,
# 104 ‘SALES’,
# 105 ‘ENGINEERING’,
# 106 ‘SUPPORT’
#
# Employee data sample
#
# name doj emp id
#
# ‘Alex’ 10-10-17 1000


departments = {
    '101': 'HRD',
    '102': 'FINANCE',
    '103': 'ACCOUNTS',
    '104': 'SALES',
    '105': 'ENGINEERING',
    '106': 'SUPPORT'
}

employees = {
    '1000': {
        'deptId': '101',
        'doj': '10-10-17',
        'name': 'Alex'
    },
    '2000': {
        'deptId': '102',
        'doj': '11-11-17',
        'name': 'Mike'
    }
}

empId = input('Employee Id: ')
employee = employees.get(empId)
if employee is not None:
    deptId = employee['deptId']
    employee['deptName'] = departments[deptId]
    print(employee)
else:
    print(f'We cannot find this employee: {empId} ')

# Exercise 2: Display products with price less or equal form user input
#
# products = {
# ‘SMART WATCH’: 550,
# ‘PHONE’ : 1000,
# ‘PLAYSTATION’: 500,
# ‘LAPTOP’ : 1550,
# ‘MUSIC PLAYER’ : 600,
# ‘TABLET’ : 400


items = {
    'SMART WATCH': 550,
    'PHONE': 1000,
    'PLAYSTATION': 500,
    'LAPTOP': 1550,
    'MUSIC PLAYER': 600,
    'TABLET': 400

}

usrPrice = int(input("Enter the price : "))

for item in items:
    if items[item] <= usrPrice:
        print(f'{item}, {items[item]} ')
#
# Exercise 3: Count number of occurrence of words in a given text.
#
#

# Sample input:
#
# This is a common message for people,
#
# message is private and circulate this with caution

import re
from collections import defaultdict

usrInput = "hahahahahah hahahahahaha he he hoooo"
wordsList = usrInput.split()
wordCountDict = {}
for word in wordsList:
    regexWord = re.sub(r'[^\w\s]', '', word).lower()
    wordCountDict[regexWord] = wordCountDict.get(regexWord, 0) + 1

print(wordCountDict)


usrInput = "hahahahahah hahahahahaha he he hoooo"
wordsList = usrInput.split()
wordCountDict = defaultdict(int)
for word in wordsList:
    regexWord = re.sub(r'[^\w\s]', '', word).lower()
    wordCountDict[regexWord] = wordCountDict[word] + 1


print(wordCountDict)

