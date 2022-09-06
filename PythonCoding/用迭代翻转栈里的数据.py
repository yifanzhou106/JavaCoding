class Solution:
    def revertStack(self, stack):
        if not stack:
            return
        last = self.pullLastNumFromStack(stack)
        self.revertStack(stack)
        stack.append(last)

    def pullLastNumFromStack(self, stack):
        obj = stack.pop()
        if not stack:
            return obj
        last = self.pullLastNumFromStack(stack)
        stack.append(obj)
        return last


so = Solution()
arr = [4, 6, 8, 12, 3, 4, 5]
so.revertStack(arr)
print(arr)

