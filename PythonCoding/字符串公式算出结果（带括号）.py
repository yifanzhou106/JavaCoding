class Solution:
    def calcualteString(self, str):
        stack1 = []
        numStack = []

        for c in str:

            if ord(c) >= ord('0') and ord(c) <= ord('9'):
                num = self.chrToNum(c)
                if numStack:
                    preNum = numStack.pop()
                    numStack.append(preNum * 10 + num)
                else:
                    numStack.append(num)
            else:
                if numStack:
                    stack1.append(numStack.pop())
                if c == ')':
                    temp = []
                    while stack1[-1] != '(':
                        temp.append(stack1.pop())
                    stack1.pop()
                    cur = self.calculateStringWithoutBucket(temp[::-1])
                    stack1.append(cur)
                else:
                    stack1.append(c)
        if numStack:
            stack1.append(numStack.pop())
        print(stack1)
        return self.calculateStringWithoutBucket(stack1)

    def calculateStringWithoutBucket(self, list):
        stack = []
        for i in range(len(list)):
            stack.append(list[i])
            if len(stack) > 1 and (stack[-2] == '*' or stack[-2] == '/'):
                num1 = stack.pop()
                op = stack.pop()
                num2 = stack.pop()
                if op == '*':
                    stack.append(num2 * num1)
                else:
                    stack.append(num2 // num1)
        res = 0
        while stack:
            if stack[0] == '-':
                stack.pop(0)
                num = - stack.pop(0)
                res += num
            elif stack[0] == '+':
                stack.pop(0)
            else:
                res += stack.pop(0)
        return res

    def chrToNum(self, c):
        return ord(c) - ord('0')


so = Solution()
s1 = "123+1"
s2 = "-123+1"
s3 = '(1+2)*3'
s4 = "11+2*3+2+16/5+6"
s5 = "0"

# print(so.calcualteString(s1))
# print(so.calcualteString(s2))
# print(so.calcualteString(s3))
print(so.calcualteString(s4))
# print(so.calcualteString(s5))
