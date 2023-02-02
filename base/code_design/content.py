#!/usr/bin/python
# -*- coding: UTF-8 -*-
#注意：使用python2.7的语法

class myException(BaseException):
    def __init__(self):
        print("实例化了一个自定义异常类")
class Test:
    def __init__(self):
        print("创建了Test类的实例对象")
    def method1(self):
        print("调用了普通方法method1")
    @staticmethod
    def smethod():
        print("这是一个静态方法")
    @classmethod
    def cmethod(cls):
        print("这是一个类方法")

    #使用装饰器函数property
    def setattr(self,value):
        self.attr1,self.attr2=value
    def getattr(self):
        return self.attr1,self.attr2
    attr=property(getattr,setattr)

    #触发异常
    def trigger_exception(self,x):
        print("1.断言异常\n2.其它异常")
        a=input("输入数字进行选择：")
        if a==1:
            assert (type(x) is type(1)), "传递参数的类型错误"
            print("程序正常执行，无异常发生")
            # print exit()
        else:
            try:
                raise myException
            except myException:
                print("捕获了一个异常")

if __name__=="__main__":
    obj=Test()
    obj.trigger_exception(2)
    obj.trigger_exception('w')