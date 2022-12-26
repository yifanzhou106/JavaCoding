class Solution:
    # 在一个数组中有两个累加和相等的数组，并且两个累加和数组里的元素不能重复使用，
    # 求最大相等的累加和是什么

    def LargestCollectionEqualSum(self, arr):
        map = {}
        map[0] = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                cur = map.copy()
                for diff in cur:
                    smallSum = cur[diff]
                    bigSum = smallSum + diff

                    # 现在有两个集合和，一个是bigSum一个是smallSum
                    # 如果arr[i]计入大的集合, bigSum+arr[i]-smallSum就是新的差值
                    map[bigSum + arr[i] - smallSum] = max(map.get(bigSum + arr[i] - smallSum, 0), smallSum)
                    # 如果arr[i]计入小的集合, 就有两种可能
                    # 1. smallSum + arr[i] < bigSum
                    if smallSum + arr[i] < bigSum:
                        map[bigSum - arr[i] - smallSum] = max(map.get(bigSum - arr[i] - smallSum, 0), smallSum + arr[i])
                    else:
                        # 2. smallSum + arr[i] >= bigSum
                        map[smallSum + arr[i] - bigSum] = max(map.get(smallSum + arr[i] - bigSum, 0), bigSum)
        return map[0]


so = Solution()
arr = [1, 2, 3, 6]
print(so.LargestCollectionEqualSum(arr))
