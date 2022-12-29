import logging
from time import sleep


def no_try_except():
    a = input("请输入一个数：")
    10 / int(a)
    print("当有异常时，本行代码则不能正常运行")


def exception():
    a = input("请输入一个数：")
    try:
        10 / int(a)
    except:
        print("异常已被我捕获,正在处理错误...")
        print("当前问题已处理")
    finally:
        print("-----------------------------")
        print("程序保持运行状态")


def raise_exception():
    s = int(input("请输入一个数："))
    # if (s == 0):
    # try:
    #     raise ZeroDivisionError()
    # except ZeroDivisionError as e:
    #     print("捕获到了ZeroDivisionError")
    try:
        2 / str(s)  # 抛出TypeError
        print(f"10/{s}的计算结果={10 / s}")  # 可能抛出ZeroDivisionError
    except ValueError:
        print("捕获到try块的ValueError")
    except ZeroDivisionError as e:
        print("捕获到try块的ZeroDivisionError")
        logging.exception(e)
        sleep(1)
        s = int(input("请重新输入一个非零数："))
        if s == 0:
            print("对不起，输错2次后将会抛出异常")
            raise
        print(f"10/{s}的计算结果={10 / s}")
    finally:
        print("finally关键字后面必须执行的内容")


def main():
    try:
        # no_try_except()
        # exception()
        raise_exception()

    except ZeroDivisionError:
        print("主函数内捕获到被调用函数内抛出的ZeroDivisionError")
    except TypeError:
        print("主函数内捕获到被调用函数内抛出的TypeError")

    print("异常被捕获后，后续代码将正常执行")
    for x in (1,2,3,4,5):
        print(x)
main()
