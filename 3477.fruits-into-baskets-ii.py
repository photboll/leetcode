#
# @lc app=leetcode id=3477 lang=python3
#
# [3477] Fruits Into Baskets II
#

# @lc code=start
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        for i in range(n):
            for j in range(n):
                if fruits[i] <= baskets[j]:
                    baskets[j] = 0
                    break
        return sum(map(lambda x: x > 0, baskets))
                
        
# @lc code=end

