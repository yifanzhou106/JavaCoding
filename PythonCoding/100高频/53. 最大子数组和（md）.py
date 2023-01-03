# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 子数组 是数组中的一个连续部分。
#
# 示例 1：
#
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组[4,-1,2,1] 的和最大，为6 。
# 示例 2：
#
# 输入：nums = [1]
# 输出：1
# 示例 3：
#
# 输入：nums = [5,4,-1,7,8]
# 输出：23

# 只用一个sum来记录当前的累加和，如果sum小于0，就直接归零
# 用一个数字来记录最大值
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _sum = nums[0] if nums[0] > 0 else 0
        res = nums[0]
        for i in range(1,len(nums)):
            _sum += nums[i]
            res = max(res, _sum)
            if _sum < 0:
                _sum = 0
        return res