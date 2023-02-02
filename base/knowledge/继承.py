# -*- coding: UTF-8 -*-
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def __init__(self):
        print("创建了一个子类")
dog=Dog()
dog.run()
