import re

"""
    {m,n}    Matches from m to n repetitions of the preceding RE.
    {m,n}?   Non-greedy version of the above.
"""

#{n} 匹配n次
print(re.match("[0-9]{1}", "1")) #匹配一次
print(re.match("[0-9]{1}", "123"))  #只匹配第一个
print(re.match("[0-9]{2}", "123"))  #匹配两个
print(re.match("[0-9]{4}", "123"))  #None

#{m,}  最少匹配m次
print(re.match("[0-9]{2,}", "1")) #None
print(re.match("[0-9]{2,}", "123")) #<re.Match object; span=(0, 3), match='123'>

#{m,n} 最少m次，最多n次
print(re.match("[0-9]{2,3}", "1234")) #<re.Match object; span=(0, 3), match='123'>
print(re.match("[0-9]{2,4}", "1234")) #<re.Match object; span=(0, 4), match='1234'>
print(re.match("[0-9]{2,4}", "1")) #None
print(re.match("[0-9]{2,4}", "12345")) #<re.Match object; span=(0, 4), match='1234'>
print(re.match("[0-9]{2,4}$", "12345")) #None  不能匹配，加了$符只能匹配四位

"""注意 ：
1》* + ？ {m,n}优先匹配多个(贪婪匹配), 后面加上？变成非贪婪匹配  
2》qq="12345",pattern=[0-9]{n}  当n <= len(qq),可以匹配前n位，若只想匹配n位数的qq,大于n位数的qq不匹配（返回None),需要加上结尾符:%
"""