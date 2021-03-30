def solution(intervals):

    if not intervals or not intervals[0]:
        return intervals

    intervals = sorted(intervals, key = lambda x:x[0])
    print(intervals)
    res = []
    start, end  = intervals[0][0], intervals[0][1]
    for i in range(len(intervals)):
        left_pointer, right_pointer = intervals[i][0], intervals[i][1]

        if left_pointer <= end:
            end = max(end, right_pointer)
        else:
            res.append([start, end])
            start, end = left_pointer, right_pointer

    res.append([start, end])
    return res



print(solution([[15,18],[1,3],[2,6],[8,10]]))