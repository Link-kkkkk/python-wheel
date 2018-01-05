#!/usr/bin/python
#coding:utf-8

L = list(range(100))
# 切数组0到3位
print L[0:3]
# 前10个数，每2个取一下
print L[:10:2]
# 所有数 每5个取一下
print L[::5]
# 字符串，对象都可以进行切片处理 ps:js开发者泪流满面

# 同于切片，字符串，对象都可以进行循环 ps：java开发者泪流满面
from collections import Iterable

# 检测对象是否可以迭代
print isinstance('abc', Iterable)
print isinstance(123, Iterable)

# 下标循环的话加多一个参数
for x, y in enumerate([1, 2, 3]):
    print x, y

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x, y

# 列表生成式
print [x * x for x in range(1, 11)]
print [x * x for x in range(1, 11) if x % 2 == 0]
# 双循环就可以全排列
print [m + n for m in 'ABC' for n in '123']
# 跑方法放前面
L2 = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L2]

# 数字无法lower()方法，如果list有数字，会报错，要先处理，用isinstance()就行