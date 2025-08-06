#
# @lc app=leetcode id=3479 lang=python3
#
# [3479] Fruits Into Baskets III
#

# @lc code=start
import math
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        """
        Can we binary search on the resulting value, we know it will always be in [0, n]
        But we need an efficient way to find if it is possible to place at least k.
        """
        n = len(baskets)
        m = int(math.sqrt(n))
        num_blocks = (n + m - 1) // m
        count = 0
        max_val = [0] * num_blocks
        
        # Find the largest basket in each block 
        for i in range(n):
            max_val[i // m] = max(max_val[i // m], baskets[i])
        
        # Try to place each fruit
        for fruit in fruits:
            unset = 1
            for block in range(num_blocks):
                if max_val[block] < fruit:# This fruit cant possibly fit in any basket of this block
                    continue
                
                # Find the leftmost basket that can fit this type of fruit
                has_placed = False
                max_val[block] = 0
                for i in range(m):
                    pos = block*m + i
                    if not has_placed and pos < n and baskets[pos] >= fruit:
                        baskets[pos] = 0
                        has_placed = True
                    
                    #Remember to update the max_val of this block 
                    if pos < n:
                        max_val[block] = max(max_val[block], baskets[pos])
                unset = 0
                break
            count += unset
        return count 
        
# @lc code=end

