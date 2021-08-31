def solution(intervals):

    if not intervals or not intervals[0]:
        return intervals

    #按做区间排序
    intervals = sorted(intervals, key = lambda x:x[0])
    print(intervals)
    res = []
    #第一个区间的左右两边
    start, end  = intervals[0][0], intervals[0][1]
    for i in range(1, len(intervals)):
        left_pointer, right_pointer = intervals[i][0], intervals[i][1]

        if left_pointer <= end:
            end = max(end, right_pointer)
        else:
            res.append([start, end])
            start, end = left_pointer, right_pointer

    res.append([start, end])
    return res



# print(solution([[15,18],[1,3],[2,6],[8,10]]))


#合并区间

class Solution():
    def __init__(self, section):
        self.section = section

    def solution(self):
        if not self.section or not self.section[0]:
            return self.section

        res =[]
        self.section = sorted(self.section, key=lambda x:x[0])
        start, end = self.section[0][0], self.section[0][1]
        for i in range(1, len(self.section)):
            left_point, right_point = self.section[i][0], self.section[i][1]
            if end >= left_point:
                end = max(end, right_point)
            else:
                res.append([start, end])
                start, end = left_point, right_point
        res.append([start, end])
        return res

solution_ins = Solution([[1,2], [4,6], [3,9]])
print(solution_ins.solution())