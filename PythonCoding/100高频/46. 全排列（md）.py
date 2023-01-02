# 给定一个不含重复数字的数组
# nums ，返回其
# 所有可能的全排列 。你可以
# 按任意顺序
# 返回答案。

# 直接dfs
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        isVisited = [False for _ in range(len(nums))]
        res = []
        self.process(nums, res, [], isVisited, 0)
        return res

    def process(self, nums, res, path, isVisited, start):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if not isVisited[i]:
                isVisited[i] = True
                self.process(nums, res, path+[nums[i]], isVisited, i + 1)
                isVisited[i] = False
