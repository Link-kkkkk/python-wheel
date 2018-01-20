#!/usr/bin/python
#coding:utf-8

import re

test = '010-12345'
if re.match(r'^\d{3}\-\d{3,8}$', test):
    print('ok')
else:
    print('failed')

print re.split(r'[\s\,\;]+', 'a,b;; c  d')

# 编译表达式:
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

print re_telephone.match('010-12345').groups()
print re_telephone.match('010-8086').groups()