# 字符串中可以使位运算答案为指定True 或者 False 的所有可能性
class Solution:
    def waysToExpected(self, exp, expected):
        if not exp:
            return 0

        if not self.isValid(exp):
            return 0
        return self.process(exp, 0, len(exp) - 1, expected)

    def isValid(self, exp):
        if len(exp) % 2 != 1:
            return False
        for i in range(0, len(exp), 2):
            if exp[i] != '0' and exp[i] != '1':
                return False
        for i in range(1, len(exp), 2):
            if exp[i] != '^' and exp[i] != '|' and exp[i] != '&':
                return False
        return True

    def process(self, exp, left, right, expected):
        if left == right:
            if exp[left] == '0':
                return 1 if not expected else 0
            else:
                return 1 if expected else 0

        for i in range(left + 1, right, 2):
            if expected:
                if exp[i] == '&':
                    return self.process(exp, left, i - 1, True) * self.process(exp, i + 1, right, True)
                elif exp[i] == '|':
                    return self.process(exp, left, i - 1, True) * self.process(exp, i + 1, right, True) + self.process(
                        exp, left, i - 1, True) * self.process(exp, i + 1, right, False) + self.process(exp, left,
                                                                                                        i - 1,
                                                                                                        False) * self.process(
                        exp, i + 1, right, True)
                elif exp[i] == '^':
                    return self.process(exp, left, i - 1, True) * self.process(exp, i + 1, right, False) + self.process(
                        exp, left, i - 1, False) * self.process(exp, i + 1, right, True)
            else:
                if exp[i] == '&':
                    return self.process(exp, left, i - 1, True) * self.process(exp, i + 1, right, False) + self.process(
                        exp, left, i - 1, False) * self.process(exp, i + 1, right, True) + self.process(exp, left,
                                                                                                        i - 1,
                                                                                                        False) * self.process(
                        exp, i + 1, right, False)
                elif exp[i] == '|':
                    return self.process(exp, left, i - 1, False) * self.process(exp, i + 1, right, False)
                elif exp[i] == '^':
                    return self.process(exp, left, i - 1, True) * self.process(exp, i + 1, right, True) + self.process(
                        exp, left, i - 1, False) * self.process(exp, i + 1, right, False)

    def waysToExpectedDP(self, exp, expected):
        if not exp:
            return 0

        if not self.isValid(exp):
            return 0
        tdp = [[0 for _ in range(len(exp))] for _ in range(len(exp))]
        fdp = [[0 for _ in range(len(exp))] for _ in range(len(exp))]

        for i in range(0, len(exp), 2):
            tdp[i][i] = 1 if exp[i] == '1' else 0
            fdp[i][i] = 1 if exp[i] == '0' else 0

        for j in range(1, len(exp), 2):
            cur = j + 1
            i = 0
            while i < len(exp) - 2 and cur < len(exp):
                if exp[j] == '&':
                    tdp[i][cur] = tdp[i][cur - 2] * tdp[i + 2][cur]
                    fdp[i][cur] = tdp[i][cur - 2] * fdp[i + 2][cur] + fdp[i][cur - 2] * tdp[i + 2][cur] + fdp[i][
                        cur - 2] * fdp[i + 2][cur]
                elif exp[j] == '|':
                    tdp[i][cur] = tdp[i][cur - 2] * tdp[i + 2][cur] + tdp[i][cur - 2] * fdp[i + 2][cur] + fdp[i][
                        cur - 2] * tdp[i + 2][cur]
                    fdp[i][cur] = fdp[i][cur - 2] * fdp[i + 2][cur]
                elif exp[j] == '^':
                    tdp[i][cur] = tdp[i][cur - 2] * fdp[i + 2][cur] + fdp[i][cur - 2] * tdp[i + 2][cur]
                    fdp[i][cur] = tdp[i][cur - 2] * tdp[i + 2][cur] + fdp[i][cur - 2] * fdp[i + 2][cur]
                cur += 2
                i += 2
        return tdp[0][-1] if expected else fdp[0][-1]


so = Solution()
exp = "1^0&1|1^1"
print(so.waysToExpected(exp, True))
print(so.waysToExpected(exp, False))

print(so.waysToExpectedDP(exp, True))
print(so.waysToExpectedDP(exp, False))
