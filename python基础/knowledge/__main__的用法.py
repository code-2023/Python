def say():
    print("人生苦短，我学Python！")


class CLanguage:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def say(self):
        print(self.name, self.url)


# 当直接运行本模块时，name变量的值为 __main__；
# 而当模块被导入到其他程序中时，本模块中的 __name__ 变量的值就变成了模块名，即if判断不通过，if后续代码不执行！！！
if __name__ == '__main__':
    # 以下代码用于测试以上定义的方法和类，仅在此脚本文件中执行！
    say()
    clangs = CLanguage("C语言中文网", "http://c.biancheng.net")
    clangs.say()
