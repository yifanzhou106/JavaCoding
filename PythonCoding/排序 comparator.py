from functools import cmp_to_key
class node:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

class Solution:
    def compare(self, x, y):
        if x.v1 < y.v1:
            return -1
        elif x.v1 > y.v1:
            return 1
        else:
            return y.v2 - x.v2

    def sort(self, arr):
        arr = sorted(arr, key=cmp_to_key(self.compare))
        for i in arr:
            print(i.v1, i.v2)


so = Solution()
arr = []
arr.append(node(2, 3))
arr.append(node(2, 2))
arr.append(node(2, 1))
arr.append(node(1, 3))
arr.append(node(4, 2))
arr.append(node(3, 6))
so.sort(arr)