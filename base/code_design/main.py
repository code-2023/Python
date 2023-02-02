#!/usr/bin/python
# -*- coding: UTF-8 -*-

from content import Test

try:
    print("提示：shell脚本调用python函数")
    print("-------------------------------------------------------")
    # 创建Test类的实例对象并调用相关方法
    obj = Test()
except:
    print("引发异常")


# 实例属性操作
def use_attribute():
    obj.attr1 = "属性1"
    obj.attr2 = "属性2"
    print("获取的属性元组为%s,%s" % (obj.attr))


# 使用方法
def use_method():
    obj.method1()
    obj.smethod()
    Test.cmethod()


# 触发异常
def trigger_exception():
    obj.trigger_exception(1)


if __name__ == "__main__":
    use_attribute()
    use_method()
    trigger_exception()
