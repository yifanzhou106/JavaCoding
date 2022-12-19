from heapq import heappush, heappop


class Program:
    def __init__(self, index, pm, start, priority, cost):
        self.pm = pm
        self.start = start
        self.priority = priority
        self.cost = cost
        self.index = index

    def __lt__(self, other):
        if self.priority != other.priority:
            return self.priority < other.priority
        if self.cost != other.cost:
            return self.cost < other.cost
        return self.start < other.start


class BigQueues:
    def __init__(self, size):
        self.pmHeap = [[] for _ in range(size + 1)]
        self.sdkHeap = [None for _ in range(size)]
        self.heapSize = 0
        self.pmIndex = [-1 for _ in range(size + 1)]

    def isEmpty(self):
        return self.heapSize == 0

    def add(self, program):
        heap = self.pmHeap[program.pm]
        heappush(heap, program)
        head = heap[0]
        index = self.pmIndex[program.pm]
        if index == -1:
            self.sdkHeap[self.heapSize] = head
            self.pmIndex[program.pm] = self.heapSize
            self.heapSize += 1
            self.heapInsert(program.index)
        else:
            self.sdkHeap[index] = head
            self.heapify(index)
            self.heapInsert(index)

    def pop(self):
        head = self.sdkHeap[0]
        heap = self.pmHeap[head.pm]
        heappop(heap)
        if not heap:
            self.swap(0, self.heapSize - 1)
            self.heapSize -= 1
            self.sdkHeap[self.heapSize] = None

            self.pmIndex[head.pm] = -1
        else:
            self.sdkHeap[0] = heap[0]
        self.heapify(0)
        return head

    def sdkCompareTo(self, o1, o2):
        if o1.cost != o2.cost:
            return o1.cost < o2.cost
        return o1.pm < o2.pm

    def heapify(self, index):
        left = index * 2 + 1
        while left < self.heapSize:
            _max = index
            if not self.sdkCompareTo(self.sdkHeap[index], self.sdkHeap[left]):
                _max = left
            if left + 1 < self.heapSize and not self.sdkCompareTo(self.sdkHeap[_max], self.sdkHeap[left + 1]):
                _max = left + 1
            if _max == index:
                break
            self.swap(index, _max)
            index = _max
            left = index * 2 + 1

    def heapInsert(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.sdkCompareTo(self.sdkHeap[index], self.sdkHeap[parent]):
                self.swap(index, parent)
                index = parent
            else:
                break

    def swap(self, index1, index2):
        p1 = self.sdkHeap[index1]
        p2 = self.sdkHeap[index2]
        self.sdkHeap[index1], self.sdkHeap[index2] = self.sdkHeap[index2], self.sdkHeap[index1]
        self.pmIndex[p1.pm] = index2
        self.pmIndex[p2.pm] = index1


class Solution:
    def workFinish(self, pms, sdes, programs):
        startQueue = []
        for i in range(len(programs)):
            program = Program(i, programs[i][0], programs[i][1], programs[i][2], programs[i][3])
            heappush(startQueue, (programs[i][1], program))
        wakeQueue = [1 for _ in range(sdes)]
        bigQueues = BigQueues(pms)
        finish = 0
        ans = [0 for _ in range(len(programs))]
        while finish != len(programs):
            sdeWakeTime = heappop(wakeQueue)
            while startQueue:
                if startQueue[0][0] > sdeWakeTime:
                    break
                bigQueues.add(heappop(startQueue)[1])
            if bigQueues.isEmpty():
                heappush(wakeQueue, startQueue[0][0])
            else:
                program = bigQueues.pop()
                ans[program.index] = sdeWakeTime + program.cost
                heappush(wakeQueue, ans[program.index])
                finish += 1
        return ans














