# 整合数组的定义： 数组排完序后左右两个数字的差值的绝对值为1
#[5, 5, 3, 2, 6, 4, 3] =》 [5, 3, 2, 6, 4] 就是答案
# 第二种整合数组的定义， 数组中没有重复值，并且最大值-最小值 == 数组长度-1

class Solution:

    def longestIntegratedLength(self, arr):
        if not arr:
            return 0
        res = 0
        for i in range(len(arr)):
            isDup = set()
            minNum = float('inf')
            maxNum = -float('inf')
            for j in range(i, len(arr)):
                if arr[j] in isDup:
                    break
                isDup.add(arr[j])
                minNum = min(minNum, arr[j])
                maxNum = max(maxNum, arr[j])

                if maxNum - minNum == j - i:
                    res = max(res, j - i + 1)
        return res


so = Solution()
n = [5, 5, 3, 2, 6, 4, 3]

print(so.longestIntegratedLength(n))