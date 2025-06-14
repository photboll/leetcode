#
# @lc app=leetcode id=2566 lang=python3
#
# [2566] Maximum Difference by Remapping a Digit
#

# @lc code=start
class Solution:
    def minMaxDifference(self, num: int) -> int:
        """
        A greedy approach might work, we separate the task into two parts, finding the maximum and the minimum 
        
        
        we look the leading digit, if it is 9 then we move to the next digit
        When we encounter our first non-9 digit we remap 
        else we want to remap it to become 9
        order of remapping will change the result, does that hinder the greedy approach
        """
        def remap(digits: List[str], src, trg):
            for i in range(len(digits)):
                if digits[i] == src:
                    digits[i] = trg
            return digits
                    
            
        def remap_num(num, remaps_available= 1, target = "9"):
            digits = [c for c in str(num)]
            for d in digits:
                if d != target:
                    remap(digits, d, target)
                    remaps_available -= 1
                
                if remaps_available <= 0:
                    break
                
            return int("".join(digits))
        maximum =remap_num(num, target="9") 
        minimum = remap_num(num, target="0")
        print(maximum, minimum)
        return remap_num(num, target="9") - remap_num(num, target="0")
        

                


            
        
# @lc code=end

