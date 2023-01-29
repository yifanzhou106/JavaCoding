# 给定一个整数数组prices，其中第prices[i]表示第i天的股票价格 。

# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
#
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。



class Solution(object):
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) <2 :
            return 0
        # i位置如果要买的最好情况
        buy = [ 0 for _ in range(len(prices))]
        # i位置如果要卖的最好情况
        sell = [ 0 for _ in range(len(prices))]
        buy[1] = max(-prices[0], -prices[1])
        sell[1] = max(0, prices[1]-prices[0])

        for i in range(2, len(prices)):
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
        return sell[-1]

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) < 2:
            return 0
        # i位置如果要买的最好情况
        buy = max(-prices[0], -prices[1])
        # i位置如果要卖的最好情况
        sell = max(0, prices[1] - prices[0])
        preSell = 0
        for i in range(2, len(prices)):
            preBuy = buy
            buy = max(buy, preSell - prices[i])
            preSell = sell
            sell = max(sell, preBuy + prices[i])
        return sell