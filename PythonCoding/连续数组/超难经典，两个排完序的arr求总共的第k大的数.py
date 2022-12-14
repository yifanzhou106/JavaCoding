import heapq


class Solution:
    # 在两个长度不同的arr中，找到两个arr的共同第k大的数， log min(n,m)
    def findKthInTwoArr(self, arr1, arr2, k):

        long = arr1 if len(arr1) > len(arr2) else arr2
        short = arr1 if len(arr1) <= len(arr2) else arr2

        m = len(long)
        n = len(short)
        # 分三种情况 k <= n，直接用方法findMidInTwoArr
        if k <= n:
            return self.findMidInTwoArr(long, 0, k - 1, short, 0, k - 1)
        elif k > m:
            # 如果k>m 前数总解决如下例子，左边总解决9个
            # s=[1,2,3,4,5] l = [1,2,3,4,5,6,7,8,9,10] k = 13
            # 左边总解决9个,剩下s= [3,4,5] l = [8,9,10] 套用方法求出其中第3大的数，得出总共第12大的数，不对
            # 两个arr再先各处理一个数字使得11 + 2 = 第13大
            if short[k - m - 1] >= long[m - 1]:
                return short[k - m - 1]
            if long[k - n - 1] >= short[n - 1]:
                return long[k - n - 1]
            return self.findMidInTwoArr(long, k - n, m - 1, short, k - m, n - 1)
        else:
            # 长的会比短的多一个数字，先解决它
            if long[m - k - 1] >= short[n - 1]:
                return long[m - k - 1]
            return self.findMidInTwoArr(long, m - k, k - 1, short, 0, n - 1)

    # 找两个相同长度下的arr，两个arr的共同中位数 lg n
    def findMidInTwoArr(self, arr1, f1, e1, arr2, f2, e2):
        if f1 == e1:
            return min(arr1[f1], arr2[f2])
        isOdd = ((e1 - f1 + 1) & 1) == 1
        mid1 = f1 + ((e1 - f1) >> 1)
        mid2 = f2 + ((e2 - f2) >> 1)
        if isOdd:
            if arr1[mid1] > arr2[mid2]:
                if arr2[mid2] > arr1[mid1 - 1]:
                    return arr2[mid2]
                return self.findMidInTwoArr(arr1, f1, mid1 - 1, arr2, mid2 + 1, e2)
            elif arr1[mid1] < arr2[mid2]:
                if arr1[mid1] > arr2[mid2 - 1]:
                    return arr1[mid1]
                return self.findMidInTwoArr(arr1, mid1 + 1, e1, arr2, f2, mid2 - 1)
            else:
                return arr1[mid1]
        else:
            if arr1[mid1] > arr2[mid2]:
                return self.findMidInTwoArr(arr1, f1, mid1, arr2, mid2 + 1, e2)
            elif arr1[mid1] < arr2[mid2]:
                return self.findMidInTwoArr(arr1, mid1 + 1, e1, arr2, f2, mid2)
            else:
                return arr1[mid1]


arr = [3, 1, 2, 7, 4]
so = Solution()
arr1 = [1, 3, 5, 7, 9]
arr2 = [2, 3, 6, 7, 10]
print(so.findMidInTwoArr(arr1, 0, 4, arr2, 0, 4))

arr1 = [1, 3, 7, 9]
arr2 = [2, 4, 6, 10]
print(so.findMidInTwoArr(arr1, 0, 3, arr2, 0, 3))
print("*********")
arr1 = [1, 3, 7, 9, 11, 14, 16, 18, 22]
arr2 = [2, 4, 6, 10, 17, 25, 30]
print(so.findKthInTwoArr(arr1, arr2, 10))  # 14
print(so.findKthInTwoArr(arr1, arr2, 12))  # 17
print(so.findKthInTwoArr(arr1, arr2, 8))  # 10
print(so.findKthInTwoArr(arr1, arr2, 4))  # 4





