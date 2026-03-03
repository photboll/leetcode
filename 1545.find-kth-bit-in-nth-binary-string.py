#
# @lc app=leetcode id=1545 lang=python3
#
# [1545] Find Kth Bit in Nth Binary String
#

# @lc code=start
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        """
        2 ** n -1 is the length of the nth string 
        depending on where k is in [1, 2 **n -1]
        recursive solution
        the base case is for the string of length one. answer always 0
        
        if k is the middle return 1
        if k is in the lower half 
            then recur with n-1 and k
        if k is in the uppef half
            then we need to recalculate k because of the reversal
            recur for n-1 and k_new
            then invert the answer
        
        
        """
        if n == 1:
            return "0"
        midpoint = pow(2, n-1)

        if k < midpoint:
            return self.findKthBit(n-1, k)
        elif k > midpoint:
            k_inv = (midpoint << 1) - k
            bit = self.findKthBit(n-1, k_inv)
            return "1" if bit == "0" else "0"
        else:# k == midpoint:
            return "1"
        
        
# @lc code=end

