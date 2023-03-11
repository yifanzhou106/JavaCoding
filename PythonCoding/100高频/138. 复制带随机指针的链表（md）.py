"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return

        cur = head
        while cur:
            copyNode = Node(cur.val, cur.next)
            cur.next = copyNode
            cur = copyNode.next
        cur = head

        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        copyhead = head.next
        cur1 = head
        cur2 = copyhead
        while cur1:
            cur1.next = cur2.next
            cur1 = cur1.next
            if cur1:
                cur2.next = cur1.next
                cur2 = cur2.next
        return copyhead



