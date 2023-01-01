# 直接用kmp算法
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return -1

        next = self.getNext(needle)
        hi = 0
        ni = 0
        while hi < len(haystack) and ni < len(needle):
            if haystack[hi] == needle[ni]:
                hi += 1
                ni += 1
            elif ni == -1:
                ni = 0
                hi += 1
            else:
                ni = next[ni]
        if ni == len(needle):
            return hi - len(needle)
        else:
            return -1

    def getNext(self, s):
        next = [0 for _ in range(len(s))]
        next[0] = -1
        right = 2
        for i in range(2, len(next)):
            cur = i - 1
            while cur != -1 and s[i - 1] != s[next[cur]]:
                cur = next[cur]
            next[i] = 0 if cur == -1 else next[cur] + 1
        return next


