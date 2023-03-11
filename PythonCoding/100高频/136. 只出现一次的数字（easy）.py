class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
        return res