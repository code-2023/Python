def decorator_with_param(str1,str2):
    print("打印装饰器的第一个参数：", str1)
    def decorator(func):
        def wrapped_function():
            print("I am doing some boring work before executing func()")
            func()
            print("I am doing some boring work after executing func()")
            print("打印装饰器第二个参数：",str2)
        return wrapped_function
    return decorator
@decorator_with_param(66,99)
def simple_function():
    print("执行简单函数")
simple_function()


