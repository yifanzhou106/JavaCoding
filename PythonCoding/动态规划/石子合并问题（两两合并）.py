class Solution:
    def minCostCombination1(self, arr):
        preSum = [0 for _ in range(len(arr) + 1)]
        for i in range(len(arr)):
            preSum[i + 1] = preSum[i] + arr[i]
        dp = [[None for _ in range(len(arr))] for _ in range(len(arr))]
        return self.process(arr, preSum, 0, len(arr) - 1, dp)

    def process(self, arr, preSum, L, R, dp):
        if dp[L][R]:
            return dp[L][R]
        if L == R:
            dp[L][R] = 0
            return dp[L][R]

        res = float('inf')

        for i in range(L, R):
            left = self.process(arr, preSum, L, i, dp)
            right = self.process(arr, preSum, i + 1, R, dp)
            res = min(res, left + right)

        dp[L][R] = res + preSum[R + 1] - preSum[L]
        return dp[L][R]


so = Solution()
arr = [3, 2, 4, 1]
print(so.minCostCombination1(arr))

arr = [3, 2, 5]
print(so.minCostCombination1(arr))

