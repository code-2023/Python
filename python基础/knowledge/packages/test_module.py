from .module import Animal  # 导入平行模块Module.py里的Animal类


class TestClass:
    def __init__(self):
        self.__attr1 = 1

    @property
    def first_func(self):
        print("调用了对象的第一个方法")
        return self

    @staticmethod
    def second_func():
        print("调用了对象的第二个方法")

    def get_attr1(self):
        return self.__attr1

    def set_attr1(self, x):
        self.__attr1 = x

    def del_attr1(self):
        del self.__attr1

    Attr = property(get_attr1, set_attr1, del_attr1)


if __name__ == "__main__":
    obj = TestClass()
    # 使用Property可以把方法设置成属性来访问
    obj.first_func.second_func()
    # 获取、设置和删除私有属性
    # print(obj.Attr)
    # obj.Attr=2
    # del obj.Attr
    # 调用平行模块的类
    dog = Animal("Dog", "Male", 3)
    dog.get_age()

else:
    print("看到这行打印输出，则说明test_module模块被import并由解释器执行该模块内代码")
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
