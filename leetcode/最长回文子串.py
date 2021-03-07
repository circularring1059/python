def longestPalindrome(str):
    def expand(str,left,right):
        while left >= 0 and right <len(str) and str[left] == str[right]:
            left -= 1
            right += 1
        return right -left-1
    start_pointer =0
    end_pointer = 0
    for i in range(len(str)):
        length1 = expand(str,i,i)
        length2 = expand(str,i,i+1)
        max_length = max(length1, length2)

        if max_length > end_pointer - start_pointer:
            start_pointer = int(i - (max_length-1)/2)
            end_pointer = int(i + max_length/2)
    return str[start_pointer:end_pointer+1]


print(longestPalindrome("yuuy"))

