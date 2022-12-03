from functools import cmp_to_key


class Envelope:
    def __init__(self, w, h):
        self.w = w
        self.h = h


class Solution:
    def EnvelopeProblem(self, arr):
        n = len(arr)
        sortedArr = sorted(arr, key=cmp_to_key(self.compare))
        heights = [0 for _ in range(n)]
        for i in range(n):
            heights[i] = sortedArr[i].h
        print(heights)
        end = [0 for _ in range(n)]
        end[0] = heights[0]

        l = 0
        r = 0
        m = 0
        right = 0
        maxLength = 0

        for i in range(1, n):
            l = 0
            r = right
            while l <= r:
                m = l + ((r - l) >> 1)
                if heights[i] > end[m]:
                    l = m + 1
                else:
                    r = m - 1

            right = max(right, l)
            end[l] = heights[i]
            maxLength = max(l + 1, maxLength)

        return maxLength

    def compare(self, x1, x2):
        return x1.w - x2.w if x1.w != x2.w else x2.h - x1.h


so = Solution()
arr = []
arr.append(Envelope(3, 2))
arr.append(Envelope(2, 4))
arr.append(Envelope(3, 5))
arr.append(Envelope(1, 2))
arr.append(Envelope(2, 3))
print(so.EnvelopeProblem(arr))