# 打字机问题
# 如果每次轮转，打字机只能把L到R范围上的字符转化成一种字符
# 求最少轮转次数
class Solution:
    def printer(self, s):
        return self.process(s, 0, len(s) - 1)

    def process(self, s, l, r):
        if l == r:
            return 1
        if l > r:
            return 0
        # 最差情况就是l...r每个一次
        res = r - l + 1
        # 如果s[l] == s[i]， 两个结果可以合成一个
        for i in range(l + 1, r + 1):
            res = min(res, self.process(s, l, i - 1) + self.process(s, i, r) - (0 if s[l] != s[i] else 1))
        return res


so = Solution()
s = 'abbbccccaaa'
print(so.printer(s))