class Solution:
    def PMinParts(self, s):
        isP = self.findIsP(s)
        return self.process(s, 0, isP)

    def process(self, s, i, isP):
        if i == len(s):
            return 0
        res = float('inf')
        for j in range(i, len(s)):
            if isP[i][j]:
                res = min(res, 1 + self.process(s, j + 1, isP))
        return res

    def findIsP(self, s):
        isP = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            isP[i][i] = True

        for i in range(len(s) - 1):
            isP[i][i + 1] = s[i] == s[i + 1]

        for j in range(2, len(s)):
            i = 0
            curj = j
            while i < len(s) and curj < len(s):
                if s[i] == s[curj]:
                    isP[i][curj] = isP[i + 1][curj - 1]
                i += 1
                curj += 1
        return isP

    def PMinPartsDP(self, s):
        isP = self.findIsP(s)
        dp = [float('inf') for _ in range(len(s) + 1)]
        dp[-1] = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if isP[i][j]:
                    dp[i] = min(dp[i], 1 + dp[j + 1])
        print(dp)
        return dp[0]

        return


so = Solution()
s = 'abacdc'
print(so.PMinParts(s))
print(so.PMinPartsDP(s))
