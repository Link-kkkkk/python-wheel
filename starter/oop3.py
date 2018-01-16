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

class Student(object):
    @property
    def score(self):
        return self._score * 2

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2018 - self._birth    

d = Student()
d.score = 60
print d.score
d.birth = 1993
print d.age
# 下面会报错，提示超出范围
# d.score = 9999
# print d.score 

# 对实例属性操作的时候，属性不是直接暴露的，而是通过getter和setter方法来实现的
# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性