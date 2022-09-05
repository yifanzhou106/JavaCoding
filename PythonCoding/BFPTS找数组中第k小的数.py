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