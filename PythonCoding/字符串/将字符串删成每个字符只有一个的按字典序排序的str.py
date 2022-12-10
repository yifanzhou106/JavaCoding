class Solution:
    def minAlph(self, s):
        if not s or len(s) == 1:
            return s
        map = [0 for _ in range(256)]

        for c in s:
            map[ord(c)] += 1

        minIndex = 0
        for i in range(len(s)):
            asc = ord(s[i])
            map[asc] -= 1
            minIndex = i if ord(s[i]) < ord(s[minIndex]) else minIndex
            if map[asc] == 0:
                break
        return s[minIndex] + self.minAlph(s[minIndex + 1:].replace(s[minIndex], ''))


so = Solution()
str = 'dacacbca'
print(so.minAlph(str))

str = 'acbcd'
print(so.minAlph(str))

str = 'dcacadb'
print(so.minAlph(str))