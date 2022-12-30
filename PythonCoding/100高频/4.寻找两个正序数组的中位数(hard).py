class Solution(object):
    # 思路： 先要有个方法可以解决两个array中第K大的数字，
    # 这个方法可以分解成三种情况
    # 1. k <= len(short) s
    # 这种情况可以直接调用子方法G（求两个array中间大的数字，这个方法必须要两个arr同长），
    # 所以这个中位数只能出现在arr1和arr2各自的0...k-1位置

    # 2. k > len(long) l
    # 这时候 s=[1,2,3,4,5] l = [1,2,3,4,5,6,7,8,9,10] k = 13
    # 假如l的数全用上 13大会出现在s的3上，l的数用越少， 13大在s上s只会向后推
    # 所以13大可能在 s = [3,4,5] (k-l-1...s-1)
    # 同理l上的13大 可能的数是 l= [8,9,10] (k-s-1...l-1)
    # 但是此时s= [3,4,5] l = [8,9,10] 得出的是第三大， 9（抛弃的前数）+ 3 总共第12大的数，不是13大
    # 所以两个arr再先各处理一个数字使得11 + 2 = 第13大
    # s上的3如果大于l上的10 直接返回3， l上的8如果大于s上的3， 直接返回8
    # 然后 s= [4,5] (k-l...s-1)
    # l = [9,10] (k-s...l-1)
    # 找中位数得出的是第二大， 11（抛弃的前数）+ 2 是13大

    # 3. k > len(short) and k <= len(long)
    # s=[1,2,3,4,5] l = [1,2,3,4,5,6,7,8,9,10] k = 8
    # 假如s的数全用上 13大会出现在l的3上，s的数用越少， 8大在l上只会向后推
    # 所以8大可能在 l = [3,4,5,6,7,8] （k-s-1...k-1）
    # 同理s上的数字都有可能 s=[1,2,3,4,5] (0...s-1)
    # 这时候 l和s不等长 所以l上先处理一个数字
    # 如果l上的3大于上的5时，l上的3就是第八大，直接返回
    # 否则 l = [4,5,6,7,8] （k-s...k-1）,s=[1,2,3,4,5] (0...s-1)
    # 找中位数得出的是第八大
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)
        isOdd = ((n + m) & 1) == 1
        if n == 0 and m == 0:
            return 0
        elif n == 0 or m == 0:
            longArr = nums1 if m == 0 else nums2
            longLen = len(longArr)
            return longArr[(longLen - 1) >> 1] if isOdd else float(
                longArr[longLen >> 1] + longArr[(longLen >> 1) - 1]) / 2
        if isOdd:
            print((n + m + 1) >> 1)
            return self.findKthInTwoArr(nums1, nums2, (n + m + 1) >> 1)
        else:
            return float(self.findKthInTwoArr(nums1, nums2, (n + m) >> 1) + self.findKthInTwoArr(nums1, nums2, (
                        (n + m) >> 1) + 1)) / 2

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
            print(long[k - n - 1], short[n - 1])
            if long[k - n - 1] >= short[n - 1]:
                return long[k - n - 1]
            return self.findMidInTwoArr(long, k - n, k - 1, short, 0, n - 1)

    # 找两个相同长度下的arr，两个arr的共同中位数 lg n
    # 默认两个arr等长，要区分奇数偶数长度
    # 如果是偶数的话s=[1,2,3,4] l = [1,2,3,4]
    # 比较s2和l2的大小，如果s2>l2 中位数(第4大)只可能出现在s= [1,2](f1..md1) l = [3,4](md2+1...e2)
    # 反之 s= [3,4](md1+1...e1) l = [1,2](f2...md2)
    # 如果s2和l2相等直接返回 s[md1]

    # 如果是奇数长短，s=[1,2,3,4,5] l = [1,2,3,4,5]
    # 如果s3>l3 中位数(第5大)只可能出现在s= [1,2](f1..md1) l = [3,4,5](md2...e2)
    # 此时长度不相等，先检查l上的3
    # 如果l上的3大于s上的2（md1-1）直接返回l上的3
    # 反之s= [1,2](f1..md1) l = [4,5](md2+1...e2)
    # 如果s3<l3 同理，s3==l3 返回s[md1]
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


so = Solution()

arr1 = [1, 2]
arr2 = [3, 4]
print(so.findMedianSortedArrays(arr1, arr2))

arr1 = []
arr2 = [3]
print(so.findMedianSortedArrays(arr1, arr2))

arr1 = []
arr2 = [1, 2, 3, 4, 5, 6]
print(so.findMedianSortedArrays(arr1, arr2))

arr1 = [1, 2]
arr2 = [1, 2, 3]
print(so.findMedianSortedArrays(arr1, arr2))

arr1 = [2]
arr2 = [1, 3, 4]
print(so.findMedianSortedArrays(arr1, arr2))




