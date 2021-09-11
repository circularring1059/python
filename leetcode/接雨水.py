class Solution():

    def trap(self, array):
        res = 0
        for i in range(len(array)):
            max_left, max_right = 0, 0
            for j in range(i):
                max_left = max(max_left, array[j])

            for j in range(i, len(array)):
                max_right = max(max_right, array[j])

            if min(max_left, max_right) > array[i]:
                res += min(max_left, max_right) - array[i]
        return res

    def trap1(self, array):
        res =0
        max_left = [0] * len(array)
        max_right = [0] * len(array)
        max_left[0] = array[0]
        max_right[len(array)-1] = array[len(array)-1]
        for i in range(1, len(array)):
            max_left[i] = max(array[i], max_left[i-1])

        for j in range(len(array)-2, -1, -1):
            max_right[j] = max(array[j], max_right[j+1])

        for i in range(len(array)):
            if min(max_left[i], max_right[i]) > array[i]:
                res += min(max_left[i], max_right[i]) - array[i]
        return res

    def trap2(self, array):
        res = 0
        left, right = 0, len(array) -1
        max_left = array[0]
        max_right = array[len(array)-1]
        while left <= right:
            max_left = max(array[left], max_left)
            max_right = max(array[right], max_right)

            if max_left < max_right:
                res += max_left - array[left]
                left += 1
            else:
                res += max_right - array[right]
                right -= 1

        return res


soution_ins = Solution()
print(soution_ins.trap([0,1,0,2]))
print(soution_ins.trap1([0,1,0,2]))
print(soution_ins.trap2([0,1,0,2]))
