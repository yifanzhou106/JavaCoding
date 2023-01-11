class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

# 用排列组合的方法，答案就是c（m+n-2, m-1）
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        part = n - 1
        all = m + n - 2
        o1 = 1
        o2 = 1

        i = part + 1
        j = 1
        while i <= all or j <= all - part:
            o1 *= i
            o2 *= j
            gcd = self.gcd(o1, o2)
            o1 /= gcd
            o2 /= gcd
            i += 1
            j += 1
        return o1

    def gcd(self, m, n):
        return m if n == 0 else self.gcd(n, m % n)