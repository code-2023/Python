#!/usr/bin/python
# -*- coding: UTF-8 -*-

def fun(name, *args, **kwargs):
    print("Hello,%s" % name)
    print("第二部分的参数用元组包裹起来：%s" % (args,))
    print("第三部分的参数用字典接收：%s" % (kwargs,))


def fun_tuple(*args):
    for i in args:
        print(i)


def fun_dict(**kwargs):
    for key, value in kwargs.items():
        print("{0}的学号是{1}".format(key, value))


fun("小明", 1, 2, A=1, B=2)
fun_tuple(0, 1, 2, 3)
fun_dict(zengpeng=3182503105, guangzhi=3182503104)
