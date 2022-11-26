class Solution:
    def findLargestSquare(self, m):

        self.r = [[0 for _ in range(len(m[0]))] for _ in range(len(m))]
        self.d = [[0 for _ in range(len(m[0]))] for _ in range(len(m))]

        self.buildRightAndDownMetric(m)
        size = min(len(m), len(m[0]))
        for i in range(size, -1, -1):
            if self.isValid(i):
                return i
        return 0

    def isValid(self, size):
        for i in range(len(self.r) - size + 1):
            for j in range(len(self.r[0]) - size + 1):
                if self.r[i][j] >= size and self.r[i + size - 1][j] >= size and self.d[i][j] >= size and self.d[i][
                    j + size - 1] >= size:
                    return True
        return False

    def buildRightAndDownMetric(self, m):
        for i in range(len(m)):
            for j in range(len(m[0]) - 1, -1, -1):
                if j == len(m[0]) - 1:
                    self.r[i][j] = m[i][j]
                else:
                    if m[i][j] == 0:
                        self.r[i][j] = 0
                    else:
                        self.r[i][j] = self.r[i][j + 1] + 1
        for j in range(len(m[0])):
            for i in range(len(m) - 1, -1, -1):
                if i == len(m) - 1:
                    self.d[i][j] = m[i][j]
                else:
                    if m[i][j] == 0:
                        self.d[i][j] = 0
                    else:
                        self.d[i][j] = self.d[i + 1][j] + 1


so = Solution()
m = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
print(so.findLargestSquare(m))







