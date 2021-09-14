class Solution():

    def insert_merge(self, array, newInterval):
        res = []
        i = 0
        while i < len(array):  # 去除 列表里的[]
            if not array[i]:
                array.remove(array[i])
            else:
                i += 1
        if not array:
            array.append(newInterval)
            return array
        array.append(newInterval)
        sorted(array, key=lambda x: x[0])
        start, end = array[0][0], array[0][1]
        for i in range(1, len(array)):  # 从第1个开始，少一次循环
            left_point, reght_point = array[i][0], array[i][1]
            if left_point <= end:
                end = max(end, array[i][1])
            else:
                res.append([start, end])
                start, end = array[i][0], array[i][1]
        res.append([start, end])
        return res


insert_merge_ins = Solution()
print(insert_merge_ins.insert_merge([[], []], [1, 8]))
