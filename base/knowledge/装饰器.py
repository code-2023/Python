#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 注意：使用python2.7的语法

#装饰器无返回值
def decorator(func):
    print("I am doing some boring work before executing func()")
    func()
    print("I am doing some boring work after executing func()")

#装饰器嵌套于外层函数中间，则需返回闭包函数
def new_decorator(func):
    def wrapTheFunction():
        print("I am doing some boring work before executing func()")
        func()
        print("I am doing some boring work after executing func()")
    return wrapTheFunction

#定义简单函数
def simple_function():
    print("执行简单函数simple_function")

# 简单函数被装饰器修饰后
"""1. 简单的装饰器, 以下语句等价于decorator(simple_function)"""
@decorator
def simple_function():
    print("执行简单函数simple_function")

print("---------------------------------------------------------")


"""2. 返回闭包函数"""
@new_decorator
def simple_function():
    print("执行简单函数simple_function")

simple_function()
# 等价于以下用法
# simple_function = new_decorator(simple_function)
# simple_function()
