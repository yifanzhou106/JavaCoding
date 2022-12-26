class Solution:
    # 给定一个字符串s，求s中有多少个字面值不同的子序列
    # 字面值不同，指的是即使子序列使用的index不一样，值一样也算相同字面值
    # 做法是遍历一遍字符串，每当加入一个原本没有重复的字符c时，总不同字面值数*=2
    # c如果已经有重复了，就总不同字面值数 += 总不同字面值数 - 原本以c为底的总数， 再更新以c为底的总数 = 原本以c为底的总数 + 总不同字面值数 - 原本以c为底的总数

    def diffSubSequence(self, s):
        # 假设只有26个字母
        chars = [0 for _ in range(26)]
        # 空集也算一个
        total = 1
        for c in s:
            index = ord(c) - ord('a')
            add = total - chars[index]
            chars[index] += add
            total += add
        return total


so = Solution()
s = 'ccc'
print(so.diffSubSequence(s))
