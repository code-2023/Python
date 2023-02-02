"""
使用import和from import都会触发普通模块xxx.py或特殊模块__init__.py中的代码执行
"""

# 注意：使用语法"from xxx import * "仅导入__all__列表中指定的模块成员
from my_package import *
from my_package.demo import *
from my_package.test_module import TestClass
# 使用包名导入包内的指定模块
# from my_package import demo
# from my_package import module

# "import 包名"相当于导入__init__模块，
import my_package

# 使用包名.模块名导入指定模块并给它起别名
# import my_package.module as module


# 使用模块名调用函数
module.func()
# 使用模块名调用类的构造方法(即创建对象)
animal = module.Animal("猫", "母", 4)

# 使用包名调用函数(需要import my_package)
my_package.package_func()
# 使用包名调用类构造方法
obj = my_package.PackageClass(1, 2)

# 使用语法[from xxx import *]之后，可以直接使用模块内__all__列表内的函数和类
package_func()
obj=PackageClass(1, 2)

_protected()
CLanguage()
say()
# disPython()   #PyCharm编辑器提示：Unresolved reference 'disPython'