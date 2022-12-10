class Node:
    def __init__(self, key=0, val=0, times=0):
        self.key = key
        self.val = val
        self.times = times
        self.up = None
        self.down = None


class NodeList:
    def __init__(self, node=None):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        if node:
            self.head.down = node
            self.tail.up = node
            node.up = self.head
            node.down = self.tail
        else:
            self.head.down = self.tail
            self.tail.up = self.head

        self.last = None
        self.next = None

    def addNodeFromHead(self, node):
        node.down = self.head.down
        node.up = self.head
        self.head.down.up = node
        self.head.down = node

    def isEmpty(self):
        return self.head.down == self.tail

    def removeNode(self, node):
        node.up.down = node.down
        node.down.up = node.up


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.size = 0
        self.record = {}
        self.heads = {}
        self.headList = NodeList()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.record:
            return -1
        else:
            node = self.record[key]
            node.times += 1
            nodeList = self.heads[node]
            self.move(node, nodeList)
            return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.cap != 0:
            if key in self.record:
                node = self.record[key]
                node.val = value
                node.times += 1
                nodeList = self.heads[node]
                self.move(node, nodeList)
            else:
                if self.size == self.cap and self.headList.next:
                    node = self.headList.next.tail.up

                    self.headList.next.removeNode(node)
                    self.modifyHeadList(self.headList.next)
                    del self.record[node.key]
                    del self.heads[node]
                    self.size -= 1

                node = Node(key, value, 1)
                if not self.headList.next:
                    nodeList = NodeList(node)
                    self.headList.next = nodeList
                    nodeList.last = self.headList

                else:
                    if self.headList.next.head.down.times == node.times:
                        self.headList.next.addNodeFromHead(node)
                    else:
                        nodeList = NodeList(node)
                        self.headList.next.last = nodeList
                        nodeList.next = self.headList.next
                        self.headList.next = nodeList
                        nodeList.last = self.headList
                self.record[key] = node
                self.heads[node] = self.headList.next
                self.size += 1

    def move(self, node, nodeList):
        nodeList.removeNode(node)
        if not nodeList.next:
            newNodeList = NodeList(node)
            nodeList.next = newNodeList
            newNodeList.last = nodeList
            self.heads[node] = newNodeList
        else:
            if nodeList.next.head.down.times == node.times:
                nodeList.next.addNodeFromHead(node)
                self.heads[node] = nodeList.next
            else:
                newNodeList = NodeList(node)
                newNodeList.next = nodeList.next
                nodeList.next = newNodeList
                newNodeList.last = nodeList
                newNodeList.next.last = newNodeList
                self.heads[node] = newNodeList

        self.modifyHeadList(nodeList)

    def modifyHeadList(self, nodeList):
        if nodeList.isEmpty():
            nodeList.last.next = nodeList.next
            if nodeList.next:
                nodeList.next.last = nodeList.last

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)