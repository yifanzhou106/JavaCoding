# 可能有问题

class Solution:
    def noDupSubarry(self, s):
        if not s:
            return 0
        l = 0
        res = 0
        map = {}

        for i in range(len(s)):
            if s[i] in map:
                res = max(res, i - l)
                l = i
            map[s[i]] = i
        return res


so = Solution()
arr = 'pwwkew'
print(so.noDupSubarry(arr))

arr = 'abcabcbb'
print(so.noDupSubarry(arr))

arr = 'bbbbb'
print(so.noDupSubarry(arr))
