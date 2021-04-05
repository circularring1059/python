import re

#{0-9a-zA-z}  匹配字母数字
# \w 匹配字母数字下划线
# \d 匹配数字
# . 匹配任意字符串，除换行符


msg = "<html>hello world<html/>"
print(re.match(r"(.+)", msg)) #<re.Match object; span=(0, 24), match='<html>hello world<html/>'>
print(re.match(r".+", msg)) #<re.Match object; span=(0, 24), match='<html>hello world<html/>'>
print(re.match(r"<\w+>", msg)) #<re.Match object; span=(0, 6), match='<html>'>
print(re.match(r"<[a-zA-Z]*>(.+)", msg)) # <re.Match object; span=(0, 24), match='<html>hello world<html/>'>
print(re.match(r"<[a-bA-Z]*>(.+)", msg)) # None  前面不匹配
print(re.match(r"<[a-zA-Z]*>.+<[a-zA-Z]*/>", msg)) # <re.Match object; span=(0, 24), match='<html>hello world<html/>'
print(re.match(r"<[a-zA-Z]*>(.+)<[a-zA-Z]*/>", msg)) # <re.Match object; span=(0, 24), match='<html>hello world<html/>'

msg1 = "<html>hello world<html/><br/>"
print(re.match(r"<[a-zA-Z]*>(.+)<[a-zA-Z]*/>", msg1)) # <re.Match object; span=(0, 29), match='<html>hello world<html/><br/>'>

msg2 = "<html><span>hello world<html/><span/>"

res = re.match(r"<([a-z]*)><([a-z]*)>(.+)<(\1/)><(\2/)>", msg2)  # ()代表一组，group(1) 表示一组
print(res) #<re.Match object; span=(0, 37), match='<html><span>hello world<html/><span/>'>
print(res.group(1))  #html
print(res.group(2))  #span
print(res.group(3))  #hello world