class Solution:

    def knight(self, M):
        dp = [[-1 for _ in range(len(M[0]))] for _ in range(len(M))]
        res = self.process(M, 0, 0, dp)
        return 1 if res < 0 else res

    def process(self, M, i, j, dp):
        if dp[i][j] != -1:
            return dp[i][j]
        if i == len(M) - 1 and j == len(M[0]) - 1:
            dp[i][j] = -M[i][j] + 1 if M[i][j] < 0 else 1
            return dp[i][j]
        elif i == len(M) - 1:
            next = self.process(M, i, j + 1, dp)
            if M[i][j] < 0:
                dp[i][j] = next - M[i][j]
                return dp[i][j]
            elif M[i][j] >= next:
                dp[i][j] = 1
                return 1
            else:
                dp[i][j] = next - M[i][j]
                return next - M[i][j]
        elif j == len(M[0]) - 1:
            next = self.process(M, i + 1, j, dp)
            if M[i][j] < 0:
                dp[i][j] = next - M[i][j]
                return dp[i][j]
            elif M[i][j] >= next:
                dp[i][j] = 1
                return 1
            else:
                dp[i][j] = next - M[i][j]
                return next - M[i][j]

        p1 = self.process(M, i + 1, j, dp)
        p2 = self.process(M, i, j + 1, dp)
        next = min(p1, p2)
        if M[i][j] < 0:
            dp[i][j] = next - M[i][j]
            return dp[i][j]
        elif M[i][j] >= next:
            dp[i][j] = 1
            return 1
        else:
            dp[i][j] = next - M[i][j]
            return next - M[i][j]

so = Solution()
M = [[-2, -3, 3], [-5, -10, 1], [0, 30, -5]]

print(so.knight(M))