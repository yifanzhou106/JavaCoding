# Online Python compiler (interpreter) to run Python online.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isHuiWen(self, head):
        if not head or not head.next:
            return true
        if not head.next.next:
            return head.val == head.next.val
        slow = head.next
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        pre = None
        cur = slow
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        l = head
        r = pre
        pre = None
        while l and r:
            if l.val != r.val:
                return False
            l = l.next
            temp = r.next
            r.next = pre
            pre = r
            r = temp

        return True


so = Solution()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(3)
n6 = Node(2)
n7 = Node(1)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

print(so.isHuiWen(n1))
temp = n1
while temp:
    print(temp.val)
    temp = temp.next

k1 = Node(1)
k2 = Node(2)
k3 = Node(3)
k4 = Node(4)
k5 = Node(3)
k6 = Node(2)
k1.next = k2
k2.next = k3
k3.next = k4
k4.next = k5
k5.next = k6

print(so.isHuiWen(k1))

m1 = Node(1)
m2 = Node(2)
m3 = Node(3)
m4 = Node(3)
m5 = Node(2)
m6 = Node(1)
m1.next = m2
m2.next = m3
m3.next = m4
m4.next = m5
m5.next = m6

print(so.isHuiWen(m1))
temp = m1
while temp:
    print(temp.val)
    temp = temp.next
