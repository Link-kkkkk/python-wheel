#!/usr/bin/python
#coding:utf-8


# map()传入一个函数一个Iterable，会将传入的函数依次作用到每个元素上，并返回新的Iterator
def f(x):
    return x * x


# Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print list(r)

from functools import reduce


def add(x, y):
    return x + y


# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4) 大概是这样，不太好描述
print reduce(add, [1, 3, 5, 7, 9])


# filter()也接收一个函数和一个序列。filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n % 2 == 1


# 函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
print list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))

# key排序
from operator import itemgetter
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print sorted(students, key=itemgetter(0))
print sorted(L, key=lambda i:i[1])
