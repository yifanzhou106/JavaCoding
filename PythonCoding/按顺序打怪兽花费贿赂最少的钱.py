class Solution:
    def beatMonster1(self, status, price):
        return self.process(status, price, 0, 0)

    def process(self, status, price, i, player):
        if i == len(status):
            return 0
        if player < status[i]:
            return price[i] + self.process(status, price, i + 1, player + status[i])
        else:
            p2 = self.process(status, price, i + 1, player)
            p3 = price[i] + self.process(status, price, i + 1, player + status[i])
            return min(p2, p3)

#每格代表了在当前price下可以达到的最大能力值
#dp的最后一行第一个不是-1的数字的p就是答案
    def beatMonster2DP(self, status, price):
        pSum = sum(price)
        dp = [[-1 for _ in range(pSum + 1)] for _ in range(len(status))]

        for j in range(pSum + 1):
            if price[0] == j:
                dp[0][j] = status[0]
        for i in range(1, len(status)):
            for j in range(pSum + 1):
                if dp[i - 1][j] >= status[i]:
                    dp[i][j] = dp[i - 1][j]
                if j > price[i] and dp[i - 1][j - price[i]] != -1:
                    dp[i][j] = max(dp[i][j], status[i] + dp[i - 1][j - price[i]])
        res = 0
        for res in range(pSum):
            if dp[-1][res] != -1:
                break
        return res


so = Solution()
x = [1, 4, 5, 3, 9]
y = [4, 4, 3, 6, 12]
print(so.beatMonster1(x, y))

print(so.beatMonster2DP(x, y))
