class Solution:
    def crossCombination(self, s1, s2, s3):
        if len(s3) != len(s1) + len(s2):
            return False
        return self.process(s1, s2, s3, 0, 0, 0)

    def process(self, s1, s2, s3, i, j, k):
        if k == len(s3):
            return True
        if i == len(s1):
            if s2[j] == s3[k]:
                return self.process(s1, s2, s3, i, j + 1, k + 1)
            else:
                return False
        if j == len(s2):
            if s1[i] == s3[k]:
                return self.process(s1, s2, s3, i + 1, j, k + 1)
            else:
                return False

        if s1[i] == s3[k] and s2[j] != s3[k]:
            return self.process(s1, s2, s3, i + 1, j, k + 1)
        elif s2[j] == s3[k] and s1[i] != s3[k]:
            return self.process(s1, s2, s3, i, j + 1, k + 1)
        elif s1[i] == s3[k] and s2[j] == s3[k]:
            return self.process(s1, s2, s3, i + 1, j, k + 1) | self.process(s1, s2, s3, i, j + 1, k + 1)
        return False

    def crossCombinationDP(self, s1, s2, s3):
        if len(s3) != len(s1) + len(s2):
            return False
        dp = [[[False for _ in range(len(s3) + 1)] for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                dp[i][j][-1] = True
        for i in range(len(s1)):
            for k in range(len(s3) - 1, -1, -1):
                dp[i][-1][k] = dp[i + 1][-1][k + 1]

        for j in range(len(s2)):
            for k in range(len(s3) - 1, -1, -1):
                dp[-1][j][k] = dp[-1][j + 1][k + 1]

        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                for k in range(len(s3) - 1, -1, -1):
                    if i == len(s1) and s2[j] == s3[k] or s2[j] == s3[k] and s1[i] != s3[k]:
                        dp[i][j][k] = dp[i][j + 1][k + 1]
                    elif j == len(s2) and s1[i] == s3[k] or s1[i] == s3[k] and s2[j] != s3[k]:
                        dp[i][j][k] = dp[i + 1][j][k + 1]
                    elif s1[i] == s3[k] and s2[j] == s3[k]:
                        dp[i][j][k] = dp[i + 1][j][k + 1] | dp[i][j + 1][k + 1]
        return dp[0][0][0]


so = Solution()
s1 = '123'
s2 = 'acks'
s3 = 'a1c2k3s'
print(so.crossCombination(s1, s2, s3))

s1 = '123'
s2 = 'acks'
s3 = 'a1c3ks2'
print(so.crossCombination(s1, s2, s3))

so = Solution()
s1 = '123'
s2 = 'acks'
s3 = 'a1c2k3s'
print(so.crossCombinationDP(s1, s2, s3))

s1 = '123'
s2 = 'acks'
s3 = 'a1c3ks2'
print(so.crossCombinationDP(s1, s2, s3))
