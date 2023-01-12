# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
#
# 注意：
#
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        map = {}
        for c in t:
            map[c] = map.get(c, 0) + 1
        all = len(t)
        left = 0
        right = 0
        res = float('inf')
        rightIndex = 0

        for left in range(len(s)):
            while all != 0 and right < len(s):
                if s[right] in map:
                    if map[s[right]] > 0:
                        all -= 1
                    map[s[right]] -= 1
                right += 1
            if all == 0 and right - left < res:
                rightIndex = right
                res = right - left
            if s[left] in map:
                if map[s[left]] == 0:
                    all += 1
                map[s[left]] += 1
        return "" if res == float('inf') else s[rightIndex - res:rightIndex]


