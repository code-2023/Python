class Test(object):
    def __init__(self):
        self.numbers=[1,2,3,4,5]
        print("创建对象并初始化")

    # 打印对象时即打印特殊方法 __str__() 的返回值
    def __str__(self):
        return "prefer to excute I am Test"

    # 当__str__方法未重写时，重写__repr__方法可替代__str__方法。
    # 此外，使用repr(obj)可在交互式编程窗口展示对象信息
    def __repr__(self):
        return "I am Test1"

    # 获取对象的长度
    def __len__(self):
        return len(self.numbers)

obj = Test()
print(obj)
print(len(obj))
