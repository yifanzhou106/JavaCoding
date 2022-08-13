# Online Python compiler (interpreter) to run Python online.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def getIntersectNode(self, head1, head2):
        if not head1 or not head2:
            return None
        loop1 = self.findLoop(head1)
        loop2 = self.findLoop(head2)
        print("loop", loop1.val, loop2.val)
        if not loop1 and not loop2:
            return self.noLoop(loop1, loop2)
        else:
            return self.hasLoop(head1, head2, loop1, loop2)
        return None

    def findLoop(self, head):
        fast = head
        slow = head
        while fast.next and fast.next.next:
            if fast.next.next == slow.next:
                break
            slow = slow.next
            fast = fast.next.next
        if not fast.next or not fast.next.next:
            return None
        slow = slow.next
        cur = head
        while slow and cur != slow:
            cur = cur.next
            slow = slow.next
        return slow

    def noLoop(self, head1, head2):
        diff = 0
        h1 = head1
        h2 = head2
        while h1:
            diff += 1
            h1 = h1.next
        while h2:
            diff -= 1
            h2 = h2.next
        c1 = h1 if diff >= 0 else h2
        c2 = h2 if diff <= 0 else h1
        diff = abs(diff)

        for _ in range(diff):
            c1 = c1.next
        while c1 != c2:
            c1 = c1.next
            c2 = c2.next
        return c1

    def hasLoop(self, head1, head2, loop1, loop2):
        if loop1 == loop2:
            diff = 0
            h1 = head1
            h2 = head2
            while h1 != loop1:
                diff += 1
                h1 = h1.next
            while h2 != loop1:
                diff -= 1
                h2 = h2.next
            c1 = h1 if diff >= 0 else h2
            c2 = h2 if diff <= 0 else h1
            diff = abs(diff)

            for _ in range(diff):
                c1 = c1.next
            while c1 != c2:
                c1 = c1.next
                c2 = c2.next
            return c1
        else:
            cur = loop1.next
            while cur != loop1:
                if cur == loop2:
                    return cur
                cur = cur.next
            return None


so = Solution()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)

r1 = Node(10)
r2 = Node(11)
r3 = Node(12)
r4 = Node(13)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n6

r1.next = r2
r2.next = r3
r3.next = r4
r4.next = n7

print(so.getIntersectNode(n1, r1).val)
