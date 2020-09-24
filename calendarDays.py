# https://www.hackerrank.com/challenges/calendar-module/problem
# Sample Input
#
# 08 05 2015
# Sample Output
#
# WEDNESDAY

import calendar

dt = input().split(" ")
wk = calendar.weekday(int(dt[2]), int(dt[0]), int(dt[1]))
print(calendar.day_name[wk].upper())

