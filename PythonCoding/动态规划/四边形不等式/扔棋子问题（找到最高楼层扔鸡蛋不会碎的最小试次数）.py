# 给定楼层N (0-N) 有k个棋子， 从0层上扔棋子一定不会碎，从i上扔可能会碎
# 求出最高不会碎的楼层的最小尝试数量
class Solution:
    # 按照第一个棋子扔的位置来分情况
    def building2(self, N, k):
        dp = [[None for _ in range(k + 1)] for _ in range(N + 1)]
        return self.process(N, k, dp)

    def process(self, rest, k, dp):
        if dp[rest][k]:
            return dp[rest][k]
        if rest == 0:
            dp[rest][k] = 0
            return dp[rest][k]
        if k == 1:
            dp[rest][k] = rest
            return dp[rest][k]

        res = rest
        for i in range(1, rest + 1):
            # 棋子扔在了i层上
            # self.process(i-1,k-1,dp) 代表碎了
            # self.process(rest-i,k,dp) 代表没碎
            # 两者中最差的情况找最小值
            res = min(res, max(self.process(i - 1, k - 1, dp), self.process(rest - i, k, dp)))
        # 当前等于后续+1
        dp[rest][k] = res + 1
        return dp[rest][k]


so = Solution()

print(so.building2(105, 2))
print(so.building2(100, 5))

