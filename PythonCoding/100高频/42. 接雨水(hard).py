# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 数组容器装水问题

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n < 3:
            return 0
        left = 0
        right = n - 1
        leftMax = height[0]
        rightMax = height[-1]
        res = 0
        while left < right:
            if height[left] < min(leftMax, rightMax):
                res += min(leftMax, rightMax) - height[left]

            if height[right] < min(leftMax, rightMax):
                res += min(leftMax, rightMax) - height[right]
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return res