# 给定一个字符串(s) 和一个字符模式(p) ，实现一个支持'?'和'*'的通配符匹配。
#
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
# 两个字符串完全匹配才算匹配成功。
#
# 说明:
#
# s可能为空，且只包含从a-z的小写字母。
# p可能为空，且只包含从a-z的小写字母，以及字符?和*。
# 示例1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 示例2:
#
# 输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释:'*' 可以匹配任意字符串。

# 注意这个匹配 '*'可以单独使用
# 没有斜率优化超时
class Solution(object):
    # def isMatch(self, s, p):
    #     """
    #     :type s: str
    #     :type p: str
    #     :rtype: bool
    #     """
    #     if not self.isValid(s,p):
    #         return False
    #     dp = [[None for _ in range(len(p)+1)] for _ in range(len(s)+1)]
    #     return self.process(s,p,0,0,dp)

    # def process(self, s, p, si, pi,dp):
    #     if dp[si][pi]:
    #         return dp[si][pi]
    #     if si == len(s):
    #         if pi == len(p):
    #             dp[si][pi] = True
    #             return dp[si][pi]
    #         else:
    #             dp[si][pi] = p[pi] == '*' and self.process(s, p, si, pi+1, dp)
    #             return dp[si][pi]
    #         dp[si][pi] = False
    #         return dp[si][pi]
    #     if pi == len(p):
    #         dp[si][pi] = si == len(s)
    #         return dp[si][pi]

    #     if p[pi] != '*':
    #         dp[si][pi] = (s[si] == p[pi] or p[pi] == '?') and self.process(s, p, si+1, pi+1, dp)
    #         return dp[si][pi]

    #     res = False
    #     while si < len(s):
    #         res |= self.process(s, p, si, pi+1, dp)
    #         if res:
    #             dp[si][pi] = res
    #             return dp[si][pi]
    #         si += 1
    #     dp[si][pi] = self.process(s, p, si, pi+1, dp)
    #     return dp[si][pi]

    # 斜率优化过，发现规律，当前位置依赖右下所有 或在一起的结果
    # dp 改成先行再列
    def isMatch(self, s, p):
        if not self.isValid(s, p):
            return False
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[len(s)][len(p)] = True
        for j in range(len(p) - 1, -1, -1):
            dp[-1][j] = p[j] == '*' and dp[-1][j + 1]

        for j in range(len(p) - 1, -1, -1):
            flag = dp[-1][j]
            for i in range(len(s) - 1, -1, -1):
                if p[j] != '*':
                    dp[i][j] = (s[i] == p[j] or p[j] == '?') and dp[i + 1][j + 1]
                else:
                    flag |= dp[i][j + 1]
                    dp[i][j] |= flag

        return dp[0][0]

    def isValid(self, s, p):
        for i in range(len(s)):
            if s[i] == '?' or s[i] == '*':
                return False

        return True
