# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
# 请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
#
# 示例 1：
#
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例2：
#
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

from functools import cmp_to_key

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        arr = [None for _ in range(len(intervals))]
        for i in range(len(arr)):
            arr[i] = Node(intervals[i][0], intervals[i][1])
        arr = sorted(arr, key=cmp_to_key(self.compator))
        res = []
        for o in arr:
            if not res:
                res.append([o.start,o.end])
            else:
                pre = res[-1]
                if o.start <= pre[1]:
                    res[-1] = [pre[0],max(o.end, pre[1])]
                else:
                    res.append([o.start,o.end])
        return res


    def compator(self, o1, o2):
        return o1.start - o2.start

