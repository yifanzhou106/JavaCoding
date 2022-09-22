class Solution:
    def findXorCount(self, nums):
        map = {}
        xor = 0
        map[0] = -1
        dp = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            xor = xor ^ nums[i]
            if xor in map:
                pre = map.get(xor)
                dp[i] = dp[pre] + 1 if pre != -1 else 1
            if i > 0:
                dp[i] = max(dp[i-1], dp[i])
            map[xor] = i
        return dp [-1]

so = Solution()
arr = [1,2,3,0,1,2,3,0]
print(so.findXorCount(arr))                                                                                                                                                                       