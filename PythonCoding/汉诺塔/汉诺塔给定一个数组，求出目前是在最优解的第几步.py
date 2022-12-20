# from 1
# other 2
# to 3
class Solution:
    def hanoi(self, arr):
        return self.process(arr, len(arr) - 1, 1, 3, 2)

    def process(self, arr, i, f, t, o):
        if i == -1:
            return 0
        # i 只会出现在from 和 to上，如果出现在other上不是最优解
        if arr[i] == o:
            return -1

        elif arr[i] == f:
            return self.process(arr, i - 1, f, o, t)
        else:
            rest = self.process(arr, i - 1, o, t, f)
            if rest == -1:
                return -1
            # 汉诺塔最优步数是2^N次方-1
            # self.process(arr,i-1,f,o,t) i-1 from -> other 2^i次方-1 步
            # i from -> to
            # self.process(arr,i-1,o,t,f) i-1 other -> to
            # 所以到此已经完成了2^i次方-1 步 + 1（i from -> to）这里是从0开始的，所以2^i
            return (1 << i) + rest


so = Solution()
arr = [3, 1, 1]
print(so.hanoi(arr))

arr = [2, 1, 1]
print(so.hanoi(arr))