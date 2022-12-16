# 给定非负数组，每个值代表其上的铜板数，轮到某人时只能在一个位置拿任意铜板不能，不能不拿
# 谁先把铜板拿完的赢
# 思路：异或和如果为零，先手赢，反之后手赢

class Solution:

    def Nim(self, arr):
        eor = 0
        for n in arr:
            eor ^= n
        if eor != 0:
            print("First Win")
        else:
            print("Second Win")


