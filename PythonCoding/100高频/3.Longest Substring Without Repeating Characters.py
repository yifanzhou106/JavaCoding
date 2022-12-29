class Solution:
    def lengthOfLongestSubstring(self, str):
        if not str:
            return 0

        include = [0 for _ in range(256)]
        res = 0
        r = 0
        for i in range(len(str)):
            while r < len(str) and include[ord(str[r])] == 0:
                include[ord(str[r])] += 1
                r += 1
            res = max(res, r - i)
            include[ord(str[i])] -= 1

        return res


so = Solution()
s = 'abccabdcdcab'
print(so.lengthOfLongestSubstring(s))
