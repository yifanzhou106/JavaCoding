class Node:
    def __init__(self, info=None):
        self.next = None
        self.info = info


class MessageBox:
    def __init__(self):
        self.headMap = {}
        self.tailMap = {}
        self.breakPoint = 1

    def receive(self, num, info):
        if num < 1:
            return
        node = Node(info)
        if num - 1 in self.tailMap:
            preNode = self.tailMap[num - 1]
            preNode.next = node
            del self.tailMap[num - 1]
        else:
            self.headMap[num] = node
        if num + 1 in self.headMap:
            postNode = self.headMap[num + 1]
            node.next = postNode
            del self.headMap[num + 1]
        else:
            self.tailMap[num] = node
        if self.breakPoint == num:
            self.print()

    def print(self):
        cur = self.headMap[self.breakPoint]
        del self.headMap[self.breakPoint]
        while cur:
            print(cur.info)
            self.breakPoint += 1
            cur = cur.next
        del self.tailMap[self.breakPoint - 1]


mb = MessageBox()
mb.receive(4, 4)
mb.receive(3, 3)
mb.receive(7, 7)
mb.receive(2, 2)
mb.receive(1, 1)
print('_____')
mb.receive(6, 6)
mb.receive(5, 5)
print('_____')
