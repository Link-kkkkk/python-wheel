#!/usr/bin/python
#coding:utf-8

def tryCatch():
    try:
        print('try...')
        r = 10 / int('2')
        print('result:', r)
    except ValueError as e:
        print 'ValueError:', e
    except ZeroDivisionError as e:
        print 'except:', e
    # 可以没有else    
    else:
        print('no error!')    
    # 可以没有finally
    finally:
        print('finally...')
    print('END')


class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n
# 错误也是一个class，可以定义抛出的错误，大部分时候不太需要
# foo('0')

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise
# 把错误上抛
# bar()