class Solution(object):
    # 每次res先*=10，然后x mod下来的值加到res上
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = x < 0
        x = x if not neg else -x
        # 要求不超过-2^31 ~ 2^31
        m = (1 << 31) // 10
        o = (1 << 31) % 10
        res = 0
        while x != 0:
            if res > m or (res == m and x % 10 > o):
                print(res, m)
                return 0
            res = res * 10 + x % 10
            x //= 10
        return -res if neg else res
