class Node:
    def __init__(self, key=0, val=0, pre=None, post=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.post = post


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.map = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.post = self.tail
        self.tail.pre = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            node = self.delete(key)
            self.insertNew(node.key, node.val)
            return node.val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map:
            self.delete(key)
        self.insertNew(key, value)
        if len(self.map) > self.cap:
            node = self.head.post
            self.delete(node.key)

    def insertNew(self, key, val):
        node = Node(key, val)
        node.pre = self.tail.pre
        node.post = self.tail
        self.tail.pre.post = node
        self.tail.pre = node
        self.map[key] = node

    def delete(self, key):
        node = self.map[key]
        node.pre.post = node.post
        node.post.pre = node.pre
        del self.map[key]
        return node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)