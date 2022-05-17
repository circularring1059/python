import threading,time
def run(n):
    time.sleep(n)
    print("task  ",n)

start_time=time.time()
t1=threading.Thread(target=run,args=(3,))
t2=threading.Thread(target=run,args=(6,))

t1.start()
t2.start()
t1.join()
# t2.join()  //join 等待当前线程结束后在执行主进程
print(time.time()-start_time)


