#!/usr/bin/python
#coding:utf-8

# 默认参数
# 定义默认参数要牢记一点：默认参数必须指向不变对象！譬如数组默认空，每次执行append就会累加
def innerInfo(name, work, age, city='HK'):
    print 'name:', name
    print 'work:', work
    print 'age:', age
    print 'city:', city


# innerInfo('Link','Web Developer', 24)


# 可变参数，可以传入任意数量的参数，或者空
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# print calc(1, 3, 5, 7)

# 传参也可变
nums = [1, 2, 3]

# print calc(*nums)


# 关键性参数，可以接受多出来的参数存储起来
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# person('Adam', 45, gender='M', job='Engineer')

# 递归
# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)

# 尾递归，每次只调用一个函数，只占用一个栈帧所以不会导致内存溢出
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    # print num, product
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print fact(5)