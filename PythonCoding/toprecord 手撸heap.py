class Node:
    def __init__(self, str):
        self.count = 1
        self.str = str
        self.index = None


class TopRecord:
    def __init__(self, K):
        self.K = K
        self.heap = [None for _ in range(K)]
        self.map = {}
        self.size = 0

    def heapify(self, node):
        while ((node.index << 1) | 1) < self.size:
            leftChild = (node.index << 1) | 1
            minCount = node.count
            minCountNode = node
            if self.heap[leftChild].count < minCount:
                minCount = self.heap[leftChild].count
                minCountNode = self.heap[leftChild]
            if leftChild + 1 < self.size and self.heap[leftChild + 1].count < minCount:
                minCount = self.heap[leftChild + 1].count
                minCountNode = self.heap[leftChild + 1]
            if minCountNode is node:
                break
            self.heap[node.index], self.heap[minCountNode.index] = self.heap[minCountNode.index], self.heap[node.index]
            node.index, minCountNode.index = minCountNode.index, node.index

    def heapInsert(self, node):
        parent = (node.index - 1) >> 1
        while node.index != 0 and self.heap[parent].count > node.count:
            parentNode = self.heap[parent]
            self.heap[parent], self.heap[node.index] = self.heap[node.index], self.heap[parent]
            parentNode.index, node.index = node.index, parentNode.index
            parent = (node.index - 1) >> 1

    def heapPop(self):
        if not self.heap:
            return
        self.heap[0].index = None
        self.heap[0] = self.heap[self.size - 1]
        self.heap[self.size - 1] = None
        self.size -= 1
        self.heap[0].index = 0
        self.heapify(self.heap[0])

    def add(self, str):
        if str not in self.map:
            node = Node(str)
            self.map[str] = node
            if self.size == self.K and node.count >= self.heap[0].count:
                self.heapPop()
            if self.size < self.K:
                node.index = self.size
                self.heap[self.size] = node
                self.size += 1
                self.heapInsert(node)
        else:
            node = self.map[str]
            node.count += 1
            if node.index == None:
                if self.size == self.K and node.count >= self.heap[0].count:
                    self.heapPop()
                if self.size < self.K:
                    node.index = self.size
                    self.heap[self.size] = node
                    self.size += 1
                    self.heapInsert(node)
            else:
                self.heapify(node)

    def top(self):
        return self.heap[:self.size]


so = TopRecord(3)
so.add('abc')
so.add('abc')
res = so.top()
for r in res:
    print(r.str, r.count, r.index)
print("********")
so.add('bc')
res = so.top()
for r in res:
    print(r.str, r.count, r.index)

print("********")
so.add('c')
so.add('c')
so.add('c')
res = so.top()
for r in res:
    print(r.str, r.count, r.index)
print("********")
so.add('d')
res = so.top()
for r in res:
    print(r.str, r.count, r.index)
print("********")
so.add('bc')
so.add('bc')
so.add('c')
so.add('abc')
res = so.top()
for r in res:
    print(r.str, r.count, r.index)
print("********")
so.add('d')
res = so.top()
for r in res:
    print(r.str, r.count, r.index)
print("********")
so.add('d')
res = so.top()
for r in res:
    print(r.str, r.count, r.index)












