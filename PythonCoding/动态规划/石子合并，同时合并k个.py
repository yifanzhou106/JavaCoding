class Solution:
    def minCostCombination2(self, arr, K):
        # 检验是否可以有答案
        if ((len(arr) - 1) % (K - 1)) > 0:
            return -1
        preSum = [0 for _ in range(len(arr) + 1)]
        for i in range(len(arr)):
            preSum[i + 1] = preSum[i] + arr[i]
        dp = [[None for _ in range(len(arr))] for _ in range(len(arr))]
        return self.process(arr, preSum, 0, len(arr) - 1, 1, K, dp)

    def process(self, arr, preSum, L, R, part, K, dp):
        if dp[L][R]:
            return dp[L][R]
        if L == R:
            dp[L][R] = 0 if part == 1 else -1
            return dp[L][R]
        if part == 1:
            p1 = self.process(arr, preSum, L, R, K, K, dp)
            if p1 == -1:
                dp[L][R] = -1
                return dp[L][R]
            else:
                dp[L][R] = p1 + preSum[R + 1] - preSum[L]
                return dp[L][R]
        res = float('inf')
        # K-1 为了筛除一下左半边必返回-1的解
        for i in range(L, R, K - 1):
            p2 = self.process(arr, preSum, L, i, 1, K, dp)
            # 右边要分成part-1部分，而不是k-1
            p3 = self.process(arr, preSum, i + 1, R, part - 1, K, dp)
            if p2 != -1 and p3 != -1:
                res = min(res, p2 + p3)

        # 不用再支付合并代价，在part=1的时候统一支付
        dp[L][R] = res
        return dp[L][R]


so = Solution()
arr = [3, 2, 4, 1]
print(so.minCostCombination2(arr, 2))

arr = [3, 2, 5]
print(so.minCostCombination2(arr, 2))

arr = [3, 5, 1, 2, 6]
print(so.minCostCombination2(arr, 3))
arr = [3, 5, 1, 2]
print(so.minCostCombination2(arr, 3))

