# 字典wordList 中从单词 beginWord和 endWord 的 转换序列 是一个按下述规格形成的序列
# beginWord -> s1-> s2-> ... -> sk：
#
# 每一对相邻的单词只差一个字母。
# 对于1 <= i <= k时，每个si都在wordList中。注意， beginWord不需要在wordList中。
# sk== endWord
# 给你两个单词 beginWord和 endWord 和一个字典 wordList ，返回 从beginWord 到endWord 的 最短转换序列 中的 单词数目 。
# 如果不存在这样的转换序列，返回 0 。

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        wordSet.add(beginWord)
        nears = self.findNears(wordSet)
        distance = self.findDistance(beginWord, wordSet, nears)

        return distance.get(endWord, 0)

    def findNears(self, wordSet):
        nears = {}

        for w in wordSet:
            nears[w] = self.findNear(wordSet, w)
        return nears

    def findNear(self, wordSet, s):
        near = []
        wList = list(s)
        for i in range(len(s)):
            for k in range(26):
                tmp = wList[i]
                wList[i] = chr(ord('a') + k)
                wStr = ''.join(wList)
                if wStr in wordSet and wStr != s:
                    near.append(wStr)
                wList[i] = tmp
        return near

    def findDistance(self, beginWord, wordSet, nears):
        distance = {}
        distance[beginWord] = 1
        q = [beginWord]
        visited = set()
        visited.add(beginWord)

        while q:
            w = q.pop(0)
            nexts = nears[w]
            for n in nexts:
                if n not in visited:
                    q.append(n)
                    visited.add(n)
                    distance[n] = distance[w] + 1
        return distance





