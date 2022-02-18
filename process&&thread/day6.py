# 进程池
import os
from multiprocessing import Pool
from time import sleep
import random


def task(parameter):
    sleep(random.randint(1, 5))
    print(parameter)
    # print("task:{} done pid:{} ppid{}".format(parameter, os.getpid(), os.getppid()))
    return "task:{} done pid:{} ppid{}".format(parameter, os.getpid(), os.getppid())


res = []


def callback_fun(parameter):  # 定义回调函数，处理进程池任务结束的返回值
    # print(parameter)
    res.append(parameter)


if __name__ == '__main__':
    pool = Pool(3)

    # 定义几个任务
    tasks = ["吃饭", "睡觉", "学习", "游戏", "娱乐"]

    for task1 in tasks:
        # pool.apply_async(task, args=(task1,), callback=callback_fun)  #async  非阻塞
        pool.map_async(task, (task1,))

    pool.close()
    pool.join()  # 阻塞主进程，否则主进程退出，子进程也退出

    print(res)
    for i in res:
        print(i)
    print("over")
