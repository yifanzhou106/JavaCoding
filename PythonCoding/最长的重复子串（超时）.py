class Solution(object):
    def longestDupSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        self.res = []
        self.maxLen = 0

        for i in range(len(s)):
            if (len(s) - i < len(self.res)):
                break
            self.kmp(s[i:])
        return "".join(self.res)

    def kmp(self, s):
        temp = [0 for _ in range(len(s) + 1)]
        temp[0] = -1
        for i in range(1, len(temp)):
            self.rec(s, i, i, temp)

    def rec(self, s, i, j, helper):
        if helper[i] == -1 or helper[j - 1] == -1:
            helper[j] = 0
            return
        if s[j - 1] == s[helper[i - 1]]:
            helper[j] = helper[i - 1] + 1
            self.maxLen = max(self.maxLen, helper[j])
            if helper[j] > len(self.res):
                self.res = s[j - helper[j]:j]
            return
        else:
            self.rec(s, helper[i - 1], j, helper)
