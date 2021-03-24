def strStr(haystak, needle):

    if haystak == needle:
        return 0
    i, length_needle = 0, len(needle)
    while i + length_needle <= len(haystak):
        if haystak[i:i+length_needle] == needle:
            return 0
        else:
            i += 1
    else:
        return -1

print(strStr("circularring1010", "ing"))