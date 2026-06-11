#
# @lc app=leetcode id=3691 lang=python3
#
# [3691] Maximum Total Subarray Value II
#

# @lc code=start
from heapq import heapreplace
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        """
        calculate the value of each possible subarry 
        prefix/suffix sum type problem? No, we care about max and min so we cant cleanly uses prefixes
        two-pointer problem? yes 
        start with finding the max for each possible subarray
        
        when one number passes out of the left side of the window. The maximum becomes the value at the top of the stack
        
        """
        n = len(nums)
        ST = SparesTable(nums)

        pq = [(-ST.query(i, n), i, n) for i in range(n)]

        res = 0
        for _ in range(k):
            val, l, r = pq[0]
            if val == 0:
                break
            res -= val
            heapreplace(pq, (-ST.query(l, r-1), l, r-1))

        return res



class SparesTable:
    """
    user to find the min and max of a subarray between left and right 


    """
    
    def __init__(self, num: list[int]):
        n = len(num)
        bitWidth = n.bit_length()
        self.min = [[0] * n for _ in range(bitWidth)]
        self.max = [[0] * n for _ in range(bitWidth)]

        for i in range(n):
            self.min[0][i] = self.max[0][i] = num[i]
        
        for i in range(1, bitWidth):
            for j in range(n - (1 << i) + 1):
                self.min[i][j] = min(self.min[i - 1][j], self.min[i - 1][j + (1 << (i - 1))])
                self.max[i][j] = max(self.max[i - 1][j], self.max[i - 1][j + (1 << (i - 1))])
            
    def query(self, left:int, right: int) -> int:
        k = (right - left).bit_length() -1
        return max(self.max[k][left], self.max[k][right - (1 << k)]) - \
                min(self.min[k][left], self.min[k][right - (1 << k)])
    
        
        
        


        
        
# @lc code=end

