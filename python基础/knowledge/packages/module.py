"""
在本模块里，你可以定义各种成员，成员包括变量、方法、类
"""
field = "模块的属性/成员变量"


def func():
    print("调用了Module模块的func函数")


class Animal:
    category = "动物类"

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
        self.weight = ''
        print("创建了Animal对象，这是一只年龄为%d岁的%s%s" % (age, sex, name))

    @staticmethod
    def behavior():
        print("调用Animal类的静态方法：动物会捕猎、进食、排便和睡觉")

    # 普通方法
    def set_weight(self, attribute):
        self.weight = attribute

    def get_sex(self):
        print("%s的性别是%s" % (self.name, self.sex))

    def get_age(self):
        print("%s的年龄是%d岁" % (self.name, self.age))


if __name__ == "__main__":
    dog = Animal("Dog", "Male", 3)
    Animal.behavior()
else:
    print("看到这行输出，则说明module模块被import，解释器会执行该模块内代码")
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
