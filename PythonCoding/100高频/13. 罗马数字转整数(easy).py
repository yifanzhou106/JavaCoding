
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        nums = [0 for _ in range(len(s))]
        for i in range(len(s)):
            n = 0
            if s[i] =='I':
                n = 1
            elif s[i] == 'V':
                n = 5
            elif s[i] == 'X':
                n = 10
            elif s[i] == 'L':
                n = 50
            elif s[i] == 'C':
                n = 100
            elif s[i] == 'D':
                n = 500
            elif s[i] == 'M':
                n = 1000
            nums[i] = n
        # 罗马数字只要前一个数字比后一个小的话，就是负数
        for i in range(len(s)):
            if i + 1 < len(s) and nums[i] < nums[i+1]:
                res -= nums[i]
            else:
                res += nums[i]
        return res