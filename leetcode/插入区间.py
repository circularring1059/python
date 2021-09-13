class Solution():

    def insert_merge(self, array, newInterval):
        res = []
        if not array:
            array.append(newInterval)
            return array
        # i = len(array)-1
        # while i < 0:
        #     if not  array[i]:
        #         ar


        #排序
        sorted(array, key=lambda x: x[0])
        start, end = array[0][0], array[0][1]
        for i in range(0, len(array)):
            left_point, reght_point = array[i][0], array[i][1]
            if left_point <= end:
                end = max(end, array[i][1])
            else:
                res.append([start, end])
                start, end = array[i][0], array[i][1]
        res.append([start, end])
        return res

insert_merge_ins = Solution()
print(insert_merge_ins.insert_merge([],[1,2]))




