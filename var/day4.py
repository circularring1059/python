#string
str1 = "hello"
str2 = "World"
print(str1+str2)  #helloWorld  拼接
print(str1,str2, sep="")
print("{}{}".format(str1, str2))

print('''*
         helloWorld
         *''')

for i in str1: #可迭代的 可遍历
    print(i)

#join
str3 = "#".join(str2)
print(str3) #W#o#r#l#d

#split rsplit
print(str1.split("e")) #['h', 'llo']
print(str1.split("l")) #['he', '', 'o']
print(str1.rsplit("l", 1)) #切割一次

print("hello".startswith("h")) #True
print("hello".endswith("lo")) #True

print("hello".index("he")) #1
print("hello".rindex("h")) #1

#切片
str4 = "ring"
print(str4[0:5])  #这种超过引索是不跑异常的
print(str4[-4::2])

#replace
print("hellloworld".replace('w', "W", 1)) #替换一次
print("hellloworldw".replace('w', "W")) #全部替换

#strip
print("  hello  ".strip())  #移除两端空格


#format
str6 = "你好，大蟒蛇"
print(len(str6))
print(format(str6, "*>20")) #**************你好，大蟒蛇
print(format(str6, "*^20"))  #居中
print(format(str6, "*<20"))  #左对齐
print(format(3.1415, ".2f"))  #保留两位小数
print(format(3.1415, ".2%")) #314.15%
print(format(3.1415, "^10.2%")) #占10个字符居中对齐

