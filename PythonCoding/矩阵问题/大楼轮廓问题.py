from functools import cmp_to_key
from heapq import heappush, heappop


class OP:
    def __init__(self, x, isUp, height):
        self.x = x
        self.isUp = isUp
        self.height = height


class Solution:
    def building(self, M):
        arr = [None for _ in range(2 * len(M))]
        for i in range(len(M)):
            arr[2 * i] = OP(M[i][0], True, M[i][2])
            arr[2 * i + 1] = OP(M[i][1], False, M[i][2])
        arr = sorted(arr, key=cmp_to_key(self.compare))

        maxHeight = {}
        xHeight = {}
        heapKey = []

        for op in arr:
            if op.isUp:
                if -op.height in maxHeight:
                    maxHeight[-op.height] += 1
                else:
                    maxHeight[-op.height] = 1
                    heappush(heapKey, -op.height)
            else:
                if maxHeight[-op.height] == 1:
                    del maxHeight[-op.height]
                    heapKey.remove(-op.height)
                else:
                    maxHeight[-op.height] -= 1
            xHeight[op.x] = 0 if not maxHeight else -heapKey[0]

        res = []
        preHeight = 0
        preIndex = 0
        for key in xHeight:
            if xHeight[key] != preHeight:
                if preHeight != 0:
                    res.append([preIndex, key, preHeight])
                preIndex = key
                preHeight = xHeight[key]
        return res

    def compare(self, o1, o2):
        if o1.x != o2.x:
            return o1.x - o2.x
        if o1.isUp != o2.isUp:
            return -1 if o1.isUp else 1
        return 0

    def printOP(self, arr):
        for o in arr:
            print(o.x, o.isUp, o.height)


so = Solution()
M = [[1, 7, 4], [2, 5, 6], [3, 6, 5], [4, 6, 7], [9, 11, 3], [10, 13, 2]]
print(so.building(M))