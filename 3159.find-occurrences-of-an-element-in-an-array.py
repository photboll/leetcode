#
# @lc app=leetcode id=3159 lang=python3
#
# [3159] Find Occurrences of an Element in an Array
#

# @lc code=start

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occurences = []
        for i, num in enumerate(nums):
            if num == x:
                occurences.append(i)
        
        answer = []
        for q in queries:
            if q <= len(occurences):
                answer.append(occurences[q-1])
            else:
                answer.append(-1)
        
        return answer
# @lc code=end

