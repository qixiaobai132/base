# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

 

# 示例 1:

# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

# 解释：

# 在 strs 中没有字符串可以通过重新排列来形成 "bat"。
# 字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。
# 字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此。

#我的解法
import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        r = collections.defaultdict(list)
        
        for index, i in enumerate(strs):
            i = ''.join(sorted(i))
            r[i].append(index)
        result = []
        for i in r.values():
            medium = []
            for j in i:
                medium.append(strs[j])
            result.append(medium)
        return result
    
#官方答案
from typing import List


class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)
        
        return list(mp.values())

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/group-anagrams/solutions/520469/zi-mu-yi-wei-ci-fen-zu-by-leetcode-solut-gyoc/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# l = ["eat", "tea", "tan", "ate", "nat", "bat"]
# l.sort()
# s = "ccb"
# sorted(s)
x = {"a":1, "b":2,  "c":3}


if __name__ == '__main__':
    
     print(x)
