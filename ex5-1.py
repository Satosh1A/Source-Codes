import math as m
from datetime import datetime

#(1)
def weather ():
    return print('今日は晴れです')

#(2)
def calc_circle_area (radius):
    area = radius*radius*m.pi
    return print(area)

hankei = 1
calc_circle_area(hankei)

#(3)
def nowstr():
    now = datetime.now()
    return print(now.hour,'時',now.minute,'分',now.second,'秒')

nowstr()

#(4)
def nowint():
    now = datetime.now()
    return now.hour,now.minute,now.second

a = nowint()
print(a)

#(5)(ex5-2を含む)
def is_leapyear (year):
    if year%400==0:
        return print('西暦{}年はうるう年です'.format(year))
    
    if year%4==0 and year%100!=0:
        return print('西暦{}年はうるう年です'.format(year))
    else:
        return print('西暦{}年はうるう年ではありません'.format(year))
    
year = 4
is_leapyear(year)