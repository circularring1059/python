from multiprocessing import Process
from time import sleep
import os

def task1(arg):
    while True:
        sleep(4)
        print("this is task1","arg is {}".format(arg))

def task2(arg):
    while True:
        sleep(3)
        print("this is task2", "arg is {}".format(arg))

if __name__ == '__main__':
    process1 = Process(target=task1, name="task1", args=('task1',))  #args  需要可迭代的
    process2 = Process(target=task2, name="task2", args=("task2",))

    print(process1.name)  #process'name
    print(process2.name)
    process1.start()
    process2.start()