import re
"""
sub 
spilt
"""

name = "circularri   ng1010circularring1010"

print(re.sub(r"\d+", "yiling", name))  #把1010 换成yilingyiling
print(re.sub(r"\d", "yiling", name))  #把1 0 f 分别换成ylling

#函数操作
def add(arg):
    int_arg = int(arg.group())
    int_arg += 1
    return(str(int_arg))

print(re.sub(r"\d+", add, name))  #1010  加 1 变成1011


print(re.split(r"[l,0]", name))  #['circu', 'arring1', '1', 'circu', 'arring1', '1', '']  切割
print(re.split(r"[l, 0]", name)) #['circu', 'arri', '', 'ng1', '1', 'circu', 'arring1', '1', '']     这里一个空格，需要注意区别

print(name.split(" "))  #只按一个切割
print(name.split())  #默认空格，多个空格都按一个切割