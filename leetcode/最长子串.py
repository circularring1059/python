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
print(lengthOfLongSubstring("abcbdf "))