# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 小根堆做，很简单
from heapq import heappop,heappush
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        head = ListNode()
        cur = head
        for node in lists:
            if node:
                heappush(heap,(node.val, node))
        while heap:
            minVal, minNode = heappop(heap)
            cur.next = minNode
            if minNode.next:
                heappush(heap,(minNode.next.val, minNode.next))
            cur = cur.next
            cur.next = None
        return head.next