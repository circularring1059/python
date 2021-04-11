from multiprocessing import Process
import os
from time import sleep


def task1():
    while True:
        sleep(1)
        print("this is task1", "pid:",os.getpid(), "ppid:",os.getppid())

def task2():
    while True:
        sleep(2)
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