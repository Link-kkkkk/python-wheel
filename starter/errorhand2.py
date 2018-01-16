#!/usr/bin/python
#coding:utf-8

def foo(s):
    n = int(s)
    # 断言，不符合条件就输出
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

# main()

import logging
# logging有4个级别的提醒
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
# print(10 / n)


