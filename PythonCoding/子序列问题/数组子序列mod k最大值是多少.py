class Solution:
    # 背包
    def arrSubsequenceMaxmodM(self, arr, m):
        _sum = sum(arr)
        n = len(arr)
        dp = [[0 for _ in range(_sum + 1)] for _ in range(n + 1)]
        res = 0
        for j in range(_sum + 1):
            dp[-1][j] = j % m
        for i in range(n - 1, -1, -1):
            for j in range(_sum + 1):
                dp[i][j] = dp[i + 1][j]
                if j + arr[i] <= _sum:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j + arr[i]])
                res = max(res, dp[i][j])
        return res

    # 每个格子代表从arr[0-i] 去mod m是否可以得出j的值，
    def arrSubsequenceMaxmodM2(self, arr, m):
        n = len(arr)
        dp = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        dp[0][arr[0] % m] = True

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j]
                cur = arr[i] % m
                if j >= cur:
                    dp[i][j] = dp[i][j] | dp[i - 1][j - cur]
                else:
                    dp[i][j] = dp[i][j] | dp[i - 1][m + j - cur]
        res = 0
        print(dp)
        for j in range(m):
            if dp[-1][j]:
                res = j
        return res


so = Solution()
arr = [3, 2, 1, 7]
print(so.arrSubsequenceMaxmodM(arr, 5))
print(so.arrSubsequenceMaxmodM2(arr, 5))


