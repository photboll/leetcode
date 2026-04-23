#
# @lc app=leetcode id=2452 lang=python3
#
# [2452] Words Within Two Edits of Dictionary
#

# @lc code=start
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        for query in queries:
            for word in dictionary:
                diff = 0
                for i in range(len(query)):
                    if query[i] != word[i]:
                        diff += 1
                if diff <= 2:
                    result.append(query)
                    break
        return result

            
        
# @lc code=end

