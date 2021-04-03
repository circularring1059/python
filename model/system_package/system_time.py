import time

print(time.time()) #时间戳

# time.sleep(5)

#time.time()
print(time.time())

#time.ctime()
print(time.ctime(time.time())) #type str Sat Apr  3 15:28:08 2021

#time.localtime()
print(time.localtime(time.time())) #<class 'time.struct_time'> time.struct_time(tm_year=2021, tm_mon=4, tm_mday=3, tm_hour=15, tm_min=32, tm_sec=58, tm_wday=5, tm_yday=93, tm_isdst=0)
print(time.localtime())
local_time = time.localtime()
time.sleep(3)
print(local_time.tm_mday, type(local_time.tm_mday)) #type int

#time.mktime()
print(time.mktime(local_time))  #转成时间戳

#time.strftme()
print(time.strftime("%Y-%m-%d %H:%M:%S",),type(time.strftime("%Y-%m-%d %H:%M:%S")))   #str time
print(time.strftime("%Y-%m-%d %H:%M:%S",local_time),type(time.strftime("%Y-%m-%d %H:%M:%S")))   #str time time.sleep(3)

str_time = "2021/04/3" # "2021/4/3 2021/04/03 结果是一样的“
print(time.strptime(str_time,"%Y/%m/%d"))  # time.struct_time(tm_year=2021, tm_mon=4, tm_mday=3, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=93, tm_isdst=-1)