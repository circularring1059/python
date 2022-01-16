def lengthOfLongSubstring(str):
    start = 0
    usedChar = {}
    max_len = 0
    for i in range(len(str)):
        if str[i]  in usedChar and usedChar[str[i]] >= start:
            start = usedChar[str[i]] +1
        else:
            max_len = max(max_len, i-start+1)
        usedChar[str[i]] = i
    print(usedChar)
    return max_len
print(lengthOfLongSubstring("abcabcbb"))


def lengthOfLongSubstring1(str):
    max_len = 0
    dict1 = {}
    start = 0
    for i in range(len(str)):
        if str[i] not in dict1:
            dict1[str[i]] = i
        else:
            max_len = max(max_len, i-start)
            if dict1[str[i]] > start:
                dict1[str[i]] = i
                start = i
            else:
                start = dict1[str[i]] + 1
                dict1[str[i]] = i

    max_len = max(max_len, len(str)-start)

    return max_len

print(lengthOfLongSubstring1("abcabcbb"))
