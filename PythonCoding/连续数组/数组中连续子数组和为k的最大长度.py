class Solution:
    def longestSubarraySum(self, nums, k):
        map = {}
        cSum = 0
        map[0] = -1
        res = -1
        for i in range(len(nums)):
            cSum += nums[i]
            if cSum - k in map:
                res = max(res, i - (map[cSum - k] + 1) + 1)

            if cSum not in map:
                map[cSum] = i

        return res


so = Solution()
arr = [7, 3, 2, 1, 1, 7, -6, -1, 7]
print(so.longestSubarraySum(arr, 7))