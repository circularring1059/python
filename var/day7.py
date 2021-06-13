#读写文件
file = open("file001.txt", "w", encoding="utf-8")  #创建文件对象  原文件存在会被删除  当前目录下写
# file.write("ring")
file.write("Learng python\n")  #\n 换行
file.write("Learng golang")
file.writelines("Learng shell")
file.writelines("Learng groovy\n")
file.close()

file = open("file001.txt", "a", encoding="utf-8")  #追加 ，不删原文件
file.write("study over")
file.close()

file = open("../file001.txt", "w", encoding="utf-8")  #当前文件夹的上一个文件夹下写
# file.write("ring")
file.write("Learng python\n")  #\n 换行
file.write("Learng golang")
file.writelines("Learng shell")
file.writelines("Learng groovy")
file.close()


#读文件
fd = open("file001.txt", "r", encoding="utf-8")
content = fd.read()  #读全部
line1 = fd.readline()  #读第一行  每次读一行
line2 = fd.readline()  #读第二行
fd.close()
print(content)
print(line1)  #null
print(line2) #null read() 读走了

#读文件
fd = open("file001.txt", "r", encoding="utf-8")
content = fd.readlines()
fd.close()
print(content) #['Learng python\n', 'Learng golangLearng shellLearng groovy']
