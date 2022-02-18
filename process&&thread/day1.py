from multiprocessing import Process
import os
from time import sleep


def task1():
    while True:
        sleep(5)
        print("this is task1", "pid:",os.getpid(), "ppid:",os.getppid())

def task2():
    while True:
        sleep(5)
        print("this is task2", "pid:", os.getpid(), "ppid:", os.getppid())



if __name__ == '__main__':
    print("open multiprocess")
    process1 = Process(target=task1)
    process2 = Process(target=task2)

    #单纯地run 起来相当于调试
    # process1.run()
    # process2.run()

    #开启进程
    process1.start()
    process2.start()

    print("The parent process")
    print("父进程不会退出，在wait 子进程")

#非进程池创建，即使主进程退出了，子进程依然继续运行