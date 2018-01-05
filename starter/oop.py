#!/usr/bin/python
#coding:utf-8

class Student(object):
    # __init__是默认执行的方法，第一个参数指向实例本身
    def __init__(self, name, score):
        #__是私有变量前缀，外部不能修改
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    def set_info(self, name, score):
        if 0 <= score <= 100:
            self.__name = name
            self.__score = score
        else:
            raise ValueError('bad score')

# 传参不需要传self
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

# 其实还是可以通过这种方式访问私有变量
# print lisa._Student__name
lisa.set_info('Lisa Lily', 60)

bart.print_score()
lisa.print_score()
