class Solution:
    def printAllFolds(self, n):
        if n == 0:
            return
        self.processPrint(1, n, True)

    def processPrint(self, cur, n, isDown):
        if cur > n:
            return
        self.processPrint(cur + 1, n, True)
        res = "0" if isDown else "1"
        print(res)
        self.processPrint(cur + 1, n, False)


so = Solution()
so.printAllFolds(3)
