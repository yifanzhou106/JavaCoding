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
        print(str)
        num = int(str)
        if num > 0 and num <= 26:
            return True
        return False


so = Solution()
print(so.findAlphaCombins('1111'))
print(so.findAlphaCombins('2468'))