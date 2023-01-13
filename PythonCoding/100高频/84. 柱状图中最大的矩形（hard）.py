# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10

# 单调栈
class Item:
    def __init__(self, val, index):
        self.val = val
        self.indexs = [index]
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        stack = [Item(heights[0],0)]
        lessThan = [None for _ in range(len(heights))]
        for i in range(1, len(heights)):
            while stack and heights[i] < stack[-1].val:
                item = stack.pop()
                left = -1
                if stack:
                    left = stack[-1].indexs[-1]
                for index in item.indexs:
                    lessThan[index] = [left, i]
            if not stack or stack[-1].val < heights[i]:
                stack.append(Item(heights[i],i))
            else:
                stack[-1].indexs.append(i)
        while stack:
            right = len(heights)
            item = stack.pop()
            left = -1
            if stack:
                left = stack[-1].indexs[-1]
            for index in item.indexs:
                lessThan[index] = [left, right]
        res = 0
        for i in range(len(lessThan)):
            res = max(res, (lessThan[i][1] - lessThan[i][0]-1)*heights[i] )
        return res



