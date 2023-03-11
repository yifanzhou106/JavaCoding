# 给定一个字符串 s 和一个字符串字典wordDict，在字符串s中增加空格来构建一个句子，使得句子中所有的单词都在词典中。
# 以任意顺序 返回所有这些可能的句子。
#
# 注意：词典中的同一个单词可能在分段中被重复使用多次。

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        words = set(wordDict)
        res = []
        self.process(s, words, 0, [], res)
        return res

    def process(self, s, words, i, path, res):
        if i == len(s):
            res.append(" ".join(path))
            return

        for j in range(i, len(s)):
            if s[i:j+1] in words:
                path.append(s[i:j+1])
                self.process(s, words, j+1, path, res)
                path.pop()

