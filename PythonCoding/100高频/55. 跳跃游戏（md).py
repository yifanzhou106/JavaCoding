# 给定一个非负整数数组nums ，你最初位于数组的 第一个下标 。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个下标。

# 示例1：
#
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
# 示例2：
#
# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

class Solution(object):
    # 此题只看能否到达最右
    # 可以只用一个变量maxPath 来记录可以到达的最右
    # 如果当前i < maxPath，说明到不了，直接返回false
    # 再更新可以到达的最右边界
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxPath = 0
        for i in range(len(nums)):
            if maxPath < i:
                return False
            maxPath = max(maxPath,i + nums[i])
            if maxPath >= len(nums)-1:
                return True
        return True

    # 以下解时间复杂度不行，直接忽略

    # def canJump(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     return self.process(nums, 0)


    # def process(self, nums, start):
    #     if start >= len(nums)-1:
    #         return True

    #     res = False
    #     for i in range(1, nums[start] + 1):
    #         res |= self.process(nums, start + i)
    #     return res

    # def canJump(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     dp = [False for _ in range(len(nums))]
    #     dp[-1] = True

    #     for i in range(len(nums)-2,-1,-1):
    #         for j in range(1, nums[i] + 1):
    #             if (i + j) < len(nums):
    #                 dp[i] |= dp[i+j]
    #             else:
    #                 dp[i] = True
    #     return dp[0]






