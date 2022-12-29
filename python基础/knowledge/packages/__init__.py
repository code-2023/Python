"""
这里可以编写一些 Python 初始化代码，比如预先导入包内常用的类，方便通过包名调用！！
则当有其它python文件导入learn包时，会自动执行__init__.py文件中的代码！
本模块使用了相对路径的导入语法，就不能直接运行本模块了，但可以用IDE的提示将其转换为绝对路径！
"""

import pandas as pd
from python基础.knowledge.packages.module import func, Animal
from python基础.knowledge.packages.test_module import TestClass


def print_df():
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6]])
    print(df)


if __name__ == "__main__":
    print_df()
    print(__name__)
else:
    print("packages包被import后，解释器会执行__init__.py模块代码！")
    print("包被import之后的特殊模块名称：", __name__)
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
