# 给你一个整数数组nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.process(nums, 0, [], res)
        return res

    def process(self, nums, start, path, res):
        if start == len(nums):
            res.append(path[:])
            return
        if start == 0 or nums[start] != nums[start - 1]:
            path.append(nums[start])
            self.process(nums, start + 1, path, res)
            path.pop()
        self.process(nums, start + 1, path, res)
