"""
lambda 表达式的语法格式如下：
lambda [list] : 表达式
其中，定义 lambda 表达式，必须使用 lambda 关键字；
[list] 作为可选参数，等同于定义函数指定的参数列表；name为该表达式的名称。
"""

#lambda函数作为函数的参数(指定具體的映射函數表達式)
obj=map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
l=list(obj)
print(l)
