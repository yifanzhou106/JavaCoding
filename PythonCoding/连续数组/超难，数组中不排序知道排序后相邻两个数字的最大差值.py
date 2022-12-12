class Solution:
# 假设9个数，放10个桶，必有一个桶是空的，
# 那么他的左右两边的非空桶由于间隔了一个空桶 minRight-maxLeft 必定大于一个空桶的大小（S）
# 这样就排除了同一个桶中的可能性，因为同一个桶里的差值必定小于一个空桶的大小（S）
    def maxDiffBetweenNeighborInArr(self, arr):
        maxNum = -float('inf')
        minNum = float('inf')
        for n in arr:
            maxNum = max(maxNum, n)
            minNum = min(minNum, n)

        if maxNum == minNum:
            return 0

        minBucket = [0 for _ in range(len(arr) + 1)]
        maxBucket = [0 for _ in range(len(arr) + 1)]
        isEmpty = [True for _ in range(len(arr) + 1)]

        for n in arr:
            index = self.hashNum(maxNum, minNum, len(arr), n)
            if isEmpty[index]:
                minBucket[index] = n
                maxBucket[index] = n
                isEmpty[index] = False
            else:
                minBucket[index] = min(minBucket[index], n)
                maxBucket[index] = max(maxBucket[index], n)
        print(minBucket, maxBucket, isEmpty)

        res = 0
        preMax = maxBucket[0]

        for i in range(1, len(arr) + 1):
            if not isEmpty[i]:
                res = max(res, minBucket[i] - preMax)
                preMax = maxBucket[i]

        return res

    def hashNum(self, maxNum, minNum, size, num):
        return (num - minNum) * size // (maxNum - minNum)


so = Solution()
M = [14, 2, 7, 9, 11, 99, 58, 43, 88]

print(so.maxDiffBetweenNeighborInArr(M))