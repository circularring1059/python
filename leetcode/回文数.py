def isPalindrome(arg):
    arg = str(arg)

    return arg == arg[::-1]

print(isPalindrome(232))

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
