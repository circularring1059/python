# from collections import Counter
#
# array = [1, 1, 2, 6]
#
# coun = Counter(array)
#
# if 1 in coun:
#     print(coun.get(1))


# def com_str(str1, str2):
#     i = 0
#     while i < len(str1) and i < len(str2):
#         if str1[i] > str2[i]:
#             return str1
#
#         if str1[i] < str2[i]:
#             return str2
#         else:
#             i += 1
#
#     if len(str1) == i:
#         return str2
#     else:
#         return str1
#
#
# print(com_str("cc", "vv"))
#
# class Person:
#     def __init__(self,tall):
#         self.__tall = tall
#
# person = Person(169)
#
# person.__tall = 168
#
# print(dir(person))
# print(person.__tall)
# print(person._Person__tall)
#
# str1 = "ringyuanrgnhj"
#
# dict_tmp = {}
# for i in range(len(str1)):
#     if str1[i] not in dict_tmp:
#         dict_tmp[str1[i]] = 1
#     else:
#         dict_tmp[str1[i]] += 1
# print(dict(sorted(dict_tmp.items(), key=lambda x:x[1], reverse=True)))
#
# print(str1.find("r"))

