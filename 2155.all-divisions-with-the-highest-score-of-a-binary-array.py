#
# @lc app=leetcode id=2155 lang=python3
#
# [2155] All Divisions With the Highest Score of a Binary Array
#

# @lc code=start

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        right_score = sum(nums)
        left_score = 0
        best_score = right_score
        result = [0]

        for i in range(len(nums)):
            if nums[i]:
                right_score -= 1
            else:
                left_score += 1
            
            cur_score = left_score + right_score

            if cur_score > best_score:
                result.clear()
                best_score = cur_score
            
            if cur_score >= best_score:
                result.append(i+1)

            #print(i, cur_score, result)
            
        return result
            
            
        
# @lc code=end

