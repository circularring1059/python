import datetime

#时间差
time_difference =datetime.timedelta(days=2)  #差两天
print(time_difference)
"""
def __init__(self, days: float = ..., seconds: float = ..., microseconds: float = ...,
                     milliseconds: float = ..., minutes: float = ..., hours: float = ...,
                     weeks: float = ..., *, fold: int = ...) -> None: ...
"""
time_now = datetime.datetime.now()
print(time_now, type(time_now))  #2021-04-03 16:21:50.177440 <class 'datetime.datetime'

time_now_add_two_days = time_now + time_difference
print(time_now_add_two_days) #2021-04-05 16:21:50.177440

print(datetime.datetime.strptime("2021-4-3","%Y-%m-%d"))
print(type(datetime.datetime.strptime("2021-4-3","%Y-%m-%d"))) #<class 'datetime.datetime'>
