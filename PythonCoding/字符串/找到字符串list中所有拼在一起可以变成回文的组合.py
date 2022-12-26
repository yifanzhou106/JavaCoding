# 找到字符串list中所有拼在一起可以变成回文的组合
# 太恶心了，没有测
class Solution:
    def pList(self, words):
        wordMap = {}
        for i in range(len(words)):
            wordMap[words[i]] = i

        res = []
        for i in range(len(words)):
            res.append(self.process(words, i, wordMap))
        return res

    def process(self, words, i, wordMap):
        res = []
        reverseWord = words[i][::-1]
        if reverseWord == words[i]:
            res.append([i, i])
        if reverseWord in wordMap:
            res.append([i, wordMap[reverseWord]])

        rs = self.manacher(words[i])
        print(manacherRes)
        mid = len(words[i]) >> 1
        for i in range(1, mid):
            if i - rs[i] == -1:
                res = words.get(reverseWord[0:mid - i])
                if res and res != i:
                    res.append([res, i])
        for i in range(mid + 1, len(words[i])):
            if i + rs[i] == len(words[i]):
                res = words.get(reverseWord[i:mid << 1])
                if res and res != i:
                    res.append([i, res])
        return res

    def manacher(self, str):
        s = ['#']
        for c in str:
            s.append(c)
            s.append('#')
        d = [0 for _ in range(len(s))]
        c = 0
        r = -1
        res = []
        for i in range(len(s)):
            if i > r:
                c = i
                count = 1
                while (i - count) >= 0 and (i + count) < len(s) and s[(i - count)] == s[i + count]:
                    d[i] += 1
                    r = i + count
                    count += 1
                print(d[i], r)
            else:
                leftR = self.findLeft(c, r)
                leftI = self.findLeft(c, i)
                if leftI - d[leftI] > leftR:
                    d[i] = d[leftI]
                elif leftI - d[leftI] < leftR:
                    d[i] = r - i
                else:
                    c = i
                    count = r - i + 1
                    d[i] = r - i
                    while (i - count) >= 0 and (i + count) < len(s) and s[(i - count)] == s[i + count]:
                        d[i] += 1
                        r = i + count
                        count += 1

            if s[i] != '#':
                res.append((d[i] + 1) // 2)
        return res

    def findLeft(self, c, i):
        return c - (i - c)


so = Solution()
s = ['ababac']
print(so.pList(s))




