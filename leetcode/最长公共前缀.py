def longestCommonPrefix(nums):
    if not nums:
        return " "

    mins = min(nums)
    maxs = max(nums)
    for i, j in enumerate(mins):
        if maxs[i] != mins[i]:
            return mins[:i]
    return mins

print(longestCommonPrefix(["abc", "a", "c"]))



