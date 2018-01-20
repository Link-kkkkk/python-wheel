#!/usr/bin/python
#coding:utf-8

# namedtuple是一个函数，它用来创建一个自定义的tuple对象，
# 并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1,5)
print p.x + p.y

# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，
# 因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import deque,defaultdict,OrderedDict

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')

# 输出不存在的默认值
q = defaultdict(lambda: 'N/A')
print q[6]

d = dict([('a', 1), ('b', 2), ('c', 3)]) # dict是无序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)]) # OrderedDict是有序的
print od