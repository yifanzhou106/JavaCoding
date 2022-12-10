import random


class SkipMapNode:
    def __init__(self, key=None, val=None):
        self.next = []
        self.key = key
        self.val = val


class SkipMap:
    def __init__(self):
        self.head = SkipMapNode()
        self.maxLevel = 0
        self.head.next.append(None)
        self.rand = 0.5
        self.size = 0

    def toMostRightLessInLevel(self, cur, level, k):
        temp = cur
        while temp.next[level] and temp.next[level] < k:
            temp = temp.next[level]
        return temp

    def toMostRightLessInTotal(self, k):
        cur = self.head
        level = self.maxLevel
        while level >= 0:
            cur = self.toMostRightLessInLevel(cur, level, k)
            level -= 1
        return cur

    def put(self, key, val):
        if not key:
            return
        latest = self.toMostRightLessInTotal(key)
        node = latest.next[0]
        if node and node.key == key:
            node.val = val
        else:
            self.size += 1
            newNodeLevel = 0
            while random(1) < self.rand:
                newNodeLevel += 1

            newNode = SkipMapNode(key, val)
            for i in range(newNodeLevel + 1):
                newNode.next.append(None)

            while newNodeLevel > self.maxLevel:
                self.head.next.append(None)
                self.maxLevel += 1
            cur = self.head
            level = self.maxLevel
            while level >= 0:
                cur = self.toMostRightLessInLevel(cur, level, k)
                if newNodeLevel >= level:
                    newNode.next[level] = cur.next[level]
                    cur.next[level] = newNode
                level -= 1

