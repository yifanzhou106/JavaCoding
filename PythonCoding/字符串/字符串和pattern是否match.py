class Solution:
    def isMatch(self, s, exp):
        if not self.isValid(s, exp):
            return False
        dp = [[None for _ in range(len(exp) + 1)] for _ in range(len(s) + 1)]
        return self.process(s, exp, 0, 0, dp)

    # 要点是ei永远都不压在*上，
    # 可能性分别是当前ei+1的值是否是*

    def process(self, s, exp, si, ei, dp):
        if dp[si][ei]:
            return dp[si][ei]

        if ei == len(exp):
            dp[si][ei] = si == len(s)
            return dp[si][ei]

        # 如果ei+1不是*的时候
        if ei + 1 == len(exp) or exp[ei + 1] != '*':
            # si 必须要非尾部
            dp[si][ei] = si != len(s) and (s[si] == exp[ei] or exp[ei] == '.') and self.process(s, exp, si + 1, ei + 1,
                                                                                                dp)
            return dp[si][ei]

            # 对于每个相等的字符可以要也可以不要
        # si 必须要非尾部 不然s[si]报错
        while si != len(s) and (s[si] == exp[ei] or exp[ei] == '.'):
            if self.process(s, exp, si, ei + 2, dp):
                dp[si][ei] = True
                return dp[si][ei]
            si += 1
        dp[si][ei] = self.process(s, exp, si, ei + 2, dp)
        return dp[si][ei]

    def isValid(self, s, exp):
        for i in range(len(s)):
            if s[i] == '*' or s[i] == '.':
                return False

        for i in range(len(exp)):
            if i == 0 and exp[i] == '*':
                return False
            elif i > 0 and exp[i - 1] == '*' and exp[i] == '*':
                return False
        return True


so = Solution()
s = 'aaaaabcd'
exp = 'a*bcd'
print(so.isMatch(s, exp))

s = 'aaaaabcd'
exp = 'a*aaaaabcd'
print(so.isMatch(s, exp))

s = 'aaaaabcd'
exp = 'a*aaaaaabcd'
print(so.isMatch(s, exp))








