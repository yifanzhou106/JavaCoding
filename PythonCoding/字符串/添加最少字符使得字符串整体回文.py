class Solution:
    def huiwen(self, s):
        newS = ['#']
        for c in s:
            newS.append(c)
            newS.append('#')
        print(''.join(newS))
        return self.process(newS, 0, len(newS) - 1)

    def process(self, s, left, right):
        if left == right:
            return 0
        if s[left] == s[right]:
            return self.process(s, left + 1, right - 1)
        else:
            return min(1 + self.process(s, left + 2, right), 1 + self.process(s, left, right - 2))

    def huiwenDp(self, s):
        newS = ['#']
        for c in s:
            newS.append(c)
            newS.append('#')
        dp = [[float('inf') for _ in range(len(newS))] for _ in range(len(newS))]
        for i in range(len(newS)):
            dp[i][i] = 0
        for i in range(len(newS) - 1):
            dp[i][i + 1] = 0 if newS[i] == newS[i + 1] else 1
        for j in range(2, len(newS)):
            cur = j
            i = 0
            while cur < len(newS):
                if newS[i] == newS[cur]:
                    dp[i][cur] = dp[i + 1][cur - 1]
                else:
                    dp[i][cur] = 1 + min(dp[i + 2][cur], dp[i][cur - 2])
                i += 1
                cur += 1
        return dp[0][-1]


so = Solution()
s = 'baabacc'
print(so.huiwen(s))
print(so.huiwenDp(s))