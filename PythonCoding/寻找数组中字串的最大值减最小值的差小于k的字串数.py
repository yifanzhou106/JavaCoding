class Node:
    def __init__(self, val=0, index=0):
        self.val = val
        self.index = index


class Solution:
    def findAllSubarrayMaxMinusMinLessThanK(self, nums, k):
        if not nums or not k:
            return 0
        left = 0
        right = 0
        maxQ = []
        minQ = []
        res = 0
        while left < len(nums):
            while right < len(nums):
                self.addNums(maxQ, minQ, nums, right)
                if maxQ[0].val - minQ[0].val > k:
                    break
                right += 1
            if maxQ[0].index == left:
                maxQ.pop(0)
            if minQ[0].index == left:
                minQ.pop(0)
            res += right - left
            left += 1
        return res

    def addNums(self, maxQ, minQ, nums, right):
        while maxQ and maxQ[-1].val <= nums[right]:
            maxQ.pop()
        while minQ and minQ[-1].val >= nums[right]:
            minQ.pop()
        maxQ.append(Node(nums[right], right))
        minQ.append(Node(nums[right], right))


so = Solution()
arr = [4, 6, 8, 12, 3, 4, 5]
print(so.findAllSubarrayMaxMinusMinLessThanK(arr, 4))

