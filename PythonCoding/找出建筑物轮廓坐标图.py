import heapq


class Solution:
    def findBuildingShadow(self, arr):
        height = []
        for b in arr:
            height.append((b[0], b[2], 1))
            height.append((b[1], b[2], -1))
        height.sort()
        res = []
        heap = [0]
        map = {}
        map[0] = -1
        beginIndex = -1
        for i in range(len(height)):
            preHeight = -heap[0]

            count = map.get(height[i][1], 0)
            count += height[i][2]
            if not map.get(height[i][1]) or map.get(height[i][1]) == 0:
                heapq.heappush(heap, -height[i][1])
            map[height[i][1]] = count
            while map.get(-heap[0]) == 0:
                heapq.heappop(heap)

            if -heap[0] != preHeight:
                if beginIndex != -1 and preHeight != 0:
                    res.append([beginIndex, height[i][0], preHeight])
                beginIndex = height[i][0]
        return res


so = Solution()
arr = [[1, 6, 4], [2, 4, 3], [5, 8, 5], [7, 10, 3]]
print(so.findBuildingShadow(arr))

arr2 = [[1, 6, 4], [7, 10, 3]]
print(so.findBuildingShadow(arr2))

arr3 = [[1,6,4],[6,10,3]]
print(so.findBuildingShadow(arr3))