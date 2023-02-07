# 在一条环路上有 n个加油站，其中第 i个加油站有汽油gas[i]升。
#
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1个加油站需要消耗汽油cost[i]升。
# 你从其中的一个加油站出发，开始时油箱为空。
#
# 给定两个整数数组 gas 和 cost ，如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。
# 如果存在解，则 保证 它是 唯一 的。

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        N = len(gas)

        power = [0 for _ in range(2 * N)]
        pre = 0
        cur = 0
        # 求辅助能量数组，也就是tmp[i] = gas[i] -cost[i]
        # 将辅助数组tmp求两倍长度的前缀和
        for i in range(2 * N):
            power[i] = pre + gas[cur] - cost[cur]
            pre = power[i]
            cur = self.findNext(N, cur)
        print(power)

        # 用单调栈求出区间内的最小值
        # 每次查看区间内的最小值- 区间前一个值就是当前区间的最小值
        minArray = []
        pre = 0
        right = 0
        for i in range(2 * N):
            if right == 2 * N:
                break
            if minArray and i > minArray[0][1]:
                minArray.pop(0)
            while right < 2 * N and right - i + 1 <= N:
                self.addToMinArray(minArray, power[right], right)
                right += 1
            minVal, index = minArray[0]
            if minVal - pre >= 0:
                return i
            pre = power[i]
        return -1

    def addToMinArray(self, minArray, n, i):
        while minArray and minArray[-1][0] >= n:
            minArray.pop()
        minArray.append((n, i))

    def findNext(self, N, i):
        if i == N - 1:
            return 0
        return i + 1

