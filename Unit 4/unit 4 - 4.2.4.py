# Python Course - unit 4
# 4.2.4

import calendar
day_list = list(calendar.day_name)
date = input('Enter a date (dd/mm/yyyy):\t')
day = calendar.weekday(int(date[6:]), int(date[3:5]), int(date[:2]))
print(day_list[day])