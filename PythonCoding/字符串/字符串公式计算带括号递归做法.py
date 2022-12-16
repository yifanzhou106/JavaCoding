class Solution:
    def calculateString(self, s):
        return self.process(s, 0)[0]

    def process(self, s, start):
        stack = []
        cur = 0
        i = start
        while i < len(s) and s[i] != ')':

            if s[i] >= '0' and s[i] <= '9':
                cur = cur * 10 + (ord(s[i]) - ord('0'))
                i += 1
            elif s[i] != '(':
                self.addNum(stack, cur)
                cur = 0
                stack.append(s[i])
                i += 1
            else:
                nextVal, nextIndex = self.process(s, i + 1)
                cur = nextVal
                i = nextIndex + 1
        self.addNum(stack, cur)
        return (self.calculateStringOnlyAddMinus(stack), i)

    def addNum(self, stack, cur):
        if stack:
            op = stack.pop()
            if op == '+' or op == '-':
                stack.append(op)
            else:
                preNum = stack.pop()
                cur = preNum // cur if op == '/' else preNum * cur
        stack.append(cur)

    def calculateStringOnlyAddMinus(self, stack):
        res = 0
        while stack:
            n = stack.pop()
            op = "+"
            if stack:
                op = stack.pop()
            if op == "+":
                res += n
            else:
                res -= n

        return res


so = Solution()
s = "-1+(3*2-1)/2+8"
print(so.calculateString(s))

s1 = "123+1"
s2 = "-123+1"
s3 = '(1+2)*3'
s4 = "11+2*3+2+16/5+6"
s5 = "3+3*(6+7*(3+1))+5"

print(so.calculateString(s1))
print(so.calculateString(s2))
print(so.calculateString(s3))
print(so.calculateString(s4))
print(so.calculateString(s5))
