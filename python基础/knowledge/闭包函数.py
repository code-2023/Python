# 闭包函数，其中 exponent 称为自由变量
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent

    return exponent_of  # 返回值是 exponent_of函数(局部函数)


square = nth_power(2)  # 传入指数2，即计算一个数的平方
cube = nth_power(3)  # 传入指数3，即计算一个数的立方
print(square(2))  # 传入底数2，计算 2 的平方
print(cube(4))  # 传入底数4，计算4的立方
