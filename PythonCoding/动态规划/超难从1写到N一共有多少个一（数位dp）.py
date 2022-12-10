class Solution:

    # 以1开头的数N， 假如有k位，k位上一共N % 10的（k-1）次方 + 1个
    # 其他位上有 （k-1）* 10的（k-2）次方 个1
    # 总共 N % 10的（k-1）次方 + 1 + （k-1）* 10的（k-2）次方 + 递归（n % 10的（k-1）次方）

    # 以1以外开头的数N， 假如有k位，k位上一共10的（k-1）次方个
    # 其他位上有 a *（k-1）* 10的（k-2）次方 个1 （a 是 N 在k位上的数）
    # 总共 10的（k-1）次方 + a *（k-1）* 10的（k-2）次方 + 递归（n % 10的（k-1）次方）

    def findOnesDuringWriteNnum(self, N):
        length = self.findLength(N)
        if length == 1:
            return 1
        tmp = self.powOfTen(length - 1)

        firstNum = N // tmp

        firstOneCount = tmp if firstNum != 1 else N % tmp + 1
        nextOneCount = firstNum * (length - 1) * (tmp // 10)
        return firstOneCount + nextOneCount + self.findOnesDuringWriteNnum(N % tmp)

    def findLength(self, n):
        res = 1
        while n // 10 != 0:
            res += 1
            n = n // 10
        return res

    def powOfTen(self, n):
        res = 1
        tmp = 10
        while n:
            if n & 1 == 1:
                res = res * tmp
            tmp *= tmp
            n = n >> 1
        return res


so = Solution()

print(so.findOnesDuringWriteNnum(28))