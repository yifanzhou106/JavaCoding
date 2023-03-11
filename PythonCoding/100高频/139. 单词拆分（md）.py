# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。
# 请你判断是否可以利用字典中出现的单词拼接出 s 。
#
# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        words = set()
        dp = [None for _ in range(len(s) + 1)]
        for w in wordDict:
            words.add(w)
        return self.process(s, words, 0, dp)

    def process(self, s, words, i, dp):
        if dp[i] != None:
            return dp[i]
        if i == len(s):
            dp[i] = True
            return dp[i]
        p = False
        for j in range(i, len(s)):
            if s[i:j + 1] in words:
                p |= self.process(s, words, j + 1, dp)
        dp[i] = p
        return dp[i]
