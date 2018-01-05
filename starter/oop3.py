#!/usr/bin/python
#coding:utf-8

class Men(object):
    # 特殊变量，只允许设置name和age这两个属性
    # __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
    __slots__ = ('name', 'age')

def set_name(self, name):
    self.name = name

# 绑定一个方法
Men.set_name = set_name

s = Men()
s.set_name('Lily')
s2 = Men()
s2.set_name('Saber')
