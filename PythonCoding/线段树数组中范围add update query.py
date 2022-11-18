class SegmentTree:
    def __init__(self, nums):
        self.N = len(nums) + 1
        self.update = [False for _ in range(self.N << 2)]
        self.change = [0 for _ in range(self.N << 2)]
        self.lazy = [0 for _ in range(self.N << 2)]
        self.tree = [0 for _ in range(self.N << 2)]

        self.arr = [0 for _ in range(self.N)]

        for i in range(len(nums)):
            self.arr[i + 1] = nums[i]

    def build(self, l, r, rt):
        if l == r:
            self.tree[rt] = self.arr[l]
            return
        mid = l + ((r - l) >> 1)
        self.build(l, mid, rt << 1)
        self.build(mid + 1, r, (rt << 1) | 1)
        self.pushUp(rt)

    def add(self, L, R, c):
        self.addProcess(L, R, 1, self.N, 1, c)

    def addProcess(self, L, R, l, r, rt, c):
        if l == r:
            self.tree[rt] += c
            return

        if L <= l and R >= r:
            self.tree[rt] += (r - l + 1) * c
            self.lazy[rt] += c
            return

        mid = l + ((r - l) >> 1)

        self.pushDown(rt, mid - l + 1, r - mid)

        if L <= mid:
            self.addProcess(L, R, l, mid, rt << 1, c)
        if R > mid:
            self.addProcess(L, R, mid + 1, r, (rt << 1) | 1, c)
        self.pushUp(rt)

    def update(self, L, R, c):
        self.updateProcess((L, R, 1, self.N, 1, c))

    def updateProcess(self, L, R, l, r, rt, c):
        if l == r:
            self.tree[rt] = c
            return
        if L <= l and R >= r:
            self.tree[rt] = (r - l + 1) * c
            self.lazy[rt] = 0
            self.update[rt] = True
            self.change[rt] = c
            return

        mid = l + ((r - l) >> 1)
        self.pushDown(rt, mid - l + 1, r - mid)
        if L <= mid:
            self.updateProcess(L, R, l, mid, rt << 1, c)
        if R > mid:
            self.updateProcess(L, R, mid + 1, r, (rt << 1) | 1, c)
        self.pushUp(rt)

    def query(self, L, R):
        self.queryProcess(L, R, 1, self.N, 1)

    def queryProcess(self, L, R, l, r, rt):
        if l == r:
            return self.tree[rt]

        if L <= l and R >= r:
            return self.tree[rt]

        ans = 0
        mid = l + ((r - l) >> 1)
        self.pushDown(rt, mid - l + 1, r - mid)
        if L <= mid:
            ans += self.queryProcess(L, R, l, mid, rt << 1)
        if R > mid:
            ans += self.queryProcess(L, R, mid + 1, r, (rt << 1) | 1)
        return ans

    def pushDown(self, rt, nl, nr):
        if self.update[rt]:
            self.tree[rt << 1] = nl * self.change[rt]
            self.lazy[rt << 1] = 0
            self.update[rt << 1] = True
            self.change[rt << 1] = self.change[rt]

            self.tree[(rt << 1) | 1] = nr * self.change[rt]
            self.lazy[(rt << 1) | 1] = 0
            self.update[(rt << 1) | 1] = True
            self.change[(rt << 1) | 1] = self.change[rt]

            self.update[rt] = False
            self.change[rt] = 0

        if self.lazy[rt] != 0:
            self.tree[rt << 1] += nl * self.lazy[rt]
            self.lazy[rt << 1] += self.lazy[rt]
            self.tree[(rt << 1) | 1] += nr * self.lazy[rt]
            self.lazy[(rt << 1) | 1] += self.lazy[rt]
            self.lazy[rt] = 0

    def pushUp(self, rt):
        self.tree[rt] = self.tree[rt << 1] + self.tree[(rt << 1) | 1]
