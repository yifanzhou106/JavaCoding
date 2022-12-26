class Solution:
    # 给定一个数组nums，长度一定是2的p次方
    # 给定另一个数组arr，里面的值一定小于p，代表将nums数组按照arr[i]的大小翻转
    # 例如arr[i] = 1，是2的1次方，代表将nums里的数字两两revert
    # 例如arr[i] = 2，是2的2次方代表将nums里的数字每4个一组revert
    # 求每次arr操作时的总逆序对数量返回一个list

    def powerPairs(self, nums, p, arr):
        dp1 = [0 for _ in range(p + 1)]
        dp2 = [0 for _ in range(p + 1)]
        tmp = nums[:]
        self.mergeSort(tmp, p, 0, len(arr), dp1, dp2)
        print(dp1, dp2, tmp)
        res = [0 for _ in range(len(arr))]
        for i in range(len(arr)):
            for j in range(arr[i] + 1):
                dp1[j], dp2[j] = dp2[j], dp1[j]
            res[i] = sum(dp1)
        return res

    def mergeSort(self, nums, p, left, right, dp1, dp2):
        if p == 0 or left == right:
            return
        mid = left + ((right - left) >> 1)

        self.mergeSort(nums, p - 1, left, mid, dp1, dp2)
        self.mergeSort(nums, p - 1, mid + 1, right, dp1, dp2)

        self.merge(nums, p, left, mid, right, dp1, dp2)

    def merge(self, nums, p, left, mid, right, dp1, dp2):
        l = left
        r = mid + 1
        tmp = []
        while l <= mid and r <= right:
            if nums[l] > nums[r]:
                dp1[p] += mid - l + 1
                tmp.append(nums[r])
                r += 1
            elif nums[l] < nums[r]:
                dp2[p] += right - r + 1
                tmp.append(nums[l])
                l += 1
            else:
                tmp.append(nums[r])
                tmp.append(nums[l])
                r += 1
                l += 1
        while l <= mid:
            tmp.append(nums[l])
            l += 1
        while r <= right:
            tmp.append(nums[r])
            r += 1
        for i in range(len(tmp)):
            nums[i + left] = tmp[i]


so = Solution()
nums = [3, 1, 2, 4]
p = 2
arr = [1, 2, 0]
print(so.powerPairs(nums, p, arr))
