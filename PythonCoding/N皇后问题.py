# Online Python compiler (interpreter) to run Python online.
class Solution:
    def NQueen(self, n):
        if not n or n < 0:
            return 0
        record = [0 for _ in range(n)]
        return self.process(0, record, n)

    def process(self, i, record, n):
        if i == n:
            return 1
        res = 0
        for j in range(n):
            if self.isValid(record, i, j):
                record[i] = j
                res += self.process(i + 1, record, n)
        return res

    def isValid(self, record, i, j):
        for k in range(i):
            if j == record[k] or abs(i - k) == abs(j - record[k]):
                return False
        return True

    # 高级做法
    def NQueen2(self, n):
        limit = -1 if n == 32 else (1 << n) - 1
        return self.process2(limit, 0, 0, 0)

    def process2(self, limit, colLimit, leftLimit, rightLimit):
        if colLimit == limit:
            return 1
        p = limit & (~(colLimit | leftLimit | rightLimit))
        res = 0
        while p != 0:
            mostRight = p & (~p + 1)
            p -= mostRight
            res += self.process2(limit, colLimit | mostRight, (leftLimit | mostRight) << 1,
                                 (rightLimit | mostRight) >> 1)
        return res


so = Solution()

print(so.NQueen(8))
print(so.NQueen2(8))