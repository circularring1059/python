#方法一
def isPalindrome(arg):
    arg = str(arg)

    return arg == arg[::-1]

print(isPalindrome(232))

#方法二
def isPalindrome1(arg):
    arg = str(arg)
    left = 0
    right = len(arg)-1
    while left < right:
        if arg[left] != arg [right]:
            return False
        left += 1
        right -= 1
    return True

print(isPalindrome1(232))

#方法三
def isPalindrome2(arg):
    arg = str(arg)
    if len(arg) == 1:
        return True

    if arg[0] != arg [-1]:
        return False
    return isPalindrome(arg[1:-1])

print(isPalindrome2("yuuy"))
