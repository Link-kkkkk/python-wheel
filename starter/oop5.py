#!/usr/bin/python
#coding:utf-8

from enum import Enum
# 枚举
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

def enum():
    for name,member in Month.__members__.items():
        print name #枚举名字
        print member
        print member.value # int常量，从1开始

from enum import Enum, unique
@unique #装饰器检查有没有重复值
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
# print day1

