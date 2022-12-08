# 可以将字符串拆分出最多异或和为0的子字符串的数量
class Solution:
    def mostXorZeroSubarrayDivision(self, nums):
        dp = [0 for _ in range(len(nums))]
        map = {}
        map[0] = -1
        xor = 0

        for i in range(len(nums)):
            xor = xor ^ nums[i]
            if xor in map:
                pre = map[xor]
                dp[i] = 1 if pre == -1 else dp[pre] + 1
            if i > 0:
                dp[i] = max(dp[i], dp[i - 1])
            map[xor] = i
        return dp[-1]


so = Solution()
nums = [1, 2, 3, 0, 4, 3, 2, 1, 0, 2, 1, 3]
print(so.mostXorZeroSubarrayDivision(nums))