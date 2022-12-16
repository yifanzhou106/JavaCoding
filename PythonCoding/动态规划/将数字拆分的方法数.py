class Solution:
    # 1 拆成 [1] 一种
    # 2 拆成 [1,1] [2] 两种
    # 3 拆成 [1,1,1] [1,2], [3] 三种
    # 4 拆成 [1,1,1,1] [1,1,2] [2,2] [1,3] [4] 5种
    def splitNum(self, N):
        return self.process(1, N)

    def process(self, preLimit, rest):
        if rest == 0:
            return 1
        if preLimit > rest:
            return 0
        res = 0
        for i in range(preLimit, rest + 1):
            res += self.process(i, rest - i)
        return res

    def splitNumDp(self, N):
        dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
        for i in range(N + 1):
            dp[i][0] = 1

        for i in range(N, 0, -1):
            for j in range(i, N + 1):
                ways = 0
                for k in range(i, j + 1):
                    ways += dp[k][j - k]
                dp[i][j] = ways
        return dp[1][-1]

    def splitNum2(self, N):
        return self.process2(1, N)

        # 通过dp 图的斜率优化得到

    def process2(self, preLimit, rest):
        if rest == 0:
            return 1
        if preLimit > rest:
            return 0
        res = self.process(preLimit, rest - preLimit)
        res += self.process(preLimit + 1, rest)
        return res

    def splitNumDp2(self, N):
        dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
        for i in range(N + 1):
            dp[i][0] = 1
        dp[N][N] = 1
        for i in range(N - 1, 0, -1):
            for j in range(i, N + 1):
                ways = 0
                dp[i][j] = dp[i + 1][j]
                dp[i][j] += dp[i][j - i]
        return dp[1][-1]


so = Solution()
print(so.splitNum(4))
print(so.splitNum(5))
print(so.splitNum(6))
print("***************")
print(so.splitNumDp(4))
print(so.splitNumDp(5))
print(so.splitNumDp(6))
print("***************")
print(so.splitNum2(4))
print(so.splitNum2(5))
print(so.splitNum2(6))
print("***************")
print(so.splitNumDp2(4))
print(so.splitNumDp2(5))
print(so.splitNumDp2(6))