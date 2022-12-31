class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            res += self.twoSum(nums,i+1,len(nums)-1, -nums[i])
        return res



    def twoSum(self, nums, left, right, k):
        res = []
        l = left
        r = right
        while l < r:
            if nums[l] + nums[r] > k:
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                if l > left and nums[l] == nums[l-1]:
                    l += 1
                    continue
                res.append([-k, nums[l], nums[r]])
                l += 1
                r -= 1
        return res

