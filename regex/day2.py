import re
"""
    "+"      Matches 1 or more (greedy) repetitions of the preceding RE.
    "?"      Matches 0 or 1 (greedy) of the preceding RE.
    *?,+?,?? Non-greedy versions of the previous three special characters.
    {m,n}    Matches from m to n repetitions of the preceding RE.
    {m,n}?   Non-greedy version of the above.
    "\\"     Either escapes special characters or signals a special sequence.
    []       Indicates a set of characters.
"""

pattern1  = "[0-9]" # 匹配 0 ~ 9
print(re.search(pattern1,"hello1word2"))  #print(re.search(pattern1,"hello1word2"))
print(re.findall(pattern1,"hello1word2"))  #['1', '2']


pattern2 = "[a-z]"  #匹配a-z

print(re.search(pattern2,"circularring1010")) #<re.Match object; span=(0, 1), match='c'>
print(re.findall(pattern2,"circularring1010")) #['c', 'i', 'r', 'c', 'u', 'l', 'a', 'r', 'r', 'i', 'n', 'g']

print("*" * 16)
# ”*" 匹配0或n个
pattern3 = "[0-9]"
print(re.search("[0-9]*",""))  #匹配0个
print(re.search("[0-9]*","12"))  #匹配2个
print(re.search("[0-9]*","354363"))  #匹配7个
print(re.findall("[0-9]*","354363"))  #['354363', '']

print("+" * 16)
#+ 匹配1个或n个
print(re.search("[0-9]+", "")) #None  0个匹配
print(re.search("[0-9]+", "7")) #  1个匹配
print(re.search("[0-9]+", "8435034")) # 8个匹配
print(re.findall("[0-9]+", "8435034")) # ['8435034']

print("?" * 16)
#? 匹配0个或1个
print(re.search("[0-9]?", "")) #  0个匹配
print(re.search("[0-9]?", "7")) #  1个匹配
print(re.search("[0-9]?", "8435034")) #  1个匹配
print(re.findall("[0-9]?", "8435034")) #  ['8', '4', '3', '5', '0', '3', '4', '']