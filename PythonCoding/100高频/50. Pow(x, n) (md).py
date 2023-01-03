# 实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，xn ）。

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        unsignedN = abs(n)
        res = 1
        tmp = x

        for i in range(32):
            if (unsignedN >> i) & 1 == 1:
                res *= tmp
            tmp *= tmp

        return res if n > 0 else 1 / res