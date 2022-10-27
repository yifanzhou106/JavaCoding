# Online Python compiler (interpreter) to run Python online.
class Solution:
    def bag(self, w, v, t):
        dp = [[0 for _ in range(t + 1)] for _ in range(len(w))]
        for i in range(t + 1):
            if i >= w[0]:
                dp[0][i] = v[0]

        for i in range(1, len(w)):
            for j in range(t + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= w[i]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - w[i]] + v[i])
        print(dp)
        return dp[-1][-1]


so = Solution()
w = [3, 2, 4, 7]
v = [5, 6, 3, 19]
print(so.bag(w, v, 11))