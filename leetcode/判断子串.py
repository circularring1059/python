# import collections
# def checkInclusion(s1, s2):
#     counter1 = collections.Counter(s1)
#     print(counter1)
#     N = len(s2)
#     # 定义滑动窗口的范围是 [left, right]，闭区间，长度与s1相等
#     left = 0
#     right = len(s1) - 1
#     # 统计窗口s2[left, right - 1]内的元素出现的次数
#     counter2 = collections.Counter(s2[0:right])
#     while right < N:
#         # 把 right 位置的元素放到 counter2 中
#         counter2[s2[right]] += 1
#         # 如果滑动窗口内各个元素出现的次数跟 s1 的元素出现次数完全一致，返回 True
#         if counter1 == counter2:
#             return True
#         # 窗口向右移动前，把当前 left 位置的元素出现次数 - 1
#         counter2[s2[left]] -= 1
#         # 如果当前 left 位置的元素出现次数为 0， 需要从字典中删除，否则这个出现次数为 0 的元素会影响两 counter 之间的比较
#         if counter2[s2[left]] == 0:
#             del counter2[s2[left]]
#         # 窗口向右移动
#         left += 1
#         right += 1
#     return False
#
# print(checkInclusion("yuy",'yyu'))


# def is_substr(str1, str2):
#     for i in range(len(str2)):
#         if i + len(str1) <= len(str2):
#             if str1[0] == str2[i]:
#                 start = i
#                 end = i + len(str1)
#                 if str1 == str2[start: end]:
#                     return True
#         else:
#             break
#     return False
#
# print(is_substr('yuan', 'wyuan'))

# def is_substr(str1, str2):
#     i, lenth_str1 = 0, len(str1)
#     for j in str2:
#         if i +1 == lenth_str1:
#             if j == str1[i]:
#                 return True
#
#         if j == str1[i]:
#             i += 1
#     return False
#
# print(is_substr('yuy', "yyu"))

# def is_substr(str1, str2):
#     i, j = 0, 0
#     while i < len(str1) and j < len(str2):
#         if str1[i] == str2[j]:
#             i += 1
#         j += 1
#     return i == len(str1)
#
# print(is_substr('yay', 'yyaun'))


