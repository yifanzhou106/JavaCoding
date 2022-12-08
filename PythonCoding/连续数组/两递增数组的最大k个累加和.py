import heapq


class Solution:
    def topKSumFromTwoArr(self, nums1, nums2, K):
        if not nums1 or not nums2 or k < 0:
            return
        topK = min(K, len(nums1) * len(nums2))

        i = len(nums1) - 1
        j = len(nums2) - 1

        heap = []
        res = []
        heapq.heappush(heap, (-nums1[i] - nums2[j], i, j))
        isVisited = [[False for _ in range(len(nums2))] for _ in range(len(nums1))]
        while heap and len(res) < topK:
            cur, i, j = heapq.heappop(heap)
            res.append(-cur)
            if i > 0 and not isVisited[i - 1][j]:
                heapq.heappush(heap, (-nums1[i - 1] - nums2[j], i - 1, j))
                isVisited[i - 1][j] = True
            if j > 0 and not isVisited[i][j - 1]:
                heapq.heappush(heap, (-nums1[i] - nums2[j - 1], i - 1, j))
                isVisited[i][j - 1] = True
        return res


so = Solution()
nums1 = [1, 4, 5, 8, 11]
nums2 = [2, 3, 4, 7, 9]
print(so.topKSumFromTwoArr(nums1, nums2, 10))
