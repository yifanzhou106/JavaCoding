# Online Python compiler (interpreter) to run Python online.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.rand = None


class Solution:
    def cloneNode(self, head):
        if not head:
            return

        node = head
        while node:
            newNode = Node(node.val, node.next)
            node.next = newNode
            node = newNode.next

        node = head
        head2 = head.next

        while node:
            node.next.rand = node.rand.next if node.rand else None
            node = node.next.next

        node = head
        while node and node.next.next:
            temp = node.next.next
            node.next.next = temp.next
            node.next = temp
            node = temp

        return head2


so = Solution()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

n1.rand = n4
n2.rand = n6
n3.rand = n5
n4.rand = n7
n5.rand = n1
n6.rand = n3
n7.rand = n1
res = so.cloneNode(n1)

temp = res
while temp:
    print(temp.val)
    temp = temp.next
print("##############")
temp = res
while temp:
    print(temp.rand.val)
    temp = temp.next

