class CLanguage:
    # 下面定义了2个类变量
    name = "C语言中文网"
    url = "http://c.biancheng.net"

    def __init__(self):
        self.name = "高等数学"
        self.url = "http://www.icourse163.org/"
        self.catalog = ''

    def say(self):
        self.catalog = 13


# 创建类的对象
clang = CLanguage()
print("实例变量name：" + clang.name)
print("实例变量add：" + clang.url)
print("类变量name：" + CLanguage.name)
print("类变量add：" + CLanguage.url)
print('------------------------------------------')
# 修改对象的属性
clang.name = "Python教程"
clang.url = "http://c.biancheng.net/python"
print("修改后的实例变量name：" + clang.name)
print("修改后的实例变量add：" + clang.url)
print("类变量name仍为：" + CLanguage.name)
print("类变量add仍为：" + CLanguage.url)
print('------------------------------------------')
# 新增实例变量
clang.new = "clang对象新增加了一个实例变量new"
print(clang.new)
