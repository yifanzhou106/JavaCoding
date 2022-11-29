import heapq


class Solution:
    def findWaterVolumnInMetric(self, M):
        if not M or len(M) < 3 or len(M[0]) < 3:
            return 0

        isVisited = [[False for _ in range(len(M[0]))] for _ in range(len(M))]
        heap = []

        for j in range(len(M[0])):
            if not isVisited[0][j]:
                heapq.heappush(heap, (M[0][j], 0, j))
                isVisited[0][j] = True
        for j in range(len(M[0])):
            if not isVisited[-1][j]:
                heapq.heappush(heap, (M[-1][j], len(M) - 1, j))
                isVisited[-1][j] = True
        for i in range(len(M)):
            if not isVisited[i][0]:
                heapq.heappush(heap, (M[i][0], i, 0))
                isVisited[i][0] = True
        for i in range(len(M)):
            if not isVisited[i][-1]:
                heapq.heappush(heap, (M[i][0], i, len(M[0]) - 1))
                isVisited[i][-1] = True
        _max = -float('inf')
        water = 0
        while heap:
            num, r, c = heapq.heappop(heap)
            _max = max(_max, num)
            if r > 0 and not isVisited[r - 1][c]:
                if M[r - 1][c] < _max:
                    water += _max - M[r - 1][c]
                heapq.heappush(heap, (M[r - 1][c], r - 1, c))
                isVisited[r - 1][c] = True
            if r < len(M) - 1 and not isVisited[r + 1][c]:
                if M[r + 1][c] < _max:
                    water += _max - M[r + 1][c]
                heapq.heappush(heap, (M[r + 1][c], r + 1, c))
                isVisited[r + 1][c] = True
            if c > 0 and not isVisited[r][c - 1]:
                if M[r][c - 1] < _max:
                    water += _max - M[r][c - 1]
                heapq.heappush(heap, (M[r][c - 1], r, c - 1))
                isVisited[r][c - 1] = True
            if c < len(M[0]) - 1 and not isVisited[r][c + 1]:
                if M[r][c + 1] < _max:
                    water += _max - M[r][c + 1]
                heapq.heappush(heap, (M[r][c + 1], r, c + 1))
                isVisited[r][c + 1] = True
        return water


so = Solution()
M = [[7, 7, 5, 9, 9, 9, 5, 8, 8], [9, 1, 2, 1, 9, 1, 2, 1, 8], [9, 9, 9, 9, 9, 8, 8, 8, 8]]
print(so.findWaterVolumnInMetric(M))



