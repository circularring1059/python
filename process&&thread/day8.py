# 进程间通行，可以使用queue
from multiprocessing import Process, Queue
from time import sleep
import random


def product(q):
    # listA = ["A", "B", "C", "D"]
    for i in range(5):
        print("put: ")
        q.put(chr(random.randint(65, 90)), )  # full 后阻塞
        # q.put(chr(random.randint(65, 90)), timeout=5)
        # sleep(1)


def consume(q):
    while True:
        sleep(2)
        # print(q.get())   #empty  阻塞
        print(q.get(timeout=3))  # 超时后退出


if __name__ == '__main__':
    q = Queue(3)

    process1 = Process(target=product, args=(q,))
    process2 = Process(target=consume, args=(q,))

    process1.start()
    process2.start()

    print("over")
