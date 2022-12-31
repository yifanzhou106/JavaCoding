# 数字 n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

# 示例 1：
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
# 示例 2：
#
# 输入：n = 1
# 输出：["()"]


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        res = []
        self.process(n, 0, "", res)
        return res

    # 递归 n 代表剩余括号对数，curLeft 目前左括号数， path 当前字符串， res 答案数组
    # 只要是 剩余括号对数 == 0，记录一个答案
    # 如果左括号数为0， 就只能添加左括号
    # 如果左括号数大于0， 有两种情况
    # 1. 如果curLeft < n，就还可以添加左括号
    # 2. 添加右括号， 但是剩余对数n要减一， 左括号数减一
    def process(self, n, curLeft, path, res):
        if n == 0:
            res.append(path)
            return
        if curLeft == 0:
            self.process(n, curLeft + 1, path + '(', res)
        elif curLeft > 0:
            if curLeft < n:
                self.process(n, curLeft + 1, path + '(', res)
            self.process(n - 1, curLeft - 1, path + ')', res)

