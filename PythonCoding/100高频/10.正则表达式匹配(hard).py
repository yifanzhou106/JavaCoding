class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not self.isValid(s, p):
            return False
        m = len(s)
        n = len(p)
        dp = [[None for _ in range(n + 1)] for _ in range(m + 1)]

        return self.process(s, p, 0, 0, dp)

    def process(self, s, p, si, pi, dp):
        m = len(s)
        n = len(p)
        if pi == n:
            dp[si][pi] = si == m
            return dp[si][pi]

        if dp[si][pi]:
            return dp[si][pi]

        if pi + 1 == n or p[pi + 1] != '*':
            dp[si][pi] = si < m and (s[si] == p[pi] or p[pi] == '.') and self.process(s, p, si + 1, pi + 1, dp)
            return dp[si][pi]

        res = False
        while si < m and (s[si] == p[pi] or p[pi] == '.'):
            res |= self.process(s, p, si, pi + 2, dp)
            if res:
                dp[si][pi] = res
                return dp[si][pi]
            si += 1
        res |= self.process(s, p, si, pi + 2, dp)
        dp[si][pi] = res
        return res

    def isValid(self, s, p):
        for i in range(len(s)):
            if s[i] == '*' or s[i] == '.':
                return False
        for i in range(len(p)):
            if i == 0:
                if p[i] == '*':
                    return False
            else:
                if p[i - 1] == p[i] and p[i] == '*':
                    return False
        return True