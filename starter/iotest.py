#!/usr/bin/python
#coding:utf-8

f = open('test.txt', 'r')
print f.read()

f.close()
import os
print os.path.abspath('.')

# 序列化为一个json
import json
d = dict(name='Bob', age=20, score=88)
print json.dumps(d)
# 反序列
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str)