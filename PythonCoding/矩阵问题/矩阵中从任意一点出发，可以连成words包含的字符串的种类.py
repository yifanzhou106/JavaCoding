

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

    def wordsPathInMatrix(self, M, words):
        t = TrieTree()
        for w in words:
            t.insert(w)
        self.res = set()
        for i in range(len(M)):
            for j in range(len(M[0])):
                cur = t.root
                self.process(M, cur, i, j)
        return list(self.res)

    def process(self, M, node, i, j):
        if i < 0 or j < 0 or j == len(M) or j == len(M[0]):
            return 0
        if M[i][j] == '0' or node.passCount == 0:
            return 0

        asc = ord(M[i][j]) - ord('a')
        if not node.next[asc]:
            return 0
        nextNode = node.next[asc]
        fix = 0
        # 不走回头路
        M[i][j] = '0'
        if nextNode.end:
            self.res.add(nextNode.end)
            fix += 1
        for k in range(26):
            if nextNode.next[k]:
                if i > 0:
                    fix += self.process(M, nextNode, i - 1, j)
                if i < len(M) - 1:
                    fix += self.process(M, nextNode, i + 1, j)
                if j > 0:
                    fix += self.process(M, nextNode, i, j - 1)
                if j < len(M[0]) - 1:
                    fix += self.process(M, nextNode, i, j + 1)
        M[i][j] = chr(asc + ord('a'))
        # 将完成的node里的pass减少完成数，以后就可以不用重复遍历
        nextNode.passCount -= fix
        return fix


so = Solution()
arr = [['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']]
words = ["oath", "pea", "eat", "rain"]
print(so.wordsPathInMatrix(arr, words))
