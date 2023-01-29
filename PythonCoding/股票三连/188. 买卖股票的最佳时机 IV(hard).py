# 给定一个整数数组prices ，它的第 i 个元素prices[i] 是一支给定的股票在第 i 天的价格。
#
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        if k >= len(prices) // 2:
            return self.findMaxProfit(prices)

        dp = [[0 for _ in range(k + 1)] for _ in range(len(prices))]
        for j in range(1, k+1):
            t = dp[0][j-1] - prices[0]
            for i in range(1, len(prices)):
                t = max(t, dp[i][j-1] - prices[i])
                dp[i][j] = max(dp[i-1][j], t + prices[i])
        return dp [-1][-1]



    def findMaxProfit(self, prices):
        res = 0

        for i in range(1,len(prices)):
            res += max(prices[i] - prices[i-1], 0)
        return res

