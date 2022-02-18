import os
from multiprocessing import Pool
from time import sleep


def task1(parameter):
    sleep(1)
    print("this is task:{}".format(parameter), "pid:{}".format(os.getpid()))


if __name__ == '__main__':
    pool = Pool(3)

    tasks = ["listing", "watching", "running", "jumping"]

    for task in tasks:
        pool.apply(task1, args=(task,))  # 阻塞，但是进程号可以复用，没有callback

    pool.close()
    pool.join()

    print("over!!!")

"""
this is task:listing pid:20300
this is task:watching pid:25860
this is task:running pid:27296
this is task:jumping pid:20300
over!!!
"""
