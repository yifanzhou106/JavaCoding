import heapq

# 给定一个咖啡机的 arr，每个数代表做一杯咖啡的时间，每台咖啡机只能按顺序做咖啡
# 不同咖啡机可以并行运作
# 求最优的时间

class Solution:
    def bestChoice(self, arr, M):
        heap = []
        for i in range(len(arr)):
            heapq.heappush(heap, (arr[i], arr[i]))
        res = []
        for i in range(M):
            minTime, during = heapq.heappop(heap)
            res.append(minTime)
            minTime += during
            heapq.heappush(heap, (minTime, during))
        return res


arr = [3, 1, 2, 7, 4]
so = Solution()
print(so.bestChoice(arr, 10))