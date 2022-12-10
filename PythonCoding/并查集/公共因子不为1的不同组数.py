class Solution:
    def largestComponentSize1(self, arr):
        if not arr:
            return
        unionFind = UnionFind(arr)

        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if self.gcd(arr[i], arr[j]) != 1:
                    unionFind.union(arr[i], arr[j])
        return unionFind.maxSize()

    def gcd(self, v1, v2):
        return v1 if v2 == 0 else self.gcd(v2, v1 % v2)

    def largestComponentSize2(self, arr):
        if not arr:
            return
        unionFind = UnionFind(arr)
        map = {}
        for i in range(len(arr)):
            for j in range(1, self.sqrt(arr[i]) + 1):
                if arr[i] % j == 0:
                    if j != 1:
                        if j in map:
                            unionFind.union(map[j], arr[i])
                        else:
                            map[j] = arr[i]
                    other = arr[i] / j
                    if other != 1:
                        if other in map:
                            unionFind.union(map[other], arr[i])
                        else:
                            map[other] = arr[i]
        print(map)
        return unionFind.maxSize()

    def sqrt(self, n):
        if n < 0:
            return 0
        res = 0
        for i in range(1, n):
            if i * i <= n:
                res = i
            else:
                break
        return res


class UnionFind:
    def __init__(self, arr):
        self.parentMap = {}
        self.sizeMap = {}
        for n in arr:
            self.parentMap[n] = n
            self.sizeMap[n] = 1

    def findRegion(self, n):
        parent = self.parentMap[n]
        if parent != n:
            parent = self.findRegion(parent)
        self.parentMap[n] = parent
        return parent

    def isSameSet(self, v1, v2):
        return self.findRegion(v1) == self.findRegion(v2)

    def union(self, v1, v2):
        if not v1 or not v2:
            return
        r1 = self.findRegion(v1)
        r2 = self.findRegion(v2)
        if r1 == r2:
            return

        s1 = self.sizeMap[r1]
        s2 = self.sizeMap[r2]
        if s1 > s2:
            self.parentMap[r2] = r1
            self.sizeMap[r1] = self.sizeMap[r1] + self.sizeMap[r2]
            del self.sizeMap[r2]
        else:
            self.parentMap[r1] = r2
            self.sizeMap[r2] = self.sizeMap[r1] + self.sizeMap[r2]
            del self.sizeMap[r1]

    def maxSize(self):
        print(self.sizeMap)
        return len(self.sizeMap)


so = Solution()
arr = [20, 7, 14, 2, 17, 3]
print(so.largestComponentSize1(arr))
print(so.largestComponentSize2(arr))







