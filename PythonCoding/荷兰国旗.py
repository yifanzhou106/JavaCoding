class Solution:
    def patition(self, nums, n):
        less = -1
        more = len(nums)
        i = 0
        while i < more:
            if nums[i] > n:
                nums[more-1], nums[i] = nums[i], nums[more-1]
                more -= 1
            elif nums[i] < n:
                nums[less+1], nums[i] = nums[i], nums[less+1]
                less += 1
                i+=1
            else:
                i+=1

so = Solution()
arr = [1,3,4,2,5,1]
so.patition(arr,5)
print (arr)