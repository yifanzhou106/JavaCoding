# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 这个解答是通过遍历数出所有节点数
class Solution(object):
    def removeNthFromEnd1(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 遍历一遍求出count
        count = 0
        cur = head
        while cur:
            cur = cur.next
            count += 1

        target = count - n
        # 如果目标是头结点的话，直接返回head.next
        if target == 0:
            return head.next
        # 再遍历找到删除节点前一个，重新链接
        count = 1
        cur = head
        while count < target:
            cur = cur.next
            count += 1
        cur.next = cur.next.next
        return head

# 只遍历一次，先让尾巴跑n位，pre的指针再向后移动
    def removeNthFromEnd2(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        cur = head
        pre = None
        while cur:
            if count >= n:
                if not pre:
                    pre = head
                else:
                    pre = pre.next
            cur = cur.next
            count += 1

        if pre == None:
            return head.next
        pre.next = pre.next.next
        return head