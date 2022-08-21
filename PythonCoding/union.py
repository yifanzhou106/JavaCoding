class Data:
    def __init__(self, val=0):
        self.val = val


class solution:
    def __init__(self, dataList):
        self.parentMap = {}
        self.sizeMap = {}
        for data in dataList:
            self.parentMap[data] = data
            self.sizeMap[data] = 1

    def findRegion(self, node):
        p = self.parentMap[node]
        if p is not node:
            p = self.findRegion(p)
        self.parentMap[node] = p
        return p

    def isSameSet(self, a, b):
        return self.findRegion(a) is self.findRegion(b)

    def union(self, a, b):
        if not a or not b:
            retun
        ra = self.findRegion(a)
        rb = self.findRegion(b)
        if ra is not rb:
            sizeA = self.sizeMap[a]
            sizeB = self.sizeMap[b]
            if sizeA > sizeB:
                self.parentMap[b] = a
                self.sizeMap[a] = self.sizeMap[a] + self.sizeMap[b]
            else:
                self.parentMap[a] = b
                self.sizeMap[b] = self.sizeMap[a] + self.sizeMap[b]


d1 = Data(1)
d2 = Data(2)
d3 = Data(3)
d4 = Data(4)
arr = [d1, d2, d3, d4]
so = solution(arr)

so.union(d1, d4)
print(so.parentMap[d1].val)
print(so.parentMap[d4].val)
print(so.isSameSet(d1, d4))
print(so.isSameSet(d2, d4))