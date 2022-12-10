class Solution:
    def findAlphaCombins(self, str):
        return self.process(str, 0)

    def process(self, str, start):
        res = 0
        if start == len(str):
            return 1
        if str[start] == '0':
            return 0
        else:
            res += self.process(str, start + 1)
            if start + 1 < len(str) and self.isAlpha(str[start: start + 2]):
                res += self.process(str, start + 2)

        return res

    def isAlpha(self, str):
        num = int(str)
        if num > 0 and num <= 26:
            return True
        return False

    def findAlphaCombinsDP(self, str):
        dp = [0 for _ in range(len(str)+1)]
        dp[-1] = 1
        for i in range(len(str)-1, -1, -1):
            if str[i] == '0':
                dp[i] = 0
            else:
                dp[i] += dp[i+1]
                if i+1 <len(str) and self.isAlpha(str[i: i + 2]):
                    dp[i] += dp[i+2]
        return dp[0]

so = Solution()
print(so.findAlphaCombins('1111'))
print(so.findAlphaCombinsDP('1111'))
print(so.findAlphaCombins('2468'))
print(so.findAlphaCombinsDP('2468'))