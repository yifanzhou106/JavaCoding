# 如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。
# 则可以认为该短语是一个 回文串 。
#
# 字母和数字都属于字母数字字符。
#
# 给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while left <= right:
            leftChar = self.toLowCase(s[left])
            rightChar = self.toLowCase(s[right])
            if not self.isValid(leftChar):
                left += 1
            elif not self.isValid(rightChar):
                right -= 1
            else:
                if leftChar != rightChar:
                    return False
                left += 1
                right -= 1
        return True


    def toLowCase(self, c):
        if ord(c) >= ord('A') and ord(c) <= ord('Z'):
            return chr(ord('a')+ord(c) - ord('A'))
        return c

    def isValid(self, c):
        return ord(c) >= ord('a') and ord(c) <= ord('z') or (ord(c) >= ord('0') and ord(c) <= ord('9'))