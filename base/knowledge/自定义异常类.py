class MyException(Exception):
    pass
def func(i):
    if i==1:
        try:
            raise ValueError("value error")
            # raise MyException("自定义异常")
        except MyException as f:
            print("捕获到了自定义异常")
        except ValueError as e:
            print(e)

    elif i!=1:
        try:
            2/int(i)
        except ValueError:
            raise
    else:
        print("程序正常执行。")

# func('a')
func(1)
print("异常处理完毕后，执行本行代码")


