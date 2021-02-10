import collections
def checkInclusion(s1, s2):
    counter1 = collections.Counter(s1)
    print(counter1)
    N = len(s2)
    # 定义滑动窗口的范围是 [left, right]，闭区间，长度与s1相等
    left = 0
    right = len(s1) - 1
    # 统计窗口s2[left, right - 1]内的元素出现的次数
    counter2 = collections.Counter(s2[0:right])
    print(counter2)
    while right < N:
        # 把 right 位置的元素放到 counter2 中
        print('+' * 10)
        print(counter2)
        counter2[s2[right]] += 1
        print(counter2)
        print('+' * 10)
        # 如果滑动窗口内各个元素出现的次数跟 s1 的元素出现次数完全一致，返回 True
        if counter1 == counter2:
            print("counter1",counter1)
            print("counter2",counter2)
            print("****this return True****")
            return True
        # 窗口向右移动前，把当前 left 位置的元素出现次数 - 1
        counter2[s2[left]] -= 1
        # 如果当前 left 位置的元素出现次数为 0， 需要从字典中删除，否则这个出现次数为 0 的元素会影响两 counter 之间的比较
        if counter2[s2[left]] == 0:
            del counter2[s2[left]]
        # 窗口向右移动
        left += 1
        right += 1
    return False

