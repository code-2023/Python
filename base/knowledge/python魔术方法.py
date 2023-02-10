class Test(object):
    def __init__(self):
        self.numbers=[1,2,3,4,5]
        print("创建对象并初始化")

    # 打印对象时即打印特殊方法 __str__() 的返回值
    def __str__(self):
        return f"返回对象中封装的数据，如{self.numbers}"

    # 当__str__方法未重写时，重写__repr__方法可替代__str__方法。
    # 介绍对象的作用
    def __repr__(self):
        return "Hello! I am a Class of Test"

    # 获取长度(具体意义可自定)
    def __len__(self):
        return len(self.numbers)

obj = Test()
print(obj)
print(repr(obj))
print(len(obj))
