class Queue:
    def __init__(self, size):
        if size <= 0:
            raise Exception("error")
        self.array = [None for _ in range(size)]
        self.start = 0
        self.end = 0
        self.size = 0

    def push(self, n):
        if len(self.array) == self.size:
            raise Exception("error")
        self.array[self.end] = n
        self.size += 1
        self.end += 1
        if self.end == len(self.array):
            self.end = 0

    def poll(self):
        if self.size == 0:
            raise Exception("error")

        temp = self.array[self.start]
        self.size -= 1
        self.start = self.start + 1 if self.start + 1 < len(self.array) else 0
        return temp


q = Queue(3)
q.push(2)
print(q.array)
q.push(1)
print(q.array)

q.push(4)
print(q.poll())
q.push(5)
print(q.array)
print(q.poll())