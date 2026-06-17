#
# @lc app=leetcode id=3614 lang=python3
#
# [3614] Process String with Special Operations II
#

# @lc code=start
class Solution:
    def processStr(self, s: str, k: int) -> str:
        #how long is the result after processing i chars in s
        cur_len = 0

        for i, char in enumerate(s):
            #print(i, cur_len)
            
            if char == "*":
                cur_len = max(cur_len - 1, 0)
            elif char == "#":
                cur_len *= 2
            elif char == "%":
                pass
            else:
                cur_len += 1

        #print(cur_len)

        if k+1 > cur_len:
            return "."
        
        #traverse s backwards and do the inverse operation
        # on both k and cur_len
        
        for char in reversed(s):
            if char == "*":
                cur_len += 1
            elif char == "#":
                #split it in two, which half does i end up in?
                if k + 1 > (cur_len + 1) //2:
                    #it is in the upper half
                    k -= (cur_len + 1)//2
                cur_len = (cur_len +1) // 2
            elif char == "%":
                #mirror k across the middle 
                k = cur_len - k - 1
            elif k + 1 == cur_len:
                return char
            else:
                #removing a lowercase letter does not affect the indexing 
                cur_len -= 1
                
        return "."

            
            

                
            



        
# @lc code=end

