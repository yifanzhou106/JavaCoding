class Solution:
    def LargestDiffAfterSort(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return 0
        bucketSize = len(nums) + 1
        _min = min(nums)
        _max = max(nums)
        if _min == _max:
            return 0
        hasNums = [False for _ in range(bucketSize)]
        mins = [float('inf') for _ in range(bucketSize)]
        maxs = [-float('inf') for _ in range(bucketSize)]

        for i in range(len(nums)):
            k = self.bucket(nums[i], len(nums), _min, _max)
            mins[k] = min(mins[k], nums[i]) if hasNums[k] else nums[i]
            maxs[k] = max((maxs[k], nums[i])) if hasNums[k] else nums[i]
            hasNums[k] = True

        res = 0
        lastMax = maxs[0]
        for i in range(1, bucketSize):
            if hasNums[i]:
                res = max(res, mins[i] - lastMax)
                lastMax = maxs[i]
        return res

    def bucket(self, n, _len, _min, _max):
        return (n - _min) * _len // (_max - _min)


so = Solution()
arr = [1, 4, 66, 34, 78, 34, 78, 98, 29]
print(so.LargestDiffAfterSort(arr))