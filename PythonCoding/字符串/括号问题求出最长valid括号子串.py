class Solution:
    def findLongestValidBucket(self, str):
        stack = []
        res = 0
        for c in str:
            count = 0
            while len(stack) > 0 and stack[-1] != '(':
                count += stack.pop()
            if count > 0:
                stack.append(count)
                res = max(res, count)
            if c == '(':
                stack.append(c)
            elif c == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                    res = max(res, 1)
                elif len(stack) > 0 and stack[-1] != '(':
                    count = stack.pop()
                    if stack[-1] and stack[-1] == '(':
                        stack.pop()
                        count += 1
                    stack.append(count)
                    res = max(res, count)
            print(stack)

        print(stack)
        return 2 * res

    def findLongestValidBucketDP(self, str):
        dp = [0 for _ in range(len(str))]
        res = 0
        pre = 0
        for i in range(1, len(str)):
            if str[i] == ')':
                pre = i - dp[i - 1] - 1
                if i >= dp[i - 1] + 1 and str[pre] == '(':
                    dp[i] = dp[i - 1] + 2
                if pre - 1 >= 0:
                    dp[i] += dp[pre - 1]
            res = max(dp[i], res)
        return res


so = Solution()
str1 = "(()()((())))"
# print(so.findLongestValidBucket(str1))

str2 = "(()()((())"
print(so.findLongestValidBucket(str2))






