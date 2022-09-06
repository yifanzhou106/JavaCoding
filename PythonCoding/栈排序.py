class Solution:

    def sortStack(self, stack):
        help = []

        while stack:
            top = stack.pop()
            while help and top > help[-1]:
                stack.append(help.pop())
            help.append(top)
        while help:
            stack.append(help.pop())


so = Solution()
arr = [4, 6, 8, 12, 3, 4, 5]
so.sortStack(arr)
print(arr)

