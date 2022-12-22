# 给定一个数组，arr[i] 代表i的父，如果arr[i] == i，就是首都，必定有一个首都
# 返回一个数组index代表距离首都的距离，arr[i]代表距离首都i距离的城市数量
# 用O(1)的容量和O(n)时间复杂度做
class Solution:
    def distanceToCap(self, arr):

        # arr = [9, 1, 4, 9, 0, 4, 8, 9, 0, 1]
        # 先循环怼得到距离首都的距离，标为负数
        # [-2, 0, -4, -2, -3, -4, -4, -2, -3, -1]
        for i in range(len(arr)):
            if arr[i] < 0 or arr[i] == i:
                continue
            next = arr[i]
            prev = i

            # 循环跳转直到next指到首都或是arr上为负数（已经计算过距离）的点跳出
            while arr[next] != next and arr[next] >= 0:
                next = arr[next]
                tmp = arr[prev]
                arr[arr[prev]] = prev
                prev = tmp
            # 跳出后next可能指在首都或者arr上为负数（已经计算过距离）的点上
            if arr[next] >= 0:
                start = 0
            else:
                start = arr[next]
            # 开始往回跳转，每次跳转距离-1
            while prev != i:
                tmp = arr[prev]
                start -= 1
                arr[prev] = start
                prev = tmp
            # while结束后prev指在i上还要更新i
            arr[i] = start - 1
        # 将首都节点的距离变为0
        for i in range(len(arr)):
            if arr[i] > 0:
                arr[i] = 0
        print(arr)
        # 开始把负数距离转化为位置上的count
        # 将上面的数组转化成答案
        # [1, 1, 3, 2, 3, 0, 0, 0, 0, 0]
        for i in range(len(arr)):
            if arr[i] <= 0:
                next = -arr[i]
                # 当arr[i] < 0的时候，循环怼
                while arr[next] < 0:
                    tmp = -arr[next]
                    arr[next] = 1
                    next = tmp
                arr[next] += 1
                # 如果当前位置还是负数，改为0，代表已经来过了，下次直接就可以++
                if arr[i] < 0:
                    arr[i] = 0
        return arr


so = Solution()
arr = [9, 1, 4, 9, 0, 4, 8, 9, 0, 1]
print(so.distanceToCap(arr))
