import math


class Solution:
    def heapSort(self, nums):
        for i in range(len(nums)):
            self.heapInsert(nums, i)

        heapSize = len(nums)
        nums[0], nums[heapSize - 1] = nums[heapSize - 1], nums[0]
        heapSize -= 1
        while (heapSize > 0):
            self.heapify(nums, 0, heapSize)
            nums[0], nums[heapSize - 1] = nums[heapSize - 1], nums[0]
            heapSize -= 1

    def heapInsert(self, nums, i):
        while (nums[i] > nums[math.ceil((i - 1) / 2)]):
            nums[i], nums[math.ceil((i - 1) / 2)] = nums[math.ceil((i - 1) / 2)], nums[i]
            i = math.ceil((i - 1) / 2)

    def heapify(self, nums, i, heapSize):
        left = 2 * i + 1
        while (left < heapSize):
            largest = left + 1 if left + 1 < heapSize and nums[left + 1] > nums[left] else left
            largest = largest if nums[largest] > nums[i] else i
            if largest == i:
                break
            nums[i], nums[largest] = nums[largest], nums[i]
            i = largest
            left = 2 * i + 1


so = Solution()
arr = [3, 2, 4, 6, 8, 1, 2]
so.heapSort(arr)
print(arr)