class Solution:
    def bag(self, w, v):
        if not v:
            return 0
        return self.rec(w, v, 0)

    def rec(self, rest, v, i):
        if i == len(v):
            return 1
        if rest - v[i] >= 0:
            return self.rec(rest - v[i], v, i + 1) + self.rec(rest, v, i + 1)

        return self.rec(rest, v, i + 1)

    def bag2(self, w, v):
        if not v:
            return 0
        return self.process(w, v, 0)

    def process(self, rest, v, i):
        if rest < 0:
            return -1
        if i == len(v):
            return 1

        n1 = self.process(rest - v[i], v, i + 1)
        n2 = self.process(rest, v, i + 1)

        return n2 + (0 if n1 == -1 else n1)

    def bagDp(self, w, v):
        dp = [[0 for _ in range(w + 1)] for _ in range(len(v) + 1)]
        for j in range(w + 1):
            dp[-1][j] = 1
        for i in range(len(v) - 1, -1, -1):
            for j in range(w + 1):
                if j - v[i] >= 0:
                    dp[i][j] = dp[i + 1][j - v[i]] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]
        return dp[0][w]

# 优化压缩空间
    def bagDp2(self, w, v):
        dp = [[0 for _ in range(w + 1)] for _ in range(2)]
        for i in range(w + 1):
            dp[1][i] = 1
        for i in range(len(v) - 1, -1, -1):
            for j in range(w + 1):
                if j - v[i] >= 0:
                    dp[0][j] = dp[1][j - v[i]] + dp[1][j]
                else:
                    dp[0][j] = dp[1][j]
            for j in range(w + 1):
                dp[1][j] = dp[0][j]

        return dp[1][w]


so = Solution()
v = [3, 1, 2, 6, 8]
print(so.bag(10, v))
print(so.bag2(10, v))
print(so.bagDp(10, v))
print(so.bagDp2(10, v))
