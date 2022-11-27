#生成一个数组
#使得数组中任意三个数 i,j,k (i<j<k)， i + k != 2j

class Solution:
    def generateArray(self, M):
        if M == 1:
            return [1]

        half = (M + 1) >> 1
        base = self.generateArray(half)
        res = [None for _ in range(M)]
        index = 0
        while index < half:
            res[index] = (base[index] << 1) - 1
            index += 1
        i = 0
        while index < M:
            res[index] = (base[i] << 1)
            index += 1
            i += 1
        return res


so = Solution()
print(so.generateArray(5))
print(so.generateArray(7))
print(so.generateArray(2))
print(so.generateArray(8))
print(so.generateArray(10))

