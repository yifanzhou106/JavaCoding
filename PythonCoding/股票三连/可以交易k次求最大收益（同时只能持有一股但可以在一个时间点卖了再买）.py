# 如果可交易次数大于arr的大小一半的时候，可以直接把所有增加线段的值加一起就是答案

class Solution:

    def stock3(self, arr, k):
        if k > len(arr) // 2:
            return self.stock2(arr)

        dp = [[0 for _ in range(k + 1)] for _ in range(len(arr))]
        res = 0
        for j in range(1, k + 1):
            # 原本需要 每次求一遍 max(dp[0...i][j-1]-arr[i])， 通过先col再row，用一个t来避免重复计算
            t = dp[0][j - 1] - arr[0]
            for i in range(1, len(arr)):
                t = max(t, dp[i][j - 1] - arr[i])
                dp[i][j] = max(dp[i - 1][j], t + arr[i])
                res = max(res, dp[i][j])
        return res

    def stock2(self, arr):
        res = 0
        for i in range(1, len(arr)):
            res += 0 if arr[i] < arr[i - 1] else arr[i] - arr[i - 1]
        return res


so = Solution()
n = [4, 1, 231, 21, 12, 312, 312, 3, 5, 2, 423, 43, 146]

print(so.stock3(n, 3))
print(so.stock3(n, 100))
