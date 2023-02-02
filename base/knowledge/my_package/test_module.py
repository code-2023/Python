def test_func():
    print("调用测试函数")
class TestClass:
    def __init__(self):
        self.__attr1 = 1

    @property
    def first_func(self):
        print("调用了对象的第一个方法; ",end='')
        return self   #返回调用该方法的对象本身

    @staticmethod
    def second_func():
        print("紧接着调用了对象的第二个方法")

    def get_attr1(self):
        return self.__attr1

    def set_attr1(self, x):
        self.__attr1 = x

    def del_attr1(self):
        del self.__attr1

    Attr = property(get_attr1, set_attr1, del_attr1)


if __name__ == "__main__":
    obj = TestClass()
    # 使用Property可以把方法设置成属性来访问；
    # 利用第一个方法返回的类对象继续调用同类的另一个方法。
    obj.first_func.second_func()
    # 获取、设置和删除私有属性
    # print(obj.Attr)
    # obj.Attr=2
    # del obj.Attr

# else:
#     print("看到这行输出，则说明test_module模块被import并由解释器执行该模块内代码")
#     test_func()
