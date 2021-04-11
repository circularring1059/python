from multiprocessing import Process
from time import sleep

def task1():
    while True:
        sleep(2)
        print("this is task1")
 #自定义进程
class MyProcess(Process):
    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    def run(self) -> None:
        while True:
            sleep(2)
            print(self.name)

if __name__ == '__main__':
    myProcess = MyProcess("task")
    myProcess.start()