class Solution:
    # 使用左右指针和include数组，将左右指针之间的所有字符存在数组中
    # 当右指针向右扩说明区间内没有重复的
    # 否则左指针扩，并移除当前左指针在数组内的count
    def lengthOfLongestSubstring1(self, s):
        if not s:
            return 0

        include = [0 for _ in range(256)]
        res = 0
        r = 0
        for i in range(len(s)):
            while r < len(s) and include[ord(s[r])] == 0:
                include[ord(s[r])] += 1
                r += 1
            res = max(res, r - i)
            include[ord(s[i])] -= 1

        return res

    # 动态规划做
    # pre 代表i-1位到达的左边界
    # 当前位置的左边界是include里上次字符出现位置和pre的最大值
    # 再讲当前字符的位置更新到include数组
    # 更新pre到现在的左边界
    def lengthOfLongestSubstring2(self, s):
        if not s:
            return 0

        include = [-1 for _ in range(256)]
        pre = -1
        res = 0
        for i in range(len(s)):
            left = max(include[ord(s[i])], pre)
            res = max(res, i - left)
            pre = left
            include[ord(s[i])] = i

        return res


so = Solution()
s = 'abccabdcdcab'
print(so.lengthOfLongestSubstring1(s))

print(so.lengthOfLongestSubstring2(s))

