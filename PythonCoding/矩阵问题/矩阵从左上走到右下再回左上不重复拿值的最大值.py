class Solution:

    def goThroughMatrixMaxPath(self, metrix):

        m = len(metrix)
        n = len(metrix[0])
        dp = [[[None for _ in range(m)] for _ in range(n)] for _ in range(m)]
        return self.process(metrix, m, n, 0, 0, 0, dp)

    # bc = ar +ac -br
    def process(self, metrix, m, n, ar, ac, br, dp):
        if dp[ar][ac][br]:
            return dp[ar][ac][br]
        if ar == m - 1 and ac == n - 1:
            dp[ar][ac][br] = metrix[ar][ac]
            return dp[ar][ac][br]

        aRightBRight = -float('inf')
        aRightBDown = -float('inf')
        aDownBRight = -float('inf')
        aDownBDown = -float('inf')
        bc = ar + ac - br
        if ac + 1 < n and bc + 1 < n:
            aRightBRight = self.process(metrix, m, n, ar, ac + 1, br, dp)
        if ac + 1 < n and br + 1 < m:
            aRightBDown = self.process(metrix, m, n, ar, ac + 1, br + 1, dp)
        if ar + 1 < m and bc + 1 < n:
            aDownBRight = self.process(metrix, m, n, ar + 1, ac, br, dp)
        if ar + 1 < m and br + 1 < m:
            aDownBDown = self.process(metrix, m, n, ar + 1, ac, br + 1, dp)

        bestNext = max(aRightBRight, aRightBDown, aDownBRight, aDownBDown)

        if ar == br:
            dp[ar][ac][br] = metrix[ar][ac] + bestNext
            return dp[ar][ac][br]
        dp[ar][ac][br] = metrix[ar][ac] + metrix[br][bc] + bestNext
        return dp[ar][ac][br]


so = Solution()
M = [[1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
     [1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]]

print(so.goThroughMatrixMaxPath(M))