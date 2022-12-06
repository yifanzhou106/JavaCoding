from functools import cmp_to_key

# 方法1 将第二个str 列出所有子序列 2^m 时间 与str1 比较在不在其中， 总共2^m *n
class Solution:
    def minStepDeleteStr2BecomeSubarrayOfStr1(self, str1, str2):
        list = []
        self.generateSubSequence(str2, list, 0, '')
        list = sorted(list, key=cmp_to_key(self.compare))

        # for s in list:
        #     if self.kmp(str1,s):
        #         print(str1,s)
        #         return len(str1) - len(s)

        for s in list:
            if s in str1:
                print(str1, s)
                return len(str1) - len(s)
        return len(str1)

    def generateSubSequence(self, s, list, start, path):
        if start == len(s):
            list.append(path)
            return
        self.generateSubSequence(s, list, start + 1, path)
        self.generateSubSequence(s, list, start + 1, path + s[start])

    def compare(self, x1, x2):
        return len(x2) - len(x1)

    def kmp(self, s1, s2):
        next = self.findNext(s2)
        i = 0
        j = 0
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1
                j += 1
            elif j == -1:
                i += 1
                j = 0
            else:
                j = next[j]
        return j == len(s2)

    def findNext(self, s):
        next = [-1 for _ in range(len(s))]
        if len(s) < 2:
            return next
        next[1] = 0
        for i in range(2, len(s)):
            cur = i - 1
            while cur != -1 and s[i - 1] != s[next[cur]]:
                cur = next[cur]
            next[i] = 0 if cur == -1 else next[cur] + 1

        return next

# 方法2 将str1 分成字串，每个字串只有插入行为变成str2，插入最少的次数就是结果
# 时间复杂度 n^2 排列字串 n*m 比较，总共 n^3*m

class Solution:
    def minStepDeleteStr2BecomeSubarrayOfStr1(self, str1, str2):
        res = len(str1)
        for i in range(len(str1)):
            for j in range(i, len(str1)):
                res = min(res, self.minCostUpdateStrDp(str1[i:j + 1], str2, 1, float('inf'), float('inf')))
        return res

    def minCostUpdateStrDp(self, str1, str2, ic, dc, rc):
        m = len(str1)
        n = len(str2)
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        dp[0][0] = rc if str1[0] != str2[0] else 0

        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + ic
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + dc

        for i in range(1, m):
            for j in range(1, n):
                if str1[i] == str2[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + dc, dp[i][j - 1] + ic, dp[i - 1][j - 1] + rc)
        return dp[-1][-1]


so = Solution()
str1 = 'abcabk'
str2 = 'abcabc'
print(so.minStepDeleteStr2BecomeSubarrayOfStr1(str1, str2))
