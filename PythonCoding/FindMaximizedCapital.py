# Online Python compiler (interpreter) to run Python online.
import heapq


class Solution:
    def maxProfit(self, cost, profit, k, w):
        minHeap = []
        maxHeap = []
        for i in range(len(cost)):
            minHeap.append((cost[i], profit[i]))
        heapq.heapify(minHeap)

        for i in range(k):
            while minHeap and minHeap[0][0] <= w:
                c, p = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, (-p, c))
            if not maxHeap:
                return w
            p, c = heapq.heappop(maxHeap)
            w -= p
        return w


so = Solution()
cost = [5, 10, 6, 20]
profit = [3, 2, 4, 9]
print(so.maxProfit(cost, profit, 5, 7))

cost = [5, 10, 6, 20]
profit = [3, 2, 4, 9]
print(so.maxProfit(cost, profit, 5, 7))
