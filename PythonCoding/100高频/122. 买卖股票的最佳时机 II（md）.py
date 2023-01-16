# 给你一个整数数组 prices ，其中prices[i] 表示某支股票第 i 天的价格。
#
# 在每一天，你可以决定是否购买和/或出售股票。你在任何时候最多只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。
#
# 返回 你能获得的 最大 利润。


# 答案就是所有的邻近两数递增线段和
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in range(1, len(prices)):
            res += 0 if prices[i] < prices[i - 1] else prices[i] - prices[i - 1]
        return res
