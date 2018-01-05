#!/usr/bin/python
#coding:utf-8

class Animal(object):
    def run(self):
        print 'A animal is running...'

# 继承Animal
class Dog(Animal):
    def __init__(self, *name):
        self.name = name

    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

class Husky(Dog):
    pass

def run_twice(animal):
    animal.run()
    animal.run()

#继承的时候子类同名方法会覆盖父类方法
dog = Dog('doggy')
dog.run()

cat = Cat()
cat.run()

# 走方法不需要改变类内部
run_twice(Tortoise())

# “开闭”原则：
# 对扩展开放：允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

# 获取信息，a是否是一个Dog()和Animal（）, Dog继承自Animal
a, d, h = Animal(), Dog(), Husky()
print isinstance(d, Dog) and isinstance(d, Animal)

# 是否有name属性
print hasattr(dog, 'name')
# 设置属性
print setattr(dog, 'name', 'lily')
# 获取属性,404是找不到的默认值
print getattr(dog, 'namee', 404)
# 正常来说dog.name就可以了