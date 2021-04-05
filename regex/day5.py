import re

"""分组
"""
#分组使用()  使用 | 表示或 与[] 不同

#匹配 0 ~ 100
print(re.match(r"[0-9]$|[1-9][0-9]$|100$", "0"))
print(re.match(r"[0-9]$|[1-9][0-9]$|100$", "2"))
print(re.match(r"[0-9]$|[1-9][0-9]$|100$", "23"))
print(re.match(r"[0-9]$|[1-9]\d$|100$", "23"))
print(re.match(r"[0-9]$|[1-9]\d$|100$", "0"))
print(re.match(r"[0-9]$|[1-9]\d$|100$", "100"))
print(re.match(r"[0-9]$|[1-9]\d$|100$", "101")) #None

#匹配-0 ~ 1000
print(re.match(r"[0-9]$|[1-9]\d$|[1-9]\d{2}$|100$", "80"))
print(re.match(r"[0-9]$|[1-9]\d$|[1-9]\d{2}$|100$", "998"))
print(re.match(r"[0-9]$|[1-9]\d$|[1-9]\d{2}$|100$", "0"))
print(re.match(r"[0-9]$|[1-9]\d$|[1-9]\d{2}$|100$", "7"))
print(re.match(r"[0-9]$|[1-9]\d$|[1-9]\d{2}$|100$", "77"))
print(re.match(r"[0-9]$|[1-9]\d$|[1-9]\d{2}$|100$", "1001")) #None