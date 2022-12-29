"""
使用import和from import会触发特殊模块__init__.py或者普通模块xxx.py中的代码执行
"""


import packages                # ”import 包名“相当于导入__init__模块，
from packages import module    # 使用包名导入模块
from packages import print_df  # 使用包名导入函数(位于__init__模块内)
# import packages.module as mod  # 使用包名.模块名导入module模块并给它起别名

# 使用包名调用函数和类
packages.func()
obj = packages.Animal("狗", "公", 3)

# 使用模块名调用函数
module.func()

# 使用模块名调用类(创建对象)
animal = module.Animal("猫", "母", 4)
print("-------------------------------------------------")

# 使用函数名调用函数
print_df()
