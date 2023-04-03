from multiprocessing import Queue, Process
import time, random

# 要写入的数据
list1 = ["java", "Python", "JavaScript"]


def write(queue):
    """
    向队列中添加数据
    ：param queue：
    ：return：
    """
    for value in list1:
        print(f"正在向队列中添加数据-->{value}")
        # put_nowait 不会等待队列有空闲位置再放入数据，如果数据放入不成功就直接崩溃,比如数据满了。put 的话就会一直等待
        queue.put_nowait(value)
        time.sleep(random.random())


def read(queue):

    while True:
        # 判断队列是否为空
        if not queue.empty():
            # get_nowait 队列为空，取值的时候不等待，但是取不到值那么直接崩溃了
            value = queue.get_nowait()
            print(f'从队列中取到的数据为-->{value}')
            time.sleep(random.random())
        else:
            break

if __name__ == '__main__':
    # 父进程创建出队列，通过参数的形式传递给子进程
    #queue = Queue(2)
    queue = Queue()

    # 创建两个进程 一个写数据 一个读数据
    write_data = Process(target=write, args=(queue,))
    read_data = Process(target=read, args=(queue,))

    # 启动进程 写入数据
    write_data.start()
    # 使用 join 等待写数据结束
    write_data.join()
    # 启动进程  读取数据
    print('*' * 20)
    read_data.start()
    # 使用 join  等待读数据结束
    read_data.join()

    print('所有的数据都写入并读取完成。。。')
