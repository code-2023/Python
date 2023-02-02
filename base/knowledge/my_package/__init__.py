"""
当有.py文件导入Python包时，会自动执行__init__.py文件中的代码！
如果本模块使用相对路径的导入语法，直接运行本模块就会报错，
但可以用PyCharm编辑器的提示将其转换为绝对路径
"""

# __all__列表里放的成员必须是[本模块内的成员]或者[包内的模块]
__all__ = ["CONSTANT_VALUE", "package_func", "PackageClass", "module"]

CONSTANT_VALUE = 2023


def package_func():
    print("调用包名对应的__init__模块的函数")


class PackageClass:
    def __init__(self, x, y):
        print("构造方法传入参数{}和{}并创建了自定义类的对象".format(x, y))


if __name__ == "__main__":
    print(__name__)

else:
    print("my_package包被import后，解释器会执行__init__.py模块代码！")
    print("此时，被import之后的特殊模块名称变为：", __name__)
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
