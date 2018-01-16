#!/usr/bin/python
#coding:utf-8

class Man(object):
    def __init__(self, *name):
        self.name = name

    # 美化输出
    def __str__(self):
        return 'Men object (name: %s)' % self.name
    
    # 美化变量输出 偷懒版本
    __repr__ = __str__

print(Man('Michael'))

s = Man('Lily')
print(s)

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
    
    def __getitem__(self, n):
        # 区分int和slice类型版本
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
    
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

f = Fib()
print f[10]
print f[:10]
print f.age()

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    # 默认方法，直接调用实例就会执行
    def __call__(self):
        pass

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

# 链式调用
print Chain().state.data.timeline.list
print Chain()