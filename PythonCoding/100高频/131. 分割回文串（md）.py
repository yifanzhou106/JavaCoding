# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
#
# 回文串 是正着读和反着读都一样的字符串。

# 先做一个辅助数组helper
# helper[i][j] 代表字符串从i而位置到j位置是否是回文串
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []

        helper = self.helper(s)
        self.res = []
        self.process(s, helper, 0, [])
        return self.res

# 通过dfs，递归 回文串+后序字符串
    def process(self, s, helper, i, path):
        if i == len(s):
            self.res.append(path[:])
            return
        for j in range(i, len(s)):
            if helper[i][j]:
                self.process(s, helper, j + 1, path + [s[i:j + 1]])

    def helper(self, s):
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
        for i in range(len(s) - 3, -1, -1):
            for j in range(i + 2, len(s)):
                dp[i][j] = True if s[i] == s[j] and dp[i + 1][j - 1] else False
        return dp