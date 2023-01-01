# 给定两个整数，被除数dividend和除数divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
#
# 返回被除数dividend除以除数divisor得到的商。
#
# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == -(1 << 31):
            return 1 if dividend == -(1 << 31) else 0
        if dividend == -(1 << 31):
            if divisor == -1:
                return (1 << 31) - 1
            res = self.div(dividend + 1, divisor)

            return res + self.div(dividend - self.muti(res, divisor), divisor)
        return self.div(dividend, divisor)
# python  由于是无限位的，加减就不方便位运算实现
    # 加法就是 n1 ^ n2（不进位加法） + (n1 & n2) << 1（进位）
    # 直到进位为0就结束
    # def add(self, n1, n2):
    #     _sum = n1
    #     while n2 != 0:
    #         _sum = n1 ^ n2
    #         n2 = (n1 & n2) << 1
    #         n1 = _sum
    #     return _sum

    # def negNum(self, num):
    #     return self.add(~num, 1)

    # def minus(self, n1, n2):
    #     return self.add(n1, self.negNum(n2))

    # 乘法 对于n2上二进制0位上如果是1 则res = res + n1
    # n1 << 1, n2 >> 1
    def muti(self, n1, n2):
        x = n1 if not self.isNeg(n1) else -n1
        y = n2 if not self.isNeg(n2) else -n2
        res = 0
        while y != 0:
            if y & 1 == 1:
                res = res + x
            x = x << 1
            y = y >> 1
        return -res if self.isNeg(n1) ^ self.isNeg(n2) else res

    # 除法 每次n2向左移动i位，直到n1恰好大于n2 << i
    # res |= 1 << i
    # 然后 n1 -= (n2 << i)
    # 重复上述操作直到n1 == 0
    def div(self, n1, n2):
        x = n1 if not self.isNeg(n1) else -n1
        y = n2 if not self.isNeg(n2) else -n2
        res = 0

        for i in range(31, -1, -1):
            if (x >> i) >= y:
                res |= (1 << i)
                x = x - (y << i)

        return -res if self.isNeg(n1) ^ self.isNeg(n2) else res

    def isNeg(self, num):
        return num < 0


