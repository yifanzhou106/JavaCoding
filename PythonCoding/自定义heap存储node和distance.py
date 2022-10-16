class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = []


class CustomHeap:
    def __init__(self, size=0):
        self.nodeIndexMap = {}
        self.distanceMap = {}
        self.nodeHeap = [None for _in range(size)]
        self.size = 0

    def swap(self, a, b):
        self.nodeIndexMap[self.nodeHeap[a]] = b
        self.nodeIndexMap[self.nodeHeap[b]] = a
        self.nodeHeap[a], self.nodeHeap[b] = self.nodeHeap[b], self.nodeHeap[a]

    def isEntered(self, node):
        return node in nodeIndexMap

    def isInHeap(self, node):
        return self.isEntered(node) and self.nodeIndexMap[node] != -1

    def heapify(self, node, size):
        i = self.nodeIndexMap[node]
        left = 2 * i + 1

        while left < size:
            smallest = left + 1 if left + 1 < size and self.distanceMap[left] > self.distanceMap[left + 1] else left
            smallest = smallest if self.distanceMap[smallest] < self.distanceMap[i]
            if smallest == i:
                break
            self.swap(smallest, i)
            i = smallest
            left = 2 * i + 1

    def heapInsert(self, node):
        i = self.nodeIndexMap[node]

        while self.distanceMap[node] < self.distanceMap[self.nodeHeap[(i - 1) / 2]]:
            self.swap(i, (i - 1) / 2)
            i = (i - 1) / 2

    def insertOrUpdateorIgnore(self, node, distance):
        if self.isInHeap(node):
            self.distanceMap[node] = min(self.distanceMap[node], distance)
            self.heapInsert(node)
        if not self.isEntered(node):
            self.nodeIndexMap[node] = self.size
            self.distanceMap[node] = distance
            self.nodeHeap[self.size] = node
            self.heapInsert(node)
            self.size += 1

    def pop(self):
        node = Node(self.nodeHeap[0], self.distanceMap[self.nodeHeap[0]])
        self.swap(0, size - 1)
        self.nodeIndexMap[self.nodeHeap[size - 1]] = -1
        del self.distanceMap[self.nodeHeap[size - 1]]
        self.nodeHeap[size - 1] = None
        self.size -= 1
        self.heapify(self.nodeHeap[0], self.size)
        return node


