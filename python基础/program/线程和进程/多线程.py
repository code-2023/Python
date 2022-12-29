import threading


def func1(t2):
    print('正在执行函数func1')
    t2.start()


def func2():
    print('正在执行函数func2')


if __name__ == '__main__':
    t2 = threading.Thread(target=func2)
    t1 = threading.Thread(target=func1, args=(t2,))
    t1.start()
