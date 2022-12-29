class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Solution:
    def addTwoNumbers(self, head1, head2):
        res = Node()
        c = 0
        h1 = head1
        h2 = head2
        tmp = res
        while h1 and h2:
            _sum = h1.val + h2.val + c
            c = _sum // 10
            tmp.next = Node(_sum % 10)
            h1 = h1.next
            h2 = h2.next
            tmp = tmp.next

        while h1:
            _sum = h1.val + c
            c = _sum // 10
            tmp.next = Node(_sum % 10)
            h1 = h1.next
            tmp = tmp.next

        while h2:
            _sum = h2.val + c
            c = _sum // 10
            tmp.next = Node(_sum % 10)
            h2 = h2.next
            tmp = tmp.next
        if c != 0:
            tmp.next = Node(1)
        return res.next


so = Solution()
n1 = Node(2)
n2 = Node(4)
n3 = Node(3)
n1.next = n2
n2.next = n3

n4 = Node(5)
n5 = Node(6)
n6 = Node(4)
n4.next = n5
n5.next = n6

res = so.addTwoNumbers(n1, n4)
while res:
    print(res.val)
    res = res.next
