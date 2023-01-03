# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
#
# 字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。

# 示例 1:
#
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 示例 2:
#
# 输入: strs = [""]
# 输出: [[""]]
# 示例 3:
#
# 输入: strs = ["a"]
# 输出: [["a"]]

# 直接把字符串排序加到map里，
# map存sortedS 和arr
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = {}
        res = []
        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS in map:
                map[sortedS].append(s)
            else:
                map[sortedS] = [s]

        for k in map:
            res.append(map[k])
        return res
