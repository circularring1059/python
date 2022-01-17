def lengthOfLongSubstring(str):
    start = 0
    usedChar = {}
    max_len = 0
    for i in range(len(str)):
        if str[i] in usedChar and usedChar[str[i]] >= start:
            start = usedChar[str[i]] + 1
        else:
            max_len = max(max_len, i - start + 1)
        usedChar[str[i]] = i
    print(usedChar)
    return max_len


# print(lengthOfLongSubstring("abcabcbb"))


def lengthOfLongSubstring1(str):
    dict1 = {}
    start,max_len= 0, 0
    for i in range(len(str)):
        if str[i] not in dict1:
            dict1[str[i]] = i
        else:
            if dict1[str[i]] >= start:
                max_len = max(max_len, i - start)
                start = dict1[str[i]] + 1
                dict1[str[i]] = i
            else:
                dict1[str[i]] = i
    max_len = max(max_len, len(str) - start)

    return max_len


print(lengthOfLongSubstring1("ohvhjdml"))
print(lengthOfLongSubstring1("pwwkew"))


def lengthOfLongSubstring2(str):
    max_len = 0
    for i in range(len(str)):
        dict1 = {}
        flag = False
        for j in range(i, len(str)):
            if str[j] not in dict1:
                dict1[str[j]] = j
            else:
                max_len = max(j - i , max_len)
                flag = True
                break
        if not flag:
            max_len = max(max_len, len(str) - i)
            break
    return max_len


# print(lengthOfLongSubstring2("aab"))