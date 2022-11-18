class BFPTR:
    def getMinKthByBFPRT(self, nums, k):
        temp = nums[:]
        return self.bfprt(nums, 0, len(nums) - 1, k)

    def bfprt(self, nums, start, end, t):
        if start == end:
            return nums[start]
        pivot = self.medianOfMediums(nums, start, end)
        medianRegion = self.partition(nums, start, end, pivot)

        if t >= medianRegion[0] and t <= medianRegion[1]:
            return nums[t]
        elif t < medianRegion[0]:
            return self.bfprt(nums, start, medianRegion[0] - 1, t)
        else:
            return self.bfprt(nums, medianRegion[1] + 1, end, t)

    def medianOfMediums(self, nums, start, end):
        size = len(nums) // 5
        offset = 1 if len(nums) % 5 != 0 else 0
        mArr = [None for _ in range(size + offset)]
        for i in range(len(mArr)):
            left = i * 5
            right = left + 4
            mArr[i] = self.getMedium(nums, left, min(right, end))

        return self.bfprt(mArr, 0, len(mArr) - 1, len(mArr) // 2)

    def getMedium(self, nums, start, end):
        self.insertSort(nums, start, end)
        _sum = start + end
        mid = _sum // 2 + _sum % 2
        return nums[mid]

    def insertSort(self, nums, start, end):
        left = start
        right = start + 1
        while right < end + 1:
            if nums[left] <= nums[right]:
                left += 1
                right += 1
            else:
                i = right
                while i - 1 >= start and nums[i] < nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]
                    i -= 1

    def partition(self, nums, start, end, pivot):
        less = start - 1
        more = end + 1
        i = start
        while i < more:
            if nums[i] > pivot:
                nums[i], nums[more - 1] = nums[more - 1], nums[i]
                more -= 1
            elif nums[i] < pivot:
                nums[i], nums[less + 1] = nums[less + 1], nums[i]
                less += 1
                i += 1
            else:
                i += 1

        return [less + 1, more - 1]


so = BFPTR()
arr = [4, 6, 8, 2, 3, 4, 5, 5, 5, 6, 123, 3, 77, 34]
print(so.getMinKthByBFPRT(arr, 6))


# 2刷

class Solution:

    def findKSmallestNumber(self, nums, k):
        if len(nums) < k:
            return nums[-1]
        return self.process(nums, 0, len(nums) - 1, k)

    def process(self, nums, left, right, k):
        if left == right:
            return nums[left]

        bfprtNum = self.bfprt(nums[left:right + 1])
        equalRange = self.patition(nums, left, right, bfprtNum)

        if k >= equalRange[0] and k <= equalRange[1]:
            return nums[k]
        elif k < equalRange[0]:
            return self.process(nums, left, equalRange[0] - 1, k)
        else:
            return self.process(nums, equalRange[1] + 1, right, k)

    def patition(self, nums, left, right, m):
        l = left - 1
        r = right + 1
        cur = left

        while cur < r:
            if nums[cur] < m:
                nums[l + 1], nums[cur] = nums[cur], nums[l + 1]
                l += 1
                cur += 1
            elif nums[cur] == m:
                cur += 1
            else:
                nums[r - 1], nums[cur] = nums[cur], nums[r - 1]
                r -= 1
        return [l + 1, r - 1]

    def bfprt(self, nums):
        if len(nums) == 1:
            return nums[0]
        mids = []
        cur = 0
        right = len(nums) - 1
        while cur <= right:
            end = min(cur + 5, right)
            self.insertSort(nums, cur, end)
            mid = cur + (end - cur) >> 1
            mids.append(nums[mid])
            cur += 5
        return self.process(mids, 0, len(mids)-1, len(mids) >> 1)

    def insertSort(self, nums, left, right):
        for i in range(left, right):
            j = i
            while j - 1 >= left and nums[j] > nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]


so = Solution()
nums = [5, 9, 8, 2, 1, 4, 6, 2, 7]
print(so.findKSmallestNumber(nums, 3))

