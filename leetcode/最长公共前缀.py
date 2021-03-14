def longestCommonPrefix(nums):
    if not nums:
        return "不存在"

    mins = min(nums)
    maxs = max(nums)
    for i, j in enumerate(mins):
        if maxs[i] != mins[i]:
            return mins[:i]
    return mins

print(longestCommonPrefix(["abc", "cd"]))