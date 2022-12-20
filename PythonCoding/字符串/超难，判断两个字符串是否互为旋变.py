# 旋变指的是将一个字符串拆成树，兄弟位置可以互相交换
# abcd => bacd,cdba,dcba .....
class Solution:
    def isXuanbianString(self, s1, s2):

        if len(s1) != len(s2):
            return False
        return self.process(s1, s2, 0, 0, len(s1))

    def process(self, s1, s2, l1, l2, size):
        # 当size == 1 的时候比较是否一样
        if size == 1:
            return s1[l1] == s2[l2]
        # 第一刀分在什么地方
        for i in range(1, size):
            # 左左为旋变并且右右为旋变 或者 s1左s2右旋变并且s1右s2左旋变
            if (self.process(s1, s2, l1, l2, i) and self.process(s1, s2, l1 + i, l2 + i, size - i)) or (
                    self.process(s1, s2, l1, l2 + size - i, i) and self.process(s1, s2, l1 + i, l2, size - i)):
                return True
        return False


so = Solution()
s1 = 'abcd'
s2 = 'badc'
print(so.isXuanbianString(s1, s2))

