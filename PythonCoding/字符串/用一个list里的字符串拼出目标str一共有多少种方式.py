class Node:
    def __init__(self, end=None):
        self.next = [None for _ in range(26)]
        # 使用pass减枝
        self.passCount = 0
        self.end = end


class TrieTree:
    def __init__(self):
        self.root = Node()

    def insert(self, s):
        cur = self.root
        for i in range(len(s)):
            cur.passCount += 1
            index = ord(s[i]) - ord('a')
            if not cur.next[index]:
                cur.next[index] = Node()
            cur = cur.next[index]
            if i == len(s) - 1:
                cur.end = s
                cur.passCount += 1


class Solution:
    def puzzleMaxWaysCombine(self, arr, s):
        words = set()
        dp = [None for _ in range(len(s) + 1)]
        for w in arr:
            words.add(w)
        return self.process(words, s, 0, dp)

    def process(self, words, s, start, dp):
        if dp[start]:
            return dp[start]
        if start == len(s):
            dp[start] = 1
            return dp[start]
        res = 0
        for i in range(start, len(s)):
            if s[start:i + 1] in words:
                res += self.process(words, s, i + 1, dp)
        dp[start] = res
        return dp[start]

# 用前缀树优化

    def puzzleMaxWaysCombine2(self, arr, s):
        tree = TrieTree()
        dp = [None for _ in range(len(s) + 1)]
        for w in arr:
            tree.insert(w)
        return self.process2(s, tree.root, 0, dp)

    def process2(self, s, root, start, dp):
        if dp[start]:
            return dp[start]
        if start == len(s):
            dp[start] = 1
            return dp[start]
        res = 0
        cur = root
        for i in range(start, len(s)):
            asc = ord(s[i]) - ord('a')
            if not cur.next[asc]:
                break
            cur = cur.next[asc]
            if cur.end:
                res += self.process2(s, root, i + 1, dp)
        dp[start] = res
        return dp[start]


so = Solution()
s = 'aaabc'
w = ['a', 'aa', 'aaa', 'ab', 'c']
print(so.puzzleMaxWaysCombine(w, s))

s = 'aaabc'
w = ['a', 'aa', 'aaa', 'ab', 'c']
print(so.puzzleMaxWaysCombine2(w, s))