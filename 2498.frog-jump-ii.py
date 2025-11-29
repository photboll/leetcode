#
# @lc app=leetcode id=2498 lang=python3
#
# [2498] Frog Jump II
#

# @lc code=start
class Solution:
    def maxJump(self, stones: List[int]) -> int:
        """
        minimum of a maximum 
        if a stone is not in either path then adding it to one of the paths 
        can improve the solution. It will never make it worse 
        
        we should alternate the assignment of each stones between the paths
        suppose we have stones = [a, b ,c, d] and we have an assignemtn 
        like p1, p2, p2, p1 . the cost will always be stones[3] - stones[0]
        since stones[i] is strictly increasing.
        if we swithc one p1 with a p2 so we have an alternating sequnce
        then we have]
        p1 : stones[2] - stones[0]
        p2 : stones[3] - stones[1]
        which is atleast as good or better then the first assignment 
        """
        n = len(stones)
        res = stones[1] - stones[0]
        #find the longest jump if we alternate
        for i in range(2, n):
            res = max(res, stones[i]- stones[i-2])
        return res



        
# @lc code=end

