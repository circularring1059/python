from multiprocessing import Process
from time import sleep


def task1():
    while True:
        print("this is task1")
        sleep(1)


def task2():
    while True:
        print("this is task2")
        sleep(2)


if __name__ == '__main__':
    process1 = Process(target=task1)
    process2 = Process(target=task2)

    process1.start()
    process2.start()

    sleep(10)
    print("*" * 8)
    process1.terminate()  # process1  退出
