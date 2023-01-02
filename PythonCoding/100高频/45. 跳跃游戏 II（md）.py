# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
#
# 每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:
#
# 0 <= j <= nums[i]
# i + j < n
# 返回到达nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
# 示例 1:
#
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#     从下标为 0 跳到下标为 1 的位置，跳1步，然后跳3步到达数组的最后一个位置。
# 示例 2:
#
# 输入: nums = [2,3,0,1,4]
# 输出: 2

class Solution(object):


    # 用三个变量分别用来 step记录步数，cur当前步数下的右边界， next新的右边界
    # 每当i > cur ，说明当前step到达不了i，step要增加1,多一步的右边界就是next
    # 不停更新next的最大值
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 用来记录步数
        step = 0
        # 当前步数下的右边界
        cur = 0
        # 新的右边界
        next = 0

        for i in range(len(nums)):
            if i > cur:
                cur = next
                step += 1
            if i > next:
                return -1
            next = max(next, i + nums[i])
        return step

    # 以下解时间复杂度不行，直接忽略
    # def jump(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     return self.process(nums, 0)

    # def process(self, nums, start):
    #     if start >= len(nums)-1:
    #         return 0
    #     res = float('inf')
    #     for i in range(1, nums[start] + 1):
    #         res = min(res, self.process(nums, start + i) + 1)
    #     return res

    # def jump(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     dp = [float('inf') for _ in range(len(nums))]
    #     dp[-1] = 0

    #     for i in range(len(nums)-2,-1,-1):
    #         for j in range(1, nums[i] + 1):
    #             if (i + j) < len(nums):
    #                 dp[i] = min(dp[i], dp[i+j] + 1)
    #             else:
    #                 dp[i] = 1

    #     return dp[0]
