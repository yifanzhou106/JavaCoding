# 给定一个正整数 n ，输出外观数列的第 n 项。
#
# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
#
# 你可以将其视作是由递归公式定义的数字字符串序列：
#
# countAndSay(1) = "1"
# countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
# 前五项如下：
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 第一项是数字 1
# 描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
# 描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
# 描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
# 描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"

# 注意类似的传整数的递归方法，可以学习一下的，先调用f(n-1)
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1:
            return ""
        if n == 1:
            return "1"

        last = self.countAndSay(n - 1)
        cur = []
        count = 1
        for i in range(1, len(last)):
            if last[i - 1] == last[i]:
                count += 1
            else:
                cur.append(str(count))
                cur.append(last[i - 1])
                count = 1
        cur.append(str(count))
        cur.append(last[-1])
        return "".join(cur)