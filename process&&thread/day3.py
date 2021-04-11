from multiprocessing import Process
from time import sleep
import os

def task1():
    for i in range(10):
        sleep(1)
        print("task1", i)

def task2():
    for i in range(10):
        sleep(2)
        print("task2",i)


if __name__ == '__main__':
    process1 = Process(target=task1)
    process2 = Process(target=task2)

    process1.start()
    process2.start()  #进程里的任务做完，进程自动退出