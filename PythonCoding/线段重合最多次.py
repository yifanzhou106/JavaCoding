import heapq

class Solution:
    def segmentOverride(self, arr):
        arr.sort()
        print(arr)
        heap = []
        res = 0
        for a in arr:
            l = a[0]
            r = a[1]
            while heap and heap[0] < l:
                heapq.heappop(heap)
            heapq.heappush(heap, r)
            res = max(res, len(heap))
        return res


so = Solution()
arr = [[4, 6], [1, 10], [2, 5], [1, 7]]
print(so.segmentOverride(arr))