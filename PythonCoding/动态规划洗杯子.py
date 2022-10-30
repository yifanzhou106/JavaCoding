# Online Python compiler (interpreter) to run Python online.
class Solution:
    def washCup(self, drinks, a, b):
        return self.process(drinks, a, b, 0, 0)

    def process(self, drinks, a, b, index, washline):
        if index == len(drinks) - 1:
            return min(max(drinks[index], washline) + a, drinks[index] + b)

        wash = max(drinks[index], washline) + a
        next1 = self.process(drinks, a, b, index + 1, wash)
        p1 = max(wash, next1)

        dry = drinks[index] + b
        next2 = self.process(drinks, a, b, index + 1, washline)
        p2 = max(dry, next2)

        return min(p1, p2)

    def washCupDP(self, drinks, a, b):
        washline = 0
        for d in drinks:
            washline = max(washline, d) + a
        dp = [[float('inf') for _ in range(washline + 1)] for _ in range(len(drinks))]

        for i in range(washline + 1):
            dp[-1][i] = min(max(drinks[-1], i) + a, drinks[-1] + b)

        for i in range(len(drinks) - 2, -1, -1):
            for j in range(washline + 1):
                p1 = float('inf')
                wash = max(drinks[i], j) + a
                if wash <= washline:
                    p1 = max(wash, dp[i + 1][wash])

                p2 = drinks[i] + b
                p2 = max(p2, dp[i + 1][j])

                dp[i][j] = min(p1, p2)
        return dp[0][0]


so = Solution()
d = [1, 1, 5, 5, 7, 10, 12, 12, 12, 12, 12, 12, 15]
a = 3
b = 10
print(so.washCup(d, a, b))
print(so.washCupDP(d, a, b))