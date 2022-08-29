import heapq


class Solution:
    def goldDivision(self, nums):
        res = 0
        heap = nums[:]
        heapq.heapify(heap)
        while len(heap) >= 2:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            _sum = a + b
            res += _sum
            heapq.heappush(heap, _sum)
        return res


so = Solution()
arr = [10, 20, 30]
print(so.goldDivision(arr))

arr = [1, 2, 6, 4, 3, 7, 1, 8]
print(so.goldDivision(arr))