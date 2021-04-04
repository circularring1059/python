import re

name = "circularring1010"

pattern = re.compile("1010")

#match  从头开始匹配，没有返回None<re.Match object; span=(12, 16), match='1010'>
print(re.match(pattern, name))  # None  从头开始匹配

patter1 = "circul"

print(re.match(patter1, name))  #<re.Match object; span=(0, 6), match='circul'>

print(re.match("cir", name)) #<re.Match object; span=(0, 3), match='cir'>

#search 开始没有匹配上可以往下匹配
print(re.search(pattern, name)) # <re.Match object; span=(12, 16), match='1010'>
res = re.search(pattern,name)
print("*" * 8)
print(res.span(),res.group())  #span() 返回iddex位置 group()返回匹配值
