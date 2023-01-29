# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = 1
        head = {}
        tail = {}

        for n in nums:
            if n not in head and n not in tail:
                head[n] = n
                tail[n] = n

                if n + 1 in head:
                    head[n] = head[n + 1]
                    tail[head[n]] = n
                    res = max(res, head[n] - n + 1)
                    del head[n + 1]
                    del tail[n]

                if n - 1 in tail:
                    tail[head[n]] = tail[n - 1]
                    head[tail[head[n]]] = head[n]
                    res = max(res, head[n] - tail[head[n]] + 1)
                    del tail[n - 1]
                    del head[n]
        return res


