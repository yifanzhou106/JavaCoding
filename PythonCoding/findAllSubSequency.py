class Solution:
    def findAllSubSequency(self, s):
        res = []
        self.rec(s, res, [], 0)
        return res

    def rec(self, s, res, temp, i):
        if i == len(s):
            res.append(temp[:])
            return

        self.rec(s, res, temp + [s[i]], i + 1)
        self.rec(s, res, temp, i + 1)


so = Solution()

print(so.findAllSubSequency("abc"))