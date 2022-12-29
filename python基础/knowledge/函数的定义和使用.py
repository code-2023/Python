from packages import TestClass


# 定义函数
def fun1():
    print("调用了定义函数func")
    return TestClass()


# 传入参数为函数
def fun2(fn):
    return fn()


# 返回函数名
def fun3():
    print("Hello")
    return fun3


if __name__ == "__main__":
    # 同模块中，通过函数名调用函数fun2
    obj = fun2(fun1)
    # obj接收的返回值是TestClass类的对象
    obj.fisrt_func.second_func()
    # 使用a接收函数返回值(函数名)
    a = fun3()
    print("a的类型是%s" % (type(a)))
    print("打印a：%s" % a)
    a()
