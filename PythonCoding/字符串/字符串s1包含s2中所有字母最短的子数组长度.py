class Solution:
    def str1IncludeStr2(self, s1, s2):
        map = {}
        all = 0
        for c in s2:
            map[c] = map.get(c, 0) + 1
            all += 1
        right = 0
        res = float('inf')
        for i in range(len(s1)):
            while all != 0 and right < len(s1):
                if s1[right] in map:
                    map[s1[right]] -= 1
                    if map[s1[right]] >= 0:
                        all -= 1
                right += 1
            if all == 0:
                res = min(res, right - i)
            if s1[i] in map:
                map[s1[i]] += 1
                if map[s1[i]] > 0:
                    all += 1
            if i == right:
                right += 1
        return res


so = Solution()
s1 = 'abcddjg'
s2 = 'dg'
print(so.str1IncludeStr2(s1, s2))



