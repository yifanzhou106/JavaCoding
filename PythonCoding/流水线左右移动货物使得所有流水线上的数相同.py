class Solution:
    def pickingMachine(self, arr):
        if not arr:
            return -1
        total = sum(arr)
        if total % len(arr) != 0:
            return -1

        target = total / len(arr)

        move = 0
        leftSum = 0
        for i in range(len(arr)):
            leftTarget = i * target
            rightSum = total - leftSum - arr[i]
            rightTarget = (len(arr) - i - 1) * target
            left = leftSum - leftTarget
            right = rightSum - rightTarget

            if left < 0 and right < 0:
                move = max(move, abs(left) + abs(right))
            else:
                move = max(move, abs(left), abs(right))
            leftSum += arr[i]
        return move


so = Solution()
arr = [1, 1, 4]
arr2 = [100, 0, 0, 0, 0]
print(so.moveBalance(arr2))



