#给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

# 设计一个算法来计算你所能获取的最大利润。你最多可以完成两笔交易。
#
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        # 记录已经卖出过一次后又买入一次的最大值
        onceSoldBuyAgainMax = -prices[0]
        # 记录只卖出一次的最大值
        onceSoldMax = 0
        res = 0
        _min = prices[0]
        for i in range(1, len(prices)):
            # 结果就是记录已经卖出过一次后又买入一次的最大值 + 当前价格的最大值
            res = max(res, onceSoldBuyAgainMax + prices[i])
            # 求出只卖出一次的最大值
            _min = min(_min, prices[i])
            onceSoldMax = max(onceSoldMax, prices[i]-_min)
            # 已经卖出过一次后又买入一次的最大值 = 只卖出一次的最大值-当前值,取最大
            onceSoldBuyAgainMax = max(onceSoldBuyAgainMax, onceSoldMax - prices[i])

        return res
