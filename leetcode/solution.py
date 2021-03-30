def solution(intervals):

    if not intervals or not intervals[0]:
        return intervals

    intervals = sorted(intervals, key = lambda x:x[0])
    res = []
    start, end  = intervals[0][0], intervals[0][1]
    for i in range(len(intervals)):
        s, e = intervals[i][0], intervals[i][1]

        if s <= end:
            end =max(end, e)
        else:
            res.append([start, end])
            start, end = s, e
    res.append([start, end])
    return res



print(solution([[1,3],[2,6],[8,10],[15,18]]))