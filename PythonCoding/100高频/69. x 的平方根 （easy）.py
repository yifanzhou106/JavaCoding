# 二分法

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x < 3:
            return 1
        left = 1
        right = x
        res = 0
        while left <= right:
            mid = left +((right-left) >> 1)
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                res = mid
                left = mid + 1
        return res